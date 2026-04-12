# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 022_suppress_scientific_notation.py
@Author    : Ctrl V
@Time      : 2026/4/12 13:28
@Desc      : Pretty print rand_arr by suppressing scientific notation (like 1e10).

@Dependencies:
    pip install numpy
"""
import numpy as np
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
print(rand_arr)
np.set_printoptions(precision=6, suppress=True)
print(rand_arr)