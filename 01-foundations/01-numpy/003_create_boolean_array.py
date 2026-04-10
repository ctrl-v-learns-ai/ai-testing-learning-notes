# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 003_create_boolean_array.py
@Author    : Ctrl V
@Time      : 2026/4/11 01:33
@Desc      : Create a 3×3 numpy array of all True values.

@Dependencies:
    pip install numpy
"""
import numpy as np

arr1 = np.full((3,3), True)
arr2 = np.ones((3,3), dtype=bool)
arr3 = np.ones((3,3)) > 0
print(arr1)
print(arr2)
print(arr3)