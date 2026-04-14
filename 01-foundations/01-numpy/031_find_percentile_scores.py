# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 031_find_percentile_scores.py
@Author    : Ctrl V
@Time      : 2026/4/13 22:24
@Desc      : Find the 5th and 95th percentile of the sepallength array.

@Dependencies:
    pip install numpy
"""
import numpy as np
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

percentile1, percentile2 = np.percentile(sepallength, [5, 95])
print(percentile1, percentile2)