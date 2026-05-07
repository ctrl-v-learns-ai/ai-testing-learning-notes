# -*- coding: utf-8 -*-
"""
Pandas Project 02: Data Cleaning Pipeline
"""

import pandas as pd
import numpy as np

# Create messy data
np.random.seed(42)
data = {
    "id": range(1, 11),
    "name": ["Alice", "Bob", "Charlie", "Alice", "David",
             "Eve", "Frank", "Bob", "Grace", "Henry"],
    "age": [25, 30, np.nan, 25, 28, 32, np.nan, 30, 27, 45],
    "salary": ["5000", "6000", "7000", "5000", "N/A",
               "8000", "6500", "6000", "5500", "90000"],
    "email": ["alice@email.com", "bob@email.com", "charlie@email.com",
              "alice@email.com", "david@email.com", "eve@email.com",
              "frank@email.com", "bob@email.com", "grace@email.com",
              "henry@email.com"],
    "join_date": ["2023-01-15", "2023-02-20", "2023-03-10",
                  "2023-01-15", "2023-04-05", "2023-05-12",
                  "2023-06-18", "2023-02-20", "2023-07-22",
                  "2023-08-30"]
}
df = pd.DataFrame(data)

print("=" * 60)
print("  Data Cleaning Pipeline")
print("=" * 60)

# Step 1: Data quality report
print("\n[Step 1] Data Quality Report")
print(f"  Total rows: {len(df)}")
print(f"  Total columns: {len(df.columns)}")
print(f"  Missing values:\n{df.isnull().sum()}")
print(f"  Duplicate rows: {df.duplicated().sum()}")

# Step 2: Handle missing values
print("\n[Step 2] Handle Missing Values")
df["age"] = df["age"].fillna(df["age"].median())
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["salary"] = df["salary"].fillna(df["salary"].median())
print("  Filled age with median")
print("  Converted salary to numeric, filled with median")

# Step 3: Remove duplicates
print("\n[Step 3] Remove Duplicates")
before = len(df)
df = df.drop_duplicates(subset=["name"], keep="first")
after = len(df)
print(f"  Removed {before - after} duplicate rows")

# Step 4: Data validation
print("\n[Step 4] Data Validation")
# Check age range
invalid_age = df[(df["age"] < 0) | (df["age"] > 100)]
print(f"  Invalid age entries: {len(invalid_age)}")

# Check salary range
invalid_salary = df[df["salary"] > 100000]
print(f"  Invalid salary entries: {len(invalid_salary)}")

# Step 5: Standardize formats
print("\n[Step 5] Standardize Formats")
df["name"] = df["name"].str.strip().str.title()
df["email"] = df["email"].str.lower()
df["join_date"] = pd.to_datetime(df["join_date"])
print("  Standardized name, email, date formats")

# Final report
print("\n" + "=" * 60)
print("  Cleaned Data Summary")
print("=" * 60)
print(f"\nFinal shape: {df.shape}")
print(f"\nData types:\n{df.dtypes}")
print(f"\nCleaned data:\n{df}")
print(f"\nStatistics:\n{df.describe()}")
