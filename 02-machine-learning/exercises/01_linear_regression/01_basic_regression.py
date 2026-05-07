# -*- coding: utf-8 -*-
"""
练习8：线性回归
练习目标：掌握线性回归的使用
前置知识：NumPy、Pandas
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler

# 练习8.1：简单线性回归
print("=== 练习8.1：简单线性回归 ===")

# 生成数据
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 2 * X.squeeze() + 3 + np.random.randn(100) * 2

# 划分数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建模型
model = LinearRegression()

# 训练
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 评估
print(f"斜率: {model.coef_[0]:.4f}")
print(f"截距: {model.intercept_:.4f}")
print(f"MSE: {mean_squared_error(y_test, y_pred):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
print(f"MAE: {mean_absolute_error(y_test, y_pred):.4f}")
print(f"R²: {r2_score(y_test, y_pred):.4f}")

# 练习8.2：多元线性回归
print("\n=== 练习8.2：多元线性回归 ===")

# 生成多特征数据
np.random.seed(42)
X = np.random.rand(100, 3) * 10
y = 2 * X[:, 0] + 3 * X[:, 1] - 1.5 * X[:, 2] + 5 + np.random.randn(100) * 2

# 划分数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建模型
model = LinearRegression()

# 训练
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 评估
print(f"系数: {model.coef_}")
print(f"截距: {model.intercept_:.4f}")
print(f"R²: {r2_score(y_test, y_pred):.4f}")

# 练习8.3：正则化
print("\n=== 练习8.3：正则化 ===")

# Ridge 回归
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
y_pred_ridge = ridge.predict(X_test)

# Lasso 回归
lasso = Lasso(alpha=1.0)
lasso.fit(X_train, y_train)
y_pred_lasso = lasso.predict(X_test)

print(f"线性回归 R²: {r2_score(y_test, y_pred):.4f}")
print(f"Ridge R²: {r2_score(y_test, y_pred_ridge):.4f}")
print(f"Lasso R²: {r2_score(y_test, y_pred_lasso):.4f}")

# 练习8.4：特征缩放
print("\n=== 练习8.4：特征缩放 ===")

# 标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 训练模型
model_scaled = LinearRegression()
model_scaled.fit(X_train_scaled, y_train)

# 预测
y_pred_scaled = model_scaled.predict(X_test_scaled)

print(f"标准化前 R²: {r2_score(y_test, y_pred):.4f}")
print(f"标准化后 R²: {r2_score(y_test, y_pred_scaled):.4f}")

# 练习8.5：交叉验证
print("\n=== 练习8.5：交叉验证 ===")

# 5折交叉验证
scores = cross_val_score(model, X, y, cv=5, scoring='r2')
print(f"交叉验证 R²: {scores.mean():.4f} (+/- {scores.std() * 2:.4f})")

"""
思考题：
1. 线性回归的公式是什么？
2. MSE、RMSE、MAE、R² 的区别？
3. 什么是正则化？Ridge 和 Lasso 的区别？
4. 什么是数据泄露？如何避免？
5. 什么是过拟合？如何解决？
"""
