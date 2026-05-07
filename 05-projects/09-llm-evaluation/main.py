# -*- coding: utf-8 -*-
"""
LLM 自动化评估平台 - 主程序
演示批量评估和报告生成
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


class LLMEvaluator:
    """LLM 评估器"""
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
            api_key=os.getenv("MIMO_API_KEY"),
            base_url=os.getenv("MIMO_API_URL"),
            temperature=0.3,
        )
        
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "你是一位测试专家，请用简洁的语言回答问题"),
            ("human", "{question}")
        ])
        
        self.chain = self.prompt | self.llm | StrOutputParser()
    
    def evaluate_single(self, question, expected_keywords):
        """评估单个问题"""
        answer = self.chain.invoke({"question": question})
        
        # 计算关键词匹配度
        matched = sum(1 for kw in expected_keywords if kw in answer)
        keyword_score = matched / len(expected_keywords)
        
        return {
            "question": question,
            "answer": answer,
            "keyword_score": keyword_score,
            "passed": keyword_score >= 0.5
        }
    
    def batch_evaluate(self, test_cases):
        """批量评估"""
        results = []
        
        for case in test_cases:
            result = self.evaluate_single(
                case["question"],
                case["keywords"]
            )
            results.append(result)
        
        return results
    
    def generate_report(self, results):
        """生成评估报告"""
        total = len(results)
        passed = sum(1 for r in results if r["passed"])
        failed = total - passed
        
        avg_score = sum(r["keyword_score"] for r in results) / total
        
        report = f"""
# LLM 评估报告

## 总体指标
- 测试用例数：{total}
- 通过数：{passed}
- 失败数：{failed}
- 通过率：{passed/total:.2%}
- 平均关键词匹配度：{avg_score:.2%}

## 详细结果
"""
        
        for r in results:
            status = "✓" if r["passed"] else "✗"
            report += f"\n{status} 问题：{r['question']}"
            report += f"\n   回答：{r['answer'][:50]}..."
            report += f"\n   关键词匹配度：{r['keyword_score']:.2%}\n"
        
        return report


def main():
    """主函数"""
    print("=" * 60)
    print("  LLM 自动化评估平台")
    print("=" * 60)
    
    evaluator = LLMEvaluator()
    
    # 测试用例
    test_cases = [
        {"question": "什么是单元测试？", "keywords": ["测试", "单元", "代码"]},
        {"question": "什么是集成测试？", "keywords": ["测试", "集成", "模块"]},
        {"question": "什么是回归测试？", "keywords": ["测试", "回归", "修改"]},
        {"question": "什么是性能测试？", "keywords": ["测试", "性能", "速度"]},
    ]
    
    # 批量评估
    print("\n[1] 批量评估")
    results = evaluator.batch_evaluate(test_cases)
    
    # 生成报告
    print("\n[2] 生成报告")
    report = evaluator.generate_report(results)
    print(report)
    
    # 保存报告
    with open("evaluation_report.md", "w", encoding="utf-8") as f:
        f.write(report)
    print("\n报告已保存：evaluation_report.md")


if __name__ == "__main__":
    main()
