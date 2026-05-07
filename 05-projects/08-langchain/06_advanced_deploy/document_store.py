# -*- coding: utf-8 -*-
import os
from langchain_community.document_loaders import CSVLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from config import API_KEY, API_URL, CHUNK_SIZE, CHUNK_OVERLAP


class DocumentStore:
    def __init__(self, index_path="faiss_index"):
        self.index_path = index_path
        self.embeddings = OpenAIEmbeddings(
            model="text-embedding-ada-002",
            openai_api_key=API_KEY,
            openai_api_base=API_URL
        )
        self.vectorstore = None
        self._load_or_create()

    def _load_or_create(self):
        if os.path.exists(self.index_path):
            self.vectorstore = FAISS.load_local(self.index_path, self.embeddings)
        else:
            self.vectorstore = FAISS.from_documents([], self.embeddings)

    def add_document(self, file_path: str):
        ext = os.path.splitext(file_path)[1].lower()
        if ext == ".csv":
            loader = CSVLoader(file_path=file_path, encoding="utf-8")
        elif ext == ".txt":
            loader = TextLoader(file_path=file_path, encoding="utf-8")
        else:
            raise ValueError(f"Unsupported file type: {ext}")

        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
        chunks = splitter.split_documents(docs)

        self.vectorstore.add_documents(chunks)
        self.vectorstore.save_local(self.index_path)
        return len(chunks)

    def search(self, query: str, k: int = 3):
        return self.vectorstore.similarity_search(query, k=k)

    def get_retriever(self, k: int = 3):
        return self.vectorstore.as_retriever(
            search_kwargs={"k": k}
        )
