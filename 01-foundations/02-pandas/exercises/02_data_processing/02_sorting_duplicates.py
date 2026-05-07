# -*- coding: utf-8 -*-
"""
Exercise 2: Sorting, Duplicates, String Operations
Goal: Learn sorting, deduplication, and string methods
Prerequisites: DataFrame basics, filtering
"""

import pandas as pd

# Create sample data
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Alice", "David"],
    "age": [25, 30, 35, 25, 28],
    "salary": [5000, 6000, 7000, 5000, 5500],
    "email": ["alice@email.com", "bob@email.com", "charlie@email.com",
              "alice@email.com", "david@email.com"]
})

print("=== Original Data ===")
print(df)

# Exercise 2.1: Sorting
print("\n=== Sorting ===")
print(f"Sort by age:\n{df.sort_values("age")}")
print(f"\nSort by age desc:\n{df.sort_values("age", ascending=False)}")
print(f"\nSort by age, then salary:\n{df.sort_values(["age", "salary"])}")

# Exercise 2.2: Duplicates
print("\n=== Duplicates ===")
print(f"Is duplicated:\n{df.duplicated()}")
print(f"\nDuplicate count: {df.duplicated().sum()}")

print(f"\nAfter drop duplicates:\n{df.drop_duplicates()}")
print(f"\nDrop duplicates by name:\n{df.drop_duplicates(subset=["name"])}")

# Exercise 2.3: String operations
print("\n=== String Operations ===")
names = df["name"]
print(f"Lower: {names.str.lower().tolist()}")
print(f"Upper: {names.str.upper().tolist()}")
print(f"Length: {names.str.len().tolist()}")
print(f"Contains 'li': {names.str.contains("li").tolist()}")

# Email domain extraction
print(f"\nEmail domains:")
df["domain"] = df["email"].str.split("@").str[1]
print(df[["email", "domain"]])

"""
Questions:
1. How to sort by multiple columns?
2. What does keep parameter do in drop_duplicates()?
3. How to extract part of a string?
"""
