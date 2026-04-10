# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 004_extract_items.py
@Author    : Ctrl V
@Time      : 2026/4/11 01:43
@Desc      : Extract all odd numbers from arr.

@Dependencies:
    pip install numpy
"""
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr2 = arr[arr % 2 == 1] #布尔索引是在分析之前过滤数据清理和子集数据集中的行的主要方法。
print(arr2)