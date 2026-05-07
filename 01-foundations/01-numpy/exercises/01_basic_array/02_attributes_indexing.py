# -*- coding: utf-8 -*-
"""
Exercise 2: Array Attributes and Indexing
Goal: Learn array properties and element access
Prerequisites: Array creation
"""

import numpy as np

# Exercise 2.1: Array attributes
print("=== Array Attributes ===")
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Shape: {arr.shape}")
print(f"Dimensions: {arr.ndim}")
print(f"Size: {arr.size}")
print(f"Dtype: {arr.dtype}")

# Exercise 2.2: Indexing
print("\n=== Indexing ===")
print(f"Element [0,0]: {arr[0, 0]}")
print(f"Element [1,2]: {arr[1, 2]}")
print(f"Last element: {arr[-1, -1]}")

# Exercise 2.3: Slicing
print("\n=== Slicing ===")
print(f"First row: {arr[0, :]}")
print(f"Second column: {arr[:, 1]}")
print(f"Sub-array: {arr[0:1, 1:]}")

# Exercise 2.4: Boolean indexing
print("\n=== Boolean Indexing ===")
arr = np.array([1, 2, 3, 4, 5, 6])
mask = arr > 3
print(f"Elements > 3: {arr[mask]}")

"""
Questions:
1. What does arr.shape return for a 1D array?
2. How to get all even numbers from an array?
3. What is the difference between arr[0] and arr[0, :]?
"""
