# -*- coding: utf-8 -*-
"""
练习3：输出解析器使用
练习目标：学会使用 StrOutputParser 和 JsonOutputParser
前置知识：ChatModel 基础、PromptTemplate
核心要点：输出解析器的作用、LCEL 链的组合
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# 初始化模型
llm = ChatOpenAI(
    model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
    api_key=os.getenv("MIMO_API_KEY"),
    base_url=os.getenv("MIMO_API_URL"),
    temperature=0.3,  # 结构化输出时建议用较低温度
)

# ===== 练习3.1：StrOutputParser =====
# 将 AIMessage 转为纯字符串

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个测试专家"),
    ("human", "用一句话解释什么是{concept}")
])

# 使用 LCEL 管道语法组合链
chain = prompt | llm | StrOutputParser()

result = chain.invoke({"concept": "回归测试"})
print("StrOutputParser 结果：")
print(result)
print(f"类型：{type(result)}")
print()

# ===== 练习3.2：JsonOutputParser =====
# 将模型输出解析为结构化 JSON

# 定义输出格式
class TestcaseOutput(BaseModel):
    name: str = Field(description="测试用例名称")
    preconditions: str = Field(description="前置条件")
    steps: list = Field(description="测试步骤列表")
    expected_result: str = Field(description="预期结果")

json_parser = JsonOutputParser(pydantic_object=TestcaseOutput)

json_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个测试专家。请按照以下格式输出：\n{format_instructions}"),
    ("human", "为{module}模块设计一条测试用例")
])

# 使用 partial_variables 注入格式说明
json_chain = json_prompt | llm | json_parser

result = json_chain.invoke({
    "module": "用户登录",
    "format_instructions": json_parser.get_format_instructions()
})
print("JsonOutputParser 结果：")
print(result)
print(f"类型：{type(result)}")
print(f"用例名称：{result.get('name', 'N/A')}")

"""
思考题：
1. StrOutputParser 的作用是什么？如果不加会怎样？

2. JsonOutputParser 中 Field 的 description 参数有什么用？

3. temperature 设为 0.3 和 0.7 对 JSON 输出有什么影响？

4. json_parser.get_format_instructions() 返回的是什么？
"""

"""可以先思考再看答案建议"""

"""
答案建议：
1.  StrOutputParser = 把 AIMessage 对象变成纯字符串
    链的下一步需要字符串 → 加
    直接给用户看结果 → 加
    需要访问 token 用量等元数据 → 不加

2.  Field 的 description 不是给人看的文档，是给模型看的指令。
    写得越精确 → 模型输出越符合预期
    不写或写得模糊 → 模型自由发挥，结果不可控

3.  temperature 越低 → JSON 越稳定、越可预测
    temperature 越高 → JSON 越不稳定、越容易出格式错误
    JSON 输出场景，宁可低一点（0.1~0.3），不要冒高 temperature 的风险。

4.  get_format_instructions() = 自动生成的"输出格式说明书"
    模型看到它 → 知道该输出什么结构的 JSON
    你不塞进 prompt → 模型不知道该输出什么格式 → 输出可能不符合预期
"""