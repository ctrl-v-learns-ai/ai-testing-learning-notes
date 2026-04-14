# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 028_compute_mean_median_and_standard.py
@Author    : Ctrl V
@Time      : 2026/4/13 22:13
@Desc      : Find the mean, median, and standard deviation of the sepallength column (1st column) from the iris dataset.

@Dependencies:
    pip install numpy
"""
import numpy as np
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
arr = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
mu, med, sd = np.mean(arr), np.median(arr), np.std(arr)
print(mu, med, sd)