# 阶段一：Model I/O 学习笔记

## 概念解释

### 什么是 Model I/O？
Model I/O 是 LangChain 的核心模块，负责：
- **输入（Input）**：将用户的问题/指令转换为模型能理解的格式
- **处理（Processing）**：调用 LLM 或 ChatModel 进行推理
- **输出（Output）**：将模型的响应解析为我们需要的格式

### LLM vs ChatModel 的区别

| 特性 | LLM | ChatModel |
|------|-----|-----------|
| 输入格式 | 纯文本字符串 | 消息列表（包含角色） |
| 输出格式 | 纯文本字符串 | 消息对象 |
| 适用场景 | 文本补全、续写 | 对话、问答、指令跟随 |
| 代表模型 | text-davinci-003 | GPT-4、DeepSeek-Chat |
| 推荐程度 | 逐渐废弃 | 推荐使用 |

**类比理解**：
- **LLM** 像是一个"自动补全器"，你给它前半句，它补全后半句
- **ChatModel** 像是一个"对话机器人"，你给它消息，它回复消息

### 为什么推荐 ChatModel？
1. **更好的指令跟随能力**：经过专门的指令微调
2. **支持多轮对话**：原生支持消息历史
3. **支持工具调用**：可以调用外部函数
4. **支持结构化输出**：可以输出 JSON 等格式

---

## 关键类/方法说明

### 1. 模型初始化

```python
# 方式一：使用提供商特定的类（推荐）
from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek

# OpenAI 模型
llm = ChatOpenAI(
    model="gpt-4",           # 模型名称
    temperature=0.7,         # 温度参数（0-2），越高越随机
    max_tokens=1000,         # 最大输出 token 数
    api_key="sk-xxx",        # API 密钥
    base_url="https://..."   # API 地址（可选）
)

# DeepSeek 模型
llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0.7,
    api_key="sk-xxx"
)

# 方式二：使用通用初始化方法（LangChain 1.0+）
from langchain.chat_models import init_chat_model

llm = init_chat_model(
    "openai:gpt-4",          # 提供商:模型名
    temperature=0.7
)
```

### 2. 消息类型

```python
from langchain_core.messages import (
    SystemMessage,    # 系统消息：设定 AI 的角色和行为
    HumanMessage,     # 人类消息：用户的输入
    AIMessage,        # AI 消息：AI 的回复
    ToolMessage       # 工具消息：工具调用的结果
)

# 构建消息列表
messages = [
    SystemMessage(content="你是一个专业的测试工程师"),
    HumanMessage(content="请帮我设计登录模块的测试用例")
]
```

### 3. PromptTemplate（文本提示模板）

```python
from langchain_core.prompts import PromptTemplate

# 创建模板
template = PromptTemplate(
    template="你是一个{role}。请用{style}的风格回答：{question}",
    input_variables=["role", "style", "question"]
)

# 格式化输出
prompt = template.format(
    role="测试工程师",
    style="专业",
    question="如何设计边界值测试？"
)
# 输出："你是一个测试工程师。请用专业的风格回答：如何设计边界值测试？"
```

### 4. ChatPromptTemplate（聊天提示模板）

```python
from langchain_core.prompts import ChatPromptTemplate

# 方式一：从消息列表创建（推荐，最常用）
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个{role}，专注于{domain}领域"),
    ("human", "{question}")
])

# 格式化输出
messages = prompt.format_messages(
    role="测试工程师",
    domain="电商系统",
    question="如何设计购物车的测试用例？"
)
```

### 5. 输出解析器

```python
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from pydantic import BaseModel, Field

# StrOutputParser：提取纯文本
# 输入: AIMessage(content="Hello") -> 输出: "Hello"
str_parser = StrOutputParser()

# JsonOutputParser：解析 JSON
class Testcase(BaseModel):
    name: str = Field(description="测试用例名称")
    steps: list = Field(description="测试步骤")
    expected: str = Field(description="预期结果")

json_parser = JsonOutputParser(pydantic_object=Testcase)
```

### 6. LCEL 链式调用

