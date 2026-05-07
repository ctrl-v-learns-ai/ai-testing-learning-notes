# -*- coding: utf-8 -*-
"""
提示模板模块
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 客服系统提示
CUSTOMER_SERVICE_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """你是一位专业的客服机器人，名叫"小助"。
你的职责是：
1. 耐心解答用户的问题
2. 记住用户之前说过的信息
3. 提供友好的服务体验

请用简洁、友好的语言回答用户的问题。"""),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])
