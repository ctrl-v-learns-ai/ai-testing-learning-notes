# -*- coding: utf-8 -*-
"""
练习1：Matplotlib 基础
练习目标：掌握 Matplotlib 图形创建、子图布局、标题标签图例
前置知识：Python 基础
"""

import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 练习1.1：创建基本图形
print("=== 练习1.1：创建基本图形 ===")
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, marker="o", color="steelblue", linewidth=2)
ax.set_title("简单折线图", fontsize=16)
ax.set_xlabel("X 轴", fontsize=12)
ax.set_ylabel("Y 轴", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("01_basic_line.png", dpi=150)
plt.close()
print("已保存：01_basic_line.png")

# 练习1.2：子图布局
print("\n=== 练习1.2：子图布局 ===")
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 子图1：折线图
axes[0, 0].plot([1, 2, 3, 4], [1, 4, 9, 16], "r-o")
axes[0, 0].set_title("折线图")
axes[0, 0].set_xlabel("X")
axes[0, 0].set_ylabel("Y")

# 子图2：柱状图
axes[0, 1].bar(["A", "B", "C", "D"], [10, 20, 15, 25], color="steelblue")
axes[0, 1].set_title("柱状图")

# 子图3：散点图
np.random.seed(42)
axes[1, 0].scatter(np.random.rand(20), np.random.rand(20), color="red", alpha=0.6)
axes[1, 0].set_title("散点图")

# 子图4：饼图
axes[1, 1].pie([30, 25, 20, 25], labels=["A", "B", "C", "D"], autopct="%1.1f%%")
axes[1, 1].set_title("饼图")

plt.suptitle("2x2 子图布局示例", fontsize=16)
plt.tight_layout()
plt.savefig("02_subplots.png", dpi=150)
plt.close()
print("已保存：02_subplots.png")

# 练习1.3：标题、标签、图例
print("\n=== 练习1.3：标题、标签、图例 ===")
x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y1, label="sin(x)", color="blue", linewidth=2)
ax.plot(x, y2, label="cos(x)", color="red", linewidth=2, linestyle="--")
ax.set_title("三角函数图像", fontsize=16)
ax.set_xlabel("x（弧度）", fontsize=12)
ax.set_ylabel("y", fontsize=12)
ax.legend(loc="upper right", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.5)
ax.axhline(y=0, color="black", linewidth=0.5)
ax.axvline(x=0, color="black", linewidth=0.5)
plt.tight_layout()
plt.savefig("03_labels_legend.png", dpi=150)
plt.close()
print("已保存：03_labels_legend.png")

# 练习1.4：颜色、线型、标记
print("\n=== 练习1.4：颜色、线型、标记 ===")
x = np.arange(1, 11)

fig, ax = plt.subplots(figsize=(10, 6))

# 不同颜色、线型、标记组合
ax.plot(x, x * 1, color="red", linestyle="-", marker="o", label="红色-实线-圆点")
ax.plot(x, x * 2, color="blue", linestyle="--", marker="s", label="蓝色-虚线-方块")
ax.plot(x, x * 3, color="green", linestyle="-.", marker="^", label="绿色-点划-三角")
ax.plot(x, x * 4, color="purple", linestyle=":", marker="*", label="紫色-点线-星号")

ax.set_title("不同样式组合", fontsize=16)
ax.set_xlabel("X", fontsize=12)
ax.set_ylabel("Y", fontsize=12)
ax.legend(loc="upper left")
ax.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("04_styles.png", dpi=150)
plt.close()
print("已保存：04_styles.png")

"""
思考题：
1. plt.subplots() 返回什么？fig 和 ax 分别是什么？
2. tight_layout() 的作用是什么？
3. 如何在同一个图上绘制多条线？
4. 如何设置图例的位置？
"""
