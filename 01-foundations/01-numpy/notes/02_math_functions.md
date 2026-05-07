# NumPy 阶段二：数学函数与计算

## 统计函数

```python
arr = np.array([1, 2, 3, 4, 5])

# 基础统计
np.mean(arr)      # 3.0 - 平均值
np.median(arr)    # 3.0 - 中位数
np.std(arr)       # 1.41 - 标准差
np.var(arr)       # 2.0 - 方差
np.min(arr)       # 1 - 最小值
np.max(arr)       # 5 - 最大值
np.sum(arr)       # 15 - 求和

# 累计统计
np.cumsum(arr)    # [1, 3, 6, 10, 15] - 累计和
np.cumprod(arr)   # [1, 2, 6, 24, 120] - 累计积

# 分位数
np.percentile(arr, 50)  # 50% 分位数
np.quantile(arr, 0.25)  # 25% 分位数
```

## 数组运算

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 逐元素运算
a + b       # [5, 7, 9]
a - b       # [-3, -3, -3]
a * b       # [4, 10, 18]
a / b       # [0.25, 0.4, 0.5]
a ** 2      # [1, 4, 9]

# 数学函数
np.sqrt(a)      # [1, 1.41, 1.73]
np.exp(a)       # [2.71, 7.38, 20.08]
np.log(a)       # [0, 0.69, 1.09]
np.sin(a)       # 三角函数
np.cos(a)
np.abs(-a)      # [1, 2, 3]
```

## 广播机制

```python
# 不同形状的数组运算
arr = np.array([[1, 2, 3], [4, 5, 6]])  # (2, 3)
scalar = 2

# 标量广播
arr + scalar  # [[3,4,5], [6,7,8]]

# 一维数组广播
row = np.array([10, 20, 30])
arr + row     # [[11,22,33], [14,25,36]]

# 列向量广播
col = np.array([[10], [20]])
arr + col     # [[11,12,13], [24,25,26]]
```

## 比较与逻辑

```python
arr = np.array([1, 2, 3, 4, 5])

# 比较运算
arr > 3         # [False, False, False, True, True]
arr == 3        # [False, False, True, False, False]

# 逻辑运算
(arr > 2) & (arr < 5)  # [False, True, True, True, False]
(arr < 2) | (arr > 4)  # [True, False, False, False, True]

# 条件选择
np.where(arr > 3, "big", "small")  # ["small", "small", "small", "big", "big"]
```

## 常见坑

### 坑1：整数溢出
```python
# 大整数可能溢出
arr = np.array([2000000000], dtype=np.int32)
arr * arr  # 溢出！

# 解决：使用 int64
arr = np.array([2000000000], dtype=np.int64)
```

### 坑2：浮点精度
```python
# 浮点运算有精度误差
0.1 + 0.2 == 0.3  # False!

# 使用 allclose 比较
np.allclose(0.1 + 0.2, 0.3)  # True
```

### 坑3：NaN 处理
```python
arr = np.array([1, np.nan, 3])
np.mean(arr)      # nan

# 使用 nanmean 忽略 NaN
np.nanmean(arr)   # 2.0
```

## 速查表

| 操作 | 代码 |
|------|------|
| 平均值 | `np.mean(arr)` |
| 标准差 | `np.std(arr)` |
| 求和 | `np.sum(arr)` |
| 最大值 | `np.max(arr)` |
| 累计和 | `np.cumsum(arr)` |
| 广播加 | `arr + scalar` |
| 条件选择 | `np.where(cond, x, y)` |
| 忽略NaN | `np.nanmean(arr)` |

## 小测验

1. 广播机制的规则是什么？
2. np.where 的三个参数分别是什么？
3. 如何处理数组中的 NaN 值？
4. mean 和 average 的区别？
5. 如何计算数组的行和列的和？
