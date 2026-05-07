# 统计学基础一：描述性统计

## 什么是描述性统计？

描述性统计是用数字或图表来概括数据特征的方法。它不试图从样本推断总体，而是直接描述已有的数据。

类比理解：
- 描述性统计 = 给数据拍照片（记录当前状态）
- 推断性统计 = 给数据做预测（从样本推断总体）

## 集中趋势

### 平均数（Mean）

```python
import numpy as np

data = [10, 20, 30, 40, 50]

# 手动计算
mean = sum(data) / len(data)
print(f"平均数: {mean}")  # 30.0

# 使用 NumPy
mean = np.mean(data)
print(f"平均数: {mean}")  # 30.0
```

### 中位数（Median）

```python
data = [10, 20, 30, 40, 50]

# 手动计算
sorted_data = sorted(data)
n = len(sorted_data)
if n % 2 == 0:
    median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
else:
    median = sorted_data[n//2]
print(f"中位数: {median}")  # 30

# 使用 NumPy
median = np.median(data)
print(f"中位数: {median}")  # 30.0
```

### 众数（Mode）

```python
from collections import Counter

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# 手动计算
counter = Counter(data)
mode = counter.most_common(1)[0][0]
print(f"众数: {mode}")  # 4

# 使用 scipy
from scipy import stats
mode = stats.mode(data)
print(f"众数: {mode.mode[0]}")  # 4
```

## 离散趋势

### 极差（Range）

```python
data = [10, 20, 30, 40, 50]

# 手动计算
range_val = max(data) - min(data)
print(f"极差: {range_val}")  # 40

# 使用 NumPy
range_val = np.ptp(data)  # peak to peak
print(f"极差: {range_val}")  # 40
```

### 方差（Variance）

```python
data = [10, 20, 30, 40, 50]

# 手动计算（总体方差）
mean = sum(data) / len(data)
variance = sum((x - mean) ** 2 for x in data) / len(data)
print(f"总体方差: {variance}")  # 200.0

# 使用 NumPy（总体方差）
variance = np.var(data)
print(f"总体方差: {variance}")  # 200.0

# 样本方差（除以 n-1）
sample_var = np.var(data, ddof=1)
print(f"样本方差: {sample_var}")  # 250.0
```

### 标准差（Standard Deviation）

```python
data = [10, 20, 30, 40, 50]

# 手动计算
std = np.sqrt(np.var(data))
print(f"标准差: {std}")  # 14.1421...

# 使用 NumPy
std = np.std(data)
print(f"标准差: {std}")  # 14.1421...
```

### 变异系数（Coefficient of Variation）

```python
data = [10, 20, 30, 40, 50]

# 变异系数 = 标准差 / 平均数
cv = np.std(data) / np.mean(data)
print(f"变异系数: {cv:.2%}")  # 47.14%
```

## 分位数

```python
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 四分位数
q1 = np.percentile(data, 25)  # 第一四分位数
q2 = np.percentile(data, 50)  # 中位数
q3 = np.percentile(data, 75)  # 第三四分位数

print(f"Q1: {q1}")  # 32.5
print(f"Q2: {q2}")  # 55.0
print(f"Q3: {q3}")  # 77.5

# 四分位距
iqr = q3 - q1
print(f"IQR: {iqr}")  # 45.0
```

## 分布形状

### 偏度（Skewness）

```python
from scipy import stats

# 正偏（右偏）
data_right = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
skew_right = stats.skew(data_right)
print(f"右偏数据偏度: {skew_right:.2f}")  # > 0

# 负偏（左偏）
data_left = [100, 9, 8, 7, 6, 5, 4, 3, 2, 1]
skew_left = stats.skew(data_left)
print(f"左偏数据偏度: {skew_left:.2f}")  # < 0

# 对称分布
data_sym = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
skew_sym = stats.skew(data_sym)
print(f"对称数据偏度: {skew_sym:.2f}")  # ≈ 0
```

### 峰度（Kurtosis）

