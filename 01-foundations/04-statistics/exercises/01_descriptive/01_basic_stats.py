# -*- coding: utf-8 -*-
"""
练习5：描述性统计
练习目标：掌握描述性统计量的计算
前置知识：Python 基础、NumPy
"""

import numpy as np
from scipy import stats

# 练习5.1：集中趋势
print("=== 练习5.1：集中趋势 ===")

data = [85, 90, 78, 92, 88, 76, 95, 89, 82, 91]

# 平均数
mean = np.mean(data)
print(f"平均数: {mean:.2f}")

# 中位数
median = np.median(data)
print(f"中位数: {median:.2f}")

# 众数
mode = stats.mode(data)
print(f"众数: {mode.mode[0]}")

# 练习5.2：离散趋势
print("\n=== 练习5.2：离散趋势 ===")

# 极差
range_val = np.ptp(data)
print(f"极差: {range_val}")

# 方差（总体）
variance = np.var(data)
print(f"总体方差: {variance:.2f}")

# 方差（样本）
sample_var = np.var(data, ddof=1)
print(f"样本方差: {sample_var:.2f}")

# 标准差
std = np.std(data)
print(f"标准差: {std:.2f}")

# 变异系数
cv = np.std(data) / np.mean(data)
print(f"变异系数: {cv:.2%}")

# 练习5.3：分位数
print("\n=== 练习5.3：分位数 ===")

q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)
iqr = q3 - q1

print(f"Q1: {q1:.2f}")
print(f"Q2: {q2:.2f}")
print(f"Q3: {q3:.2f}")
print(f"IQR: {iqr:.2f}")

# 练习5.4：偏度和峰度
print("\n=== 练习5.4：偏度和峰度 ===")

# 右偏数据
data_right = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
skew_right = stats.skew(data_right)
print(f"右偏数据偏度: {skew_right:.2f}")

# 左偏数据
data_left = [100, 9, 8, 7, 6, 5, 4, 3, 2, 1]
skew_left = stats.skew(data_left)
print(f"左偏数据偏度: {skew_left:.2f}")

# 对称数据
data_sym = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
skew_sym = stats.skew(data_sym)
print(f"对称数据偏度: {skew_sym:.2f}")

# 练习5.5：综合统计
print("\n=== 练习5.5：综合统计 ===")

# 创建数据
data = {
    "数学": [85, 90, 78, 92, 88, 76, 95, 89, 82, 91],
    "英语": [78, 85, 82, 88, 90, 75, 92, 86, 80, 87],
    "物理": [92, 88, 85, 90, 82, 78, 96, 84, 88, 93]
}

import pandas as pd
df = pd.DataFrame(data)

print("基本统计量：")
print(df.describe())

print("\n相关系数矩阵：")
print(df.corr())

"""
思考题：
1. 平均数、中位数、众数的区别和适用场景？
2. 总体方差和样本方差的区别？
3. 标准差的作用是什么？
4. 偏度和峰度分别表示什么？
5. 什么时候用中位数比平均数更合适？
"""
