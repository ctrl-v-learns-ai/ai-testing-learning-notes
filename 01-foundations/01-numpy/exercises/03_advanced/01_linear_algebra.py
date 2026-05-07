# -*- coding: utf-8 -*-
"""
Exercise 1: Linear Algebra
Goal: Learn matrix operations
Prerequisites: Array operations
"""

import numpy as np

# Exercise 1.1: Matrix operations
print("=== Matrix Operations ===")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"A:\n{A}")
print(f"B:\n{B}")
print(f"A @ B (matrix multiply):\n{A @ B}")
print(f"A * B (element-wise):\n{A * B}")

# Exercise 1.2: Determinant and Inverse
print("\n=== Determinant and Inverse ===")
print(f"det(A): {np.linalg.det(A):.2f}")
print(f"inv(A):\n{np.linalg.inv(A)}")

# Exercise 1.3: Eigenvalues
print("\n=== Eigenvalues ===")
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"Eigenvalues: {eigenvalues}")
print(f"Eigenvectors:\n{eigenvectors}")

# Exercise 1.4: Solve linear equations
print("\n=== Solve Ax = b ===")
A = np.array([[2, 1], [1, 3]])
b = np.array([5, 7])
x = np.linalg.solve(A, b)
print(f"Solution x: {x}")
print(f"Verify A @ x: {A @ x}")

"""
Questions:
1. What is the difference between @ and *?
2. When do we need inverse matrix?
3. What are eigenvalues used for?
"""
