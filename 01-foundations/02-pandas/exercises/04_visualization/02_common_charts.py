# -*- coding: utf-8 -*-
"""
练习2：常用图表类型
练习目标：掌握折线图、柱状图、散点图、饼图、直方图、箱线图的绘制
前置知识：Matplotlib 基础
"""

import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 练习2.1：折线图（趋势分析）
print("=== 练习2.1：折线图 ===")
months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
sales_2023 = [100, 120, 150, 130, 160, 180, 200, 190, 220, 250, 230, 280]
sales_2024 = [110, 130, 160, 140, 170, 190, 210, 200, 230, 260, 240, 300]

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(months, sales_2023, marker="o", linewidth=2, label="2023年")
ax.plot(months, sales_2024, marker="s", linewidth=2, label="2024年")
ax.set_title("月度销售趋势对比", fontsize=16)
ax.set_xlabel("月份", fontsize=12)
ax.set_ylabel("销售额（万元）", fontsize=12)
ax.legend(fontsize=12)
ax.grid(True, linestyle="--", alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("05_line_chart.png", dpi=150)
plt.close()
print("已保存：05_line_chart.png")

# 练习2.2：柱状图（对比分析）
print("\n=== 练习2.2：柱状图 ===")
categories = ["电子产品", "服装", "食品", "日用品", "其他"]
values = [4500, 3200, 2800, 1500, 800]
colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(categories, values, color=colors, edgecolor="white", linewidth=2)

# 在柱子上方显示数值
for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50,
            f"{value}", ha="center", fontsize=11, fontweight="bold")

ax.set_title("各品类销售额对比", fontsize=16)
ax.set_ylabel("销售额（万元）", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.7, axis="y")
plt.tight_layout()
plt.savefig("06_bar_chart.png", dpi=150)
plt.close()
print("已保存：06_bar_chart.png")

# 练习2.3：散点图（相关性分析）
print("\n=== 练习2.3：散点图 ===")
np.random.seed(42)
advertising = np.random.uniform(10, 100, 50)
sales = advertising * 2.5 + np.random.normal(0, 20, 50)

fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(advertising, sales, c=sales, cmap="viridis", 
                     alpha=0.7, edgecolors="white", s=100)

# 添加趋势线
z = np.polyfit(advertising, sales, 1)
p = np.poly1d(z)
x_line = np.linspace(min(advertising), max(advertising), 100)
ax.plot(x_line, p(x_line), "r--", linewidth=2, label="趋势线")

# 添加颜色条
cbar = plt.colorbar(scatter)
cbar.set_label("销售额", fontsize=12)

ax.set_title("广告投入与销售额的关系", fontsize=16)
ax.set_xlabel("广告投入（万元）", fontsize=12)
ax.set_ylabel("销售额（万元）", fontsize=12)
ax.legend(fontsize=12)
plt.tight_layout()
plt.savefig("07_scatter_chart.png", dpi=150)
plt.close()
print("已保存：07_scatter_chart.png")

# 练习2.4：饼图（占比分析）
print("\n=== 练习2.4：饼图 ===")
categories = ["电子产品", "服装", "食品", "日用品", "其他"]
values = [4500, 3200, 2800, 1500, 800]
colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"]
explode = (0.05, 0, 0, 0, 0)  # 突出显示第一块

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    values, labels=categories, colors=colors, explode=explode,
    autopct="%1.1f%%", startangle=90, pctdistance=0.85,
    textprops={"fontsize": 12}
)

# 美化文字
for text in autotexts:
    text.set_color("white")
    text.set_fontweight("bold")

ax.set_title("各品类销售占比", fontsize=16, pad=20)
plt.tight_layout()
plt.savefig("08_pie_chart.png", dpi=150)
plt.close()
print("已保存：08_pie_chart.png")

# 练习2.5：直方图（分布分析）
print("\n=== 练习2.5：直方图 ===")
np.random.seed(42)
scores = np.random.normal(75, 15, 200)  # 均值75，标准差15

fig, ax = plt.subplots(figsize=(10, 6))
n, bins, patches = ax.hist(scores, bins=20, color="steelblue", 
                           edgecolor="white", alpha=0.7)

# 添加均值线和标准差区域
mean_val = scores.mean()
std_val = scores.std()
ax.axvline(mean_val, color="red", linestyle="--", linewidth=2, label=f"均值: {mean_val:.1f}")
ax.axvspan(mean_val - std_val, mean_val + std_val, alpha=0.2, color="red", 
           label=f"标准差: {std_val:.1f}")

ax.set_title("考试成绩分布", fontsize=16)
ax.set_xlabel("分数", fontsize=12)
ax.set_ylabel("人数", fontsize=12)
ax.legend(fontsize=12)
ax.grid(True, linestyle="--", alpha=0.7, axis="y")
plt.tight_layout()
plt.savefig("09_histogram.png", dpi=150)
plt.close()
print("已保存：09_histogram.png")

# 练习2.6：箱线图（异常值检测）
print("\n=== 练习2.6：箱线图 ===")
np.random.seed(42)
data = {
    "华东": np.random.normal(200, 30, 100),
    "华南": np.random.normal(180, 40, 100),
    "华北": np.random.normal(220, 35, 100),
    "西部": np.random.normal(150, 50, 100)
}

fig, ax = plt.subplots(figsize=(10, 6))
bp = ax.boxplot(data.values(), labels=data.keys(), patch_artist=True,
                boxprops=dict(facecolor="lightblue", linewidth=2),
                medianprops=dict(color="red", linewidth=2),
                flierprops=dict(marker="o", markerfacecolor="red", markersize=8))

ax.set_title("各地区销售数据分布", fontsize=16)
ax.set_ylabel("销售额（万元）", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.7, axis="y")
plt.tight_layout()
plt.savefig("10_boxplot.png", dpi=150)
plt.close()
print("已保存：10_boxplot.png")

"""
思考题：
1. 折线图和柱状图分别适合什么场景？
2. 如何在柱状图上显示数值？
3. 散点图的颜色映射有什么作用？
4. 箱线图的五个数值（最小值、Q1、中位数、Q3、最大值）分别代表什么？
5. 饼图的 explode 参数有什么作用？
"""
