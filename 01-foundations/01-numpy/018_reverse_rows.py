# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 018_reverse_rows.py
@Author    : Ctrl V
@Time      : 2026/4/12 13:04
@Desc      : Reverse the row order of the 2D array arr.

@Dependencies:
    pip install numpy
"""
import numpy as np
arr = np.arange(9).reshape(3,3)
print(arr)
result = arr[::-1]
print(result)