# -*- coding: utf-8 -*-
"""
练习3：Embedding 与 VectorStore
练习目标：学会使用嵌入模型和向量数据库
前置知识：DocumentLoader、TextSplitter
核心要点：Embedding 原理、FAISS 使用、相似度搜索
"""

import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

load_dotenv()

# ===== 练习3.1：Embedding 基础 =====
print("=== Embedding 基础 ===")

# 初始化 Embedding 模型
# 注意：这里如果使用 OpenAI 兼容接口，你需要配置正确的 API
embeddings = HuggingFaceEmbeddings(
    model_name="shibing624/text2vec-base-chinese"
)

# 将文本转换为向量
text = "什么是回归测试？"
vector = embeddings.embed_query(text)
print(f"文本：{text}")
print(f"向量维度：{len(vector)}")
print(f"向量前5个值：{vector[:5]}")

# ===== 练习3.2：计算文本相似度 =====
print("\n=== 文本相似度 ===")

import numpy as np

# 准备几段文本
texts = [
    "回归测试是修改代码后重新测试以确认没有引入新错误",
    "单元测试是对软件最小单元的测试",
    "回归测试确保旧功能在新修改后仍然正常工作",
    "性能测试检查系统在高负载下的表现"
]

# 计算向量
text_vectors = embeddings.embed_documents(texts)

# 计算余弦相似度
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# 查询
query = "什么是回归测试？"
query_vector = embeddings.embed_query(query)

print(f"查询：{query}")
print("相似度排名：")
similarities = []
for i, (text, vec) in enumerate(zip(texts, text_vectors)):
    sim = cosine_similarity(query_vector, vec)
    similarities.append((sim, text))

similarities.sort(reverse=True)
for sim, text in similarities:
    print(f"  {sim:.4f} - {text}")

# ===== 练习3.3：FAISS 向量数据库 =====
print("\n=== FAISS 向量数据库 ===")

# 准备文档
documents = [
    Document(page_content="回归测试是修改代码后重新测试", metadata={"type": "testing"}),
    Document(page_content="单元测试是对最小单元的测试", metadata={"type": "testing"}),
    Document(page_content="Python是一种编程语言", metadata={"type": "programming"}),
    Document(page_content="性能测试检查系统负载能力", metadata={"type": "testing"}),
]

# 创建向量数据库
vectorstore = FAISS.from_documents(documents, embeddings)
print(f"向量数据库中的文档数量：{vectorstore.index.ntotal}")

# 相似度搜索
query = "什么是回归测试？"
results = vectorstore.similarity_search(query, k=2)
print(f"\n查询：{query}")
print("Top 2 结果：")
for doc in results:
    print(f"  - {doc.page_content} (元数据: {doc.metadata})")

# 保存和加载
vectorstore.save_local("test_faiss_index")
print("\n向量数据库已保存到 test_faiss_index/")

# 重新加载
loaded_store = FAISS.load_local("test_faiss_index", embeddings)
print("向量数据库已重新加载")

"""
思考题：
1. Embedding 模型输出的向量是什么？维度由什么决定？

2. 为什么"回归测试"和"单元测试"的相似度比"回归测试"和"Python"高？

3. FAISS 的 similarity_search 方法内部做了什么？

4. save_local 和 load_local 的作用是什么？什么时候需要保存？
"""

"""可以先思考再看答案建议"""

"""
1.  向量 = 一组浮点数，代表文本的语义
    维度 = 模型决定的，不能改
    维度越高 → 精度越高，成本也越高
    语义相近的文本 → 向量距离近

2.  回归测试和单元测试 → 都是测试方法 → 语义相近 → 向量距离近
    回归测试和 Python  → 不同领域    → 语义不同 → 向量距离远
    
3.  similarity_search 内部做了四件事：
    1. 查询文本 → Embedding → 查询向量
    2. 查询向量 和 库中所有向量 计算距离
    3. 按距离排序，取最近的 k 个
    4. 返回对应的 Document
    本质就是：语义相似度搜索

4.  save_local → 把向量库存到磁盘（算一次，用多次）
    load_local → 从磁盘加载（省掉重新计算的时间和费用）
    文档量大或用付费 API → 一定要保存
    文档经常变 → 每次更新后重新保存
"""
