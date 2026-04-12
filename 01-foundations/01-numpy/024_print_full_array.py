# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 024_print_full_array.py
@Author    : Ctrl V
@Time      : 2026/4/12 13:40
@Desc      : Print the full numpy array a without truncation, even when the print threshold is set low.

@Dependencies:
    pip install numpy
"""
import sys

import numpy as np
a= np.arange(1500)
print(a)
np.set_printoptions(threshold=sys.maxsize)
print(a)