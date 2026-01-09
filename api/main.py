from fastapi import FastAPI, UploadFile, File
import shutil
import os

from pipeline.controller import run_pipeline
from api.schemas import TextRequest, SummaryResponse

app = FastAPI(
    title="Multimodal Summarization API",
    description="Summarize text, audio, and video using AI models",
    version="1.0"
)

UPLOAD_DIR = "data/raw"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/summarize/text", response_model=SummaryResponse)
def summarize_text(request: TextRequest):
    summary = run_pipeline("text", request.text)
    return {"summary": summary}


@app.post("/summarize/audio", response_model=SummaryResponse)
def summarize_audio(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    summary = run_pipeline("audio", file_path)
    return {"summary": summary}


@app.post("/summarize/video", response_model=SummaryResponse)
def summarize_video(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    summary = run_pipeline("video", file_path)
    return {"summary": summary}


@app.get("/")
def root():
    return {"message": "Multimodal Summarization API is running"}
