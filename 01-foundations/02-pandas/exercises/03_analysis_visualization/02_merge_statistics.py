# -*- coding: utf-8 -*-
"""
Exercise 2: Merge and Statistical Analysis
Goal: Learn data merging and statistics
Prerequisites: GroupBy basics
"""

import pandas as pd

# Exercise 2.1: Create related DataFrames
employees = pd.DataFrame({
    "emp_id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "dept_id": [101, 102, 101, 103, 102]
})

departments = pd.DataFrame({
    "dept_id": [101, 102, 103],
    "dept_name": ["IT", "HR", "Sales"]
})

print("=== Employees ===")
print(employees)
print("\n=== Departments ===")
print(departments)

# Exercise 2.2: Merge (Inner Join)
print("\n=== Inner Join ===")
merged = pd.merge(employees, departments, on="dept_id")
print(merged)

# Exercise 2.3: Left Join
print("\n=== Left Join ===")
left = pd.merge(employees, departments, on="dept_id", how="left")
print(left)

# Exercise 2.4: Concat
print("\n=== Concat ===")
df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
print(f"Vertical:\n{pd.concat([df1, df2])}")
print(f"\nHorizontal:\n{pd.concat([df1, df2], axis=1)}")

# Exercise 2.5: Statistical functions
print("\n=== Statistics ===")
data = pd.DataFrame({
    "math": [85, 90, 78, 92, 88],
    "english": [80, 85, 90, 88, 92],
    "science": [90, 88, 85, 80, 82]
})
print(f"Correlation:\n{data.corr()}")
print(f"\nValue counts for math:\n{data["math"].value_counts()}")

"""
Questions:
1. What is the difference between inner and left join?
2. When to use concat vs merge?
3. What does corr() return?
"""
