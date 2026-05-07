# -*- coding: utf-8 -*-
"""
Exercise 2: Array Operations and Broadcasting
Goal: Learn element-wise operations and broadcasting
Prerequisites: Array creation, statistics
"""

import numpy as np

# Exercise 2.1: Element-wise operations
print("=== Element-wise Operations ===")
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(f"a + b = {a + b}")
print(f"a * b = {a * b}")
print(f"a ** 2 = {a ** 2}")
print(f"sqrt(a) = {np.sqrt(a)}")

# Exercise 2.2: Broadcasting
print("\n=== Broadcasting ===")
arr = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10

print(f"arr + scalar:\n{arr + scalar}")

row = np.array([10, 20, 30])
print(f"arr + row:\n{arr + row}")

col = np.array([[100], [200]])
print(f"arr + col:\n{arr + col}")

# Exercise 2.3: Comparison and Logic
print("\n=== Comparison ===")
arr = np.array([1, 2, 3, 4, 5])
print(f"arr > 3: {arr > 3}")
print(f"arr == 3: {arr == 3}")
print(f"(arr > 2) & (arr < 5): {(arr > 2) & (arr < 5)}")

# Exercise 2.4: np.where
print("\n=== np.where ===")
result = np.where(arr > 3, "big", "small")
print(f"Where arr > 3: {result}")

"""
Questions:
1. What are the rules of broadcasting?
2. How to combine multiple conditions?
3. What does np.where return?
"""
