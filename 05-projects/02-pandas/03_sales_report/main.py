# -*- coding: utf-8 -*-
"""
Pandas Project 03: Sales Data Analysis Report
"""

import pandas as pd
import numpy as np

# Create sample sales data
np.random.seed(42)
n = 100

data = {
    "order_id": range(1001, 1001 + n),
    "date": pd.date_range("2024-01-01", periods=n, freq="D"),
    "product": np.random.choice(["Laptop", "Phone", "Tablet", "Monitor"], n),
    "region": np.random.choice(["North", "South", "East", "West"], n),
    "quantity": np.random.randint(1, 10, n),
    "unit_price": np.random.choice([5999, 3999, 2999, 1999], n)
}
df = pd.DataFrame(data)
df["revenue"] = df["quantity"] * df["unit_price"]

print("=" * 60)
print("  Sales Data Analysis Report")
print("=" * 60)

# Overall summary
print("\n[1] Overall Summary")
print(f"  Total orders: {len(df)}")
print(f"  Total revenue: {df["revenue"].sum():,}")
print(f"  Average order value: {df["revenue"].mean():,.0f}")
print(f"  Date range: {df["date"].min()} to {df["date"].max()}")

# Product analysis
print("\n[2] Product Analysis")
product_stats = df.groupby("product").agg(
    orders=("order_id", "count"),
    total_qty=("quantity", "sum"),
    total_revenue=("revenue", "sum"),
    avg_revenue=("revenue", "mean")
).sort_values("total_revenue", ascending=False)
print(product_stats)

# Region analysis
print("\n[3] Region Analysis")
region_stats = df.groupby("region").agg(
    orders=("order_id", "count"),
    total_revenue=("revenue", "sum")
).sort_values("total_revenue", ascending=False)
print(region_stats)

# Pivot table: Product x Region
print("\n[4] Revenue by Product and Region")
pivot = pd.pivot_table(
    df,
    values="revenue",
    index="product",
    columns="region",
    aggfunc="sum",
    margins=True,
    margins_name="Total"
)
print(pivot)

# Top orders
print("\n[5] Top 5 Orders by Revenue")
top5 = df.nlargest(5, "revenue")[["order_id", "product", "region", "revenue"]]
print(top5.to_string(index=False))

# Monthly trend
print("\n[6] Monthly Revenue Trend")
df["month"] = df["date"].dt.to_period("M")
monthly = df.groupby("month")["revenue"].sum()
print(monthly)

print("\n" + "=" * 60)
print("  Report Complete")
print("=" * 60)
