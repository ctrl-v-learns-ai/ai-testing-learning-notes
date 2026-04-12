# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 027_convert_array.py
@Author    : Ctrl V
@Time      : 2026/4/12 21:32
@Desc      : Convert the 1D structured array iris_1d to a 2D array iris_2d by omitting the species text field and keeping only the four numeric columns.

@Dependencies:
    pip install numpy
"""
import numpy as np
from numpy import ndarray

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
arr = np.genfromtxt(url, delimiter=',', dtype=None, usecols=(0, 1, 2, 3))
print(arr[:4])
