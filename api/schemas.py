from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

class SummaryResponse(BaseModel):
    summary: str
