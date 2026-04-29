# -*- coding: utf-8 -*-
"""
练习4：复杂链组合 - 文档分析管道
练习目标：综合运用 LCEL 构建复杂的分析管道
前置知识：基础链、并行链、自定义函数
核心要点：多步骤链的组合与嵌套
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
    api_key=os.getenv("MIMO_API_KEY"),
    base_url=os.getenv("MIMO_API_URL"),
    temperature=0.3,
)

# ===== 构建文档分析管道 =====
print("=== 文档分析管道 ===")

# 步骤1：文本预处理
def preprocess(data):
    """清理和准备文本"""
    text = data["text"].strip()
    word_count = len(text.split())
    return {"text": text, "word_count": word_count}

# 步骤2：并行分析（摘要 + 关键词 + 情感）
summary_prompt = ChatPromptTemplate.from_messages([
    ("system", "用一句话总结以下内容"),
    ("human", "{text}")
])
summary_chain = summary_prompt | llm | StrOutputParser()

keywords_prompt = ChatPromptTemplate.from_messages([
    ("system", "提取3个关键词，用逗号分隔"),
    ("human", "{text}")
])
keywords_chain = keywords_prompt | llm | StrOutputParser()

sentiment_prompt = ChatPromptTemplate.from_messages([
    ("system", "判断文本情感：积极/消极/中性"),
    ("human", "{text}")
])
sentiment_chain = sentiment_prompt | llm | StrOutputParser()

# 并行分析
analysis_parallel = RunnableParallel(
    summary=summary_chain,
    keywords=keywords_chain,
    sentiment=sentiment_chain
)

# 步骤3：生成报告
report_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个报告生成专家"),
    ("human", """根据以下分析结果生成报告：
    
摘要：{summary}
关键词：{keywords}
情感：{sentiment}

请生成一段简洁的分析报告。""")
])
report_chain = report_prompt | llm | StrOutputParser()

# 组合完整管道
full_chain = (
    RunnableLambda(preprocess)  # 预处理
    | analysis_parallel         # 并行分析
    | report_chain              # 生成报告
)

# 测试
test_text = """
软件测试是软件开发过程中不可或缺的一部分。
通过系统化的测试，我们可以发现软件中的缺陷，
确保软件产品满足用户需求。
测试不仅提高了软件质量，还降低了维护成本。
"""

print("输入文本：", test_text[:50], "...")
print("\n分析报告：")
result = full_chain.invoke({"text": test_text})
print(result)

"""
思考题：
1. 这个管道的数据流是怎样的？
2. 为什么并行分析后可以直接传给 report_chain？
3. 如果某个并行任务失败了，整个管道会怎样？
4. 如何给这个管道添加错误处理？
"""
