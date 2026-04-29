# -*- coding: utf-8 -*-
"""
配置管理模块
"""

import os
from dotenv import load_dotenv

load_dotenv()

# API 配置
API_KEY = os.getenv("MIMO_API_KEY")
API_URL = os.getenv("MIMO_API_URL")
MODEL_NAME = os.getenv("MIMO_MODEL", "mimo-v2-flash")

# 分析配置
TEMPERATURE = 0.3  # 分析任务用较低温度
