# -*- coding: utf-8 -*-
"""
Exercise 1: Array Creation
Goal: Learn different ways to create NumPy arrays
Prerequisites: Python basics
"""

import numpy as np

# Exercise 1.1: Create array from list
print("=== Create from List ===")
arr1d = np.array([1, 2, 3, 4, 5])
print(f"1D array: {arr1d}")
print(f"Type: {type(arr1d)}")

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D array:\n{arr2d}")

# Exercise 1.2: Create special arrays
print("\n=== Special Arrays ===")
zeros = np.zeros((2, 3))
print(f"Zeros:\n{zeros}")

ones = np.ones((3, 2))
print(f"Ones:\n{ones}")

eye = np.eye(3)
print(f"Identity matrix:\n{eye}")

# Exercise 1.3: Create sequences
print("\n=== Sequences ===")
arange = np.arange(0, 10, 2)
print(f"arange(0,10,2): {arange}")

linspace = np.linspace(0, 1, 5)
print(f"linspace(0,1,5): {linspace}")

# Exercise 1.4: Random arrays
print("\n=== Random Arrays ===")
rand = np.random.rand(2, 3)
print(f"Random (0-1):\n{rand}")

randint = np.random.randint(0, 10, (2, 3))
print(f"Random int (0-10):\n{randint}")

"""
Questions:
1. What is the difference between arange and linspace?
2. How to create a 3x3 matrix filled with 7?
3. What does np.random.seed(42) do?
"""
