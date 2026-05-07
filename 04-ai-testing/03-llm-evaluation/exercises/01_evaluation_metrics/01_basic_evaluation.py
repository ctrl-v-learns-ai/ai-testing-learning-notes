# -*- coding: utf-8 -*-
"""
练习16：LLM 评估基础
练习目标：掌握 LLM 评估的基本方法
前置知识：LangChain 基础
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
    temperature=0.3,
)

# 练习16.1：准确性评估
print("=== 练习16.1：准确性评估 ===")

def evaluate_accuracy(predicted, expected):
    """评估回答是否正确"""
    # 简单的关键词匹配
    expected_keywords = expected.split()
    matched = sum(1 for keyword in expected_keywords if keyword in predicted)
    return matched / len(expected_keywords)

# 测试
question = "什么是回归测试？"
expected = "回归测试是修改代码后重新测试"

prompt = ChatPromptTemplate.from_messages([
    ("system", "请用一句话回答问题"),
    ("human", "{question}")
])

chain = prompt | llm | StrOutputParser()
answer = chain.invoke({"question": question})

accuracy = evaluate_accuracy(answer, expected)
print(f"问题：{question}")
print(f"回答：{answer}")
print(f"期望：{expected}")
print(f"准确率：{accuracy:.2%}")

# 练习16.2：相关性评估
print("\n=== 练习16.2：相关性评估 ===")

def evaluate_relevance_simple(question, answer):
    """简单相关性评估"""
    # 检查问题关键词是否在回答中出现
    question_keywords = set(question.replace("？", "").replace("?", "").split())
    answer_keywords = set(answer.split())
    
    overlap = question_keywords & answer_keywords
    relevance = len(overlap) / len(question_keywords) if question_keywords else 0
    
    return relevance

relevance = evaluate_relevance_simple(question, answer)
print(f"相关性：{relevance:.2%}")

# 练习16.3：完整性评估
print("\n=== 练习16.3：完整性评估 ===")

def evaluate_completeness(answer, required_points):
    """评估回答的完整性"""
    covered = sum(1 for point in required_points if point in answer)
    return covered / len(required_points)

required_points = ["修改", "重新测试", "没有引入新错误"]
completeness = evaluate_completeness(answer, required_points)
print(f"完整性：{completeness:.2%}")

# 练习16.4：使用 LLM 作为评估器
print("\n=== 练习16.4：LLM 作为评估器 ===")

eval_prompt = ChatPromptTemplate.from_messages([
    ("system", """请评估以下回答的质量，给出1-10分的评分：

评估标准：
- 准确性（4分）：回答是否正确
- 完整性（3分）：回答是否完整
- 清晰度（3分）：回答是否清晰

请按以下格式输出：
分数：X/10
理由：..."""),
    ("human", "问题：{question}\n回答：{answer}")
])

eval_chain = eval_prompt | llm | StrOutputParser()
eval_result = eval_chain.invoke({"question": question, "answer": answer})
print(f"LLM 评估结果：\n{eval_result}")

# 练习16.5：批量评估
print("\n=== 练习16.5：批量评估 ===")

test_cases = [
    {"question": "什么是单元测试？", "expected": "单元测试是对最小可测试单元进行测试"},
    {"question": "什么是集成测试？", "expected": "集成测试是测试多个模块的交互"},
    {"question": "什么是系统测试？", "expected": "系统测试是测试整个系统"},
]

def batch_evaluation(chain, test_cases):
    """批量评估"""
    results = []
    
    for case in test_cases:
        answer = chain.invoke({"question": case["question"]})
        accuracy = evaluate_accuracy(answer, case["expected"])
        
        results.append({
            "question": case["question"],
            "answer": answer,
            "expected": case["expected"],
            "accuracy": accuracy
        })
    
    return results

results = batch_evaluation(chain, test_cases)

print("批量评估结果：")
for r in results:
    print(f"  问题：{r['question']}")
    print(f"  准确率：{r['accuracy']:.2%}")
    print()

"""
思考题：
1. LLM 评估的主要指标有哪些？
2. 如何使用 LLM 作为评估器？
3. 如何设计评估数据集？
4. 批量评估的好处是什么？
5. 如何分析评估结果？
"""
