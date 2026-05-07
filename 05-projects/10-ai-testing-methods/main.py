# -*- coding: utf-8 -*-
"""
测试用例生成器 - 主程序
演示使用 AI 自动生成测试用例
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


class TestCaseGenerator:
    """测试用例生成器"""
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
            api_key=os.getenv("MIMO_API_KEY"),
            base_url=os.getenv("MIMO_API_URL"),
            temperature=0.3,
        )
        
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """你是一位资深的测试工程师，擅长设计全面的测试用例。

请按以下格式生成测试用例：
---
测试用例 #N
名称：[用例名称]
类型：[正常/边界/异常]
前置条件：[前置条件]
输入：[输入参数]
预期输出：[预期结果]
测试目的：[目的]
---"""),
            ("human", "请为以下功能生成测试用例：\n{function_desc}")
        ])
        
        self.chain = self.prompt | self.llm | StrOutputParser()
    
    def generate_test_cases(self, function_desc):
        """生成测试用例"""
        return self.chain.invoke({"function_desc": function_desc})
    
    def analyze_boundary(self, function_desc):
        """分析边界条件"""
        prompt = ChatPromptTemplate.from_messages([
            ("system", """请分析以下功能的边界条件：

1. 输入参数的边界值
2. 输出结果的边界值
3. 特殊情况
4. 异常场景"""),
            ("human", "功能描述：{function_desc}")
        ])
        
        chain = prompt | self.llm | StrOutputParser()
        return chain.invoke({"function_desc": function_desc})


def main():
    """主函数"""
    print("=" * 60)
    print("  测试用例生成器")
    print("=" * 60)
    
    generator = TestCaseGenerator()
    
    # 示例功能描述
    function_desc = """
    函数名：calculate_discount
    输入：price (float), membership (str)
    输出：discounted_price (float)
    
    功能说明：
    - 根据会员等级计算折扣
    - 普通会员：9折
    - 银卡会员：8折
    - 金卡会员：7折
    - 钻石会员：6折
    - 价格不能为负数
    - 会员等级必须有效
    """
    
    # 生成测试用例
    print("\n[1] 生成测试用例")
    test_cases = generator.generate_test_cases(function_desc)
    print(test_cases)
    
    # 分析边界条件
    print("\n[2] 分析边界条件")
    boundary_analysis = generator.analyze_boundary(function_desc)
    print(boundary_analysis)
    
    # 保存结果
    with open("test_cases.md", "w", encoding="utf-8") as f:
        f.write("# 测试用例\n\n")
        f.write(test_cases)
        f.write("\n\n# 边界条件分析\n\n")
        f.write(boundary_analysis)
    print("\n结果已保存：test_cases.md")


if __name__ == "__main__":
    main()
