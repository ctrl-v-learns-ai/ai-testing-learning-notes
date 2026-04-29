# -*- coding: utf-8 -*-
"""
练习2：RunnableParallel 并行执行
练习目标：学会使用 RunnableParallel 并行处理多个任务
前置知识：基础 LCEL 链
核心要点：并行执行、结果合并
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
    api_key=os.getenv("MIMO_API_KEY"),
    base_url=os.getenv("MIMO_API_URL"),
    temperature=0.7,
)

# ===== 练习2.1：并行执行两个任务 =====
print("=== 并行执行 ===")

# 链1：生成摘要
summary_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个文本摘要专家"),
    ("human", "请用一句话总结以下内容：{text}")
])
summary_chain = summary_prompt | llm | StrOutputParser()

# 链2：提取关键词
keywords_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个关键词提取专家"),
    ("human", "请从以下内容中提取3个关键词，用逗号分隔：{text}")
])
keywords_chain = keywords_prompt | llm | StrOutputParser()

# 使用 RunnableParallel 并行执行
parallel_chain = RunnableParallel(
    summary=summary_chain,
    keywords=keywords_chain
)

# 测试文本
test_text = """
软件测试是软件开发过程中不可或缺的一部分。
它包括单元测试、集成测试、系统测试和验收测试等多种类型。
测试的目的是发现软件中的缺陷，确保软件质量。
"""

# 调用并行链
result = parallel_chain.invoke({"text": test_text})

print(f"摘要：{result['summary']}")
print(f"关键词：{result['keywords']}")

# ===== 练习2.2：并行链与顺序链组合 =====
print("\n=== 并行 + 顺序组合 ===")

# 先并行处理，再合并结果
final_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个报告生成专家"),
    ("human", "根据以下摘要和关键词，生成一段分析报告：\n摘要：{summary}\n关键词：{keywords}")
])
final_chain = final_prompt | llm | StrOutputParser()

# 组合：并行 -> 顺序
full_chain = parallel_chain | final_chain

report = full_chain.invoke({"text": test_text})
print(f"分析报告：{report}")

"""
思考题：
1. RunnableParallel 和直接顺序执行有什么区别？
2. 并行链的结果格式是什么？怎么访问？
3. 什么时候应该使用并行执行？
"""
