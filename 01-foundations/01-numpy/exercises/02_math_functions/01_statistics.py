# -*- coding: utf-8 -*-
"""
Exercise 1: Statistical Functions
Goal: Learn NumPy statistical operations
Prerequisites: Array creation
"""

import numpy as np

# Create sample data
data = np.array([85, 90, 78, 92, 88, 76, 95, 82, 90, 87])

print("=== Statistical Functions ===")
print(f"Data: {data}")
print(f"Mean: {np.mean(data):.1f}")
print(f"Median: {np.median(data):.1f}")
print(f"Std: {np.std(data):.1f}")
print(f"Variance: {np.var(data):.1f}")
print(f"Min: {np.min(data)}")
print(f"Max: {np.max(data)}")
print(f"Sum: {np.sum(data)}")

print("\n=== Cumulative ===")
print(f"Cumsum: {np.cumsum(data)}")

print("\n=== Percentiles ===")
print(f"25th: {np.percentile(data, 25)}")
print(f"50th: {np.percentile(data, 50)}")
print(f"75th: {np.percentile(data, 75)}")

"""
Questions:
1. What is the difference between std and var?
2. When to use median instead of mean?
3. What does cumsum return?
"""
