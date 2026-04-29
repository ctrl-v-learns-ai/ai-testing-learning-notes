# -*- coding: utf-8 -*-
"""
练习1：ChatModel 基本使用
练习目标：学会初始化 ChatModel 并进行简单对话
前置知识：Python 基础，API 概念
核心要点：ChatOpenAI/ChatDeepSeek 初始化，invoke 方法
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# 第一步：加载环境变量
load_dotenv()

# 第二步：初始化 ChatModel
llm = ChatOpenAI(
    model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
    api_key=os.getenv("MIMO_API_KEY"),
    base_url=os.getenv("MIMO_API_URL"),
    temperature=0.7,
)

# 第三步：调用模型
# 方式一：直接传 HumanMessage 列表（推荐）
response = llm.invoke([HumanMessage(content="hello, please introduce yourself")])
print("AI response:", response.content)

# 方式二：包含系统消息，设定 AI 角色
messages = [
    SystemMessage(content="You are a senior software test engineer"),
    HumanMessage(content="What is regression testing?")
]
response = llm.invoke(messages)
print("Test Engineer:", response.content)

# 查看响应对象
print("--- Response Info ---")
print("Type:", type(response))
print("Content:", response.content)

"""
思考题：
1. ChatModel 和普通的 LLM 有什么区别？
2. temperature 参数设为 0 和设为 1.5 会有什么不同的效果？
3. SystemMessage 的作用是什么？
4. 如果你想让 AI 扮演"产品经理"，应该怎么改？
"""
