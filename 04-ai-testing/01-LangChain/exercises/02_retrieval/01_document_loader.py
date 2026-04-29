# -*- coding: utf-8 -*-
"""
练习1：DocumentLoader 文档加载
练习目标：学会加载不同格式的文档
前置知识：Python 文件操作基础
核心要点：各种 Loader 的使用、Document 对象结构
"""

import os
from dotenv import load_dotenv
from langchain_community.document_loaders import CSVLoader, TextLoader

load_dotenv()

# ===== 练习1.1：加载 CSV 文件 =====
print("=== 加载 CSV 文件 ===")

# 项目中有一个现成的 CSV 文件
csv_path = os.path.join(os.path.dirname(__file__), "..", "..", "01-LangChain", "OutdoorClothingCatalog_1000.csv")

# 检查文件是否存在
if os.path.exists(csv_path):
    loader = CSVLoader(file_path=csv_path, encoding="utf-8")
    documents = loader.load()
    
    print(f"加载了 {len(documents)} 条文档")
    print(f"第一条文档内容预览：{documents[0].page_content[:200]}...")
    print(f"元数据：{documents[0].metadata}")
else:
    print(f"CSV 文件不存在：{csv_path}")
    print("请确保 OutdoorClothingCatalog_1000.csv 文件在正确位置")

# ===== 练习1.2：Document 对象结构 =====
print("\n=== Document 对象结构 ===")

# 手动创建 Document 对象
from langchain_core.documents import Document

doc = Document(
    page_content="这是一个测试文档的内容",
    metadata={"source": "test.txt", "page": 1}
)
print(f"内容：{doc.page_content}")
print(f"元数据：{doc.metadata}")

"""
思考题：
1. Document 对象的 page_content 和 metadata 分别存储什么？
2. CSVLoader 的 load() 方法返回的是什么类型？
3. 如果要加载 PDF 文件，应该用什么 Loader？
4. metadata 中的 source 字段有什么用？
"""
