# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 023_limit_num_of_print.py
@Author    : Ctrl V
@Time      : 2026/4/12 13:32
@Desc      : Set NumPy print options so that array a displays a maximum of 6 elements, with the rest replaced by ellipsis.

@Dependencies:
    pip install numpy
"""
import numpy as np
a = np.arange(15)
print(a)
np.set_printoptions(threshold=6)
print(a)