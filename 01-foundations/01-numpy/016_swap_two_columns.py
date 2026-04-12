# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 016_swap_two_columns.py
@Author    : Ctrl V
@Time      : 2026/4/12 12:59
@Desc      : Swap columns 1 and 2 in the array arr.

@Dependencies:
    pip install numpy
"""
import numpy as np
arr = np.arange(9).reshape(3,3)

arr1 = arr[:, [1,0,2]]
print(arr1)