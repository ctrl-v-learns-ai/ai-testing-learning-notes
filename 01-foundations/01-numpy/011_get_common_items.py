# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 011_get_common_items.py
@Author    : Ctrl V
@Time      : 2026/4/12 00:05
@Desc      : Find the common items between arrays a and b.

@Dependencies:
    pip install numpy
"""
import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c = np.intersect1d(a,b)
print(c)