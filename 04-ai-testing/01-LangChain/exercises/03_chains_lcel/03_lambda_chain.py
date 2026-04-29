# -*- coding: utf-8 -*-
"""
练习3：RunnableLambda 自定义函数
练习目标：学会在 LCEL 链中使用自定义函数
前置知识：基础 LCEL 链
核心要点：RunnableLambda 的使用、数据预处理和后处理
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
    api_key=os.getenv("MIMO_API_KEY"),
    base_url=os.getenv("MIMO_API_URL"),
    temperature=0.7,
)

# ===== 练习3.1：使用 RunnableLambda 进行数据预处理 =====
print("=== 数据预处理 ===")

def clean_text(text_data):
    """清理文本：去除多余空白"""
    cleaned = text_data["text"].strip().replace("\n", " ")
    return {"text": cleaned}

# 将函数转换为 Runnable
clean_runnable = RunnableLambda(clean_text)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个文本分析专家"),
    ("human", "分析以下文本的主题：{text}")
])

# 链：预处理 -> 提示 -> 模型 -> 解析
chain = clean_runnable | prompt | llm | StrOutputParser()

result = chain.invoke({"text": "  \n  软件测试是确保软件质量的重要手段  \n  "})
print(f"分析结果：{result}")

# ===== 练习3.2：使用 RunnableLambda 进行数据后处理 =====
print("\n=== 数据后处理 ===")

def format_output(text):
    """格式化输出：添加标记"""
    return f"【分析结果】{text}"

format_runnable = RunnableLambda(format_output)

# 链：提示 -> 模型 -> 解析 -> 后处理
chain2 = prompt | llm | StrOutputParser() | format_runnable

result2 = chain2.invoke({"text": "Python是一种流行的编程语言"})
print(f"格式化结果：{result2}")

# ===== 练习3.3：使用 lambda 表达式 =====
print("\n=== Lambda 表达式 ===")

# 简单的 lambda 也可以
to_upper = RunnableLambda(lambda x: x.upper())

chain3 = prompt | llm | StrOutputParser() | to_upper
result3 = chain3.invoke({"text": "hello world"})
print(f"大写结果：{result3}")

"""
思考题：
1. RunnableLambda 和普通函数有什么区别？
2. 什么时候需要预处理？什么时候需要后处理？
3. lambda 表达式和命名函数各适合什么场景？
"""
