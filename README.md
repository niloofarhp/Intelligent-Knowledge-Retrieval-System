# Multimodal Content Retriever

A powerful and extensible Conversational AI assistant for querying and summarizing your documents. Built using LangChain, OpenAI's GPT-4, and Streamlit, this system enables seamless question answering over `.txt`, `.pdf`, `.md`, and even image files (`.png`, `.jpg`) — with memory-aware, context-rich responses.

---

## Features

- **Conversational RAG** (Retrieval-Augmented Generation)
- Load and query documents from local folders
- Memory-enabled Q&A for rich chat interactions
- Multi-format support (`.txt`, `.md`, `.pdf`, and image files like `.png`, `.jpg`)
- OCR-based text extraction from images
- Vector-based document retrieval with ChromaDB
- Clean Streamlit UI for interaction
- Secure API key handling via `.env`

---

## How It Works

1. **Document Loading**:
   - Supports `.txt`, `.md`, `.pdf`, and image files (`.png`, `.jpg`).
   - Text from images is extracted using OCR (EasyOCR).

2. **Text Splitting**:
   - Documents are split into manageable chunks for efficient retrieval using chromadb.

3. **Vector Embeddings**:
   - Text chunks are converted into vector embeddings using OpenAI Embedding model.

4. **Conversational Interface**:
   - A memory-enabled chatbot interface allows users to ask questions and receive context-aware answers.

---
