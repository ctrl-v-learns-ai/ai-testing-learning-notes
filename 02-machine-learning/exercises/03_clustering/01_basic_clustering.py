# -*- coding: utf-8 -*-
"""
练习10：聚类算法
练习目标：掌握常用聚类算法的使用
前置知识：NumPy、Pandas
"""

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, calinski_harabasz_score
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 练习10.1：K-Means 聚类
print("=== 练习10.1：K-Means 聚类 ===")

# 生成数据
X, y = make_blobs(n_samples=300, centers=4, random_state=42)

# 创建模型
kmeans = KMeans(n_clusters=4, random_state=42)

# 训练
kmeans.fit(X)

# 预测
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# 评估
silhouette = silhouette_score(X, labels)
print(f"轮廓系数: {silhouette:.4f}")
print(f"惯性: {kmeans.inertia_:.4f}")

# 练习10.2：选择 K 值
print("\n=== 练习10.2：选择 K 值 ===")

# 计算不同 K 值的惯性
inertias = []
K_range = range(1, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

print("K 值 vs 惯性:")
for k, inertia in zip(K_range, inertias):
    print(f"  K={k}: {inertia:.4f}")

# 练习10.3：层次聚类
print("\n=== 练习10.3：层次聚类 ===")

# 创建模型
hierarchical = AgglomerativeClustering(n_clusters=4)

# 训练
labels_hierarchical = hierarchical.fit_predict(X)

# 评估
silhouette_hierarchical = silhouette_score(X, labels_hierarchical)
print(f"轮廓系数: {silhouette_hierarchical:.4f}")

# 练习10.4：DBSCAN
print("\n=== 练习10.4：DBSCAN ===")

# 创建模型
dbscan = DBSCAN(eps=0.5, min_samples=5)

# 训练
labels_dbscan = dbscan.fit_predict(X)

# 统计
n_clusters = len(set(labels_dbscan)) - (1 if -1 in labels_dbscan else 0)
n_noise = list(labels_dbscan).count(-1)

print(f"聚类数量: {n_clusters}")
print(f"噪声点数量: {n_noise}")

if n_clusters > 1:
    silhouette_dbscan = silhouette_score(X, labels_dbscan)
    print(f"轮廓系数: {silhouette_dbscan:.4f}")

# 练习10.5：特征缩放
print("\n=== 练习10.5：特征缩放 ===")

# 特征缩放
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 对比缩放前后的效果
kmeans_original = KMeans(n_clusters=4, random_state=42)
kmeans_scaled = KMeans(n_clusters=4, random_state=42)

labels_original = kmeans_original.fit_predict(X)
labels_scaled = kmeans_scaled.fit_predict(X_scaled)

print(f"原始数据轮廓系数: {silhouette_score(X, labels_original):.4f}")
print(f"缩放后轮廓系数: {silhouette_score(X_scaled, labels_scaled):.4f}")

# 练习10.6：模型比较
print("\n=== 练习10.6：模型比较 ===")

models = {
    "K-Means": KMeans(n_clusters=4, random_state=42),
    "层次聚类": AgglomerativeClustering(n_clusters=4),
    "DBSCAN": DBSCAN(eps=0.5, min_samples=5)
}

for name, model in models.items():
    labels = model.fit_predict(X)
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    
    if n_clusters > 1:
        silhouette = silhouette_score(X, labels)
        print(f"{name}: 聚类数={n_clusters}, 轮廓系数={silhouette:.4f}")
    else:
        print(f"{name}: 聚类数={n_clusters}")

"""
思考题：
1. 监督学习和无监督学习的区别？
2. K-Means 的原理是什么？
3. 如何选择 K 值？
4. DBSCAN 和 K-Means 的区别？
5. 聚类评估指标有哪些？
"""
