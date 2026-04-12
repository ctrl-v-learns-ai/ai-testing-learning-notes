# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 019_reverse_columns.py
@Author    : Ctrl V
@Time      : 2026/4/12 13:12
@Desc      : Reverse the column order of the 2D array arr.

@Dependencies:
    pip install numpy
"""
import numpy as np
arr = np.arange(9).reshape(3,3)

result = arr[:, ::-1]
print(result)