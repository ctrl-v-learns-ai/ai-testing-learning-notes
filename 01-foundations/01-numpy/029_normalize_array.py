# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 029_normalize_array.py
@Author    : Ctrl V
@Time      : 2026/4/13 22:19
@Desc      : Normalize the sepallength array so the minimum maps to 0 and the maximum maps to 1.

@Dependencies:
    pip install numpy
"""
import numpy as np
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

max_num, min_num = np.max(sepallength), np.min(sepallength)
result = (sepallength - min_num) / (max_num - min_num)
print(result)