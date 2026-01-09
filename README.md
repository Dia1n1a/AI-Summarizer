# AI-Powered Multimodal Summarization System

## Abstract
With the exponential growth of digital content in the form of documents, podcasts, lectures, and videos, efficient information consumption has become a major challenge. Manual summarization of such multimodal data is time-consuming and often impractical.

This project presents an AI-powered multimodal summarization system capable of generating concise summaries from text, audio, and video inputs. The system integrates Automatic Speech Recognition (ASR) using OpenAI Whisper, transformer-based abstractive summarization using HuggingFace models, and a FastAPI-based RESTful deployment architecture. Robust preprocessing, chunk-based summarization, and careful system design ensure stability under real-world constraints.

---

## 1. Introduction
The rapid digitization of information has led to an overwhelming amount of unstructured data across multiple modalities. Educational lectures, meetings, interviews, and media content are increasingly recorded in audio and video formats, making it difficult for users to quickly extract key insights.

This project addresses this problem by building a unified multimodal summarization system that supports text, audio, and video through a single, scalable pipeline.

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

This design ensures modularity, maintainability, and scalability.

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
- Render (Cloud Deployment)  

---

## 5. Implementation Details

### Text Summarization
- Accepts raw text or text files  
- Uses chunk-based summarization to avoid token limits  
- Implements safeguards for short inputs  
- Uses facebook/bart-large-cnn for abstractive summarization  

### Audio Summarization
- Accepts audio files (.wav, .mp3)  
- Normalizes audio using FFmpeg  
- Transcribes speech using Whisper  
- Summarizes transcribed text  

### Video Summarization
- Accepts video files (.mp4)  
- Extracts audio using FFmpeg  
- Applies ASR and summarization pipeline  

---

## 6. Evaluation
ROUGE metrics are used for offline evaluation:
- ROUGE-1  
- ROUGE-2  
- ROUGE-L  

These metrics measure lexical overlap between generated and reference summaries.

---

## 7. Challenges Faced
- Dependency issues with MoviePy on Windows  
- FFmpeg path configuration problems  
- Transformer token limit crashes  
- Incorrect handling of raw text vs file paths  
- FastAPI routing conflicts  
- Cloud deployment constraints on free-tier environments  

All issues were systematically debugged and resolved.

---

## 8. Enhancements
- Chunk-based summarization for long inputs  
- Graceful handling of short text  
- Unified pipeline across all modalities  
- Robust preprocessing and error handling  
- Cloud deployment with public access  

---

## 9. Results
| Feature | Status |
|-------|--------|
| Text summarization | Working |
| Audio summarization | Working |
| Video summarization | Working |
| ROUGE evaluation | Implemented |
| FastAPI deployment | Stable |
| Cloud deployment | Live |

---

## 10. Limitations
- Performance constrained on CPU-based free-tier cloud services  
- Summarization quality depends on ASR accuracy  
- ROUGE does not capture semantic similarity fully  

---

## 11. Future Work
- Multilingual summarization  
- GPU acceleration  
- Semantic evaluation (BERTScore)  
- Frontend integration  
- Real-time streaming support  

---

## 12. Conclusion
This project demonstrates the design, implementation, and deployment of a real-world multimodal AI system. By integrating ASR, transformer-based summarization, and RESTful APIs, the system effectively addresses practical challenges in modern AI applications and is suitable for real-world usage.

---

## Final Outcome
A fully deployed AI-powered multimodal summarization system capable of processing text, audio, and video inputs through a unified, production-ready pipeline.
