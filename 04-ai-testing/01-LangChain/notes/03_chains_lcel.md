# 阶段三：Chains & LCEL 链式调用 学习笔记

## 概念解释

### 什么是 Chain（链）？
Chain 是将多个组件串联起来形成一个完整的工作流程。

类比理解：
- 单个组件 = 工厂里的单个工人
- Chain = 工厂里的流水线
- 数据 = 流水线上的产品

### 什么是 LCEL？
LCEL = LangChain Expression Language（LangChain 表达式语言）

它是 LangChain 中组合链的核心语法，使用 `|` 管道运算符。

```python
# LCEL 语法：像 Linux 管道一样传递数据
chain = prompt | llm | parser
result = chain.invoke({"input": "你好"})
```

### LCEL 的优势
1. **统一接口**：所有组件都实现 Runnable 接口
2. **自动支持**：invoke、stream、batch、ainvoke、astream、abatch
3. **并行执行**：RunnableParallel 可以并行处理多个任务
4. **错误处理**：RunnableFallback 提供降级方案
5. **可观测性**：自动集成 LangSmith 进行调试

---

## Runnable 接口

### 核心方法

```python
# 1. invoke：同步调用（最常用）
result = chain.invoke({"input": "你好"})

# 2. stream：流式输出（实时显示生成过程）
for chunk in chain.stream({"input": "你好"}):
    print(chunk, end="")

# 3. batch：批量调用（同时处理多个请求）
results = chain.batch([{"input": "你好"}, {"input": "再见"}])

# 4. ainvoke：异步调用（用于异步编程）
result = await chain.ainvoke({"input": "你好"})
```

### 输入输出格式

```python
# PromptTemplate 接收字典，输出 PromptValue
prompt = ChatPromptTemplate.from_messages([...])
prompt_value = prompt.invoke({"input": "你好"})

# LLM 接收 PromptValue 或消息列表，输出 AIMessage
llm_output = llm.invoke(prompt_value)

# OutputParser 接收 AIMessage，输出字符串或其他格式
parser_output = parser.invoke(llm_output)
```

---

## 关键类/方法说明

### 1. 基础链（最简单的 LCEL 链）

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 创建链
chain = prompt | llm | StrOutputParser()

# 调用链
result = chain.invoke({"input": "你好"})
```

### 2. RunnableParallel（并行执行）

```python
from langchain_core.runnables import RunnableParallel

# 并行执行多个链
parallel_chain = RunnableParallel(
    summary=summary_chain,
    keywords=keywords_chain
)

# 结果是一个字典
result = parallel_chain.invoke({"input": "这是一段文本"})
print(result["summary"])   # 摘要结果
print(result["keywords"])  # 关键词结果
```

### 3. RunnablePassthrough（透传输入）

```python
from langchain_core.runnables import RunnablePassthrough

# RunnablePassthrough 将输入直接传递给下一个组件
chain = RunnablePassthrough() | llm | parser

# 在 RAG 中常用
rag_chain = {
    "context": retriever | format_docs,
    "question": RunnablePassthrough()  # 直接传递问题
} | rag_prompt | llm | parser
```

### 4. RunnableLambda（自定义函数）

```python
from langchain_core.runnables import RunnableLambda

# 将普通函数转换为 Runnable
def my_function(input_data):
    # 自定义处理逻辑
    return processed_data

runnable_func = RunnableLambda(my_function)

# 在链中使用
chain = prompt | llm | parser | runnable_func
```

### 5. 链的组合与嵌套

```python
# 子链
analysis_chain = prompt1 | llm | parser1
summary_chain = prompt2 | llm | parser2

# 组合成更大的链
full_chain = analysis_chain | summary_chain

# 或者并行组合
parallel_chain = RunnableParallel(
    analysis=analysis_chain,
    summary=summary_chain
)
```

### 6. 条件分支

```python
from langchain_core.runnables import RunnableBranch

# 根据条件选择不同的链
branch = RunnableBranch(
    (lambda x: x["type"] == "short", short_chain),
    (lambda x: x["type"] == "long", long_chain),
    default_chain  # 默认分支
)
```

---

## 常见坑

### 坑1：输入格式不匹配
```python
# 错误：直接传字符串
result = chain.invoke("你好")  # 如果 prompt 需要字典会报错

# 正确：传字典
result = chain.invoke({"input": "你好"})
```

### 坑2：忘记输出解析器
```python
# 没有解析器：返回 AIMessage 对象
chain = prompt | llm
result = chain.invoke({"input": "你好"})
print(result)  # AIMessage(content='你好！')

# 有解析器：返回字符串
chain = prompt | llm | StrOutputParser()
result = chain.invoke({"input": "你好"})
print(result)  # "你好！"
```

### 坑3：并行链的结果格式
```python
# 并行链返回字典
parallel = RunnableParallel(a=chain1, b=chain2)
result = parallel.invoke({"input": "你好"})

# 错误：直接打印
print(result)  # {'a': '...', 'b': '...'}

# 正确：通过键访问
print(result["a"])
print(result["b"])
```

---

## 速查表

### 基础链速查
```python
chain = prompt | llm | StrOutputParser()
result = chain.invoke({"key": "value"})
```

### 并行链速查
```python
parallel = RunnableParallel(
    task1=chain1,
    task2=chain2
)
result = parallel.invoke({"input": "..."})
```

### 自定义函数速查
```python
func = RunnableLambda(lambda x: x.upper())
chain = prompt | llm | parser | func
```

### 批量调用速查
```python
results = chain.batch([
    {"input": "问题1"},
    {"input": "问题2"}
])
```

---

## 小测验

1. **LCEL 中 `|` 运算符的作用是什么？**
2. **RunnableParallel 和顺序执行的区别是什么？**
3. **RunnablePassthrough 的作用是什么？在什么场景下使用？**
4. **invoke、stream、batch 三种调用方式的区别？**
5. **如何将一个普通函数集成到 LCEL 链中？**

---

## 扩展阅读

- [LangChain 官方文档 - LCEL](https://docs.langchain.com/oss/python/langchain/lcel)
- [LangChain 官方文档 - Runnable Interface](https://docs.langchain.com/oss/python/langchain/runnables)
- [LangChain 官方文档 - Streaming](https://docs.langchain.com/oss/python/langchain/streaming)
