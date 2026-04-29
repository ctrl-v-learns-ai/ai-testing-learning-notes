# -*- coding: utf-8 -*-
"""
练习4：LCEL 链式调用进阶
练习目标：掌握 LCEL 的 invoke、stream、batch 方法
前置知识：ChatModel、PromptTemplate、OutputParser
核心要点：LCEL 管道语法、流式输出、批量调用
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
    api_key=os.getenv("MIMO_API_KEY"),
    base_url=os.getenv("MIMO_API_URL"),
    temperature=0.7,
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个测试专家"),
    ("human", "用3个要点解释：{topic}")
])

chain = prompt | llm | StrOutputParser()

# ===== 练习4.1：invoke（单次调用）=====
print("=== invoke 调用 ===")
result = chain.invoke({"topic": "单元测试"})
print(result)
print()

# ===== 练习4.2：stream（流式输出）=====
# 适合长文本生成，实时显示结果
print("=== stream 流式输出 ===")
for chunk in chain.stream({"topic": "集成测试"}):
    print(chunk, end="", flush=True)
print()
print()

# ===== 练习4.3：batch（批量调用）=====
# 同时处理多个请求，提高效率
print("=== batch 批量调用 ===")
topics = [
    {"topic": "单元测试"},
    {"topic": "集成测试"},
    {"topic": "端到端测试"},
]
results = chain.batch(topics)
for topic, result in zip(topics, results):
    print(f"\n[{topic['topic']}]:")
    print(result[:100] + "..." if len(result) > 100 else result)

"""
思考题：
1. invoke、stream、batch 三种调用方式分别适合什么场景？
2. 流式输出的好处是什么？什么时候应该用流式？
3. batch 调用比逐个调用 invoke 快吗？为什么？
4. 如果 batch 中有一个请求失败了，其他请求会受影响吗？
"""
