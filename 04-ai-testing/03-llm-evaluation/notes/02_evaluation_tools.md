# LLM 评估二：评估工具

## 常用评估工具

### 1. LangSmith

```python
# LangSmith 是 LangChain 的官方评估平台
# 功能：追踪、调试、评估 LLM 应用

# 安装
# pip install langsmith

# 配置环境变量
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-api-key"

# 使用
from langsmith import Client

client = Client()

# 创建数据集
dataset = client.create_dataset("test-dataset")

# 添加测试用例
client.create_example(
    inputs={"question": "什么是回归测试？"},
    outputs={"expected": "回归测试是修改代码后重新测试以确认没有引入新错误"}
)
```

### 2. DeepEval

```python
# DeepEval 是一个 LLM 评估框架
# 安装：pip install deepeval

from deepeval import evaluate
from deepeval.metrics import (
    AnswerRelevancyMetric,
    FaithfulnessMetric,
    ContextualPrecisionMetric
)
from deepeval.test_case import LLMTestCase

# 创建测试用例
test_case = LLMTestCase(
    input="什么是回归测试？",
    actual_output="回归测试是修改代码后重新测试",
    expected_output="回归测试是修改代码后重新测试以确认没有引入新错误",
    retrieval_context=["回归测试是软件测试的一种类型"]
)

# 定义指标
metrics = [
    AnswerRelevancyMetric(threshold=0.7),
    FaithfulnessMetric(threshold=0.7),
    ContextualPrecisionMetric(threshold=0.7)
]

# 评估
evaluate([test_case], metrics)
```

### 3. RAGAS

```python
# RAGAS 专注于 RAG 系统评估
# 安装：pip install ragas

from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall
)

# 准备数据
data = {
    "question": ["什么是回归测试？"],
    "answer": ["回归测试是修改代码后重新测试"],
    "contexts": [["回归测试是软件测试的一种类型"]],
    "ground_truth": ["回归测试是修改代码后重新测试以确认没有引入新错误"]
}

# 评估
result = evaluate(
    dataset=data,
    metrics=[
        faithfulness,
        answer_relevancy,
        context_precision,
        context_recall
    ]
)

print(result)
```

### 4. Promptfoo

```python
# Promptfoo 是一个命令行评估工具
# 安装：npm install -g promptfoo

# 配置文件 promptfooconfig.yaml
"""
prompts:
  - "请回答以下问题：{{question}}"
  - "你是一位测试专家，请回答：{{question}}"

providers:
  - id: openai:gpt-4
    config:
      api_key: xxx

tests:
  - vars:
      question: "什么是回归测试？"
    assert:
      - type: contains
        value: "重新测试"
      - type: llm-rubric
        value: "回答应该解释回归测试的概念"
"""
```

## 评估流程

### 1. 准备评估数据集

```python
# 创建评估数据集
evaluation_dataset = [
    {
        "input": "什么是单元测试？",
        "expected": "单元测试是对软件中最小可测试单元进行检查和验证",
        "category": "概念解释"
    },
    {
        "input": "如何设计测试用例？",
        "expected": "设计测试用例需要考虑正常场景、边界条件和异常情况",
        "category": "方法指导"
    },
    # ... 更多测试用例
]

# 保存为 JSON
import json
with open("evaluation_dataset.json", "w", encoding="utf-8") as f:
    json.dump(evaluation_dataset, f, ensure_ascii=False, indent=2)
```

### 2. 运行评估

```python
def run_evaluation(chain, dataset):
    """运行评估"""
    results = []
    
    for item in dataset:
        # 调用链
        output = chain.invoke({"input": item["input"]})
        
        # 计算分数
        score = calculate_score(output, item["expected"])
        
        results.append({
            "input": item["input"],
            "expected": item["expected"],
            "actual": output,
            "score": score,
            "category": item["category"]
        })
    
    return results
```

### 3. 分析结果

```python
def analyze_results(results):
    """分析评估结果"""
    # 总体分数
    total_score = sum(r["score"] for r in results) / len(results)
    
    # 按类别分析
    categories = {}
    for r in results:
        cat = r["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(r["score"])
    
    category_scores = {
        cat: sum(scores) / len(scores) 
        for cat, scores in categories.items()
    }
    
    # 找出低分用例
    low_score_cases = [r for r in results if r["score"] < 0.7]
    
    return {
        "total_score": total_score,
        "category_scores": category_scores,
        "low_score_cases": low_score_cases
    }
```

## 评估最佳实践

### 1. 评估数据集设计

```python
# 好的评估数据集应该包含：
evaluation_guidelines = {
    "多样性": "覆盖不同类型的问题",
    "代表性": "代表实际使用场景",
    "平衡性": "正常、边界、异常场景平衡",
    "规模": "至少100个测试用例"
}
```

### 2. 评估指标选择

```python
# 根据任务选择指标
metrics_by_task = {
    "问答系统": ["faithfulness", "relevancy", "precision"],
    "文本摘要": ["rouge", "bleu", "coherence"],
    "机器翻译": ["bleu", "meteor", "ter"],
    "代码生成": ["pass@k", "execution_accuracy"]
}
```

### 3. 持续评估

```python
# 建立持续评估流程
def continuous_evaluation(chain, new_data):
    """持续评估"""
    # 1. 运行评估
    results = run_evaluation(chain, new_data)
    
    # 2. 分析结果
    analysis = analyze_results(results)
    
    # 3. 如果分数下降，触发告警
    if analysis["total_score"] < 0.8:
        send_alert("评估分数下降")
    
    # 4. 记录历史
    save_to_history(analysis)
    
    return analysis
```

## 评估报告模板

```python
def generate_evaluation_report(analysis):
    """生成评估报告"""
    report = f"""
# LLM 评估报告

## 总体指标
- 总体分数：{analysis['total_score']:.2f}
- 测试用例数：{analysis['total_cases']}
- 通过率：{analysis['pass_rate']:.2%}

## 分类表现
{format_category_scores(analysis['category_scores'])}

## 低分用例分析
{format_low_score_cases(analysis['low_score_cases'])}

## 改进建议
{generate_suggestions(analysis)}
"""
    return report
```

## 速查表

| 工具 | 说明 | 安装 |
|------|------|------|
| LangSmith | LangChain 官方评估平台 | `pip install langsmith` |
| DeepEval | LLM 评估框架 | `pip install deepeval` |
| RAGAS | RAG 系统评估 | `pip install ragas` |
| Promptfoo | 命令行评估工具 | `npm install -g promptfoo` |

## 小测验

1. LangSmith 的主要功能是什么？
2. DeepEval 和 RAGAS 的区别？
3. 如何设计评估数据集？
4. 如何选择评估指标？
5. 持续评估的好处是什么？
