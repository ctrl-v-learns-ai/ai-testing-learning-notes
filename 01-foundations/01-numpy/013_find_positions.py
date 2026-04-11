# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 013_find_positions.py
@Author    : Ctrl V
@Time      : 2026/4/12 00:21
@Desc      : Get the positions (indices) where elements of a and b are equal.

@Dependencies:
    pip install numpy
"""
import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c = np.where(a == b)
print(c)