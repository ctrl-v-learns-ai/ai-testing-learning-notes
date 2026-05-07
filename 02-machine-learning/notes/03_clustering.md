# 机器学习三：聚类算法

## 什么是聚类？

聚类是无监督学习任务，将相似的数据点分组在一起。

类比理解：
- 分类 = 你告诉计算机"这是猫，这是狗"，计算机学习区分
- 聚类 = 你给计算机一堆照片，计算机自己把相似的分在一起

## K-Means 聚类

### 原理

K-Means 通过迭代找到 K 个聚类中心，将数据点分配到最近的聚类。

```python
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 生成数据
from sklearn.datasets import make_blobs
X, y = make_blobs(n_samples=300, centers=4, random_state=42)

# 创建模型
kmeans = KMeans(n_clusters=4, random_state=42)

# 训练
kmeans.fit(X)

# 预测
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# 可视化
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50, alpha=0.6)
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='聚类中心')
plt.title('K-Means 聚类结果')
plt.legend()
plt.savefig("kmeans_clustering.png", dpi=150)
plt.close()
```

### 选择 K 值（肘部法则）

```python
# 计算不同 K 值的惯性
inertias = []
K_range = range(1, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

# 绘制肘部图
plt.figure(figsize=(10, 6))
plt.plot(K_range, inertias, marker='o')
plt.xlabel('K 值')
plt.ylabel('惯性')
plt.title('肘部法则')
plt.savefig("elbow_method.png", dpi=150)
plt.close()
```

### 轮廓系数

```python
from sklearn.metrics import silhouette_score

# 计算轮廓系数
silhouette_avg = silhouette_score(X, labels)
print(f"轮廓系数: {silhouette_avg:.4f}")

# 轮廓系数范围 [-1, 1]
# 越接近 1 表示聚类效果越好
```

## 层次聚类

### 原理

层次聚类通过合并或分裂来构建聚类层次。

```python
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# 创建模型
hierarchical = AgglomerativeClustering(n_clusters=4)

# 训练
labels = hierarchical.fit_predict(X)

# 绘制树状图
plt.figure(figsize=(12, 8))
linkage_matrix = linkage(X, method='ward')
dendrogram(linkage_matrix)
plt.title('层次聚类树状图')
plt.savefig("dendrogram.png", dpi=150)
plt.close()
```

## DBSCAN

### 原理

DBSCAN 基于密度进行聚类，可以发现任意形状的聚类。

```python
from sklearn.cluster import DBSCAN

# 创建模型
dbscan = DBSCAN(eps=0.5, min_samples=5)

# 训练
labels = dbscan.fit_predict(X)

# 统计
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)

print(f"聚类数量: {n_clusters}")
print(f"噪声点数量: {n_noise}")
```

## 聚类评估

### 内部评估

```python
from sklearn.metrics import silhouette_score, calinski_harabasz_score

# 轮廓系数
silhouette = silhouette_score(X, labels)

# Calinski-Harabasz 指数
ch_score = calinski_harabasz_score(X, labels)

print(f"轮廓系数: {silhouette:.4f}")
print(f"Calinski-Harabasz: {ch_score:.4f}")
```

### 外部评估（有真实标签时）

```python
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score

# 调整兰德指数
ari = adjusted_rand_score(y_true, labels)

# 标准化互信息
nmi = normalized_mutual_info_score(y_true, labels)

print(f"调整兰德指数: {ari:.4f}")
print(f"标准化互信息: {nmi:.4f}")
```

## 特征缩放对聚类的影响

```python
from sklearn.preprocessing import StandardScaler

# 特征缩放很重要
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 对比缩放前后的效果
kmeans_original = KMeans(n_clusters=4, random_state=42)
kmeans_scaled = KMeans(n_clusters=4, random_state=42)

labels_original = kmeans_original.fit_predict(X)
labels_scaled = kmeans_scaled.fit_predict(X_scaled)

print(f"原始数据轮廓系数: {silhouette_score(X, labels_original):.4f}")
print(f"缩放后轮廓系数: {silhouette_score(X_scaled, labels_scaled):.4f}")
```

## 常见坑

### 坑1：K 值选择

```python
# 问题：K 值选择不当
# 解决方案：
# 1. 肘部法则
# 2. 轮廓系数
# 3. 业务需求
```

### 坑2：特征缩放

```python
# 问题：不同特征量级差异大
# 解决方案：标准化或归一化
```

### 坑3：算法选择

```python
# K-Means：球形聚类，需要指定 K
# 层次聚类：小数据集，需要树状图
# DBSCAN：任意形状，自动确定聚类数
```

## 速查表

| 算法 | 代码 | 适用场景 |
|------|------|----------|
| K-Means | `KMeans(n_clusters=K)` | 球形聚类 |
| 层次聚类 | `AgglomerativeClustering()` | 小数据集 |
| DBSCAN | `DBSCAN(eps, min_samples)` | 任意形状 |

## 小测验

1. 监督学习和无监督学习的区别？
2. K-Means 的原理是什么？
3. 如何选择 K 值？
4. DBSCAN 和 K-Means 的区别？
5. 聚类评估指标有哪些？
