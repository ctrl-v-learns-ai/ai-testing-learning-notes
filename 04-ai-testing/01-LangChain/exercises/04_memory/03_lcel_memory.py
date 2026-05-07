# -*- coding: utf-8 -*-
"""
练习3：LCEL 方式实现记忆
练习目标：学会使用 RunnableWithMessageHistory 实现记忆
前置知识：LCEL 链、Memory 基础
核心要点：RunnableWithMessageHistory 的使用
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
    api_key=os.getenv("MIMO_API_KEY"),
    base_url=os.getenv("MIMO_API_URL"),
    temperature=0.7,
)

# ===== 练习3.1：创建带记忆的链 =====
print("=== LCEL 记忆链 ===")

# 创建提示模板（包含历史占位符）
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个友好的助手，能记住之前的对话"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# 创建基础链
chain = prompt | llm | StrOutputParser()

# 创建会话存储
store = {}

def get_session_history(session_id: str):
    """获取或创建会话历史"""
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 包装链，添加记忆功能
with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

# ===== 练习3.2：多轮对话测试 =====
print("\n=== 多轮对话测试 ===")

# 配置会话 ID
config = {"configurable": {"session_id": "user_001"}}

# 第一轮
response1 = with_memory.invoke({"input": "你好，我叫李四"}, config=config)
print(f"用户：你好，我叫李四")
print(f"AI：{response1}")

# 第二轮（测试是否记住名字）
response2 = with_memory.invoke({"input": "我叫什么名字？"}, config=config)
print(f"\n用户：我叫什么名字？")
print(f"AI：{response2}")

# 第三轮
response3 = with_memory.invoke({"input": "我喜欢Python编程"}, config=config)
print(f"\n用户：我喜欢Python编程")
print(f"AI：{response3}")

# 第四轮（测试是否记住兴趣）
response4 = with_memory.invoke({"input": "我之前说了我喜欢什么？"}, config=config)
print(f"\n用户：我之前说了我喜欢什么？")
print(f"AI：{response4}")

# ===== 练习3.3：多用户独立历史 =====
print("\n=== 多用户独立历史 ===")

# 不同的 session_id 是独立的历史
config2 = {"configurable": {"session_id": "user_002"}}

response5 = with_memory.invoke({"input": "你好，我叫王五"}, config=config2)
print(f"用户002：你好，我叫王五")
print(f"AI：{response5}")

# 用户001的历史不会影响用户002
response6 = with_memory.invoke({"input": "我叫什么？"}, config=config2)
print(f"\n用户002：我叫什么？")
print(f"AI：{response6}")

"""
思考题：
1. MessagesPlaceholder 的作用是什么？
2. session_id 的作用是什么？如何实现多用户？
3. RunnableWithMessageHistory 和 ConversationChain 有什么区别？
4. 如果要持久化保存历史，应该怎么修改？
"""
