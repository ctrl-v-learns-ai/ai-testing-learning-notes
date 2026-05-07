# -*- coding: utf-8 -*-
"""
Exercise 3: Shape Operations
Goal: Learn reshape, transpose, concatenate, split
Prerequisites: Array creation, indexing
"""

import numpy as np

# Exercise 3.1: Reshape
print("=== Reshape ===")
arr = np.arange(12)
print(f"Original: {arr}")
print(f"Reshape (3,4):\n{arr.reshape(3, 4)}")
print(f"Reshape (2,-1):\n{arr.reshape(2, -1)}")

# Exercise 3.2: Transpose
print("\n=== Transpose ===")
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original:\n{arr2d}")
print(f"Transposed:\n{arr2d.T}")

# Exercise 3.3: Flatten
print("\n=== Flatten ===")
arr2d = np.array([[1, 2], [3, 4]])
print(f"Flattened: {arr2d.flatten()}")

# Exercise 3.4: Concatenate
print("\n=== Concatenate ===")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"Concatenate: {np.concatenate([a, b])}")

a2d = np.array([[1, 2], [3, 4]])
b2d = np.array([[5, 6], [7, 8]])
print(f"Vstack:\n{np.vstack([a2d, b2d])}")
print(f"Hstack:\n{np.hstack([a2d, b2d])}")

# Exercise 3.5: Split
print("\n=== Split ===")
arr = np.array([1, 2, 3, 4, 5, 6])
parts = np.split(arr, 3)
print(f"Split into 3: {parts}")

"""
Questions:
1. What does -1 mean in reshape?
2. What is the difference between flatten and ravel?
3. When to use vstack vs hstack?
"""
