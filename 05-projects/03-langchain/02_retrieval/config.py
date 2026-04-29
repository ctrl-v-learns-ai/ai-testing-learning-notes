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

# RAG 配置
CHUNK_SIZE = 500        # 文本分割块大小
CHUNK_OVERLAP = 50      # 块重叠大小
TOP_K = 3               # 检索返回的文档数量
TEMPERATURE = 0.3       # 生成温度（RAG 场景建议较低）
