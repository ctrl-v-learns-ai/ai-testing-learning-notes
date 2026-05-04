# -*- coding: utf-8 -*-
"""
练习4：完整 RAG 链
练习目标：构建一个完整的 RAG 问答系统
前置知识：DocumentLoader、TextSplitter、Embedding、VectorStore
核心要点：RAG 链的组合、retriever 的使用
"""

import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

# ===== 第一步：加载文档 =====
print("=== 第一步：加载文档 ===")

csv_path = os.path.join(os.path.dirname(__file__), "..", "..", "OutdoorClothingCatalog_1000.csv")

if not os.path.exists(csv_path):
    print(f"CSV 文件不存在：{csv_path}")
    print("请确保文件路径正确")
    exit()

loader = CSVLoader(file_path=csv_path, encoding="utf-8")
documents = loader.load()
print(f"加载了 {len(documents)} 条文档")

# ===== 第二步：文本分割 =====
print("\n=== 第二步：文本分割 ===")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(documents)
print(f"分割后得到 {len(chunks)} 个块")

# ===== 第三步：创建向量数据库 =====
print("\n=== 第三步：创建向量数据库 ===")

embeddings = HuggingFaceEmbeddings(
    model_name="shibing624/text2vec-base-chinese"
)

vectorstore = FAISS.from_documents(chunks, embeddings)
print("向量数据库创建完成")

# ===== 第四步：创建 Retriever =====
print("\n=== 第四步：创建 Retriever ===")

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}  # 返回前3个最相似的文档
)
print("Retriever 创建完成")

# ===== 第五步：构建 RAG 链 =====
print("\n=== 第五步：构建 RAG 链 ===")

# 初始化 LLM
llm = ChatOpenAI(
    model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
    api_key=os.getenv("MIMO_API_KEY"),
    base_url=os.getenv("MIMO_API_URL"),
    temperature=0.3,
)

# RAG 提示模板
rag_prompt = ChatPromptTemplate.from_messages([
    ("system", "根据以下参考资料回答用户问题。如果资料中没有相关信息，请说明不知道。\n\n参考资料：{context}"),
    ("human", "{question}")
])

# 格式化检索到的文档
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 构建 RAG 链
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | rag_prompt
    | llm
    | StrOutputParser()
)

print("RAG 链构建完成")

# ===== 第六步：测试 RAG 链 =====
print("\n=== 第六步：测试 RAG 链 ===")

question = "推荐一件防晒的衣服"
print(f"问题：{question}")
print("回答：")
answer = rag_chain.invoke(question)
print(answer)

"""
思考题：
1. retriever | format_docs 这个管道的作用是什么？

2. RunnablePassthrough() 的作用是什么？

3. 为什么 RAG 链的 temperature 设为 0.3 而不是 0.7？

4. 如果要支持多轮对话，需要怎么修改 RAG 链？
"""

"""可以先思考再看答案建议"""

"""
1.  retriever | format_docs

    retriever  → 从向量库检索相关文档（List[Document]）
    format_docs → 把文档列表拼成字符串（str）
    
    两者用 | 管道连接 = 先检索，再格式化，一步到位

2.  RunnablePassthrough = 透传器，输入什么就输出什么
    用途：在管道中保持原始输入不变，同时传递给多个分支
    RAG 场景：用户问题既要用来检索，又要作为提问 → 用 RunnablePassthrough 保持原样

3.  RAG = 基于资料回答，不是自由发挥
    temperature 低 → 忠实于资料，回答稳定
    temperature 高 → 模型自由发挥，可能编造内容
    RAG 场景推荐 temperature = 0.1 ~ 0.3

4.  单轮 RAG → 多轮 RAG，三步改造：

    1. 保存对话历史（List[Message]）
    2. 重写当前问题（解决指代不明）
    3. Prompt 中加入对话历史（让模型知道之前聊了什么）
    
    额外注意：历史太长要截断，防止 token 超限
"""
