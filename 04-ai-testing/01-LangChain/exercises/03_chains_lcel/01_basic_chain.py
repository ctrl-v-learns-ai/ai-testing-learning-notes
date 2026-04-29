# -*- coding: utf-8 -*-
"""
练习1：基础 LCEL 链
练习目标：掌握 LCEL 的基本语法和 invoke/stream/batch 调用
前置知识：ChatModel、PromptTemplate、OutputParser
核心要点：管道运算符 | 的使用
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# 初始化模型
llm = ChatOpenAI(
    model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
    api_key=os.getenv("MIMO_API_KEY"),
    base_url=os.getenv("MIMO_API_URL"),
    temperature=0.7,
)

# ===== 练习1.1：创建基础链 =====
print("=== 基础链 ===")

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个测试专家"),
    ("human", "用一句话解释：{topic}")
])

# LCEL 语法：使用 | 管道运算符组合组件
chain = prompt | llm | StrOutputParser()

# invoke 调用
result = chain.invoke({"topic": "单元测试"})
print(f"invoke 结果：{result}")

# ===== 练习1.2：stream 流式输出 =====
print("\n=== 流式输出 ===")

for chunk in chain.stream({"topic": "集成测试"}):
    print(chunk, end="", flush=True)
print()

# ===== 练习1.3：batch 批量调用 =====
print("\n=== 批量调用 ===")

topics = [
    {"topic": "单元测试"},
    {"topic": "集成测试"},
    {"topic": "系统测试"},
]

results = chain.batch(topics)
for t, r in zip(topics, results):
    print(f"{t['topic']}: {r}")

"""
思考题：
1. prompt | llm | StrOutputParser() 中数据是怎么传递的？
2. invoke 和 stream 的区别是什么？什么时候用 stream？
3. batch 比逐个调用 invoke 快吗？为什么？
"""
