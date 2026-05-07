# -*- coding: utf-8 -*-
"""
Exercise 2: Data Selection and IO
Goal: Learn data selection and file operations
Prerequisites: Series, DataFrame basics
"""

import pandas as pd
import os

# Exercise 2.1: Create sample data
print("=== Create DataFrame ===")
data = {
    "product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "price": [5999, 3999, 2999, 1999, 499],
    "stock": [50, 100, 75, 30, 200],
    "category": ["Computer", "Phone", "Tablet", "Computer", "Accessory"]
}
df = pd.DataFrame(data)
print(df)

# Exercise 2.2: Select columns
print("\n=== Select Columns ===")
print(f"Single column (Series):\n{df["product"]}")
print(f"\nMultiple columns (DataFrame):\n{df[["product", "price"]]}")

# Exercise 2.3: Select rows
print("\n=== Select Rows ===")
print(f"First row (iloc):\n{df.iloc[0]}")
print(f"\nFirst 2 rows:\n{df.iloc[0:2]}")

# Exercise 2.4: Select rows and columns
print("\n=== Select Both ===")
print(f"iloc [0:2, 0:2]:\n{df.iloc[0:2, 0:2]}")

# Exercise 2.5: Add and drop columns
print("\n=== Add/Drop Columns ===")
df["total_value"] = df["price"] * df["stock"]
print(f"Added total_value:\n{df}")

df_dropped = df.drop("total_value", axis=1)
print(f"\nDropped total_value:\n{df_dropped}")

# Exercise 2.6: Save and load CSV
print("\n=== CSV IO ===")
df.to_csv("temp_products.csv", index=False)
df_loaded = pd.read_csv("temp_products.csv")
print(f"Loaded from CSV:\n{df_loaded}")

# Cleanup
os.remove("temp_products.csv")

"""
Questions:
1. What is the difference between df["col"] and df[["col"]]?
2. What does axis=1 mean in drop()?
3. Why use index=False in to_csv()?
"""
