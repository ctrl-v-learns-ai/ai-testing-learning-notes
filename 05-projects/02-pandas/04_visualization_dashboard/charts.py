# -*- coding: utf-8 -*-
"""
图表生成模块
生成各种类型的图表用于数据分析
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 设置 Seaborn 样式
sns.set_theme(style="whitegrid")


def plot_monthly_trend(monthly_df, save_path="01_monthly_trend.png"):
    """
    绘制月度销售趋势图
    
    参数:
        monthly_df: 月度汇总数据
        save_path: 保存路径
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(monthly_df["月份"], monthly_df["销售额"], marker="o", 
            linewidth=2, label="销售额", color="steelblue")
    ax.plot(monthly_df["月份"], monthly_df["成本"], marker="s", 
            linewidth=2, label="成本", color="orange")
    ax.plot(monthly_df["月份"], monthly_df["利润"], marker="^", 
            linewidth=2, label="利润", color="green")
    
    ax.set_title("月度销售趋势分析", fontsize=16)
    ax.set_xlabel("月份", fontsize=12)
    ax.set_ylabel("金额（万元）", fontsize=12)
    ax.legend(fontsize=12)
    ax.grid(True, linestyle="--", alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"已保存：{save_path}")


def plot_region_comparison(region_df, save_path="02_region_comparison.png"):
    """
    绘制地区销售对比图
    
    参数:
        region_df: 地区汇总数据
        save_path: 保存路径
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # 柱状图
    colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4"]
    bars = axes[0].bar(region_df["地区"], region_df["销售额"], color=colors)
    axes[0].set_title("各地区销售额对比", fontsize=14)
    axes[0].set_ylabel("销售额（万元）", fontsize=12)
    axes[0].grid(True, linestyle="--", alpha=0.7, axis="y")
    
    # 在柱子上方显示数值
    for bar, value in zip(bars, region_df["销售额"]):
        axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100,
                     f"{value:,.0f}", ha="center", fontsize=10)
    
    # 饼图
    axes[1].pie(region_df["销售额"], labels=region_df["地区"], colors=colors,
                autopct="%1.1f%%", startangle=90, textprops={"fontsize": 12})
    axes[1].set_title("各地区销售占比", fontsize=14)
    
    plt.suptitle("地区销售分析", fontsize=16, y=1.02)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"已保存：{save_path}")


def plot_product_pie(product_df, save_path="03_product_pie.png"):
    """
    绘制产品销售占比图
    
    参数:
        product_df: 产品汇总数据
        save_path: 保存路径
    """
    colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"]
    
    fig, ax = plt.subplots(figsize=(10, 8))
    wedges, texts, autotexts = ax.pie(
        product_df["销售额"], labels=product_df["产品类别"], colors=colors,
        autopct="%1.1f%%", startangle=90, pctdistance=0.85,
        textprops={"fontsize": 12}
    )
    
    # 美化文字
    for text in autotexts:
        text.set_color("white")
        text.set_fontweight("bold")
    
    ax.set_title("各产品类别销售占比", fontsize=16, pad=20)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"已保存：{save_path}")


def plot_price_distribution(df, save_path="04_price_distribution.png"):
    """
    绘制价格分布图
    
    参数:
        df: 原始销售数据
        save_path: 保存路径
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # 直方图
    axes[0].hist(df["销售额"], bins=30, color="steelblue", edgecolor="white", alpha=0.7)
    axes[0].axvline(df["销售额"].mean(), color="red", linestyle="--", linewidth=2,
                    label=f"均值: {df['销售额'].mean():.2f}")
    axes[0].set_title("销售额分布", fontsize=14)
    axes[0].set_xlabel("销售额（万元）", fontsize=12)
    axes[0].set_ylabel("频数", fontsize=12)
    axes[0].legend(fontsize=12)
    axes[0].grid(True, linestyle="--", alpha=0.7, axis="y")
    
    # 箱线图（按地区）
    df.boxplot(column="销售额", by="地区", ax=axes[1])
    axes[1].set_title("各地区销售额分布", fontsize=14)
    axes[1].set_xlabel("地区", fontsize=12)
    axes[1].set_ylabel("销售额（万元）", fontsize=12)
    axes[1].grid(True, linestyle="--", alpha=0.7, axis="y")
    
    plt.suptitle("价格分布分析", fontsize=16, y=1.02)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"已保存：{save_path}")


