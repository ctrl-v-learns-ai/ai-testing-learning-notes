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