```python
from scipy import stats

# 尖峰分布
data_leptokurtic = [1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 7, 8, 9]
kurt_lep = stats.kurtosis(data_leptokurtic)
print(f"尖峰分布峰度: {kurt_lep:.2f}")  # > 0

# 平峰分布
data_platykurtic = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kurt_plat = stats.kurtosis(data_platykurtic)
print(f"平峰分布峰度: {kurt_plat:.2f}")  # < 0
```

## 数据可视化

```python
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 生成数据
np.random.seed(42)
data = np.random.normal(100, 15, 1000)

# 直方图
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].hist(data, bins=30, color="steelblue", edgecolor="white")
axes[0].set_title("直方图")
axes[0].axvline(np.mean(data), color="red", linestyle="--", label=f"均值: {np.mean(data):.1f}")
axes[0].legend()

# 箱线图
axes[1].boxplot(data)
axes[1].set_title("箱线图")

# 密度图
from scipy import stats
density = stats.gaussian_kde(data)
x = np.linspace(min(data), max(data), 100)
axes[2].plot(x, density(x))
axes[2].set_title("密度图")

plt.tight_layout()
plt.savefig("descriptive_stats.png", dpi=150)
plt.close()
print("已保存：descriptive_stats.png")
```

## 综合统计

```python
import pandas as pd
import numpy as np

# 创建数据
data = {
    "数学": [85, 90, 78, 92, 88, 76, 95, 89, 82, 91],
    "英语": [78, 85, 82, 88, 90, 75, 92, 86, 80, 87],
    "物理": [92, 88, 85, 90, 82, 78, 96, 84, 88, 93]
}
df = pd.DataFrame(data)

# 基本统计
print("基本统计量：")
print(df.describe())

# 相关系数
print("\n相关系数矩阵：")
print(df.corr())
```

## 常见坑

### 坑1：总体方差 vs 样本方差

```python
data = [10, 20, 30, 40, 50]

# 总体方差（除以 n）
pop_var = np.var(data)
print(f"总体方差: {pop_var}")  # 200.0

# 样本方差（除以 n-1）
sample_var = np.var(data, ddof=1)
print(f"样本方差: {sample_var}")  # 250.0

# 选择建议：
# - 如果数据是整个总体，使用总体方差
# - 如果数据是样本，使用样本方差
```

### 坑2：平均数受异常值影响

```python
data_normal = [10, 20, 30, 40, 50]
data_outlier = [10, 20, 30, 40, 1000]

print(f"正常数据平均数: {np.mean(data_normal)}")  # 30.0
print(f"异常数据平均数: {np.mean(data_outlier)}")  # 220.0

print(f"正常数据中位数: {np.median(data_normal)}")  # 30.0
print(f"异常数据中位数: {np.median(data_outlier)}")  # 30.0

# 建议：有异常值时，使用中位数更可靠
```

### 坑3：偏度的解释

```python
from scipy import stats

# 偏度 > 0：右偏（正偏）
# 偏度 < 0：左偏（负偏）
# 偏度 = 0：对称

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
skew = stats.skew(data)
print(f"偏度: {skew:.2f}")  # > 0，右偏
```

## 速查表

| 统计量 | 公式 | NumPy 函数 |
|--------|------|------------|
| 平均数 | Σx/n | `np.mean()` |
| 中位数 | 排序后中间值 | `np.median()` |
| 众数 | 出现次数最多 | `scipy.stats.mode()` |
| 极差 | max - min | `np.ptp()` |
| 方差 | Σ(x-mean)²/n | `np.var()` |
| 标准差 | √方差 | `np.std()` |
| 变异系数 | std/mean | `np.std()/np.mean()` |
| 四分位距 | Q3 - Q1 | `np.percentile(75) - np.percentile(25)` |

## 小测验

1. 平均数、中位数、众数的区别和适用场景？
2. 总体方差和样本方差的区别？
3. 标准差的作用是什么？
4. 偏度和峰度分别表示什么？
5. 什么时候用中位数比平均数更合适？
