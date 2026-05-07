# -*- coding: utf-8 -*-
"""
练习9：分类算法
练习目标：掌握常用分类算法的使用
前置知识：NumPy、Pandas
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 练习9.1：逻辑回归
print("=== 练习9.1：逻辑回归 ===")

# 生成数据
X, y = make_classification(n_samples=200, n_features=5, n_classes=2, random_state=42)

# 划分数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建模型
model = LogisticRegression(random_state=42)

# 训练
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 评估
print(f"准确率: {accuracy_score(y_test, y_pred):.4f}")
print(f"\n分类报告:\n{classification_report(y_test, y_pred)}")

# 练习9.2：决策树
print("\n=== 练习9.2：决策树 ===")

# 创建模型
dt = DecisionTreeClassifier(max_depth=3, random_state=42)

# 训练
dt.fit(X_train, y_train)

# 预测
y_pred_dt = dt.predict(X_test)

# 评估
print(f"准确率: {accuracy_score(y_test, y_pred_dt):.4f}")

# 练习9.3：随机森林
print("\n=== 练习9.3：随机森林 ===")

# 创建模型
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# 训练
rf.fit(X_train, y_train)

# 预测
y_pred_rf = rf.predict(X_test)

# 评估
print(f"准确率: {accuracy_score(y_test, y_pred_rf):.4f}")
print(f"特征重要性: {rf.feature_importances_}")

# 练习9.4：SVM
print("\n=== 练习9.4：SVM ===")

# 创建模型
svm = SVC(kernel='rbf', C=1.0, random_state=42)

# 训练
svm.fit(X_train, y_train)

# 预测
y_pred_svm = svm.predict(X_test)

# 评估
print(f"准确率: {accuracy_score(y_test, y_pred_svm):.4f}")

# 练习9.5：KNN
print("\n=== 练习9.5：KNN ===")

# 创建模型
knn = KNeighborsClassifier(n_neighbors=5)

# 训练
knn.fit(X_train, y_train)

# 预测
y_pred_knn = knn.predict(X_test)

# 评估
print(f"准确率: {accuracy_score(y_test, y_pred_knn):.4f}")

# 练习9.6：模型比较
print("\n=== 练习9.6：模型比较 ===")

models = {
    "逻辑回归": LogisticRegression(random_state=42),
    "决策树": DecisionTreeClassifier(max_depth=3, random_state=42),
    "随机森林": RandomForestClassifier(n_estimators=100, random_state=42),
    "SVM": SVC(kernel='rbf', C=1.0, random_state=42),
    "KNN": KNeighborsClassifier(n_neighbors=5)
}

for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    print(f"{name}: {scores.mean():.4f} (+/- {scores.std() * 2:.4f})")

# 练习9.7：网格搜索
print("\n=== 练习9.7：网格搜索 ===")

# 定义参数网格
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10]
}

# 网格搜索
grid_search = GridSearchCV(RandomForestClassifier(random_state=42), 
                           param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

print(f"最佳参数: {grid_search.best_params_}")
print(f"最佳分数: {grid_search.best_score_:.4f}")

# 使用最佳模型
best_model = grid_search.best_estimator_
y_pred_best = best_model.predict(X_test)
print(f"测试集准确率: {accuracy_score(y_test, y_pred_best):.4f}")

"""
思考题：
1. 分类和回归的区别？
2. 混淆矩阵的四个值分别代表什么？
3. 精确率和召回率的区别？
4. 什么是过拟合？如何解决？
5. 如何选择合适的分类算法？
"""
