# -*- coding: utf-8 -*-
"""
练习15：高级提示技巧
练习目标：掌握思维链、反思等高级提示技巧
前置知识：提示工程基础
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# 初始化模型
llm = ChatOpenAI(
    model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
    api_key=os.getenv("MIMO_API_KEY"),
    base_url=os.getenv("MIMO_API_URL"),
    temperature=0.7,
)

# 练习15.1：思维链提示
print("=== 练习15.1：思维链提示 ===")

prompt = ChatPromptTemplate.from_messages([
    ("system", """请逐步解决问题，按以下格式输出：
步骤1：[分析]
步骤2：[推理]
步骤3：[结论]"""),
    ("human", "{question}")
])

chain = prompt | llm | StrOutputParser()
result = chain.invoke({"question": "一个商店有15个苹果，卖掉了8个，又进了12个，现在有多少个？"})
print(f"思维链解答：\n{result}")

# 练习15.2：自我反思
print("\n=== 练习15.2：自我反思 ===")

prompt = ChatPromptTemplate.from_messages([
    ("system", """请完成任务后进行自我反思：

1. 先完成任务
2. 检查结果是否正确
3. 分析是否有改进空间
4. 给出改进版本（如果需要）"""),
    ("human", "{task}")
])

chain = prompt | llm | StrOutputParser()
result = chain.invoke({"task": "写一个函数计算斐波那契数列"})
print(f"反思结果：\n{result}")

# 练习15.3：多方案对比
print("\n=== 练习15.3：多方案对比 ===")

prompt = ChatPromptTemplate.from_messages([
    ("system", """请用三种不同的方法解决问题，并对比优缺点：

方法一：[方法名]
  - 优点：
  - 缺点：

方法二：[方法名]
  - 优点：
  - 缺点：

方法三：[方法名]
  - 优点：
  - 缺点：

最终建议："""),
    ("human", "{problem}")
])

chain = prompt | llm | StrOutputParser()
result = chain.invoke({"problem": "如何对一个大文件进行排序？"})
print(f"多方案对比：\n{result}")

# 练习15.4：结构化输出
print("\n=== 练习15.4：结构化输出 ===")

prompt = ChatPromptTemplate.from_messages([
    ("system", """请按以下格式生成测试用例：

---
测试用例 #1
名称：[用例名称]
前置条件：[前置条件]
输入：[输入参数]
预期输出：[预期结果]
测试目的：[目的]
---

请生成至少3个测试用例。"""),
    ("human", "函数：calculate_discount(price: float, membership: str) -> float")
])

chain = prompt | llm | StrOutputParser()
result = chain.invoke({})
print(f"测试用例：\n{result}")

# 练习15.5：约束提示
print("\n=== 练习15.5：约束提示 ===")

prompt = ChatPromptTemplate.from_messages([
    ("system", """请写一个 Python 函数，要求：

必须满足：
1. 函数名：validate_email
2. 输入：字符串
3. 输出：布尔值
4. 使用正则表达式
5. 添加类型提示

禁止：
1. 不要使用第三方库
2. 不要超过 15 行代码"""),
    ("human", "请实现邮箱验证函数")
])

chain = prompt | llm | StrOutputParser()
result = chain.invoke({})
print(f"约束代码：\n{result}")

"""
思考题：
1. 什么是思维链提示？
2. 自我反思提示的作用是什么？
3. 多方案对比适合什么场景？
4. 如何设计结构化输出？
5. 约束提示的好处是什么？
"""
