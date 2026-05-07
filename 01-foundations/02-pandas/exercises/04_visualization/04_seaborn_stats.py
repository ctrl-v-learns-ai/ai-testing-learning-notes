# -*- coding: utf-8 -*-
"""
练习4：Seaborn 统计图表
练习目标：掌握 Seaborn 分类图、关系图、热力图的绘制
前置知识：Pandas 基础、Matplotlib 基础
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 设置 Seaborn 样式
sns.set_theme(style="whitegrid")

# 练习4.1：分类图 - 柱状图（带误差线）
print("=== 练习4.1：分类图 - 柱状图 ===")
np.random.seed(42)
df = pd.DataFrame({
    "地区": np.repeat(["华东", "华南", "华北", "西部"], 50),
    "销售额": np.concatenate([
        np.random.normal(200, 30, 50),
        np.random.normal(180, 40, 50),
        np.random.normal(220, 35, 50),
        np.random.normal(150, 50, 50)
    ])
})

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df, x="地区", y="销售额", ax=ax, palette="Set2", ci=95)
ax.set_title("各地区平均销售额（95%置信区间）", fontsize=16)
ax.set_ylabel("销售额（万元）", fontsize=12)
ax.set_xlabel("地区", fontsize=12)
plt.tight_layout()
plt.savefig("19_seaborn_bar.png", dpi=150)
plt.close()
print("已保存：19_seaborn_bar.png")

# 练习4.2：分类图 - 计数图
print("\n=== 练习4.2：分类图 - 计数图 ===")
df = pd.DataFrame({
    "产品类别": np.random.choice(["电子产品", "服装", "食品", "日用品"], 200),
    "地区": np.random.choice(["华东", "华南", "华北", "西部"], 200)
})

fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=df, x="产品类别", hue="地区", ax=ax, palette="Set2")
ax.set_title("各地区产品类别分布", fontsize=16)
ax.set_xlabel("产品类别", fontsize=12)
ax.set_ylabel("数量", fontsize=12)
ax.legend(title="地区")
plt.tight_layout()
plt.savefig("20_seaborn_count.png", dpi=150)
plt.close()
print("已保存：20_seaborn_count.png")

# 练习4.3：分类图 - 箱线图
print("\n=== 练习4.3：分类图 - 箱线图 ===")
np.random.seed(42)
df = pd.DataFrame({
    "部门": np.repeat(["技术", "市场", "销售", "人事"], 50),
    "薪资": np.concatenate([
        np.random.normal(15000, 3000, 50),
        np.random.normal(12000, 2500, 50),
        np.random.normal(10000, 2000, 50),
        np.random.normal(8000, 1500, 50)
    ])
})

fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x="部门", y="薪资", ax=ax, palette="Set3")
ax.set_title("各部门薪资分布", fontsize=16)
ax.set_ylabel("薪资（元）", fontsize=12)
ax.set_xlabel("部门", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.7, axis="y")
plt.tight_layout()
plt.savefig("21_seaborn_box.png", dpi=150)
plt.close()
print("已保存：21_seaborn_box.png")

# 练习4.4：分类图 - 小提琴图
print("\n=== 练习4.4：分类图 - 小提琴图 ===")
fig, ax = plt.subplots(figsize=(10, 6))
sns.violinplot(data=df, x="部门", y="薪资", ax=ax, palette="Set3", inner="box")
ax.set_title("各部门薪资分布（小提琴图）", fontsize=16)
ax.set_ylabel("薪资（元）", fontsize=12)
ax.set_xlabel("部门", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.7, axis="y")
plt.tight_layout()
plt.savefig("22_seaborn_violin.png", dpi=150)
plt.close()
print("已保存：22_seaborn_violin.png")

# 练习4.5：关系图 - 散点图（带分类颜色）
print("\n=== 练习4.5：关系图 - 散点图 ===")
np.random.seed(42)
df = pd.DataFrame({
    "广告投入": np.random.uniform(10, 100, 100),
    "销售额": np.random.uniform(50, 300, 100),
    "地区": np.random.choice(["华东", "华南", "华北"], 100)
})

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x="广告投入", y="销售额", hue="地区", 
                style="地区", s=100, ax=ax, palette="Set2")
ax.set_title("广告投入与销售额的关系", fontsize=16)
ax.set_xlabel("广告投入（万元）", fontsize=12)
ax.set_ylabel("销售额（万元）", fontsize=12)
ax.legend(title="地区")
plt.tight_layout()
plt.savefig("23_seaborn_scatter.png", dpi=150)
plt.close()
print("已保存：23_seaborn_scatter.png")

# 练习4.6：关系图 - 线图（带置信区间）
print("\n=== 练习4.6：关系图 - 线图 ===")
np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=12, freq="M")
df = pd.DataFrame({
    "日期": np.tile(dates, 3),
    "销售额": np.concatenate([
        np.random.normal(200, 20, 12) + np.linspace(0, 50, 12),
        np.random.normal(180, 25, 12) + np.linspace(0, 40, 12),
        np.random.normal(150, 30, 12) + np.linspace(0, 30, 12)
    ]),
    "地区": np.repeat(["华东", "华南", "华北"], 12)
})

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=df, x="日期", y="销售额", hue="地区", 
             style="地区", markers=True, dashes=False, ax=ax)
ax.set_title("各地区月度销售趋势", fontsize=16)
ax.set_xlabel("日期", fontsize=12)
ax.set_ylabel("销售额（万元）", fontsize=12)
ax.legend(title="地区")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("24_seaborn_line.png", dpi=150)
plt.close()
print("已保存：24_seaborn_line.png")

# 练习4.7：分布图 - 直方图（带核密度估计）
print("\n=== 练习4.7：分布图 - 直方图 ===")
np.random.seed(42)
df = pd.DataFrame({
    "成绩": np.random.normal(75, 15, 200)
})

fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data=df, x="成绩", bins=20, kde=True, ax=ax, color="steelblue")
ax.set_title("考试成绩分布", fontsize=16)
ax.set_xlabel("分数", fontsize=12)
ax.set_ylabel("频数", fontsize=12)
ax.axvline(df["成绩"].mean(), color="red", linestyle="--", linewidth=2, 
           label=f"均值: {df['成绩'].mean():.1f}")
ax.legend()
plt.tight_layout()
plt.savefig("25_seaborn_hist.png", dpi=150)
plt.close()
print("已保存：25_seaborn_hist.png")

# 练习4.8：分布图 - 核密度估计图
print("\n=== 练习4.8：分布图 - 核密度估计图 ===")
np.random.seed(42)
df = pd.DataFrame({
    "华东": np.random.normal(200, 30, 100),
    "华南": np.random.normal(180, 40, 100),
    "华北": np.random.normal(220, 35, 100)
})

fig, ax = plt.subplots(figsize=(10, 6))
sns.kdeplot(data=df, ax=ax, fill=True, alpha=0.3)
ax.set_title("各地区销售数据分布（核密度估计）", fontsize=16)
ax.set_xlabel("销售额（万元）", fontsize=12)
ax.set_ylabel("密度", fontsize=12)
plt.tight_layout()
plt.savefig("26_seaborn_kde.png", dpi=150)
plt.close()
print("已保存：26_seaborn_kde.png")

# 练习4.9：热力图
print("\n=== 练习4.9：热力图 ===")
np.random.seed(42)
df = pd.DataFrame({
    "销售额": np.random.uniform(100, 300, 50),
    "成本": np.random.uniform(50, 150, 50),
    "利润": np.random.uniform(20, 80, 50),
    "广告投入": np.random.uniform(10, 50, 50),
    "客户数": np.random.randint(100, 1000, 50)
})

corr_matrix = df.corr()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", center=0,
            square=True, linewidths=1, fmt=".2f", ax=ax)
ax.set_title("变量相关性热力图", fontsize=16)
plt.tight_layout()
plt.savefig("27_seaborn_heatmap.png", dpi=150)
plt.close()
print("已保存：27_seaborn_heatmap.png")

# 练习4.10：成对关系图
print("\n=== 练习4.10：成对关系图 ===")
np.random.seed(42)
df = pd.DataFrame({
    "销售额": np.random.uniform(100, 300, 50),
    "成本": np.random.uniform(50, 150, 50),
    "利润": np.random.uniform(20, 80, 50),
    "地区": np.random.choice(["华东", "华南", "华北"], 50)
})

# 使用 pairplot（会自动保存）
g = sns.pairplot(df, hue="地区", palette="Set2", diag_kind="kde")
g.fig.suptitle("成对关系图", y=1.02, fontsize=16)
plt.savefig("28_seaborn_pairplot.png", dpi=150, bbox_inches="tight")
plt.close()
print("已保存：28_seaborn_pairplot.png")

"""
思考题：
1. Seaborn 的 barplot 和 Pandas 的 plot(kind="bar") 有什么区别？
2. 箱线图和小提琴图分别适合什么场景？
3. 热力图的 annot 参数有什么作用？
4. 如何在 Seaborn 中设置分类颜色（hue 参数）？
5. pairplot 的作用是什么？适合什么场景？
"""
