# -*- coding: utf-8 -*-
"""
文档加载和处理模块
"""

import os
from langchain_community.document_loaders import CSVLoader, TextLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from config import CHUNK_SIZE, CHUNK_OVERLAP, API_KEY, API_URL


def load_documents(doc_path: str) -> list:
    """
    加载指定路径的文档
    
    Args:
        doc_path: 文档路径（可以是文件或目录）
    
    Returns:
        Document 列表
    """
    documents = []
    
    if os.path.isfile(doc_path):
        # 单个文件
        ext = os.path.splitext(doc_path)[1].lower()
        if ext == ".csv":
            loader = CSVLoader(file_path=doc_path, encoding="utf-8")
        elif ext == ".txt":
            loader = TextLoader(file_path=doc_path, encoding="utf-8")
        else:
            print(f"不支持的文件格式：{ext}")
            return []
        documents = loader.load()
    elif os.path.isdir(doc_path):
        # 目录：加载所有支持的文件
        for filename in os.listdir(doc_path):
            filepath = os.path.join(doc_path, filename)
            if os.path.isfile(filepath):
                ext = os.path.splitext(filename)[1].lower()
                if ext == ".csv":
                    loader = CSVLoader(file_path=filepath, encoding="utf-8")
                elif ext == ".txt":
                    loader = TextLoader(file_path=filepath, encoding="utf-8")
                else:
                    continue
                documents.extend(loader.load())
    else:
        print(f"路径不存在：{doc_path}")
    
    return documents


def split_documents(documents: list, chunk_size: int = CHUNK_SIZE, chunk_overlap: int = CHUNK_OVERLAP) -> list:
    """
    分割文档
    
    Args:
        documents: Document 列表
        chunk_size: 块大小
        chunk_overlap: 块重叠大小
    
    Returns:
        分割后的 Document 列表
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(documents)


def create_vectorstore(chunks: list) -> FAISS:
    """
    从文档块创建向量数据库
    
    Args:
        chunks: 分割后的 Document 列表
    
    Returns:
        FAISS 向量数据库
    """
    embeddings = OpenAIEmbeddings(
        model="text-embedding-ada-002",
        openai_api_key=API_KEY,
        openai_api_base=API_URL
    )
    return FAISS.from_documents(chunks, embeddings)


def load_or_create_vectorstore(doc_path: str, index_path: str = "faiss_index") -> FAISS:
    """
    加载现有向量数据库或创建新的
    
    Args:
        doc_path: 文档路径
        index_path: 向量数据库保存路径
    
    Returns:
        FAISS 向量数据库
    """
    embeddings = OpenAIEmbeddings(
        model="text-embedding-ada-002",
        openai_api_key=API_KEY,
        openai_api_base=API_URL
    )
    
    if os.path.exists(index_path):
        print(f"加载现有向量数据库：{index_path}")
        return FAISS.load_local(index_path, embeddings)
    else:
        print("创建新的向量数据库...")
        documents = load_documents(doc_path)
        if not documents:
            raise ValueError("没有加载到任何文档")
        
        chunks = split_documents(documents)
        print(f"文档分割完成：{len(documents)} 条文档 -> {len(chunks)} 个块")
        
        vectorstore = create_vectorstore(chunks)
        vectorstore.save_local(index_path)
        print(f"向量数据库已保存到：{index_path}")
        
        return vectorstore
