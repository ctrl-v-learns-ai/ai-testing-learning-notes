# -*- coding: utf-8 -*-
"""
客户细分项目 - 主程序
演示聚类分析的完整流程
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


def generate_customer_data(n_samples=300):
    """生成模拟客户数据"""
    np.random.seed(42)
    
    # 生成不同类型的客户
    # 高价值客户
    n1 = n_samples // 3
    income1 = np.random.normal(8000, 1000, n1)
    spending1 = np.random.normal(80, 10, n1)
    frequency1 = np.random.normal(15, 3, n1)
    
    # 中等价值客户
    n2 = n_samples // 3
    income2 = np.random.normal(5000, 800, n2)
    spending2 = np.random.normal(50, 15, n2)
    frequency2 = np.random.normal(8, 2, n2)
    
    # 低价值客户
    n3 = n_samples - n1 - n2
    income3 = np.random.normal(3000, 500, n3)
    spending3 = np.random.normal(30, 10, n3)
    frequency3 = np.random.normal(4, 1, n3)
    
    # 合并数据
    income = np.concatenate([income1, income2, income3])
    spending = np.concatenate([spending1, spending2, spending3])
    frequency = np.concatenate([frequency1, frequency2, frequency3])
    
    # 创建 DataFrame
    data = pd.DataFrame({
        '月收入': income,
        '月消费': spending,
        '消费频率': frequency
    })
    
    return data


def explore_data(data):
    """数据探索"""
    print("数据统计描述:")
    print(data.describe())
    
    print("\n数据相关性:")
    print(data.corr())


def find_optimal_k(data, max_k=10):
    """寻找最佳聚类数"""
    inertias = []
    silhouette_scores = []
    K_range = range(2, max_k + 1)
    
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        inertias.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(data, kmeans.labels_))
    
    return K_range, inertias, silhouette_scores


def plot_elbow_silhouette(K_range, inertias, silhouette_scores):
    """绘制肘部图和轮廓系数图"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # 肘部图
    axes[0].plot(K_range, inertias, marker='o', color='steelblue')
    axes[0].set_title('肘部法则', fontsize=14)
    axes[0].set_xlabel('K 值')
    axes[0].set_ylabel('惯性')
    axes[0].grid(True, linestyle='--', alpha=0.7)
    
    # 轮廓系数图
    axes[1].plot(K_range, silhouette_scores, marker='o', color='green')
    axes[1].set_title('轮廓系数', fontsize=14)
    axes[1].set_xlabel('K 值')
    axes[1].set_ylabel('轮廓系数')
    axes[1].grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('elbow_silhouette.png', dpi=150)
    plt.close()
    print("已保存: elbow_silhouette.png")


def perform_clustering(data, n_clusters):
    """执行聚类"""
    # K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans_labels = kmeans.fit_predict(data)
    
    # 层次聚类
    hierarchical = AgglomerativeClustering(n_clusters=n_clusters)
    hierarchical_labels = hierarchical.fit_predict(data)
    
    return kmeans_labels, hierarchical_labels


def evaluate_clustering(data, labels, method_name):
    """评估聚类"""
    silhouette = silhouette_score(data, labels)
    print(f"{method_name} 轮廓系数: {silhouette:.4f}")
    return silhouette


def analyze_clusters(data, labels):
    """分析聚类结果"""
    data_with_labels = data.copy()
    data_with_labels['聚类'] = labels
    
    # 每个聚类的统计
    cluster_stats = data_with_labels.groupby('聚类').agg(['mean', 'std', 'count'])
    
    print("\n聚类统计:")
    print(cluster_stats)
    
    return data_with_labels


def plot_clusters(data, labels, centers=None):
    """可视化聚类结果"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # 散点图：月收入 vs 月消费
    scatter = axes[0].scatter(data['月收入'], data['月消费'], c=labels, cmap='viridis', s=50, alpha=0.6)
    if centers is not None:
        axes[0].scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='聚类中心')
    axes[0].set_title('客户细分结果', fontsize=14)
    axes[0].set_xlabel('月收入')
    axes[0].set_ylabel('月消费')
    axes[0].legend()
    
    # 散点图：月收入 vs 消费频率
    scatter = axes[1].scatter(data['月收入'], data['消费频率'], c=labels, cmap='viridis', s=50, alpha=0.6)
    if centers is not None:
        axes[1].scatter(centers[:, 0], centers[:, 2], c='red', marker='X', s=200, label='聚类中心')
    axes[1].set_title('客户细分结果', fontsize=14)
    axes[1].set_xlabel('月收入')
    axes[1].set_ylabel('消费频率')
    axes[1].legend()
    
    plt.tight_layout()
    plt.savefig('customer_segments.png', dpi=150)
    plt.close()
    print("已保存: customer_segments.png")


def main():
    """主函数"""
    print("=" * 60)
    print("  客户细分项目")
    print("=" * 60)
    
    # 1. 生成数据
    print("\n[1] 生成数据...")
    data = generate_customer_data(300)
    print(f"数据形状: {data.shape}")
    print(f"\n数据预览:")
    print(data.head())
    
    # 2. 数据探索
    print("\n[2] 数据探索...")
    explore_data(data)
    
    # 3. 数据预处理
    print("\n[3] 数据预处理...")
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    print("标准化完成")
    
    # 4. 寻找最佳聚类数
    print("\n[4] 寻找最佳聚类数...")
    K_range, inertias, silhouette_scores = find_optimal_k(data_scaled)
    plot_elbow_silhouette(K_range, inertias, silhouette_scores)
    
    # 选择最佳 K
    best_k = K_range[np.argmax(silhouette_scores)]
    print(f"最佳聚类数: {best_k}")
    
    # 5. 执行聚类
    print("\n[5] 执行聚类...")
    kmeans_labels, hierarchical_labels = perform_clustering(data_scaled, best_k)
    
    # 6. 评估聚类
    print("\n[6] 评估聚类...")
    evaluate_clustering(data_scaled, kmeans_labels, "K-Means")
    evaluate_clustering(data_scaled, hierarchical_labels, "层次聚类")
    
    # 7. 分析聚类结果
    print("\n[7] 分析聚类结果...")
    data_with_labels = analyze_clusters(data, kmeans_labels)
    
    # 8. 可视化
    print("\n[8] 可视化结果...")
    kmeans = KMeans(n_clusters=best_k, random_state=42)
    kmeans.fit(data_scaled)
    plot_clusters(data, kmeans_labels, kmeans.cluster_centers_)
    
    # 9. 总结
    print("\n" + "=" * 60)
    print("  总结")
    print("=" * 60)
    print(f"\n最佳聚类数: {best_k}")
    print(f"每个聚类的客户数量:")
    for i in range(best_k):
        count = (kmeans_labels == i).sum()
        print(f"  聚类 {i}: {count} 个客户")


if __name__ == "__main__":
    main()
