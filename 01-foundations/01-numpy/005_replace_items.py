# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 005_replace_items.py
@Author    : Ctrl V
@Time      : 2026/4/11 01:47
@Desc      : Replace all odd numbers in arr with -1.

@Dependencies:
    pip install numpy
"""
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr[arr % 2 == 1] = -1
print(arr)