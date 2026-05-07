# -*- coding: utf-8 -*-
"""
练习14：提示工程基础
练习目标：掌握基本的提示设计技巧
前置知识：LangChain 基础
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

# 练习14.1：角色设定
print("=== 练习14.1：角色设定 ===")

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一位资深的软件测试工程师，拥有10年测试经验，擅长自动化测试和性能测试"),
    ("human", "{question}")
])

chain = prompt | llm | StrOutputParser()
result = chain.invoke({"question": "什么是回归测试？"})
print(f"回答：{result}")

# 练习14.2：提供示例（少样本提示）
print("\n=== 练习14.2：少样本提示 ===")

prompt = ChatPromptTemplate.from_messages([
    ("system", "请将句子分类为正面或负面"),
    ("human", "句子：今天天气真好"),
    ("ai", "分类：正面"),
    ("human", "句子：这部电影太无聊了"),
    ("ai", "分类：负面"),
    ("human", "句子：{sentence}")
])

chain = prompt | llm | StrOutputParser()
result = chain.invoke({"sentence": "这个餐厅的菜很好吃"})
print(f"分类结果：{result}")

# 练习14.3：指定输出格式
print("\n=== 练习14.3：指定输出格式 ===")

prompt = ChatPromptTemplate.from_messages([
    ("system", """请将用户信息提取为 JSON 格式，严格按以下格式输出：
{{
  "name": "姓名",
  "age": 年龄,
  "city": "城市",
  "job": "职业"
}}"""),
    ("human", "{info}")
])

chain = prompt | llm | StrOutputParser()
result = chain.invoke({"info": "张三，25岁，北京，工程师"})
print(f"JSON 输出：\n{result}")

# 练习14.4：分隔符使用
print("\n=== 练习14.4：分隔符使用 ===")

prompt = ChatPromptTemplate.from_messages([
    ("system", """请分析以下代码的潜在问题：

---代码开始---
{code}
---代码结束---

请指出：
1. 可能的异常情况
2. 改进建议"""),
    ("human", "请分析这段代码")
])

chain = prompt | llm | StrOutputParser()
result = chain.invoke({"code": "def divide(a, b): return a / b"})
print(f"分析结果：\n{result}")

# 练习14.5：长度限制
print("\n=== 练习14.5：长度限制 ===")

prompt = ChatPromptTemplate.from_messages([
    ("system", "请用50字以内回答问题"),
    ("human", "{question}")
])

chain = prompt | llm | StrOutputParser()
result = chain.invoke({"question": "什么是机器学习？"})
print(f"简短回答：{result}")

"""
思考题：
1. 提示的基本结构是什么？
2. 零样本和少样本提示的区别？
3. 为什么使用分隔符？
4. 如何控制输出格式？
5. 如何限制输出长度？
"""
