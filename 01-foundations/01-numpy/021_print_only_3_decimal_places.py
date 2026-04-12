# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 021_print_only_3_decimal_places.py
@Author    : Ctrl V
@Time      : 2026/4/12 13:24
@Desc      : Set NumPy print options so that the array rand_arr displays only 3 decimal places.

@Dependencies:
    pip install numpy
"""
import numpy as np
rand_arr = np.random.random((5,3))
np.set_printoptions(precision=3, suppress=True)
print(rand_arr[:4])