# 阶段项目：个人知识库问答系统

## 项目简介
一个基于 RAG 的个人知识库问答系统，支持上传文档后对文档内容进行提问。

## 功能特性
- 支持加载 CSV、TXT 格式的文档
- 自动分割文档并创建向量索引
- 基于检索的智能问答
- 支持多轮对话
- 显示答案来源（引用的文档片段）

## 运行方式
```bash
# 安装依赖
pip install -r requirements.txt

# 运行程序
python main.py

# 指定文档目录
python main.py --docs ./documents
```

## 核心知识点
1. DocumentLoader 加载文档
2. TextSplitter 分割文本
3. Embedding 模型将文本转为向量
4. FAISS 向量数据库存储和检索
5. RAG 链组合检索和生成

## 项目结构
```
05-projects/02_retrieval/
  main.py           # 程序入口
  rag_bot.py        # RAG 问答机器人核心类
  document_loader.py # 文档加载和处理
  config.py         # 配置管理
  requirements.txt
  README.md
```
