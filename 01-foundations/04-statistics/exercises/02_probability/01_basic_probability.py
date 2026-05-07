# -*- coding: utf-8 -*-
"""
练习6：概率基础
练习目标：掌握概率分布和计算
前置知识：Python 基础、NumPy
"""

import numpy as np
from scipy import stats

# 练习6.1：基本概率
print("=== 练习6.1：基本概率 ===")

# 掷骰子
sample_space = {1, 2, 3, 4, 5, 6}
event_even = {2, 4, 6}
event_odd = {1, 3, 5}

prob_even = len(event_even) / len(sample_space)
prob_odd = len(event_odd) / len(sample_space)

print(f"偶数概率: {prob_even}")
print(f"奇数概率: {prob_odd}")

# 练习6.2：条件概率
print("\n=== 练习6.2：条件概率 ===")

# 从一副牌中抽牌
total_cards = 52
red_cards = 26
hearts = 13

prob_heart = hearts / total_cards
prob_red = red_cards / total_cards
prob_heart_given_red = (hearts / total_cards) / (red_cards / total_cards)

print(f"抽到红心的概率: {prob_heart:.2f}")
print(f"抽到红色牌的概率: {prob_red:.2f}")
print(f"已知是红色牌，抽到红心的概率: {prob_heart_given_red:.2f}")

# 练习6.3：二项分布
print("\n=== 练习6.3：二项分布 ===")

n = 10  # 试验次数
p = 0.5  # 每次成功概率

# 概率质量函数 P(X = k)
k = 5
prob = stats.binom.pmf(k, n, p)
print(f"P(X = {k}) = {prob:.4f}")

# 累积分布函数 P(X <= k)
prob_cum = stats.binom.cdf(k, n, p)
print(f"P(X <= {k}) = {prob_cum:.4f}")

# 练习6.4：泊松分布
print("\n=== 练习6.4：泊松分布 ===")

lam = 3  # 平均每小时发生3次

k = 2
prob = stats.poisson.pmf(k, lam)
print(f"P(X = {k}) = {prob:.4f}")

prob_cum = stats.poisson.cdf(k, lam)
print(f"P(X <= {k}) = {prob_cum:.4f}")

# 练习6.5：正态分布
print("\n=== 练习6.5：正态分布 ===")

mu = 100  # 均值
sigma = 15  # 标准差

# 概率密度函数
x = 100
pdf = stats.norm.pdf(x, mu, sigma)
print(f"f({x}) = {pdf:.4f}")

# 累积分布函数
cdf = stats.norm.cdf(x, mu, sigma)
print(f"F({x}) = {cdf:.4f}")

# 68-95-99.7 法则
print(f"68% 数据在 [{mu-sigma}, {mu+sigma}]")
print(f"95% 数据在 [{mu-2*sigma}, {mu+2*sigma}]")
print(f"99.7% 数据在 [{mu-3*sigma}, {mu+3*sigma}]")

"""
思考题：
1. 条件概率和联合概率的区别？
2. 二项分布和泊松分布的区别？
3. 正态分布的 68-95-99.7 法则是什么？
4. 什么时候使用均匀分布？
5. 贝叶斯定理的公式是什么？
"""
