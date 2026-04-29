# 阶段二：Retrieval 数据连接 学习笔记

## 概念解释

### 什么是 RAG（检索增强生成）？
RAG = Retrieval（检索）+ Augmented（增强）+ Generation（生成）

核心思想：先从知识库中检索相关信息，再把检索到的内容交给 LLM 生成回答。

类比理解：
- 没有 RAG 的 LLM = 开卷考试不让带书（只能靠训练时记住的知识）
- 有 RAG 的 LLM = 开卷考试可以翻书（先找相关资料，再回答问题）

### RAG 的完整流程

```
用户提问
    |
    v
[检索阶段] 从知识库中找到相关文档
    |
    v
[增强阶段] 把检索到的文档拼接到提示词中
    |
    v
[生成阶段] LLM 根据增强后的提示词生成回答
    |
    v
返回答案
```

### 为什么需要 RAG？
1. **知识更新**：LLM 训练数据有截止日期，RAG 可以随时更新知识库
2. **领域专业**：可以导入企业内部文档、技术手册等专业资料
3. **减少幻觉**：基于真实文档回答，比 LLM 自己编造更可靠
4. **成本更低**：比微调模型更简单、更便宜

---

## RAG 五大核心组件

### 1. DocumentLoader（文档加载器）
作用：从不同来源加载文档（PDF、网页、CSV、TXT 等）

### 2. TextSplitter（文本分割器）
作用：将长文档切分成小块（chunk），便于检索

### 3. Embedding（嵌入模型）
作用：将文本转换为向量（数字数组），便于计算相似度

### 4. VectorStore（向量数据库）
作用：存储和检索向量

### 5. Retriever（检索器）
作用：根据用户问题，从向量数据库中检索相关文档

---

## 关键类/方法说明

### 1. DocumentLoader（文档加载器）

```python
# CSV 加载器
from langchain_community.document_loaders import CSVLoader
loader = CSVLoader(file_path="data.csv", encoding="utf-8")
documents = loader.load()  # 返回 Document 对象列表

# PDF 加载器
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader(file_path="document.pdf")
documents = loader.load()

# 网页加载器
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://example.com/article")
documents = loader.load()

# 文本文件加载器
from langchain_community.document_loaders import TextLoader
loader = TextLoader(file_path="readme.txt", encoding="utf-8")
documents = loader.load()
```

Document 对象结构：
```python
# 每个 Document 包含：
# - page_content: 文本内容（字符串）
# - metadata: 元数据（字典，如来源文件名、页码等）
print(documents[0].page_content)  # 文本内容
print(documents[0].metadata)      # {'source': 'data.csv', 'row': 0}
```

### 2. TextSplitter（文本分割器）

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # 每个块的最大字符数
    chunk_overlap=50,    # 块之间的重叠字符数（保持上下文连续性）
    separators=["\n\n", "\n", "。", "！", "？", " "]  # 分割符优先级
)

# 分割文档
chunks = splitter.split_documents(documents)

# 也可以直接分割文本
texts = splitter.split_text("这是一段很长的文本...")
```

为什么需要 chunk_overlap？
- 类比：看书时翻页，前一页最后几行和下一页开头内容是连续的
- overlap 确保切分点附近的语义不会丢失

### 3. Embedding（嵌入模型）

```python
# 使用 OpenAI 兼容的 Embedding 模型
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002",
    openai_api_key="sk-xxx",
    openai_api_base="https://..."
)

# 将文本转换为向量
vector = embeddings.embed_query("什么是回归测试？")
print(f"向量维度：{len(vector)}")  # 通常是 1536 维

# 批量转换
vectors = embeddings.embed_documents(["测试用例", "缺陷报告", "回归测试"])
```

### 4. VectorStore（向量数据库）

```python
# FAISS（本地向量数据库，适合学习和小规模应用）
from langchain_community.vectorstores import FAISS

# 从文档创建向量数据库
vectorstore = FAISS.from_documents(
    documents=chunks,           # 切分后的文档块
    embedding=embeddings        # 嵌入模型
)

# 保存到本地
vectorstore.save_local("faiss_index")

