# -*- coding: utf-8 -*-
"""
练习20：机器学习面试基础
练习目标：掌握机器学习面试常见问题
前置知识：机器学习基础
"""

import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# 练习20.1：线性回归
print("=== 练习20.1：线性回归 ===")

# 生成数据
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 2 * X.squeeze() + 3 + np.random.randn(100) * 2

# 划分数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
model = LinearRegression()
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

print(f"斜率: {model.coef_[0]:.4f}")
print(f"截距: {model.intercept_:.4f}")

# 练习20.2：逻辑回归
print("\n=== 练习20.2：逻辑回归 ===")

from sklearn.datasets import make_classification

# 生成数据
X, y = make_classification(n_samples=100, n_features=5, n_classes=2, random_state=42)

# 划分数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

print(f"准确率: {accuracy_score(y_test, y_pred):.4f}")

# 练习20.3：决策树
print("\n=== 练习20.3：决策树 ===")

# 训练模型
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train, y_train)

# 预测
y_pred_dt = dt.predict(X_test)

print(f"准确率: {accuracy_score(y_test, y_pred_dt):.4f}")

# 练习20.4：随机森林
print("\n=== 练习20.4：随机森林 ===")

# 训练模型
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 预测
y_pred_rf = rf.predict(X_test)

print(f"准确率: {accuracy_score(y_test, y_pred_rf):.4f}")
print(f"特征重要性: {rf.feature_importances_}")

# 练习20.5：交叉验证
print("\n=== 练习20.5：交叉验证 ===")

# 5折交叉验证
scores = cross_val_score(rf, X, y, cv=5, scoring='accuracy')
print(f"交叉验证准确率: {scores.mean():.4f} (+/- {scores.std() * 2:.4f})")

# 练习20.6：混淆矩阵
print("\n=== 练习20.6：混淆矩阵 ===")

cm = confusion_matrix(y_test, y_pred_rf)
print(f"混淆矩阵:\n{cm}")

# 练习20.7：分类报告
print("\n=== 练习20.7：分类报告 ===")

report = classification_report(y_test, y_pred_rf)
print(f"分类报告:\n{report}")

# 练习20.8：特征缩放
print("\n=== 练习20.8：特征缩放 ===")

# 标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(f"原始数据均值: {X.mean(axis=0)[:3]}")
print(f"标准化后均值: {X_scaled.mean(axis=0)[:3]}")

"""
思考题：
1. 监督学习和无监督学习的区别？
2. 偏差-方差权衡是什么？
3. 如何解决过拟合？
4. 精确率和召回率的区别？
5. 随机森林的原理？
"""
