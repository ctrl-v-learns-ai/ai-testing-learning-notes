# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 007_reshape_array.py
@Author    : Ctrl V
@Time      : 2026/4/11 14:05
@Desc      : Convert the 1D array arr to a 2D array with 2 rows.

@Dependencies:
    pip install numpy
"""
import numpy as np
arr = np.arange(10)
arr2 = arr.reshape(2, 5)
arr3 = arr.reshape(2, -1) # Setting to -1 automatically decides the number of cols
print(arr2)
print(arr3)