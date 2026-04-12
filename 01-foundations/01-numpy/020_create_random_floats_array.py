# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 020_create_random_floats_array.py
@Author    : Ctrl V
@Time      : 2026/4/12 13:15
@Desc      : Create a 2D array of shape 5×3 containing random decimal numbers between 5 and 10.

@Dependencies:
    pip install numpy
"""
import numpy as np
arr = np.random.uniform(low=5, high=10, size=(5,3))
print(arr)