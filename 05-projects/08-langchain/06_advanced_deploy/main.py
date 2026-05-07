# -*- coding: utf-8 -*-
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from rag_chain import RAGChain

app = FastAPI(title="RAG API")
rag = RAGChain()


class ChatRequest(BaseModel):
    input: str
    session_id: str = "default"


class ChatResponse(BaseModel):
    response: str


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response = rag.chat(request.input, request.session_id)
    return ChatResponse(response=response)


@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    async def generate():
        for chunk in rag.chat_stream(request.input, request.session_id):
            yield chunk
    return StreamingResponse(generate(), media_type="text/plain")


@app.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    chunks = rag.add_document(file_path)
    return {"message": f"Added {chunks} chunks from {file.filename}"}


@app.get("/")
async def root():
    return {"message": "RAG API is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
