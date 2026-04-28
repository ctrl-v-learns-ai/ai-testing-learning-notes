# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 01_langchain_prompt.py
@Author    : Ctrl V
@Time      : 2026/4/27 23:30
@Desc      : 

@Dependencies:
    pip install langchain langchain-community langchain_openai python-dotenv openai
"""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 加载 .env 文件的环境变量
load_dotenv()

# 获取环境变量
api_key = os.getenv("MIMO_API_KEY")
base_url = os.getenv("MIMO_API_URL")
model_name = os.getenv("MIMO_MODEL")
# api_key = os.getenv("DEEPSEEK_API_KEY")
# base_url = os.getenv("DEEPSEEK_API_URL")
# model_name = os.getenv("DEEPSEEK_MODEL")

llm = ChatOpenAI(
    api_key=api_key,
    base_url=base_url,
    model_name=model_name,
)

# 直接调用模型
# response = llm.invoke("请讲一个笑话")
# print(response.content)

# 处理多行输入
