# -*- coding: utf-8 -*-
"""
练习2：PromptTemplate 使用
练习目标：学会使用 PromptTemplate 构建动态提示
前置知识：Python 字符串格式化
核心要点：PromptTemplate 创建、变量替换、模板语法
"""

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

# ===== 练习2.1：PromptTemplate（简单文本模板）=====
# 适用场景：简单的文本格式化，不需要区分角色

# 创建模板
template = PromptTemplate(
    template="你是一个{role}。请用{style}的风格回答：{question}",
    input_variables=["role", "style", "question"]
)

# 格式化输出
prompt = template.format(
    role="测试工程师",
    style="专业",
    question="如何设计边界值测试？"
)
print("PromptTemplate 输出：")
print(prompt)
print()

# ===== 练习2.2：ChatPromptTemplate（聊天模板）=====
# 适用场景：需要区分系统消息和用户消息的对话场景

# 从元组列表创建（最常用的方式）
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个{role}，专注于{domain}领域"),
    ("human", "{question}")
])

# 格式化为消息列表
messages = chat_prompt.format_messages(
    role="测试工程师",
    domain="电商系统",
    question="如何设计购物车的测试用例？"
)

print("ChatPromptTemplate 输出：")
for msg in messages:
    print(f"[{msg.type}] {msg.content}")

# ===== 练习2.3：模板的高级用法 =====

# 使用 partial_variables 预设部分变量
prompt_with_role = ChatPromptTemplate.from_messages([
    ("system", "你是一个{role}"),
    ("human", "{question}")
]).partial(role="资深测试工程师")

# 只需提供剩余变量
messages = prompt_with_role.format_messages(question="如何做性能测试？")
print("\nPartial 变量输出：")
for msg in messages:
    print(f"[{msg.type}] {msg.content}")

"""
思考题：
1. PromptTemplate 和 ChatPromptTemplate 的区别是什么？什么时候用哪个？

2. from_messages 方法中 ("system", "...") 和 ("human", "...") 分别代表什么？

3. partial 方法的作用是什么？什么场景下会用到？

4. 如果模板中有变量但调用时没有提供，会发生什么？
"""
