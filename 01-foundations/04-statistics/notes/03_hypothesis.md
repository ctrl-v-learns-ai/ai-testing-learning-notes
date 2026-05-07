# 统计学基础三：假设检验

## 什么是假设检验？

假设检验是用样本数据来判断关于总体的假设是否成立的统计方法。

类比理解：
- 假设检验 = 法庭审判（先假设无罪，再找证据推翻）
- 零假设 = 被告无罪（默认状态）
- 备择假设 = 被告有罪（需要证明的状态）

## 假设检验的基本步骤

1. **提出假设**：零假设 H₀ 和备择假设 H₁
2. **选择检验统计量**：t 统计量、z 统计量等
3. **确定显著性水平 α**：通常 0.05
4. **计算 p 值**：观察到的数据或更极端数据出现的概率
5. **做出决策**：p 值 < α 拒绝 H₀，否则不拒绝 H₀

## 单样本 t 检验

```python
import numpy as np
from scipy import stats

# 场景：检验某班级平均分是否等于 75 分
# H₀: μ = 75
# H₁: μ ≠ 75

# 样本数据
np.random.seed(42)
scores = np.random.normal(78, 10, 30)  # 均值78，标准差10，30个样本

# 单样本 t 检验
t_stat, p_value = stats.ttest_1samp(scores, 75)

print(f"样本均值: {np.mean(scores):.2f}")
print(f"t 统计量: {t_stat:.4f}")
print(f"p 值: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"p值 {p_value:.4f} < {alpha}，拒绝零假设")
    print("结论：班级平均分不等于75分")
else:
    print(f"p值 {p_value:.4f} >= {alpha}，不拒绝零假设")
    print("结论：没有足够证据说明班级平均分不等于75分")
```

## 双样本 t 检验

```python
import numpy as np
from scipy import stats

# 场景：比较两个班级的平均分
# H₀: μ₁ = μ₂
# H₁: μ₁ ≠ μ₂

# 两个班级的样本数据
np.random.seed(42)
class_a = np.random.normal(78, 10, 30)  # 班级A
class_b = np.random.normal(82, 10, 30)  # 班级B

# 独立双样本 t 检验
t_stat, p_value = stats.ttest_ind(class_a, class_b)

print(f"班级A均值: {np.mean(class_a):.2f}")
print(f"班级B均值: {np.mean(class_b):.2f}")
print(f"t 统计量: {t_stat:.4f}")
print(f"p 值: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"p值 {p_value:.4f} < {alpha}，拒绝零假设")
    print("结论：两个班级平均分有显著差异")
else:
    print(f"p值 {p_value:.4f} >= {alpha}，不拒绝零假设")
    print("结论：没有足够证据说明两个班级平均分有差异")
```

## 配对样本 t 检验

```python
import numpy as np
from scipy import stats

# 场景：比较培训前后的成绩
# H₀: μ_diff = 0
# H₁: μ_diff ≠ 0

# 培训前后的成绩
np.random.seed(42)
before = np.random.normal(70, 10, 30)
after = before + np.random.normal(5, 3, 30)  # 培训后提高5分左右

# 配对样本 t 检验
t_stat, p_value = stats.ttest_rel(before, after)

print(f"培训前均值: {np.mean(before):.2f}")
print(f"培训后均值: {np.mean(after):.2f}")
print(f"差值均值: {np.mean(after - before):.2f}")
print(f"t 统计量: {t_stat:.4f}")
print(f"p 值: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"p值 {p_value:.4f} < {alpha}，拒绝零假设")
    print("结论：培训后成绩有显著提高")
else:
    print(f"p值 {p_value:.4f} >= {alpha}，不拒绝零假设")
    print("结论：没有足够证据说明培训后成绩有提高")
```

## 卡方检验

```python
import numpy as np
from scipy import stats

# 场景：检验骰子是否公平
# H₀：骰子是公平的（每个面概率相等）
# H₁：骰子不公平

# 观察频数
observed = np.array([10, 12, 8, 15, 11, 14])  # 6个面的出现次数

# 期望频数（如果骰子公平）
expected = np.array([sum(observed)/6] * 6)

# 卡方检验
chi2, p_value = stats.chisquare(observed, expected)

print(f"观察频数: {observed}")
print(f"期望频数: {expected}")
print(f"卡方统计量: {chi2:.4f}")
print(f"p 值: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"p值 {p_value:.4f} < {alpha}，拒绝零假设")
    print("结论：骰子不公平")
else:
    print(f"p值 {p_value:.4f} >= {alpha}，不拒绝零假设")
    print("结论：没有足够证据说明骰子不公平")
```

