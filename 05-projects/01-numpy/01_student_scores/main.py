# -*- coding: utf-8 -*-
"""
NumPy Project 01: Student Scores Manager
"""

import numpy as np

# Create sample data: 5 students x 3 subjects (Math, English, Science)
scores = np.array([
    [85, 92, 78],
    [90, 88, 95],
    [76, 85, 82],
    [95, 90, 88],
    [88, 76, 90]
])

student_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
subjects = ["Math", "English", "Science"]

print("=" * 50)
print("  Student Scores Manager")
print("=" * 50)

# Display all scores
print("\nAll Scores:")
print(f"{'Student':<10}", end="")
for s in subjects:
    print(f"{s:<10}", end="")
print()
for i, name in enumerate(student_names):
    print(f"{name:<10}", end="")
    for score in scores[i]:
        print(f"{score:<10}", end="")
    print()

# Statistics per subject
print("\nSubject Statistics:")
print(f"{'Subject':<10} {'Mean':<8} {'Max':<8} {'Min':<8} {'Std':<8}")
for j, subject in enumerate(subjects):
    col = scores[:, j]
    print(f"{subject:<10} {col.mean():<8.1f} {col.max():<8} {col.min():<8} {col.std():<8.1f}")

# Total scores per student
totals = scores.sum(axis=1)
print("\nStudent Rankings:")
rankings = np.argsort(totals)[::-1]
for rank, idx in enumerate(rankings, 1):
    print(f"  {rank}. {student_names[idx]}: {totals[idx]} points")

# Overall statistics
print(f"\nOverall Statistics:")
print(f"  Total students: {len(student_names)}")
print(f"  Average score: {scores.mean():.1f}")
print(f"  Highest score: {scores.max()}")
print(f"  Lowest score: {scores.min()}")
