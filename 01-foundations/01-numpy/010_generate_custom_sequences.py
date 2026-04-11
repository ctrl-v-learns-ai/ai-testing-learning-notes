# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 010_generate_custom_sequences.py
@Author    : Ctrl V
@Time      : 2026/4/11 23:53
@Desc      : Using only numpy functions and the input array A, produce an array that first
            repeats each element 3 times, then tiles the whole array 3 times.

@Dependencies:
    pip install numpy
"""
import numpy as np
a = np.array([1,2,3])
b = np.repeat(a, 3)
print(b)
c = np.concatenate([b,a,a,a])
print(c)