# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 006_replace_items_without_modifying.py
@Author    : Ctrl V
@Time      : 2026/4/11 13:50
@Desc      : Replace all odd numbers in arr with -1 without modifying the original arr.

@Dependencies:
    pip install numpy
"""
import numpy as np
arr1 = np.arange(10)
arr2 = np.copy(arr1)
arr2[arr2 % 2 == 1] = -1
arr3 = np.where(arr1 % 2 == 1, -1, arr1) #最推荐
print(arr1)
print(arr2)
print(arr3)