```python
# 使用 | 运算符组合组件（像 Linux 管道一样）
chain = prompt | llm | StrOutputParser()

# 调用链
result = chain.invoke({
    "role": "测试工程师",
    "domain": "电商系统",
    "question": "如何设计购物车的测试用例？"
})

# 流式输出（实时显示生成过程）
for chunk in chain.stream({"role": "测试工程师", "domain": "电商系统", "question": "如何设计购物车？"}):
    print(chunk, end="", flush=True)

# 批量调用（同时处理多个请求）
results = chain.batch([
    {"role": "测试工程师", "domain": "电商", "question": "如何测试登录？"},
    {"role": "测试工程师", "domain": "支付", "question": "如何测试支付？"}
])
```

---

## 常见坑

### 坑1：API 密钥配置问题
```python
# 错误：硬编码密钥（不安全，且换环境就失效）
llm = ChatOpenAI(api_key="sk-xxx")

# 正确：使用环境变量
import os
from dotenv import load_dotenv
load_dotenv()  # 自动加载 .env 文件
llm = ChatOpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_API_URL")
)
```

### 坑2：消息格式错误
```python
# 错误：直接传字符串（某些旧教程这样写）
result = llm.invoke("你好")

# 正确：传消息列表
from langchain_core.messages import HumanMessage
result = llm.invoke([HumanMessage(content="你好")])
```

### 坑3：模板变量未提供
```python
# 错误：缺少变量会报 KeyError
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是{role}"),
    ("human", "{question}")
])
prompt.format_messages(question="你好")  # 缺少 role！

# 正确：提供所有变量
prompt.format_messages(role="测试工程师", question="你好")
```

### 坑4：输出解析失败
```python
# 错误：模型输出不是有效 JSON 时会报错
json_parser.parse("这不是JSON格式的输出")

# 正确：在提示中明确要求输出格式
prompt = ChatPromptTemplate.from_messages([
    ("system", "你必须输出JSON格式"),
    ("human", "{question}")
])
```

### 坑5：温度参数设置不当
```python
# 错误：需要精确输出时温度太高
llm = ChatOpenAI(temperature=1.5)  # 输出会很随机

# 正确：根据场景设置温度
# 代码生成、测试用例：temperature=0.1~0.3（精确）
# 创意写作、头脑风暴：temperature=0.7~1.0（随机）
```

---

## 速查表

### 模型初始化速查
```python
# DeepSeek（你当前用的）
from langchain_deepseek import ChatDeepSeek
llm = ChatDeepSeek(model="deepseek-chat", temperature=0.7, api_key="xxx")

# OpenAI 兼容接口
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4", temperature=0.7, api_key="xxx", base_url="xxx")

# 通用方法（LangChain 1.0+）
from langchain.chat_models import init_chat_model
llm = init_chat_model("openai:gpt-4", temperature=0.7)
```

### 提示模板速查
```python
# 聊天模板（最常用）
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是{role}"),
    ("human", "{question}")
])

# 简单文本模板
from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("你是{role}，请回答{question}")
```

### 输出解析器速查
```python
# 纯文本（最常用）
from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()

# JSON 结构化
from langchain_core.output_parsers import JsonOutputParser
parser = JsonOutputParser(pydantic_object=MyModel)
```

### LCEL 链速查
```python
# 基础链
chain = prompt | llm | StrOutputParser()
result = chain.invoke({"key": "value"})

# 流式输出
for chunk in chain.stream({"key": "value"}):
    print(chunk, end="")

# 批量调用
results = chain.batch([{"key": "v1"}, {"key": "v2"}])
```

---

## 小测验

1. **LLM 和 ChatModel 的主要区别是什么？为什么推荐使用 ChatModel？**
2. **SystemMessage 和 HumanMessage 的作用分别是什么？**
3. **为什么要使用输出解析器？StrOutputParser 和 JsonOutputParser 的使用场景区别？**
4. **LCEL 链中 `|` 运算符的作用是什么？**
5. **temperature 参数的作用是什么？在什么场景下应该设置较低的 temperature？**

---

## 扩展阅读

- [LangChain 官方文档 - Chat Models](https://docs.langchain.com/oss/python/langchain/chat-models)
- [LangChain 官方文档 - Prompt Templates](https://docs.langchain.com/oss/python/langchain/prompt-templates)
- [LangChain 官方文档 - Output Parsers](https://docs.langchain.com/oss/python/langchain/output-parsers)
- [LangChain 官方文档 - LCEL](https://docs.langchain.com/oss/python/langchain/lcel)
