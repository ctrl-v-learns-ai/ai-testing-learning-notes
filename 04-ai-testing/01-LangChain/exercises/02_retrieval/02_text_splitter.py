# -*- coding: utf-8 -*-
"""
练习2：TextSplitter 文本分割
练习目标：学会使用文本分割器将长文档切分成小块
前置知识：DocumentLoader 基础
核心要点：chunk_size、chunk_overlap 的作用
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# ===== 练习2.1：基本文本分割 =====
print("=== 基本文本分割 ===")

# 创建一个长文本
long_text = """
软件测试是软件开发过程中不可或缺的一部分。它包括多种测试类型：
单元测试是对软件中最小可测试单元进行检查和验证。单元测试通常由开发人员编写。
集成测试是在单元测试的基础上，将所有模块按照设计要求组装成为子系统或系统，进行集成测试。
系统测试是将已经集成好的软件系统，作为整个基于计算机系统的一个元素，与计算机硬件、外设、某些支持软件、数据和人员等其他系统元素结合在一起，在实际运行环境下，对计算机系统进行一系列的集成测试和确认测试。
验收测试是部署软件之前的最后一个测试操作。在软件产品完成了单元测试、集成测试和系统测试之后，产品发布之前所进行的软件测试活动。
回归测试是指修改了旧代码后，重新进行测试以确认修改没有引入新的错误或导致其他代码产生错误。
性能测试是通过自动化的测试工具模拟多种正常、峰值以及异常负载条件来对系统的各项性能指标进行测试。
"""

# 创建分割器
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,      # 每个块最多 200 个字符
    chunk_overlap=20,    # 块之间重叠 20 个字符
    separators=["\n", "。", "，", " "]  # 分割符优先级
)

# 分割文本
chunks = splitter.split_text(long_text)

print(f"原始文本长度：{len(long_text)} 字符")
print(f"分割后块数：{len(chunks)}")
for i, chunk in enumerate(chunks):
    print(f"\n--- 块 {i+1}（{len(chunk)} 字符）---")
    print(chunk)

# ===== 练习2.2：分割 Document 对象 =====
print("\n=== 分割 Document 对象 ===")

# 创建 Document 列表
docs = [
    Document(page_content=long_text, metadata={"source": "test.txt"})
]

# split_documents 方法可以直接处理 Document 对象
split_chunks = splitter.split_documents(docs)
print(f"分割后 Document 数量：{len(split_chunks)}")
print(f"第一个块的元数据：{split_chunks[0].metadata}")

# ===== 练习2.3：不同 chunk_size 的效果对比 =====
print("\n=== 不同 chunk_size 对比 ===")

for size in [100, 300, 500]:
    s = RecursiveCharacterTextSplitter(chunk_size=size, chunk_overlap=20)
    c = s.split_text(long_text)
    print(f"chunk_size={size}: 分成 {len(c)} 块")

"""
思考题：
1. chunk_size 设为 100 和 500 分别会有什么效果？
2. chunk_overlap 的作用是什么？设为 0 会有什么问题？
3. separators 参数中的顺序有什么意义？
4. split_text 和 split_documents 的区别是什么？
"""
