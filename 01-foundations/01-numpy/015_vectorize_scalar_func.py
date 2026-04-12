# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 015_vectorize_scalar_func.py
@Author    : Ctrl V
@Time      : 2026/4/12 12:50
@Desc      : Convert the scalar function maxx into a vectorized version that works element-wise on arrays a and b.

@Dependencies:
    pip install numpy
"""
import numpy as np

def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

max_arr = np.vectorize(maxx, otypes=[float])
c = max_arr(a, b)
print(c)