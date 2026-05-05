# -*- coding: utf-8 -*-
"""
RAG 问答机器人核心类
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from config import API_KEY, API_URL, MODEL_NAME, TEMPERATURE, TOP_K
from document_loader import load_or_create_vectorstore


class RAGBot:
    """基于 RAG 的问答机器人类"""
    
    def __init__(self, doc_path: str, index_path: str = "faiss_index"):
        """
        初始化 RAG 机器人
        
        Args:
            doc_path: 文档路径（文件或目录）
            index_path: 向量数据库保存路径
        """
        # 加载或创建向量数据库
        self.vectorstore = load_or_create_vectorstore(doc_path, index_path)
        
        # 创建 Retriever
        self.retriever = self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": TOP_K}
        )
        
        # 初始化 LLM
        self.llm = ChatOpenAI(
            model=MODEL_NAME,
            api_key=API_KEY,
            base_url=API_URL,
            temperature=TEMPERATURE,
        )
        
        # 创建 RAG 提示模板
        self.rag_prompt = ChatPromptTemplate.from_messages([
            ("system", "根据以下参考资料回答用户问题。如果资料中没有相关信息，请说明不知道。\n\n参考资料：{context}"),
            ("human", "{question}")
        ])
        
        # 构建 RAG 链
        self.chain = (
            {"context": self.retriever | self._format_docs, "question": RunnablePassthrough()}
            | self.rag_prompt
            | self.llm
            | StrOutputParser()
        )
        
        # 对话历史
        self.history = []
    
    def _format_docs(self, docs) -> str:
        """格式化检索到的文档"""
        return "\n\n".join(doc.page_content for doc in docs)
    
    def ask(self, question: str) -> dict:
        """
        提问并获取答案
        
        Args:
            question: 用户问题
        
        Returns:
            包含答案和来源的字典
        """
        # 检索相关文档
        relevant_docs = self.retriever.invoke(question)
        
        # 生成答案
        answer = self.chain.invoke(question)
        
        # 保存历史
        self.history.append({"role": "user", "content": question})
        self.history.append({"role": "assistant", "content": answer})
        
        return {
            "answer": answer,
            "sources": [doc.page_content[:100] + "..." for doc in relevant_docs]
        }
    
    def clear_history(self):
        """清除对话历史"""
        self.history = []
        return "对话历史已清除"
