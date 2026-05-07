# Complete RAG Application

## Project Overview
A full-featured RAG application with document management, conversational memory, and REST API.

## Features
- Document upload (CSV, TXT)
- Vector store with FAISS
- Conversational memory
- Streaming responses
- REST API with FastAPI

## How to Run
```bash
pip install -r requirements.txt

# Start API server
python main.py

# Or with uvicorn
uvicorn main:app --reload --port 8000
```

## API Endpoints
- POST /chat - Chat with the bot
- POST /chat/stream - Streaming chat
- POST /documents/upload - Upload document
- GET /documents - List documents

## Core Concepts
1. RAG pipeline
2. Vector store management
3. Conversational memory
4. Streaming API
5. Error handling

## Project Structure
```
05-projects/06_advanced_deploy/
  main.py           # FastAPI app
  rag_chain.py      # RAG chain
  document_store.py # Document management
  config.py         # Configuration
  requirements.txt
  README.md
```
