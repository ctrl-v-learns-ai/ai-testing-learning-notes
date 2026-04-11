# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 012_remove_items_in_other_array.py
@Author    : Ctrl V
@Time      : 2026/4/12 00:16
@Desc      : From array A, remove all items that are present in array B.

@Dependencies:
    pip install numpy
"""
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
c= np.setdiff1d(a,b)
print(c)