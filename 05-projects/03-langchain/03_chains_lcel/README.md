# 阶段项目：多步文档分析管道

## 项目简介
一个基于 LCEL 的多步文档分析管道，支持加载文档后进行摘要、关键词提取、情感分析等多维度分析。

## 功能特性
- 支持加载 CSV、TXT 格式的文档
- 并行执行多个分析任务（摘要、关键词、情感）
- 自动生成综合分析报告
- 支持批量处理多个文档
- 流式输出实时显示分析进度

## 运行方式
```bash
# 安装依赖
pip install -r requirements.txt

# 运行程序
python main.py

# 指定文档路径
python main.py --doc ./documents/test.txt
```

## 核心知识点
1. LCEL 管道语法
2. RunnableParallel 并行执行
3. RunnableLambda 自定义函数
4. 多步骤链的组合与嵌套
5. 批量处理

## 项目结构
```
05-projects/03_chains_lcel/
  main.py           # 程序入口
  analysis_chain.py # 分析管道核心
  prompts.py        # 提示模板
  config.py         # 配置管理
  requirements.txt
  README.md
```
