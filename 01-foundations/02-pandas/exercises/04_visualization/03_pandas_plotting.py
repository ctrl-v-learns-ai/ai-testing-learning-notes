# -*- coding: utf-8 -*-
"""
练习3：Pandas 内置绘图
练习目标：掌握 Pandas 的 df.plot() 方法和分组绘图
前置知识：Pandas 基础、Matplotlib 基础
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 练习3.1：df.plot() 基础用法
print("=== 练习3.1：df.plot() 基础用法 ===")
df = pd.DataFrame({
    "月份": ["1月", "2月", "3月", "4月", "5月", "6月"],
    "销售额": [100, 120, 150, 130, 160, 180],
    "成本": [80, 90, 110, 100, 120, 140]
})

# 折线图
fig, ax = plt.subplots(figsize=(10, 6))
df.plot(x="月份", y=["销售额", "成本"], kind="line", marker="o", ax=ax)
ax.set_title("月度销售与成本趋势", fontsize=16)
ax.set_ylabel("金额（万元）", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("11_pandas_line.png", dpi=150)
plt.close()
print("已保存：11_pandas_line.png")

# 柱状图
fig, ax = plt.subplots(figsize=(10, 6))
df.plot(x="月份", y=["销售额", "成本"], kind="bar", ax=ax)
ax.set_title("月度销售与成本对比", fontsize=16)
ax.set_ylabel("金额（万元）", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.7, axis="y")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("12_pandas_bar.png", dpi=150)
plt.close()
print("已保存：12_pandas_bar.png")

# 练习3.2：分组绘图
print("\n=== 练习3.2：分组绘图 ===")
df = pd.DataFrame({
    "地区": np.repeat(["华东", "华南", "华北", "西部"], 4),
    "季度": np.tile(["Q1", "Q2", "Q3", "Q4"], 4),
    "销售额": [200, 220, 250, 230, 180, 190, 210, 200, 250, 270, 300, 280, 150, 160, 180, 170]
})

# 透视表
pivot_df = df.pivot(index="季度", columns="地区", values="销售额")
print("透视表：")
print(pivot_df)

# 分组柱状图
fig, ax = plt.subplots(figsize=(12, 6))
pivot_df.plot(kind="bar", ax=ax)
ax.set_title("各地区季度销售对比", fontsize=16)
ax.set_ylabel("销售额（万元）", fontsize=12)
ax.set_xlabel("季度", fontsize=12)
ax.legend(title="地区", fontsize=10)
ax.grid(True, linestyle="--", alpha=0.7, axis="y")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("13_grouped_bar.png", dpi=150)
plt.close()
print("已保存：13_grouped_bar.png")

# 练习3.3：散点图和相关性
print("\n=== 练习3.3：散点图和相关性 ===")
np.random.seed(42)
df = pd.DataFrame({
    "广告投入": np.random.uniform(10, 100, 50),
    "销售额": np.random.uniform(50, 300, 50),
    "客户数": np.random.randint(100, 1000, 50)
})

# 散点图
fig, ax = plt.subplots(figsize=(10, 6))
df.plot(kind="scatter", x="广告投入", y="销售额", c="客户数", 
        colormap="viridis", alpha=0.7, ax=ax)
ax.set_title("广告投入与销售额的关系", fontsize=16)
plt.tight_layout()
plt.savefig("14_pandas_scatter.png", dpi=150)
plt.close()
print("已保存：14_pandas_scatter.png")

# 练习3.4：饼图
print("\n=== 练习3.4：饼图 ===")
df = pd.DataFrame({
    "品类": ["电子产品", "服装", "食品", "日用品", "其他"],
    "销售额": [4500, 3200, 2800, 1500, 800]
})

fig, ax = plt.subplots(figsize=(10, 8))
df.set_index("品类")["销售额"].plot(kind="pie", autopct="%1.1f%%", 
                                 startangle=90, ax=ax, 
                                 colors=["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"])
ax.set_title("各品类销售占比", fontsize=16)
ax.set_ylabel("")  # 隐藏默认的ylabel
plt.tight_layout()
plt.savefig("15_pandas_pie.png", dpi=150)
plt.close()
print("已保存：15_pandas_pie.png")

# 练习3.5：直方图和箱线图
print("\n=== 练习3.5：直方图和箱线图 ===")
np.random.seed(42)
df = pd.DataFrame({
    "华东": np.random.normal(200, 30, 100),
    "华南": np.random.normal(180, 40, 100),
    "华北": np.random.normal(220, 35, 100),
    "西部": np.random.normal(150, 50, 100)
})

# 直方图
fig, ax = plt.subplots(figsize=(10, 6))
df.plot(kind="hist", alpha=0.5, bins=20, ax=ax)
ax.set_title("各地区销售数据分布", fontsize=16)
ax.set_xlabel("销售额（万元）", fontsize=12)
ax.set_ylabel("频数", fontsize=12)
ax.legend(title="地区")
plt.tight_layout()
plt.savefig("16_pandas_hist.png", dpi=150)
plt.close()
print("已保存：16_pandas_hist.png")

# 箱线图
fig, ax = plt.subplots(figsize=(10, 6))
df.plot(kind="box", ax=ax)
ax.set_title("各地区销售数据分布（箱线图）", fontsize=16)
ax.set_ylabel("销售额（万元）", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.7, axis="y")
plt.tight_layout()
plt.savefig("17_pandas_box.png", dpi=150)
plt.close()
print("已保存：17_pandas_box.png")

# 练习3.6：面积图
print("\n=== 练习3.6：面积图 ===")
df = pd.DataFrame({
    "月份": ["1月", "2月", "3月", "4月", "5月", "6月"],
    "线上": [50, 60, 75, 70, 85, 95],
    "线下": [80, 90, 100, 95, 110, 120]
})

fig, ax = plt.subplots(figsize=(10, 6))
df.set_index("月份").plot(kind="area", alpha=0.5, ax=ax)
ax.set_title("线上与线下销售趋势", fontsize=16)
ax.set_ylabel("销售额（万元）", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("18_pandas_area.png", dpi=150)
plt.close()
print("已保存：18_pandas_area.png")

"""
思考题：
1. df.plot() 和 ax.plot() 有什么区别？
2. 如何使用 Pandas 创建分组柱状图？
3. pivot() 函数在绘图中有什么作用？
4. Pandas 的 plot(kind="scatter") 和 Matplotlib 的 ax.scatter() 有什么区别？
5. 面积图适合展示什么类型的数据？
"""
