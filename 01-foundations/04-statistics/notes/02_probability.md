# 统计学基础二：概率基础

## 什么是概率？

概率是描述事件发生可能性的数值，范围在 0 到 1 之间。

类比理解：
- 概率 = 天气预报的降水概率（0% 不会下雨，100% 一定会下雨）

## 基本概率概念

### 样本空间和事件

```python
# 样本空间：所有可能结果的集合
# 事件：样本空间的子集

# 掷骰子
sample_space = {1, 2, 3, 4, 5, 6}
event_even = {2, 4, 6}  # 偶数事件
event_odd = {1, 3, 5}   # 奇数事件

# 计算概率
prob_even = len(event_even) / len(sample_space)
prob_odd = len(event_odd) / len(sample_space)

print(f"偶数概率: {prob_even}")  # 0.5
print(f"奇数概率: {prob_odd}")   # 0.5
```

### 概率的加法规则

```python
# P(A 或 B) = P(A) + P(B) - P(A 且 B)

# 掷骰子
sample_space = {1, 2, 3, 4, 5, 6}
event_even = {2, 4, 6}
event_less_4 = {1, 2, 3}
event_even_and_less_4 = {2}  # 既是偶数又小于4

prob_even = len(event_even) / len(sample_space)
prob_less_4 = len(event_less_4) / len(sample_space)
prob_even_and_less_4 = len(event_even_and_less_4) / len(sample_space)

prob_even_or_less_4 = prob_even + prob_less_4 - prob_even_and_less_4
print(f"偶数或小于4的概率: {prob_even_or_less_4}")  # 0.6667
```

### 条件概率

```python
# P(A|B) = P(A 且 B) / P(B)

# 从一副牌中抽牌
# 事件 A：抽到红心
# 事件 B：抽到红色牌
# P(A|B) = P(A 且 B) / P(B) = (13/52) / (26/52) = 0.5

total_cards = 52
red_cards = 26
hearts = 13

prob_heart = hearts / total_cards
prob_red = red_cards / total_cards
prob_heart_given_red = (hearts / total_cards) / (red_cards / total_cards)

print(f"抽到红心的概率: {prob_heart}")           # 0.25
print(f"抽到红色牌的概率: {prob_red}")            # 0.5
print(f"已知是红色牌，抽到红心的概率: {prob_heart_given_red}")  # 0.5
```

## 常见概率分布

### 离散分布

#### 伯努利分布

```python
import numpy as np
from scipy import stats

# 伯努利分布：只有两种结果（成功/失败）
# 参数 p：成功的概率

# 生成伯努利分布数据
p = 0.6  # 成功概率
data = np.random.binomial(1, p, 1000)

# 统计
print(f"成功次数: {sum(data)}")
print(f"成功比例: {sum(data)/len(data):.3f}")
print(f"理论概率: {p}")
```

#### 二项分布

```python
import numpy as np
from scipy import stats

# 二项分布：n 次独立伯努利试验中成功的次数
# 参数 n：试验次数，p：每次成功的概率

n = 10  # 试验次数
p = 0.5  # 每次成功概率

# 概率质量函数 P(X = k)
k = 5  # 成功5次
prob = stats.binom.pmf(k, n, p)
print(f"P(X = {k}) = {prob:.4f}")

# 累积分布函数 P(X <= k)
prob_cum = stats.binom.cdf(k, n, p)
print(f"P(X <= {k}) = {prob_cum:.4f}")

# 生成随机数
data = np.random.binomial(n, p, 1000)
print(f"均值: {np.mean(data):.2f} (理论: {n*p})")
print(f"方差: {np.var(data):.2f} (理论: {n*p*(1-p)})")
```

#### 泊松分布

```python
import numpy as np
from scipy import stats

# 泊松分布：单位时间内事件发生的次数
# 参数 λ：平均发生次数

lam = 3  # 平均每小时发生3次

# 概率质量函数 P(X = k)
k = 2  # 发生2次
prob = stats.poisson.pmf(k, lam)
print(f"P(X = {k}) = {prob:.4f}")

# 累积分布函数 P(X <= k)
prob_cum = stats.poisson.cdf(k, lam)
print(f"P(X <= {k}) = {prob_cum:.4f}")

# 生成随机数
data = np.random.poisson(lam, 1000)
print(f"均值: {np.mean(data):.2f} (理论: {lam})")
print(f"方差: {np.var(data):.2f} (理论: {lam})")
```

### 连续分布

#### 均匀分布

```python
import numpy as np
from scipy import stats

# 均匀分布：在区间 [a, b] 内等可能取值
a, b = 0, 10

# 概率密度函数
x = 5
pdf = stats.uniform.pdf(x, a, b-a)
print(f"f({x}) = {pdf:.4f}")

# 累积分布函数
cdf = stats.uniform.cdf(x, a, b-a)
print(f"F({x}) = {cdf:.4f}")

# 生成随机数
data = np.random.uniform(a, b, 1000)
print(f"均值: {np.mean(data):.2f} (理论: {(a+b)/2})")
print(f"方差: {np.var(data):.2f} (理论: {(b-a)**2/12})")
```

