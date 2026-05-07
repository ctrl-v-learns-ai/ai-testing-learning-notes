# -*- coding: utf-8 -*-
"""
Exercise 1: Series and DataFrame Basics
Goal: Learn Pandas core data structures
Prerequisites: Python basics
"""

import pandas as pd

# Exercise 1.1: Series
print("=== Series ===")
s = pd.Series([10, 20, 30, 40, 50], index=["a", "b", "c", "d", "e"])
print(s)
print(f"\nAccess by label: s["b"] = {s["b"]}")
print(f"Access by position: s.iloc[1] = {s.iloc[1]}")

# Exercise 1.2: DataFrame from dict
print("\n=== DataFrame from Dict ===")
data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 28],
    "city": ["Beijing", "Shanghai", "Guangzhou", "Shenzhen"]
}
df = pd.DataFrame(data)
print(df)

# Exercise 1.3: DataFrame attributes
print("\n=== DataFrame Attributes ===")
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"Dtypes:\n{df.dtypes}")

# Exercise 1.4: Basic operations
print("\n=== Basic Operations ===")
print(f"Head 2:\n{df.head(2)}")
print(f"\nDescribe:\n{df.describe()}")

"""
Questions:
1. What is the difference between Series and DataFrame?
2. How to access elements in Series?
3. What does df.describe() return?
"""
