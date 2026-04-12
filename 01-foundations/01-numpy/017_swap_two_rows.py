# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 017_swap_two_rows.py
@Author    : Ctrl V
@Time      : 2026/4/12 13:02
@Desc      : Swap rows 1 and 2 in the array arr.

@Dependencies:
    pip install numpy
"""
import numpy as np
arr = np.arange(9).reshape(3,3)
result = arr[[1,0,2], :]
print(result)