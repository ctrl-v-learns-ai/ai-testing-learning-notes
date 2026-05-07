# -*- coding: utf-8 -*-
"""
练习7：假设检验
练习目标：掌握假设检验的基本方法
前置知识：概率基础、NumPy
"""

import numpy as np
from scipy import stats

# 练习7.1：单样本 t 检验
print("=== 练习7.1：单样本 t 检验 ===")

# 场景：检验某班级平均分是否等于 75 分
np.random.seed(42)
scores = np.random.normal(78, 10, 30)

t_stat, p_value = stats.ttest_1samp(scores, 75)

print(f"样本均值: {np.mean(scores):.2f}")
print(f"t 统计量: {t_stat:.4f}")
print(f"p 值: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"结论：拒绝零假设，班级平均分不等于75分")
else:
    print(f"结论：不拒绝零假设，没有足够证据说明班级平均分不等于75分")

# 练习7.2：双样本 t 检验
print("\n=== 练习7.2：双样本 t 检验 ===")

np.random.seed(42)
class_a = np.random.normal(78, 10, 30)
class_b = np.random.normal(82, 10, 30)

t_stat, p_value = stats.ttest_ind(class_a, class_b)

print(f"班级A均值: {np.mean(class_a):.2f}")
print(f"班级B均值: {np.mean(class_b):.2f}")
print(f"t 统计量: {t_stat:.4f}")
print(f"p 值: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"结论：拒绝零假设，两个班级平均分有显著差异")
else:
    print(f"结论：不拒绝零假设，没有足够证据说明两个班级平均分有差异")

# 练习7.3：配对样本 t 检验
print("\n=== 练习7.3：配对样本 t 检验 ===")

np.random.seed(42)
before = np.random.normal(70, 10, 30)
after = before + np.random.normal(5, 3, 30)

t_stat, p_value = stats.ttest_rel(before, after)

print(f"培训前均值: {np.mean(before):.2f}")
print(f"培训后均值: {np.mean(after):.2f}")
print(f"差值均值: {np.mean(after - before):.2f}")
print(f"t 统计量: {t_stat:.4f}")
print(f"p 值: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"结论：拒绝零假设，培训后成绩有显著提高")
else:
    print(f"结论：不拒绝零假设，没有足够证据说明培训后成绩有提高")

# 练习7.4：卡方检验
print("\n=== 练习7.4：卡方检验 ===")

observed = np.array([10, 12, 8, 15, 11, 14])
expected = np.array([sum(observed)/6] * 6)

chi2, p_value = stats.chisquare(observed, expected)

print(f"观察频数: {observed}")
print(f"期望频数: {expected}")
print(f"卡方统计量: {chi2:.4f}")
print(f"p 值: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"结论：拒绝零假设，骰子不公平")
else:
    print(f"结论：不拒绝零假设，没有足够证据说明骰子不公平")

# 练习7.5：相关性检验
print("\n=== 练习7.5：相关性检验 ===")

np.random.seed(42)
advertising = np.random.uniform(10, 100, 50)
sales = advertising * 2.5 + np.random.normal(0, 20, 50)

corr, p_value = stats.pearsonr(advertising, sales)

print(f"皮尔逊相关系数: {corr:.4f}")
print(f"p 值: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"结论：拒绝零假设，广告投入和销售额有显著相关性")
else:
    print(f"结论：不拒绝零假设，没有足够证据说明广告投入和销售额有相关性")

"""
思考题：
1. 零假设和备择假设的区别？
2. p 值的含义是什么？
3. 统计显著和实际显著的区别？
4. 什么时候用配对 t 检验？
5. 多重比较问题是什么？如何解决？
"""
