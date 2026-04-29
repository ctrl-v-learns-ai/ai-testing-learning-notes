# -*- coding: utf-8 -*-
"""
提示模板模块
"""

from langchain_core.prompts import ChatPromptTemplate

# 摘要提示
SUMMARY_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "你是一个文本摘要专家。请用一句话简洁地总结以下内容。"),
    ("human", "{text}")
])

# 关键词提取提示
KEYWORDS_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "你是一个关键词提取专家。请从以下内容中提取3-5个关键词，用逗号分隔。"),
    ("human", "{text}")
])

# 情感分析提示
SENTIMENT_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "你是一个情感分析专家。请判断以下文本的情感倾向，只回答：积极/消极/中性"),
    ("human", "{text}")
])

# 报告生成提示
REPORT_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "你是一个报告生成专家"),
    ("human", """根据以下分析结果生成一份简洁的分析报告：

摘要：{summary}
关键词：{keywords}
情感倾向：{sentiment}

请生成一段结构清晰的分析报告。""")
])
