# NumPy 阶段一：基础数组操作

## 什么是 NumPy？
NumPy (Numerical Python) 是 Python 科学计算的基础库，核心是 ndarray 对象。

类比理解：
- Python list = 仓库里的散货（类型混杂，效率低）
- NumPy array = 仓库里的标准化货架（类型统一，效率高）

## 安装与导入
```python
pip install numpy
import numpy as np
```

## 数组创建

```python
# 从列表创建
arr = np.array([1, 2, 3, 4, 5])

# 创建全零数组
zeros = np.zeros((3, 4))  # 3行4列

# 创建全一数组
ones = np.ones((2, 3))  # 2行3列

# 创建等差数组
arange = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1.0]

# 创建随机数组
random = np.random.rand(3, 3)  # 0-1随机数
randint = np.random.randint(0, 10, (2, 3))  # 0-10随机整数
```

## 数组属性

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

arr.shape      # (2, 3) - 形状
arr.ndim       # 2 - 维度数
arr.size       # 6 - 元素总数
arr.dtype      # int32 - 数据类型
arr.itemsize   # 4 - 每个元素字节数
```

## 索引与切片

```python
arr = np.array([10, 20, 30, 40, 50])

# 一维索引
arr[0]     # 10
arr[-1]    # 50

# 一维切片
arr[1:4]   # [20, 30, 40]
arr[::2]   # [10, 30, 50]

# 二维数组
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[0, 0]      # 1
arr2d[1, :]      # [4, 5, 6] - 第2行
arr2d[:, 1]      # [2, 5, 8] - 第2列
arr2d[0:2, 1:]   # [[2, 3], [5, 6]]
```

## 形状操作

```python
arr = np.array([1, 2, 3, 4, 5, 6])

# reshape - 改变形状
arr.reshape(2, 3)   # [[1,2,3], [4,5,6]]
arr.reshape(3, -1)  # -1 表示自动计算

# flatten - 展平
arr2d.flatten()     # 返回一维副本

# transpose - 转置
arr2d.T             # 行列互换

# 合并
np.concatenate([arr1, arr2])  # 拼接
np.vstack([arr1, arr2])       # 垂直堆叠
np.hstack([arr1, arr2])       # 水平堆叠

# 分割
np.split(arr, 3)              # 分成3份
```

## 数据类型

```python
arr = np.array([1, 2, 3])

arr.astype(float)    # 转为浮点
arr.astype(str)      # 转为字符串

# 常见类型
np.int32, np.int64
np.float32, np.float64
np.bool_
np.str_
```

## 常见坑

### 坑1：视图 vs 副本
```python
# 切片返回视图（修改会影响原数组）
arr = np.array([1, 2, 3, 4, 5])
slice_arr = arr[1:3]
slice_arr[0] = 99  # arr 也会变！

# 需要副本时用 copy()
copy_arr = arr[1:3].copy()
```

### 坑2：广播形状不匹配
```python
# 形状不兼容会报错
a = np.zeros((3, 4))
b = np.zeros((3, 5))
# a + b  # ValueError
```

### 坑3：整数除法
```python
# Python 3 中 / 是浮点除法
# 但 NumPy 整数数组 / 整数仍是整数（旧版本）
arr = np.array([1, 2, 3])
result = arr / 2  # [0.5, 1.0, 1.5] - 新版本没问题
```

## 速查表

| 操作 | 代码 |
|------|------|
| 创建数组 | `np.array([1,2,3])` |
| 全零 | `np.zeros((3,4))` |
| 全一 | `np.ones((2,3))` |
| 等差 | `np.arange(0,10,2)` |
| 随机 | `np.random.rand(3,3)` |
| 形状 | `arr.shape` |
| 重塑 | `arr.reshape(2,3)` |
| 转置 | `arr.T` |
| 切片 | `arr[1:3, :]` |
| 拼接 | `np.concatenate([a,b])` |

## 小测验

1. NumPy 数组和 Python 列表的区别？
2. 视图和副本的区别？什么时候用 copy()？
3. reshape 中 -1 表示什么？
4. 如何创建一个 3x3 的单位矩阵？
5. 如何获取数组中大于 5 的所有元素？
