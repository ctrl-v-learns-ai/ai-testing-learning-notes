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
    temperature=1.0,
)

# 第三步：调用模型
# 方式一：直接传 HumanMessage 列表（推荐）
response = llm.invoke([HumanMessage(content="hello, please introduce yourself")])
print("AI response:", response.content)

# 方式二：包含系统消息，设定 AI 角色
messages = [
    SystemMessage(content="你是一名高级软件测试工程师"),
    HumanMessage(content="什么是回归测试？")
]
response = llm.invoke(messages)
print("测试工程师:", response.content)

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

"""可以先思考再看答案建议"""

"""
答案建议：
1. LLM 是文本补全，ChatModel 是对话补全。

2. 把它想象成创造力的旋钮：拧到 0 是严谨的工程师，拧到 1.5 是喝醉了的诗人。

3. SystemMessage = 给模型的角色卡 + 操作手册
   它不参与"对话内容"，而是定义对话的"游戏规则"。

4. 你是一个拥有 8 年经验的互联网产品经理，擅长：
    - 需求分析与用户调研
    - PRD（产品需求文档）撰写
    - 竞品分析
    - 数据驱动的决策
    
    工作风格：
    - 回答问题时先梳理背景和目标，再给出方案
    - 用结构化的方式表达（编号、表格、优先级排序）
    - 会主动追问不明确的需求
    - 涉及取舍时，给出理由而不是只给结论

    SystemMessage 的质量直接决定 AI 回答的质量
    一个写得好的 SystemMessage = 身份 + 经验 + 领域 + 风格 + 输出规范
    一个写得差的 SystemMessage = "你是产品经理"（五个字，效果约等于没有）
"""