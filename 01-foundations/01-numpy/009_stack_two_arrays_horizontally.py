# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 009_stack_two_arrays_horizontally.py
@Author    : Ctrl V
@Time      : 2026/4/11 23:42
@Desc      : Stack arrays a and b horizontally.

@Dependencies:
    pip install numpy
"""
import numpy as np

a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([a, b], axis=1)
print(c)