# -*- coding: utf-8 -*-
"""
Exercise 1: GroupBy and Pivot Table
Goal: Learn data aggregation operations
Prerequisites: DataFrame basics, filtering
"""

import pandas as pd

# Create sample data
df = pd.DataFrame({
    "dept": ["IT", "HR", "IT", "HR", "IT", "Sales", "Sales"],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"],
    "salary": [5000, 6000, 7000, 5500, 8000, 4500, 6500],
    "age": [25, 30, 35, 28, 32, 24, 29]
})

print("=== Original Data ===")
print(df)

# Exercise 1.1: Basic GroupBy
print("\n=== Basic GroupBy ===")
print(f"Mean salary by dept:\n{df.groupby("dept")["salary"].mean()}")
print(f"\nCount by dept:\n{df.groupby("dept")["name"].count()}")

# Exercise 1.2: Multiple aggregations
print("\n=== Multiple Aggregations ===")
result = df.groupby("dept").agg({
    "salary": ["mean", "max", "min"],
    "age": "mean"
})
print(result)

# Exercise 1.3: Named aggregations
print("\n=== Named Aggregations ===")
result = df.groupby("dept").agg(
    avg_salary=("salary", "mean"),
    max_salary=("salary", "max"),
    headcount=("name", "count")
)
print(result)

# Exercise 1.4: Pivot Table
print("\n=== Pivot Table ===")
pivot = pd.pivot_table(
    df,
    values="salary",
    index="dept",
    aggfunc=["mean", "sum", "count"]
)
print(pivot)

"""
Questions:
1. What does GroupBy do internally?
2. How to apply multiple aggregation functions?
3. What is the difference between agg and transform?
"""
