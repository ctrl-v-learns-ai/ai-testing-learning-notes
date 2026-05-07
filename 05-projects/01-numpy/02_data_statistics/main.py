# -*- coding: utf-8 -*-
"""
NumPy Project 02: Data Statistics Tool
"""

import numpy as np

# Generate sample data: 100 temperature readings
np.random.seed(42)
temperatures = np.random.normal(loc=25, scale=5, size=100)  # mean=25, std=5

print("=" * 50)
print("  Data Statistics Tool")
print("=" * 50)

# Basic statistics
print("\nBasic Statistics:")
print(f"  Sample size: {len(temperatures)}")
print(f"  Mean: {np.mean(temperatures):.2f}")
print(f"  Median: {np.median(temperatures):.2f}")
print(f"  Std: {np.std(temperatures):.2f}")
print(f"  Min: {np.min(temperatures):.2f}")
print(f"  Max: {np.max(temperatures):.2f}")

# Percentiles
print("\nPercentiles:")
print(f"  25th: {np.percentile(temperatures, 25):.2f}")
print(f"  50th: {np.percentile(temperatures, 50):.2f}")
print(f"  75th: {np.percentile(temperatures, 75):.2f}")

# Outlier detection (using IQR method)
q1 = np.percentile(temperatures, 25)
q3 = np.percentile(temperatures, 75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = temperatures[(temperatures < lower_bound) | (temperatures > upper_bound)]
print(f"\nOutlier Detection (IQR method):")
print(f"  Lower bound: {lower_bound:.2f}")
print(f"  Upper bound: {upper_bound:.2f}")
print(f"  Outliers found: {len(outliers)}")
if len(outliers) > 0:
    print(f"  Outlier values: {outliers}")

# Data normalization (Min-Max scaling)
normalized = (temperatures - np.min(temperatures)) / (np.max(temperatures) - np.min(temperatures))
print(f"\nNormalized Data (Min-Max):")
print(f"  Min: {np.min(normalized):.2f}")
print(f"  Max: {np.max(normalized):.2f}")
print(f"  Mean: {np.mean(normalized):.2f}")

# Z-score standardization
z_scores = (temperatures - np.mean(temperatures)) / np.std(temperatures)
print(f"\nZ-score Standardization:")
print(f"  Mean: {np.mean(z_scores):.2f}")
print(f"  Std: {np.std(z_scores):.2f}")
