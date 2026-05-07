# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MIMO_API_KEY")
API_URL = os.getenv("MIMO_API_URL")
MODEL_NAME = os.getenv("MIMO_MODEL", "mimo-v2-flash")

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 3
TEMPERATURE = 0.3
