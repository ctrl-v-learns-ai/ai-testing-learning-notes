# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 014_extract_numbers.py
@Author    : Ctrl V
@Time      : 2026/4/12 00:23
@Desc      : From array A, extract all items between 5 and 10 (inclusive).

@Dependencies:
    pip install numpy
"""
import numpy as np
a = np.array([2, 6, 1, 9, 10, 3, 27])
c = a[(a >= 5) & (a <= 10)]
print(c)