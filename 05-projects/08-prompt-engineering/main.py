# -*- coding: utf-8 -*-
"""
提示词优化工具 - 主程序
演示提示词 A/B 测试和效果评估
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


class PromptOptimizer:
    """提示词优化器"""
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
            api_key=os.getenv("MIMO_API_KEY"),
            base_url=os.getenv("MIMO_API_URL"),
            temperature=0.3,
        )
        self.prompts = {}
        self.results = {}
    
    def add_prompt(self, name, system_message, human_template):
        """添加提示词模板"""
        self.prompts[name] = ChatPromptTemplate.from_messages([
            ("system", system_message),
            ("human", human_template)
        ])
    
    def test_prompt(self, name, question):
        """测试提示词"""
        if name not in self.prompts:
            return None
        
        chain = self.prompts[name] | self.llm | StrOutputParser()
        return chain.invoke({"question": question})
    
    def ab_test(self, prompt_a, prompt_b, test_cases):
        """A/B 测试"""
        results_a = []
        results_b = []
        
        for case in test_cases:
            result_a = self.test_prompt(prompt_a, case)
            result_b = self.test_prompt(prompt_b, case)
            
            results_a.append(result_a)
            results_b.append(result_b)
        
        return {
            "prompt_a": results_a,
            "prompt_b": results_b
        }
    
    def evaluate_response(self, response, criteria):
        """评估回答质量"""
        score = 0
        
        # 检查关键词
        for keyword in criteria.get("keywords", []):
            if keyword in response:
                score += 1
        
        # 检查长度
        min_length = criteria.get("min_length", 0)
        if len(response) >= min_length:
            score += 1
        
        return score


def main():
    """主函数"""
    print("=" * 60)
    print("  提示词优化工具")
    print("=" * 60)
    
    optimizer = PromptOptimizer()
    
    # 添加两个不同风格的提示词
    optimizer.add_prompt(
        "简洁版",
        "请简洁地回答问题",
        "{question}"
    )
    
    optimizer.add_prompt(
        "详细版",
        "你是一位资深的测试工程师，请详细、专业地回答问题，包含示例和最佳实践",
        "{question}"
    )
    
    # 测试用例
    test_cases = [
        "什么是单元测试？",
        "如何设计测试用例？",
        "什么是回归测试？"
    ]
    
    # A/B 测试
    print("\n[1] A/B 测试")
    results = optimizer.ab_test("简洁版", "详细版", test_cases)
    
    for i, case in enumerate(test_cases):
        print(f"\n问题：{case}")
        print(f"简洁版回答：{results['prompt_a'][i][:100]}...")
        print(f"详细版回答：{results['prompt_b'][i][:100]}...")
    
    # 效果评估
    print("\n[2] 效果评估")
    criteria = {"keywords": ["测试", "用例", "验证"], "min_length": 50}
    
    for i, case in enumerate(test_cases):
        score_a = optimizer.evaluate_response(results["prompt_a"][i], criteria)
        score_b = optimizer.evaluate_response(results["prompt_b"][i], criteria)
        
        print(f"\n问题：{case}")
        print(f"简洁版得分：{score_a}")
        print(f"详细版得分：{score_b}")


if __name__ == "__main__":
    main()