#### 正态分布

```python
import numpy as np
from scipy import stats

# 正态分布：最重要的连续分布
# 参数 μ：均值，σ：标准差

mu = 100  # 均值
sigma = 15  # 标准差

# 概率密度函数
x = 100
pdf = stats.norm.pdf(x, mu, sigma)
print(f"f({x}) = {pdf:.4f}")

# 累积分布函数
cdf = stats.norm.cdf(x, mu, sigma)
print(f"F({x}) = {cdf:.4f}")

# 生成随机数
data = np.random.normal(mu, sigma, 1000)
print(f"均值: {np.mean(data):.2f} (理论: {mu})")
print(f"标准差: {np.std(data):.2f} (理论: {sigma})")

# 68-95-99.7 法则
print(f"68% 数据在 [{mu-sigma}, {mu+sigma}]")
print(f"95% 数据在 [{mu-2*sigma}, {mu+2*sigma}]")
print(f"99.7% 数据在 [{mu-3*sigma}, {mu+3*sigma}]")
```

## 概率可视化

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 二项分布
n, p = 10, 0.5
x = np.arange(0, n+1)
pmf = stats.binom.pmf(x, n, p)
axes[0, 0].bar(x, pmf, color="steelblue")
axes[0, 0].set_title(f"二项分布 (n={n}, p={p})")
axes[0, 0].set_xlabel("k")
axes[0, 0].set_ylabel("P(X=k)")

# 泊松分布
lam = 3
x = np.arange(0, 15)
pmf = stats.poisson.pmf(x, lam)
axes[0, 1].bar(x, pmf, color="green")
axes[0, 1].set_title(f"泊松分布 (λ={lam})")
axes[0, 1].set_xlabel("k")
axes[0, 1].set_ylabel("P(X=k)")

# 正态分布
mu, sigma = 0, 1
x = np.linspace(-4, 4, 100)
pdf = stats.norm.pdf(x, mu, sigma)
axes[1, 0].plot(x, pdf, color="red")
axes[1, 0].fill_between(x, pdf, alpha=0.3)
axes[1, 0].set_title(f"正态分布 (μ={mu}, σ={sigma})")
axes[1, 0].set_xlabel("x")
axes[1, 0].set_ylabel("f(x)")

# 均匀分布
a, b = 0, 10
x = np.linspace(-1, 11, 100)
pdf = stats.uniform.pdf(x, a, b-a)
axes[1, 1].plot(x, pdf, color="orange")
axes[1, 1].fill_between(x, pdf, alpha=0.3)
axes[1, 1].set_title(f"均匀分布 (a={a}, b={b})")
axes[1, 1].set_xlabel("x")
axes[1, 1].set_ylabel("f(x)")

plt.tight_layout()
plt.savefig("probability_distributions.png", dpi=150)
plt.close()
print("已保存：probability_distributions.png")
```

## 常见坑

### 坑1：条件概率的误解

```python
# 错误：P(A|B) = P(B|A)
# 正确：P(A|B) = P(A 且 B) / P(B)

# 例子：疾病检测
# 疾病患病率：1%
# 检测准确率：99%（真阳性率）
# 误报率：1%（假阳性率）

# 如果检测阳性，实际患病的概率是多少？
p_disease = 0.01
p_positive_given_disease = 0.99
p_positive_given_no_disease = 0.01

# 使用贝叶斯定理
p_positive = p_disease * p_positive_given_disease + (1-p_disease) * p_positive_given_no_disease
p_disease_given_positive = (p_positive_given_disease * p_disease) / p_positive

print(f"检测阳性时实际患病概率: {p_disease_given_positive:.2%}")  # 约 50%
```

### 坑2：独立事件的误解

```python
# 错误：如果事件 A 发生了，事件 B 就不会发生
# 正确：独立事件指 A 的发生不影响 B 的概率

# 独立事件：P(A 且 B) = P(A) * P(B)
# 不独立事件：P(A 且 B) ≠ P(A) * P(B)

# 例子：掷两次骰子
# 独立：第一次结果不影响第二次
# 不独立：第一次是6，第二次是6的概率仍然是 1/6
```

## 速查表

| 分布 | 参数 | 用途 | NumPy 函数 |
|------|------|------|------------|
| 伯努利 | p | 两种结果 | `np.random.binomial(1, p)` |
| 二项分布 | n, p | n次试验成功次数 | `np.random.binomial(n, p)` |
| 泊松分布 | λ | 单位时间事件次数 | `np.random.poisson(λ)` |
| 均匀分布 | a, b | 等可能取值 | `np.random.uniform(a, b)` |
| 正态分布 | μ, σ | 自然现象 | `np.random.normal(μ, σ)` |

## 小测验

1. 条件概率和联合概率的区别？
2. 二项分布和泊松分布的区别？
3. 正态分布的 68-95-99.7 法则是什么？
4. 什么时候使用均匀分布？
5. 贝叶斯定理的公式是什么？
