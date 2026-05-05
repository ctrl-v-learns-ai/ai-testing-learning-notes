# -*- coding: utf-8 -*-
"""
配置管理模块
集中管理 API 密钥、模型参数等配置
"""

import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# API 配置
API_KEY = os.getenv("MIMO_API_KEY")
API_URL = os.getenv("MIMO_API_URL")
MODEL_NAME = os.getenv("MIMO_MODEL", "mimo-v2-flash")

# 模型参数
TEMPERATURE = 0.7  # 对话场景用较高温度，增加创造性
MAX_TOKENS = 2000  # 最大输出长度
