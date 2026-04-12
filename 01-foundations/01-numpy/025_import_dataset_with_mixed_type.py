# -*- coding: utf-8 -*-
"""
@Project   : ai-testing-learning-notes
@File      : 025_import_dataset_with_mixed_type.py
@Author    : Ctrl V
@Time      : 2026/4/12 13:43
@Desc      : Import the iris dataset from the URL, keeping the text (species) column intact alongside the numeric columns.

@Dependencies:
    pip install numpy
"""
import numpy as np
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
arr = np.genfromtxt(url, delimiter=',', dtype='object')
print(arr)
print(arr[:3])