def plot_correlation_scatter(df, save_path="05_correlation_scatter.png"):
    """
    绘制相关性散点图
    
    参数:
        df: 原始销售数据
        save_path: 保存路径
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # 销售额 vs 成本
    axes[0].scatter(df["销售额"], df["成本"], alpha=0.5, color="steelblue", edgecolors="white")
    z = np.polyfit(df["销售额"], df["成本"], 1)
    p = np.poly1d(z)
    x_line = np.linspace(df["销售额"].min(), df["销售额"].max(), 100)
    axes[0].plot(x_line, p(x_line), "r--", linewidth=2, label="趋势线")
    axes[0].set_title("销售额 vs 成本", fontsize=14)
    axes[0].set_xlabel("销售额（万元）", fontsize=12)
    axes[0].set_ylabel("成本（万元）", fontsize=12)
    axes[0].legend(fontsize=12)
    axes[0].grid(True, linestyle="--", alpha=0.7)
    
    # 销售额 vs 利润
    axes[1].scatter(df["销售额"], df["利润"], alpha=0.5, color="green", edgecolors="white")
    z = np.polyfit(df["销售额"], df["利润"], 1)
    p = np.poly1d(z)
    x_line = np.linspace(df["销售额"].min(), df["销售额"].max(), 100)
    axes[1].plot(x_line, p(x_line), "r--", linewidth=2, label="趋势线")
    axes[1].set_title("销售额 vs 利润", fontsize=14)
    axes[1].set_xlabel("销售额（万元）", fontsize=12)
    axes[1].set_ylabel("利润（万元）", fontsize=12)
    axes[1].legend(fontsize=12)
    axes[1].grid(True, linestyle="--", alpha=0.7)
    
    plt.suptitle("相关性分析", fontsize=16, y=1.02)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"已保存：{save_path}")


def plot_correlation_heatmap(df, save_path="06_correlation_heatmap.png"):
    """
    绘制相关性热力图
    
    参数:
        df: 原始销售数据
        save_path: 保存路径
    """
    # 选择数值列
    numeric_cols = ["销售额", "成本", "利润", "数量", "客户数"]
    corr_matrix = df[numeric_cols].corr()
    
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", center=0,
                square=True, linewidths=1, fmt=".2f", ax=ax)
    ax.set_title("变量相关性热力图", fontsize=16)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"已保存：{save_path}")


def create_dashboard(df, monthly_df, region_df, product_df, save_path="07_dashboard.png"):
    """
    创建综合仪表板
    
    参数:
        df: 原始销售数据
        monthly_df: 月度汇总数据
        region_df: 地区汇总数据
        product_df: 产品汇总数据
        save_path: 保存路径
    """
    fig = plt.figure(figsize=(16, 12))
    
    # 子图1：月度趋势
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(monthly_df["月份"], monthly_df["销售额"], marker="o", linewidth=2)
    ax1.set_title("月度销售趋势", fontsize=12)
    ax1.set_xlabel("月份")
    ax1.set_ylabel("销售额（万元）")
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(True, linestyle="--", alpha=0.7)
    
    # 子图2：地区对比
    ax2 = fig.add_subplot(2, 2, 2)
    colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4"]
    ax2.bar(region_df["地区"], region_df["销售额"], color=colors)
    ax2.set_title("地区销售对比", fontsize=12)
    ax2.set_ylabel("销售额（万元）")
    ax2.grid(True, linestyle="--", alpha=0.7, axis="y")
    
    # 子图3：产品占比
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.pie(product_df["销售额"], labels=product_df["产品类别"], colors=colors,
            autopct="%1.1f%%", startangle=90)
    ax3.set_title("产品销售占比", fontsize=12)
    
    # 子图4：价格分布
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.hist(df["销售额"], bins=20, color="steelblue", edgecolor="white", alpha=0.7)
    ax4.axvline(df["销售额"].mean(), color="red", linestyle="--", linewidth=2)
    ax4.set_title("销售额分布", fontsize=12)
    ax4.set_xlabel("销售额（万元）")
    ax4.set_ylabel("频数")
    ax4.grid(True, linestyle="--", alpha=0.7, axis="y")
    
    plt.suptitle("销售数据可视化仪表板", fontsize=18, y=1.02)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"已保存：{save_path}")
