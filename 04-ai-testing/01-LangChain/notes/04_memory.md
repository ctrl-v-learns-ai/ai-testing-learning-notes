# 阶段四：Memory 记忆与对话 学习笔记

## 概念解释

### 什么是 Memory？
Memory 是让 LLM 应用拥有"记忆"能力的机制，可以记住之前的对话内容。

类比理解：
- 没有 Memory 的 AI = 金鱼（每次对话都是全新的）
- 有 Memory 的 AI = 正常人（能记住之前的对话）

### 为什么需要 Memory？
1. **多轮对话**：用户可能会说"继续刚才的话题"
2. **上下文理解**：需要知道"它"指的是什么
3. **个性化**：记住用户的偏好和历史
4. **连贯性**：保持对话的逻辑连贯

### Memory 的类型

| 类型 | 原理 | 适用场景 |
|------|------|----------|
| ConversationBufferMemory | 保存所有对话历史 | 短对话 |
| ConversationSummaryMemory | 对历史进行摘要 | 长对话 |
| ConversationBufferWindowMemory | 只保留最近N轮 | 有限上下文 |

---

## 关键类/方法说明

### 1. ConversationBufferMemory（缓冲记忆）

```python
from langchain.memory import ConversationBufferMemory

# 创建记忆
memory = ConversationBufferMemory(
    return_messages=True,  # 返回消息列表格式
    memory_key="history"   # 在提示模板中使用的变量名
)

# 保存对话
memory.save_context(
    {"input": "你好，我叫张三"},
    {"output": "你好张三！有什么可以帮你的？"}
)

# 获取历史
history = memory.load_memory_variables({})
print(history["history"])
```

### 2. ConversationSummaryMemory（摘要记忆）

```python
from langchain.memory import ConversationSummaryMemory

# 创建摘要记忆（需要 LLM 来生成摘要）
memory = ConversationSummaryMemory(
    llm=llm,
    return_messages=True,
    memory_key="history"
)

# 保存对话（会自动摘要）
memory.save_context(
    {"input": "我正在做一个电商项目"},
    {"output": "好的，电商项目需要考虑很多方面"}
)

# 获取摘要
history = memory.load_memory_variables({})
print(history["history"])  # 返回摘要而不是完整历史
```

### 3. 在链中使用 Memory

```python
from langchain.chains import ConversationChain

# 创建带记忆的对话链
conversation = ConversationChain(
    llm=llm,
    memory=ConversationBufferMemory(return_messages=True),
    verbose=True  # 打印详细信息
)

# 多轮对话
response1 = conversation.predict(input="你好，我叫张三")
response2 = conversation.predict(input="我叫什么名字？")  # 能记住"张三"
```

### 4. 手动管理对话历史

```python
# 手动构建对话历史
from langchain_core.messages import HumanMessage, AIMessage

# 方法一：在提示模板中直接使用
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个友好的助手"),
    ("placeholder", "{history}"),  # 历史消息占位符
    ("human", "{input}")
])

# 方法二：使用 MessagesPlaceholder
from langchain_core.prompts import MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个友好的助手"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# 手动构建历史
history = [
    HumanMessage(content="你好，我叫张三"),
    AIMessage(content="你好张三！"),
    HumanMessage(content="我喜欢Python"),
    AIMessage(content="Python是个好语言！"),
]
```

### 5. RunnableWithMessageHistory（LCEL 方式）

```python
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

# 创建会话存储
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 包装链，添加记忆功能
with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

# 使用时需要指定 session_id
config = {"configurable": {"session_id": "user_123"}}
response = with_memory.invoke({"input": "你好"}, config=config)
```

---

## 常见坑

### 坑1：Memory 变量名不匹配
```python
# 错误：memory_key 和模板中的变量名不一致
memory = ConversationBufferMemory(memory_key="chat_history")
prompt = ChatPromptTemplate.from_messages([
    ("placeholder", "{history}")  # 应该是 {chat_history}
])

# 正确：保持一致
memory = ConversationBufferMemory(memory_key="history")
prompt = ChatPromptTemplate.from_messages([
    ("placeholder", "{history}")
])
```

### 坑2：忘记保存上下文
```python
# 错误：对话后没有保存到记忆
response = llm.invoke(messages)
# memory 中没有记录

# 正确：手动保存
memory.save_context(
    {"input": user_input},
    {"output": response.content}
)
```

### 坑3：长对话超出 Token 限制
```python
# 错误：使用 BufferMemory，对话太长会超出模型限制
memory = ConversationBufferMemory()  # 保存所有历史

# 正确：使用 SummaryMemory 或 WindowMemory
memory = ConversationSummaryMemory(llm=llm)  # 自动摘要
# 或
memory = ConversationBufferWindowMemory(k=10)  # 只保留最近10轮
```

---

## 速查表

### BufferMemory 速查
```python
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory(return_messages=True, memory_key="history")
memory.save_context({"input": "..."}, {"output": "..."})
history = memory.load_memory_variables({})
```

### SummaryMemory 速查
```python
from langchain.memory import ConversationSummaryMemory
memory = ConversationSummaryMemory(llm=llm, memory_key="history")
```

### LCEL 记忆速查
```python
from langchain_core.runnables.history import RunnableWithMessageHistory
with_memory = RunnableWithMessageHistory(chain, get_session_history, ...)
```

---

## 小测验

1. **ConversationBufferMemory 和 ConversationSummaryMemory 的区别是什么？**
2. **Memory 的 memory_key 参数有什么用？**
3. **为什么长对话建议用 SummaryMemory？**
4. **RunnableWithMessageHistory 的作用是什么？**
5. **如何实现多用户独立的对话历史？**

---

## 扩展阅读

- [LangChain 官方文档 - Memory](https://docs.langchain.com/oss/python/langchain/memory)
- [LangChain 官方文档 - Chat History](https://docs.langchain.com/oss/python/langchain/chat-history)