## 相关性检验

```python
import numpy as np
from scipy import stats

# 场景：检验广告投入和销售额是否有相关性
# H₀：ρ = 0（没有相关性）
# H₁：ρ ≠ 0（有相关性）

# 数据
np.random.seed(42)
advertising = np.random.uniform(10, 100, 50)
sales = advertising * 2.5 + np.random.normal(0, 20, 50)

# 皮尔逊相关系数检验
corr, p_value = stats.pearsonr(advertising, sales)

print(f"皮尔逊相关系数: {corr:.4f}")
print(f"p 值: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"p值 {p_value:.4f} < {alpha}，拒绝零假设")
    print("结论：广告投入和销售额有显著相关性")
else:
    print(f"p值 {p_value:.4f} >= {alpha}，不拒绝零假设")
    print("结论：没有足够证据说明广告投入和销售额有相关性")
```

## 效应量

```python
import numpy as np
from scipy import stats

# Cohen's d 效应量
def cohens_d(group1, group2):
    """计算 Cohen's d 效应量"""
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    d = (np.mean(group1) - np.mean(group2)) / pooled_std
    return d

# 解释效应量
# d ≈ 0.2：小效应
# d ≈ 0.5：中效应
# d ≈ 0.8：大效应

# 例子
np.random.seed(42)
group_a = np.random.normal(100, 15, 30)
group_b = np.random.normal(108, 15, 30)

d = cohens_d(group_a, group_b)
print(f"Cohen's d: {d:.4f}")

if abs(d) < 0.2:
    print("效应量：小")
elif abs(d) < 0.5:
    print("效应量：小到中")
elif abs(d) < 0.8:
    print("效应量：中到大")
else:
    print("效应量：大")
```

## 置信区间

```python
import numpy as np
from scipy import stats

# 计算均值的置信区间
def confidence_interval(data, confidence=0.95):
    """计算均值的置信区间"""
    n = len(data)
    mean = np.mean(data)
    se = stats.sem(data)  # 标准误差
    h = se * stats.t.ppf((1 + confidence) / 2, n - 1)
    return mean - h, mean + h

# 例子
np.random.seed(42)
data = np.random.normal(100, 15, 30)

ci_lower, ci_upper = confidence_interval(data, 0.95)
print(f"样本均值: {np.mean(data):.2f}")
print(f"95% 置信区间: [{ci_lower:.2f}, {ci_upper:.2f}]")
```

## 常见坑

### 坑1：p 值的误解

```python
# 错误：p 值是 H₀ 为真的概率
# 正确：p 值是在 H₀ 为真的假设下，观察到当前数据或更极端数据的概率

# 错误：p 值越小，效应越大
# 正确：p 值受样本量影响，样本量大时即使小效应也会有小 p 值
```

### 坑2：统计显著 vs 实际显著

```python
import numpy as np
from scipy import stats

# 统计显著但实际不显著
np.random.seed(42)
group_a = np.random.normal(100, 10, 1000)
group_b = np.random.normal(101, 10, 1000)  # 只差1分

t_stat, p_value = stats.ttest_ind(group_a, group_b)
print(f"p 值: {p_value:.4f}")  # 可能 < 0.05
print(f"差值: {np.mean(group_b) - np.mean(group_a):.2f}")  # 只有1分

# 结论：统计显著但实际意义不大
```

### 坑3：多重比较问题

```python
import numpy as np
from scipy import stats

# 多次检验会增加犯第一类错误的概率
# 如果进行 20 次检验，期望有 1 次是假阳性（0.05 * 20）

# 解决方案：
# 1. Bonferroni 校正：α' = α / m
# 2. FDR 校正：控制错误发现率
```

## 速查表

| 检验方法 | 用途 | 函数 |
|----------|------|------|
| 单样本 t 检验 | 检验均值是否等于某值 | `stats.ttest_1samp()` |
| 双样本 t 检验 | 比较两组均值 | `stats.ttest_ind()` |
| 配对 t 检验 | 比较配对数据 | `stats.ttest_rel()` |
| 卡方检验 | 检验分类变量 | `stats.chisquare()` |
| 相关性检验 | 检验相关性 | `stats.pearsonr()` |

## 小测验

1. 零假设和备择假设的区别？
2. p 值的含义是什么？
3. 统计显著和实际显著的区别？
4. 什么时候用配对 t 检验？
5. 多重比较问题是什么？如何解决？