# 从本地加载
vectorstore = FAISS.load_local("faiss_index", embeddings)

# 相似度搜索
results = vectorstore.similarity_search("什么是回归测试？", k=3)
```

### 5. Retriever（检索器）

```python
# 从 VectorStore 创建 Retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",  # 检索类型
    search_kwargs={"k": 3}     # 返回前3个最相似的文档
)

# 使用 Retriever 检索
docs = retriever.invoke("什么是回归测试？")
for doc in docs:
    print(doc.page_content)
    print("---")
```

### 6. 完整 RAG 链

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# 构建 RAG 提示模板
rag_prompt = ChatPromptTemplate.from_messages([
    ("system", "根据以下参考资料回答用户问题。如果资料中没有相关信息，请说明不知道。\n\n参考资料：{context}"),
    ("human", "{question}")
])

# 格式化检索到的文档
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 构建 RAG 链
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | rag_prompt
    | llm
    | StrOutputParser()
)

# 调用
answer = rag_chain.invoke("什么是回归测试？")
print(answer)
```

---

## 常见坑

### 坑1：chunk_size 设置不当
```python
# 错误：chunk_size 太大（比如 5000），检索精度低
# 错误：chunk_size 太小（比如 50），语义不完整

# 推荐：根据文档类型调整
# 技术文档：500-1000 字符
# 对话记录：200-500 字符
# 通用文本：300-800 字符
```

### 坑2：没有设置 chunk_overlap
```python
# 错误：overlap=0，切分点附近的语义可能丢失
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)

# 正确：设置 50-100 的 overlap
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
```

### 坑3：Embedding 模型不匹配
```python
# 错误：创建索引和查询时用了不同的 Embedding 模型
# 创建时用 model_a
vectorstore = FAISS.from_documents(docs, embeddings_a)
# 查询时用 model_b（会报错或结果不准确）
results = vectorstore.similarity_search(query)  # 底层用的是 embeddings_a
```

### 坑4：忘记加载 .env 文件
```python
# 错误：直接使用环境变量但没有加载 .env
embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("API_KEY"))  # None

# 正确：先加载 .env
from dotenv import load_dotenv
load_dotenv()
```

### 坑5：没有指定编码
```python
# 错误：中文文档可能出现乱码
loader = CSVLoader(file_path="data.csv")

# 正确：指定编码
loader = CSVLoader(file_path="data.csv", encoding="utf-8")
```

---

## 速查表

### DocumentLoader 速查
```python
from langchain_community.document_loaders import (
    CSVLoader,           # CSV 文件
    PyPDFLoader,         # PDF 文件
    WebBaseLoader,       # 网页
    TextLoader,          # 文本文件
    DirectoryLoader      # 整个目录
)
docs = loader.load()  # 返回 Document 列表
```

### TextSplitter 速查
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)
```

### Embedding 速查
```python
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
vector = embeddings.embed_query("文本")
```

### VectorStore 速查
```python
from langchain_community.vectorstores import FAISS
vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("faiss_index")
results = vectorstore.similarity_search("问题", k=3)
```

### RAG 链速查
```python
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | rag_prompt
    | llm
    | StrOutputParser()
)
answer = rag_chain.invoke("问题")
```

---

## 小测验

1. **RAG 的完整流程是什么？每个步骤的作用？**
2. **为什么要进行文本分割？chunk_size 和 chunk_overlap 分别控制什么？**
3. **Embedding 模型的作用是什么？它输出的是什么？**
4. **FAISS 和 Chroma 的区别是什么？什么时候用哪个？**
5. **在 RAG 链中，retriever | format_docs 是什么意思？**

---

## 扩展阅读

- [LangChain 官方文档 - Document Loaders](https://docs.langchain.com/oss/python/langchain/document-loaders)
- [LangChain 官方文档 - Text Splitters](https://docs.langchain.com/oss/python/langchain/text-splitters)
- [LangChain 官方文档 - Vector Stores](https://docs.langchain.com/oss/python/langchain/vector-stores)
- [LangChain 官方文档 - Retrievers](https://docs.langchain.com/oss/python/langchain/retrievers)
- [FAISS 官方文档](https://faiss.ai/)
