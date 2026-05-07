# -*- coding: utf-8 -*-
"""
练习2：ConversationSummaryMemory 摘要记忆
练习目标：学会使用摘要记忆处理长对话
前置知识：ConversationBufferMemory
核心要点：自动摘要、节省 Token
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationSummaryMemory

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
    api_key=os.getenv("MIMO_API_KEY"),
    base_url=os.getenv("MIMO_API_URL"),
    temperature=0.3,
)

# ===== 练习2.1：摘要记忆 =====
print("=== 摘要记忆 ===")

# 创建摘要记忆（需要 LLM 来生成摘要）
memory = ConversationSummaryMemory(
    llm=llm,
    return_messages=True,
    memory_key="history"
)

# 模拟多轮对话
conversations = [
    ("我正在做一个电商项目，用Python开发", "好的，Python很适合Web开发"),
    ("主要功能包括用户注册、商品浏览、购物车", "这些是电商的核心功能"),
    ("我现在在做购物车模块", "购物车需要考虑库存、价格计算等"),
    ("遇到了一个问题，并发下单时库存会超卖", "这是经典的并发问题，需要用锁机制"),
]

for user_input, ai_output in conversations:
    memory.save_context({"input": user_input}, {"output": ai_output})

# 获取摘要（而不是完整历史）
history = memory.load_memory_variables({})
print("摘要记忆：")
print(history["history"])

# ===== 练习2.2：对比 Buffer 和 Summary =====
print("\n=== 对比 Buffer 和 Summary ===")

from langchain.memory import ConversationBufferMemory

buffer_memory = ConversationBufferMemory(return_messages=True, memory_key="history")

# 保存相同的对话
for user_input, ai_output in conversations:
    buffer_memory.save_context({"input": user_input}, {"output": ai_output})

print(f"Buffer 历史条数：{len(buffer_memory.chat_memory.messages)}")
print(f"Buffer 总字符数：{sum(len(m.content) for m in buffer_memory.chat_memory.messages)}")

print(f"\nSummary 内容：")
print(history["history"])

"""
思考题：
1. SummaryMemory 比 BufferMemory 节省了多少 Token？
2. SummaryMemory 的缺点是什么？
3. 什么时候用 BufferMemory？什么时候用 SummaryMemory？
4. 摘要是怎么生成的？用的是哪个模型？
"""
