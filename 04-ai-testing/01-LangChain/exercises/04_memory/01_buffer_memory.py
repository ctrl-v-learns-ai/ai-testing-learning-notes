# -*- coding: utf-8 -*-
"""
练习1：ConversationBufferMemory 基础记忆
练习目标：学会使用 ConversationBufferMemory 管理对话历史
前置知识：ChatModel、PromptTemplate
核心要点：记忆的创建、保存、加载
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

load_dotenv()

# ===== 练习1.1：基本记忆操作 =====
print("=== 基本记忆操作 ===")

# 创建记忆
memory = ConversationBufferMemory(
    return_messages=True,  # 返回消息列表格式
    memory_key="history"   # 在模板中使用的变量名
)

# 保存第一轮对话
memory.save_context(
    {"input": "你好，我叫张三"},
    {"output": "你好张三！有什么可以帮你的？"}
)

# 保存第二轮对话
memory.save_context(
    {"input": "我喜欢Python编程"},
    {"output": "Python是个很好的语言！你用Python做什么项目？"}
)

# 获取历史
history = memory.load_memory_variables({})
print("对话历史：")
for msg in history["history"]:
    print(f"  [{msg.type}] {msg.content}")

# ===== 练习1.2：记忆的持久化问题 =====
print("\n=== 记忆的持久化问题 ===")

# 注意：ConversationBufferMemory 是内存存储
# 程序退出后历史会丢失
print(f"当前历史条数：{len(memory.chat_memory.messages)}")

# 清空记忆
memory.clear()
print(f"清空后历史条数：{len(memory.chat_memory.messages)}")

"""
思考题：
1. return_messages=True 和 False 有什么区别？
2. memory_key 的作用是什么？
3. 为什么说 ConversationBufferMemory 是"内存存储"？
4. 如果要持久化保存对话历史，应该怎么做？
"""
