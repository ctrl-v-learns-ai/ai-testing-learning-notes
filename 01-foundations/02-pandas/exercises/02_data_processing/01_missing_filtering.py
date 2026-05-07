# -*- coding: utf-8 -*-
"""
Exercise 1: Missing Values and Filtering
Goal: Learn data cleaning operations
Prerequisites: DataFrame basics
"""

import pandas as pd
import numpy as np

# Create data with missing values
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "age": [25, np.nan, 35, 28, np.nan],
    "salary": [5000, 6000, np.nan, 5500, 7000],
    "city": ["Beijing", "Shanghai", "Guangzhou", np.nan, "Shenzhen"]
})

print("=== Original Data ===")
print(df)

# Exercise 1.1: Detect missing values
print("\n=== Missing Values ===")
print(df.isnull())
print(f"\nMissing per column:\n{df.isnull().sum()}")
print(f"Total missing: {df.isnull().sum().sum()}")

# Exercise 1.2: Fill missing values
print("\n=== Fill Missing ===")
df_filled = df.copy()
df_filled["age"] = df_filled["age"].fillna(df_filled["age"].mean())
df_filled["salary"] = df_filled["salary"].fillna(0)
df_filled["city"] = df_filled["city"].fillna("Unknown")
print(df_filled)

# Exercise 1.3: Drop missing values
print("\n=== Drop Missing ===")
print(f"Drop rows with any missing:\n{df.dropna()}")
print(f"\nDrop rows where age is missing:\n{df.dropna(subset=["age"])}")

# Exercise 1.4: Conditional filtering
print("\n=== Filtering ===")
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "age": [25, 30, 35, 28, 32],
    "salary": [5000, 6000, 7000, 5500, 8000],
    "dept": ["IT", "HR", "IT", "HR", "IT"]
}
df2 = pd.DataFrame(data)

print(f"Age > 28:\n{df2[df2["age"] > 28]}")
print(f"\nDept is IT:\n{df2[df2["dept"] == "IT"]}")
print(f"\nAge > 25 and salary > 5500:\n{df2[(df2["age"] > 25) & (df2["salary"] > 5500)]}")

"""
Questions:
1. What is the difference between dropna() and fillna()?
2. How to combine multiple filter conditions?
3. What does subset parameter do in dropna()?
"""
