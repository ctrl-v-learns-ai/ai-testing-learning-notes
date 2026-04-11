# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 008_stack_two_arrays_vertically.py
@Author    : Ctrl V
@Time      : 2026/4/11 14:35
@Desc      : Stack arrays a and b vertically.

@Dependencies:
    pip install numpy
"""
import numpy as np

a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([a, b])
print(c)