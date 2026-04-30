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

"""可以先思考再看答案建议"""

"""
1.  invoke：发一次请求，等完整结果（同步）
    stream：边生成边返回，实时看到输出（流式）
    batch：一次提交多条请求，内部并发处理（批量）

2.  面向用户显示内容 → 用流式（stream）
    后台处理或需要结构化输出 → 不用流式（invoke）
    流式 = 好的用户体验
    invoke = 好的程序处理

3.  batch 调用比逐个调用 invoke 快  
    batch = 多个请求同时发出去，等最慢的那个回来
    invoke = 一个一个排队，等前一个完成才发下一个
    有多个独立任务要处理 → 用 batch，速度快很多

4.  默认 batch → 一荣俱荣，一损俱损
    batch + return_exceptions=True → 各自独立，互不影响
    处理批量任务时，建议始终加上 return_exceptions=True
"""
