# -*- coding: utf-8 -*-
"""
Pandas Project 01: CSV Data Analyzer
"""

import pandas as pd

# Create sample data
data = {
    "OrderID": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard",
                "Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "Price": [5999, 3999, 2999, 1999, 499, 5999, 3999, 2999, 1999, 499],
    "Quantity": [2, 5, 3, 4, 10, 1, 3, 2, 5, 8],
    "Customer": ["Alice", "Bob", "Charlie", "David", "Eve",
                 "Alice", "Frank", "Grace", "Bob", "Henry"]
}
df = pd.DataFrame(data)

print("=" * 60)
print("  CSV Data Analyzer")
print("=" * 60)

# Data overview
print("\nData Overview:")
print(f"  Rows: {df.shape[0]}")
print(f"  Columns: {df.shape[1]}")
print(f"  Columns: {list(df.columns)}")

print("\nFirst 5 rows:")
print(df.head())

# Data types
print("\nData Types:")
print(df.dtypes)

# Basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Product analysis
print("\nProduct Analysis:")
product_stats = df.groupby("Product").agg({
    "Quantity": "sum",
    "Price": "mean"
}).rename(columns={"Quantity": "Total_Sold", "Price": "Avg_Price"})
print(product_stats)

# Customer analysis
print("\nCustomer Analysis:")
customer_stats = df.groupby("Customer")["OrderID"].count().rename("Order_Count")
print(customer_stats.sort_values(ascending=False))

# Revenue calculation
df["Revenue"] = df["Price"] * df["Quantity"]
print(f"\nTotal Revenue: {df["Revenue"].sum():,}")

# Top orders
print("\nTop 3 Orders by Revenue:")
top_orders = df.nlargest(3, "Revenue")
print(top_orders[["OrderID", "Product", "Revenue"]])

# Save results
df.to_csv("orders_analyzed.csv", index=False)
print("\nResults saved to orders_analyzed.csv")
