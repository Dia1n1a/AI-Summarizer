# AI-Powered Multimodal Summarization System

## Abstract
With the exponential growth of digital content in the form of documents, podcasts, lectures, and videos, efficient information consumption has become a major challenge. Manual summarization of such multimodal data is time-consuming and often impractical.

This project presents an AI-powered multimodal summarization system capable of generating concise summaries from **text, audio, and video inputs**. The system integrates **Automatic Speech Recognition (ASR)** using **OpenAI Whisper**, **transformer-based abstractive summarization** using **HuggingFace models**, and a **FastAPI-based RESTful architecture**. Robust preprocessing, chunk-based summarization, and careful system design ensure stability under real-world constraints.

The system is **successfully deployed and executed in a local environment**, demonstrating reliable multimodal summarization performance.

---

## 1. Introduction
The rapid digitization of information has led to an overwhelming amount of unstructured data across multiple modalities. Educational lectures, meetings, interviews, and media content are increasingly recorded in audio and video formats, making it difficult for users to quickly extract key insights.

This project addresses this problem by building a **unified multimodal summarization system** that supports **text, audio, and video** through a single, scalable pipeline, with a strong emphasis on **backend ML engineering and system robustness**.

---

## 2. Objectives
- Design a unified multimodal summarization pipeline  
- Convert audio and video speech into text using Whisper ASR  
- Generate abstractive summaries using transformer-based models  
- Deploy the system as a RESTful API using FastAPI  
- Evaluate summarization quality using ROUGE metrics  
- Handle real-world constraints such as long inputs and deployment limitations  

---

## 3. System Architecture
The system follows a modular layered architecture:

User Input (Text / Audio / Video)  
→ FastAPI Endpoints  
→ Pipeline Controller  
→ Preprocessing Layer  
→ Model Inference Layer  
→ Summary Output  

This architecture ensures **modularity, maintainability, and scalability**, enabling easy extension and debugging.

---

## 4. Technology Stack
**Language:** Python 3.11  

**Frameworks & Libraries:**  
- FastAPI  
- Uvicorn  
- HuggingFace Transformers  
- OpenAI Whisper  
- FFmpeg  
- Evaluate, ROUGE  

**Tools:**  
- VS Code  
- Swagger UI  
- GitHub  

---

## 5. Implementation Details

### Text Summarization
- Accepts raw text or text files  
- Uses chunk-based summarization to avoid transformer token limits  
- Implements safeguards for short inputs  
- Uses `facebook/bart-large-cnn` for abstractive summarization  

### Audio Summarization
- Accepts audio files (`.wav`, `.mp3`)  
- Normalizes audio using FFmpeg  
- Transcribes speech using Whisper  
- Summarizes the transcribed text  

### Video Summarization
- Accepts video files (`.mp4`)  
- Extracts audio using FFmpeg  
- Applies ASR and summarization pipeline on extracted audio  

---

## 6. Evaluation
ROUGE metrics are used for offline evaluation:
- ROUGE-1  
- ROUGE-2  
- ROUGE-L  

These metrics measure lexical overlap between generated summaries and reference summaries. While ROUGE provides quantitative insights, qualitative evaluation is also considered.

---

## 7. Challenges Faced
- Dependency issues with MoviePy on Windows  
- FFmpeg path configuration problems  
- Transformer token limit crashes for long inputs  
- Incorrect handling of raw text vs file paths  
- FastAPI routing conflicts during development  
- Memory limitations on free-tier cloud platforms  

All issues were **systematically identified, debugged, and resolved** during development.

---

## 8. Enhancements
- Chunk-based summarization for long inputs  
- Graceful handling of short text  
- Unified pipeline across all modalities  
- Robust preprocessing and error handling  
- Stable and reproducible local deployment  

---

## 9. Results
| Feature | Status |
|-------|--------|
| Text summarization | Working |
| Audio summarization | Working |
| Video summarization | Working |
| ROUGE evaluation | Implemented |
| FastAPI deployment | Stable |
| Local deployment | Successful |

---

## 10. Limitations
- Performance is constrained on CPU-only systems for large inputs  
- Summarization quality depends on ASR transcription accuracy  
- ROUGE does not fully capture semantic similarity  

---

## 11. Deployment Note (Local Deployment)

This project is **intended to be run locally** due to the **memory-intensive nature of the underlying ML models**, specifically:
- OpenAI Whisper (ASR)
- Transformer-based summarization models (BART)

An attempt was made to deploy the system on **free-tier cloud platforms (e.g., Render)**. However, such platforms provide limited RAM, leading to **out-of-memory (OOM) errors during model loading**. This is a known and expected limitation when deploying large ML models on free-tier infrastructure.

The system runs **stably and reliably in a local environment** or on **high-memory / GPU-backed servers**, which is appropriate for real-world ML inference workloads.

---

## 12. Future Work
- Multilingual summarization support  
- GPU acceleration for faster inference  
- Semantic evaluation using BERTScore  
- Optional frontend integration  
- Real-time streaming summarization  

---

## 13. Conclusion
This project demonstrates the complete design, implementation, and execution of a **real-world multimodal AI system**. By integrating ASR, transformer-based summarization, and RESTful APIs, the system effectively addresses practical challenges encountered in modern AI applications. The final implementation is **robust, modular, and production-ready for local and high-resource environments**.

---

## Final Outcome
A fully functional AI-powered multimodal summarization system capable of processing **text, audio, and video inputs** through a unified, production-ready pipeline, successfully deployed and demonstrated in a local environment.
