# -*- coding: utf-8 -*-
"""
练习5：综合练习 - 缺陷报告生成器
练习目标：综合运用 Model I/O 所有知识点
前置知识：ChatModel、PromptTemplate、OutputParser、LCEL
核心要点：端到端构建一个完整的 AI 应用
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# 定义缺陷报告的输出格式
class BugReport(BaseModel):
    title: str = Field(description="缺陷标题")
    severity: str = Field(description="严重程度：P0/P1/P2/P3")
    module: str = Field(description="所属模块")
    steps_to_reproduce: list = Field(description="复现步骤列表")
    expected_result: str = Field(description="预期结果")
    actual_result: str = Field(description="实际结果")
    suggestion: str = Field(description="修复建议")

# 初始化模型
llm = ChatOpenAI(
    model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
    api_key=os.getenv("MIMO_API_KEY"),
    base_url=os.getenv("MIMO_API_URL"),
    temperature=0.3,
)

# 创建解析器
parser = JsonOutputParser(pydantic_object=BugReport)

# 创建提示模板
prompt = ChatPromptTemplate.from_messages([
    ("system", """你是一位资深测试工程师。根据用户描述的问题，生成一份标准的缺陷报告。
请严格按照以下JSON格式输出：
{format_instructions}"""),
    ("human", "模块：{module}\n现象：{symptom}")
])

# 组合链
chain = prompt | llm | parser

# 调用
result = chain.invoke({
    "module": "用户登录",
    "symptom": "输入正确密码后页面白屏，控制台报500错误",
    "format_instructions": parser.get_format_instructions()
})

print("=== 缺陷报告 ===")
print(f"标题：{result['title']}")
print(f"严重程度：{result['severity']}")
print(f"所属模块：{result['module']}")
print(f"复现步骤：")
for i, step in enumerate(result['steps_to_reproduce'], 1):
    print(f"  {i}. {step}")
print(f"预期结果：{result['expected_result']}")
print(f"实际结果：{result['actual_result']}")
print(f"修复建议：{result['suggestion']}")

"""
思考题：
1. 这个缺陷报告生成器用到了本阶段哪些知识点？

2. temperature 设为 0.3 的原因是什么？

3. 如果要支持多种输出格式（JSON/Markdown/纯文本），应该怎么设计？

4. 这个工具对你的测试工作有什么帮助？还能扩展哪些功能？
"""

"""可以先思考再看答案建议"""

"""
1.  ChatModel 初始化
    ChatPromptTemplate
    OutputParser + Pydantic
    LCEL 链式组合
    链的调用

2.  这里设 0.3 的原因是缺陷报告需要结构化、可预测的输出：
        JSON 格式必须严格正确
        严重程度只能是 P0/P1/P2/P3
        复现步骤要基于描述，不能瞎编
    如果设成 1.0，LLM 可能会：
        输出格式不稳定（有时 JSON，有时纯文本）
        严重程度给出 "紧急"、"非常严重" 这种非标准值
        复现步骤加入不存在的细节
        
3.  新建两个json转md和text的方法，先统一生成 JSON，再按格式转换

4.  这个工具不是替代你写报告，而是让你专注于发现问题，把写报告的重复劳动交给 AI。
"""