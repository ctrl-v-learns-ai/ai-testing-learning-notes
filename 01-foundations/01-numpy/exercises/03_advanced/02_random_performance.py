# -*- coding: utf-8 -*-
"""
Exercise 2: Random Numbers and Performance
Goal: Learn random generation and vectorization
Prerequisites: Basic operations
"""

import numpy as np
import time

# Exercise 2.1: Random number generation
print("=== Random Numbers ===")

# Set seed for reproducibility
np.random.seed(42)

# Different distributions
uniform = np.random.rand(5)
print(f"Uniform [0,1): {uniform}")

normal = np.random.normal(0, 1, 5)
print(f"Normal (0,1): {normal}")

randint = np.random.randint(1, 10, 5)
print(f"Random int: {randint}")

# Exercise 2.2: Random choice
print("\n=== Random Choice ===")
arr = np.array([10, 20, 30, 40, 50])
choices = np.random.choice(arr, size=3, replace=False)
print(f"Random choice: {choices}")

# Exercise 2.3: Performance comparison
print("\n=== Performance ===")

# Python loop
start = time.time()
total = 0
for i in range(1000000):
    total += i
loop_time = time.time() - start

# NumPy vectorized
start = time.time()
total = np.sum(np.arange(1000000))
numpy_time = time.time() - start

print(f"Loop time: {loop_time:.4f}s")
print(f"NumPy time: {numpy_time:.4f}s")
print(f"Speedup: {loop_time/numpy_time:.1f}x")

"""
Questions:
1. Why set random seed?
2. What is vectorization?
3. When replace=False in choice?
"""
