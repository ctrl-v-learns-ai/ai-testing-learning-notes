# LLM 评估一：评估指标

## 为什么需要评估？

LLM 的输出是非确定性的，需要系统化的评估方法来衡量质量。

类比理解：
- 评估 = 考试（检验学习成果）
- 评估指标 = 评分标准（客观衡量质量）

## 评估维度

### 1. 准确性（Accuracy）

```python
# 任务完成度评估
def evaluate_accuracy(predicted, expected):
    """评估回答是否正确"""
    correct = sum(1 for p, e in zip(predicted, expected) if p == e)
    return correct / len(predicted)
```

### 2. 相关性（Relevance）

```python
# 回答与问题的相关程度
def evaluate_relevance(question, answer):
    """评估回答与问题的相关性"""
    # 使用语义相似度
    from sentence_transformers import SentenceTransformer
    
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode([question, answer])
    
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return similarity
```

### 3. 连贯性（Coherence）

```python
# 回答的逻辑连贯性
def evaluate_coherence(text):
    """评估文本的连贯性"""
    # 检查句子之间的逻辑关系
    sentences = text.split('。')
    
    coherence_score = 0
    for i in range(len(sentences) - 1):
        # 检查相邻句子的语义连贯性
        similarity = get_similarity(sentences[i], sentences[i+1])
        coherence_score += similarity
    
    return coherence_score / (len(sentences) - 1)
```

### 4. 忠实度（Faithfulness）

```python
# 回答是否基于给定的上下文
def evaluate_faithfulness(context, answer):
    """评估回答是否忠实于上下文"""
    # 检查回答中的信息是否都在上下文中
    prompt = f"""
    请判断回答是否忠实于上下文：
    
    上下文：{context}
    回答：{answer}
    
    如果回答中的信息都在上下文中，输出"忠实"
    如果回答中包含上下文没有的信息，输出"不忠实"
    """
    return prompt
```

### 5. 有害性（Harmfulness）

```python
# 检测有害内容
def evaluate_harmfulness(text):
    """检测文本中的有害内容"""
    harmful_keywords = ['暴力', '歧视', '色情', '违法']
    
    for keyword in harmful_keywords:
        if keyword in text:
            return True, f"包含有害关键词：{keyword}"
    
    return False, "无有害内容"
```

## 评估方法

### 1. 人工评估

```python
# 人工评估标准
evaluation_criteria = {
    "准确性": "回答是否正确",
    "相关性": "回答是否与问题相关",
    "连贯性": "回答是否逻辑清晰",
    "完整性": "回答是否完整",
    "有用性": "回答是否有帮助"
}

# 评分标准（1-5分）
rating_scale = {
    1: "非常差",
    2: "差",
    3: "一般",
    4: "好",
    5: "非常好"
}
```

### 2. 自动评估

```python
# BLEU 分数（机器翻译）
from nltk.translate.bleu_score import sentence_bleu

def calculate_bleu(reference, candidate):
    """计算 BLEU 分数"""
    return sentence_bleu([reference.split()], candidate.split())

# ROUGE 分数（文本摘要）
from rouge_score import rouge_scorer

def calculate_rouge(reference, candidate):
    """计算 ROUGE 分数"""
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference, candidate)
    return scores
```

### 3. LLM 作为评估器

```python
# 使用 LLM 评估 LLM 输出
def llm_as_judge(question, answer, criteria):
    """使用 LLM 作为评估器"""
    prompt = f"""
    请评估以下回答的质量：
    
    问题：{question}
    回答：{answer}
    
    评估标准：{criteria}
    
    请给出：
    1. 分数（1-10）
    2. 优点
    3. 缺点
    4. 改进建议
    """
    return prompt
```

## 评估框架

### 1. RAGAS（RAG 评估）

```python
# RAGAS 评估指标
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall
)

# 评估 RAG 系统
def evaluate_rag(question, answer, contexts, ground_truth):
    """评估 RAG 系统"""
    metrics = {
        "faithfulness": faithfulness,
        "answer_relevancy": answer_relevancy,
        "context_precision": context_precision,
        "context_recall": context_recall
    }
    
    return evaluate(
        question=question,
        answer=answer,
        contexts=contexts,
        ground_truth=ground_truth,
        metrics=metrics
    )
```

### 2. LangSmith 评估

```python
# LangSmith 评估配置
from langsmith import Client

client = Client()

# 创建评估数据集
dataset = client.create_dataset("my-evaluation-dataset")

# 添加测试用例
client.create_example(
    inputs={"question": "什么是回归测试？"},
    outputs={"answer": "回归测试是修改代码后重新测试"}
)

# 运行评估
def evaluate_with_langsmith(chain, dataset):
    """使用 LangSmith 进行评估"""
    results = []
    
    for example in dataset:
        output = chain.invoke(example.inputs)
        score = calculate_score(output, example.outputs)
        results.append(score)
    
    return sum(results) / len(results)
```

## 评估指标速查表

| 指标 | 说明 | 适用场景 |
|------|------|----------|
| BLEU | n-gram 匹配 | 机器翻译 |
| ROUGE | 召回率 | 文本摘要 |
| Perplexity | 语言模型质量 | 文本生成 |
| Faithfulness | 忠实度 | RAG 系统 |
| Relevancy | 相关性 | 问答系统 |

## 常见坑

### 坑1：只看分数不看质量

```python
# 错误：只关注 BLEU 分数
# 正确：结合人工评估和自动评估
```

### 坑2：评估数据集太小

```python
# 错误：只有10个测试用例
# 正确：至少100个测试用例，覆盖各种场景
```

### 坑3：忽略边界情况

```python
# 错误：只测试正常输入
# 正确：测试边界、异常、对抗性输入
```

## 小测验

1. LLM 评估的主要指标有哪些？
2. BLEU 和 ROUGE 的区别？
3. 什么是忠实度评估？
4. 如何使用 LLM 作为评估器？
5. RAGAS 评估框架的作用？
