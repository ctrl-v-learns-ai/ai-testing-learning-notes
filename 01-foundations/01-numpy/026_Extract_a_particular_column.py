# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 026_Extract_a_particular_column.py
@Author    : Ctrl V
@Time      : 2026/4/12 21:26
@Desc      : Extract the text column species (5th field) from the 1D structured array iris_1d.

@Dependencies:
    pip install numpy
"""
import numpy as np
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
arr = np.genfromtxt(url, delimiter=',', dtype=None)
print(arr.shape)

result = np.array([row[4] for row in arr])
print(result[:5])