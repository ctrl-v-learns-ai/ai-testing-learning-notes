# NumPy 学习笔记

---

## 目录

- [第一部分：初识 NumPy](#第一部分初识-numpy)
- [第二部分：NumPy 基本使用](#第二部分numpy-基本使用)
- [第三部分：元素操作](#第三部分元素操作)
- [第四部分：数组操作](#第四部分数组操作)
- [第五部分：常用方法与技巧](#第五部分常用方法与技巧)
- [第六部分：常用函数大全](#第六部分常用函数大全)
- [第七部分：nan 和 inf](#第七部分nan-和-inf)

---

## 第一部分：初识 NumPy

### 1. NumPy 简介

NumPy（Numerical Python）是 Python 的第三方库，支持大量高维度数组与矩阵运算，并提供大量数学函数。

**核心作用：** 运行速度极快的数学库，主要用于数组计算。

**包含内容：**
- 强大的 N 维数组对象 `ndarray`
- 广播功能函数
- 线性代数、傅里叶变换、随机数生成等功能

**优势：**
- 比纯 Python 代码便捷且高效（底层用 C 语言编写）
- 数组的存储效率和 I/O 性能远优于 Python 原生数据结构
- 性能提升与数组元素数量成正比

### 2. ndarray 对象

ndarray 是一系列相同类型元素组成的数组集合，每个元素占有大小相同的内存块。它采用索引机制，将每个元素映射到内存块上，按行或列排列。

### 3. 安装与导入

```bash
pip install numpy
```

```python
import numpy as np
```

---

## 第二部分：NumPy 基本使用

### 1. 数据类型

NumPy 支持比 Python 内置类型更多的数值类型，基本可与 C 语言对应：

| 类型 | 类型代码 | 说明 |
|------|----------|------|
| int8 / uint8 | i1 / u1 | 8位有符号/无符号整型 |
| int16 / uint16 | i2 / u2 | 16位有符号/无符号整型 |
| int32 / uint32 | i4 / u4 | 32位有符号/无符号整型 |
| int64 / uint64 | i8 / u8 | 64位有符号/无符号整型 |
| float16 | f2 | 半精度浮点数 |
| float32 | f4 | 单精度浮点数 |
| float64 | f8 | 双精度浮点数（Python float 兼容） |
| bool | b | 布尔类型 |

```python
import numpy as np

dt = np.dtype(np.int32)
print(dt)    # int32

dt1 = np.dtype('i1')
print(dt1)   # int8
```

### 2. 创建数组

```python
import numpy as np

# 从列表创建
t1 = np.array([1, 2, 3])

# 从 range 创建
t2 = np.array(range(10))

# 使用 arange（推荐）
t3 = np.arange(10)

# arange 指定起止步长
t4 = np.arange(2, 10, 2)

# 指定数据类型
a = np.array([1, 2, 3, 4, 5])
print(a.dtype)  # int32
```

### 3. 数组属性

| 属性 | 说明 |
|------|------|
| `ndim` | 秩（轴的数量/维度数） |
| `shape` | 数组维度，返回元组（如 `(2, 3)` 表示2行3列） |
| `size` | 元素总个数 |
| `dtype` | 元素类型 |
| `itemsize` | 每个元素的大小（字节） |
| `flags` | 内存信息 |

```python
import numpy as np

# ndim 示例
arr = np.arange(24)
print(arr.ndim)  # 1

li = arr.reshape(2, 3, 4)
print(li.ndim)   # 3

# shape 示例
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)   # (2, 3)
arr.shape = (3, 2) # 直接修改 shape

# 其他属性
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.size)      # 6
print(arr.dtype)     # int32
print(arr.itemsize)  # 4
```

---

## 第三部分：元素操作

### 1. 索引和切片

```python
import numpy as np

t = np.arange(0, 20).reshape(5, 4)

# 取行
t[0]              # 第1行
t[:2]             # 前2行
t[2:]             # 第3行起
t[[2, 4]]         # 第3和第5行（不连续）

# 取列
t[:, 0]           # 第1列
t[:, :2]          # 前2列
t[:, [0, 2]]      # 第1和第3列

# 取行列
t[2, 3]           # 第3行第4列 → 11
t[2:5, 1:4]       # 第3~5行，第2~4列
t[[0, 2], [0, 1]] # 取点 (0,0) 和 (2,1) → [0, 9]
```

### 2. 布尔索引

```python
import numpy as np

t = np.arange(0, 20).reshape(5, 4)

t < 10         # 返回布尔数组
t[t > 10]      # 取大于10的值
t[t < 10]      # 取小于10的值
```

### 3. 广播原则

NumPy 对不同形状的数组进行数值计算的机制。

**形状相同：** 对应位直接运算
```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = a + b  # [6, 8, 10, 12]
```

**形状不同：** 较小数组广播到较大数组的形状
```python
import numpy as np

a = np.array([[0, 0], [1, 1], [2, 2]])
b = np.array([3, 3])
c = a + b
# [[3 3]
#  [4 4]
#  [5 5]]
```

**广播规则：**
1. 向最长形状看齐，不足部分前面加 1 补齐
2. 输出形状是各维度最大值
3. 某维度长度相同或为 1 时可运算，否则报错
4. 长度为 1 的维度沿此维度复制

### 4. 轴（axis）

- 一维数组：只有 0 轴
- 二维数组：0 轴（行方向）、1 轴（列方向）
- 三维数组：0 轴、1 轴、2 轴

**记忆方式：** `axis=0` 对每列操作，`axis=1` 对每行操作

---

## 第四部分：数组操作

### 1. 查看和修改数组形状

```python
import numpy as np

# 查看形状
a1 = np.array([1, 2, 3, 4, 5])
print(a1.shape)  # (5,) → 一维

a2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a2.shape)  # (2, 4) → 二维

# reshape：修改形状（返回新数组，不影响原数组）
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
b = a.reshape(4, 2)  # 用变量接收

# flatten：展平为一维
c = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
c.flatten()                        # [1, 2, 3, 4, 5, 6, 7, 8]
c.reshape(c.shape[0] * c.shape[1],)  # 另一种方式
```

### 2. 数组与数/数组的计算

```python
import numpy as np

a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# 数组与数（广播）
a + 1      # 每个元素 +1
a * 2      # 每个元素 ×2
a / 10     # 每个元素 ÷10

# 同形状数组
b = np.arange(11, 21).reshape(2, 5)
a + b      # 对应位相加
a * b      # 对应位相乘

# 不同维度（可广播的情况）
a = np.arange(1, 6).reshape(5,)       # (5,)
b = np.arange(11, 21).reshape(2, 5)   # (2, 5)
a + b  # a 广播为 (2, 5)

# 不可广播 → ValueError
a = np.arange(1, 13).reshape(3, 4)    # (3, 4)
b = np.arange(1, 11).reshape(2, 5)    # (2, 5)
# a + b  # 报错！
```

### 3. 转置

```python
import numpy as np

t = np.arange(0, 18).reshape(3, 6)

t.transpose()      # 方法1
t.swapaxes(1, 0)   # 方法2：交换轴
t.T                # 方法3：属性（最常用）
```

### 4. 拼接

```python
import numpy as np

t1 = np.arange(0, 12).reshape(2, 6)
t2 = np.arange(12, 24).reshape(2, 6)

np.vstack((t1, t2))   # 竖直拼接（行增加）
np.hstack((t1, t2))   # 水平拼接（列增加）
```

> ⚠️ 竖直拼接时，每列代表的意义应相同！

### 5. 行列交换

```python
import numpy as np

t = np.arange(12, 24).reshape(3, 4)

# 行交换：第2行和第3行互换
t[[1, 2], :] = t[[2, 1], :]

# 列交换：第1列和第3列互换
t[:, [0, 2]] = t[:, [2, 0]]
```

### 6. 裁剪与数值修改

```python
import numpy as np

t = np.arange(0, 20).reshape(5, 4)

# clip 裁剪：小于9的设为9，大于10的设为10
t.clip(9, 10)

# 直接修改
t[0, 0] = 100     # 修改单个元素
t[:, 0:2] = 0     # 修改多列
t[t < 20] = 0     # 布尔索引批量修改
t[t == 0] = 1     # 等于0的都改为1
```

---

## 第五部分：常用方法与技巧

### 1. 特殊数组创建

```python
import numpy as np

np.zeros((3, 4))   # 全0数组
np.ones((3, 4))    # 全1数组
np.eye(3)          # 单位矩阵（对角线为1）
```

### 2. 最大最小值位置

```python
import numpy as np

t = np.arange(1, 11).reshape(2, 5)

np.argmax(t, axis=0)   # 每列最大值的索引
np.argmin(t, axis=0)   # 每列最小值的索引
np.argmax(t, axis=1)   # 每行最大值的索引
```

### 3. 生成随机数

| 方法 | 说明 |
|------|------|
| `np.random.rand(d0, d1, ...)` | 均匀分布 [0, 1) |
| `np.random.randn(d0, d1, ...)` | 标准正态分布 |
| `np.random.randint(low, high, shape)` | 随机整数 ⭐常用 |
| `np.random.uniform(low, high, size)` | 均匀分布小数 |
| `np.random.normal(loc, scale, size)` | 正态分布 |
| `np.random.seed(s)` | 设置随机种子（可复现） |

```python
import numpy as np

np.random.randint(10, 20, (3, 3))
# 每次运行结果不同，例如：
# array([[13, 15, 18],
#        [18, 17, 15],
#        [15, 10, 12]])
```

### 4. 赋值、视图与副本

| 操作 | 类型 | 是否共享内存 | 修改是否影响原数组 |
|------|------|-------------|-------------------|
| `a = b` | 赋值 | ✅ 完全共享 | ✅ 相互影响 |
| `a = b[:]` 或 `a = b.view()` | 视图（浅拷贝） | ✅ 共享数据 | ✅ 影响原数组 |
| `a = b.copy()` | 副本（深拷贝） | ❌ 独立 | ❌ 不影响 |

```python
import numpy as np

# 赋值：同一对象，相互影响
x = np.array([1, 2, 3, 4, 5, 6])
y = x
print(id(x) == id(y))  # True

# 视图：切片返回视图，修改会影响原数组
x = np.arange(12)
y = x[3:]
y[1] = 100
print(x[4])  # 100，原数组被修改！

# 副本：互不影响
x = np.array([[10, 10], [2, 3], [4, 5]])
y = x.copy()
print(y is x)  # False
```

---

## 第六部分：常用函数大全

### 1. 字符串函数

基于 `np.char` 模块：

```python
import numpy as np

# 字符串连接
np.char.add(['hello'], ['python'])       # ['hellopython']
np.char.add(['hello', 'python'], ['yyds'])  # ['helloyyds' 'pythonyyds']

# 多重连接
np.char.multiply(['hello'], 3)           # ['hellohellohello']

# 居中填充
np.char.center(['hello', 'python'], 15, fillchar='-')
# ['-----hello-----' '-----python----']

# 大小写转换
np.char.capitalize(['hello', 'python'])  # ['Hello' 'Python']
np.char.title(['hello python'])          # ['Hello Python']
np.char.lower(['Hello Python'])          # ['hello python']
np.char.upper(['Hello Python'])          # ['HELLO PYTHON']

# 分割
np.char.split(['Hello Python'], sep=' ')  # [['Hello', 'Python']]
np.char.splitlines(['Hello\nPython\nyyds'])  # [['Hello', 'Python', 'yyds']]

# 去除首尾字符
np.char.strip(['--Hello--', '--python--'], '-')  # ['Hello' 'python']

# 连接
np.char.join("*", ['Hello', 'python'])  # ['H*e*l*l*o' 'p*y*t*h*o*n']

# 替换
np.char.replace(['Hello', 'python'], 'python', 'java')  # ['Hello' 'java']

# 编码解码
encoded = np.char.encode(['Hello', 'python'], 'utf-8')  # [b'Hello' b'python']
np.char.decode(encoded, 'utf-8')  # ['Hello' 'python']
```

### 2. 数学函数

```python
import numpy as np

a = np.array([0, 30, 45, 60, 90, 180])

# 三角函数（角度需转弧度：角度 * np.pi / 180）
np.sin(a * np.pi / 180)    # 正弦
np.cos(a * np.pi / 180)    # 余弦
np.tan(a * np.pi / 180)    # 正切

# 反三角函数（返回弧度）
inv = np.arcsin(np.sin(a * np.pi / 180))
np.degrees(inv)             # 弧度转角度

# 舍入
a = np.array([1.0, 2.22, 3.456, 4.4444, 5.5555])
np.around(a)                # 四舍五入 → [1., 2., 3., 4., 6.]
np.around(a, decimals=1)    # 保留1位小数
np.around(a, decimals=-1)   # 十位取整
np.floor(a)                 # 向下取整
np.ceil(a)                  # 向上取整
```

### 3. 算术函数

```python
import numpy as np

x = np.arange(9, dtype="f").reshape(3, 3)
y = np.array([10, 10, 10])

np.add(x, y)          # 加
np.subtract(x, y)     # 减
np.multiply(x, y)     # 乘
np.divide(x, y)       # 除
np.reciprocal(x)      # 逐元素倒数

a = np.array([1, 2, 3])
b = np.array([10, 10, 10])
np.power(a, b)        # 幂运算 → [1, 1024, 59049]

a = np.array([10, 10, 10])
b = np.array([1, 2, 3])
np.mod(a, b)          # 取模 → [0, 0, 1]
np.remainder(a, b)    # 取余（同 mod）
```

### 4. 统计函数

```python
import numpy as np

a = np.arange(12).reshape(3, 4)

# 最大值、最小值
np.amax(a, axis=0)    # 每列最大值
np.amin(a, axis=1)    # 每行最小值

# 极差（最大 - 最小）
np.ptp(a, axis=0)

# 百分位数（50% = 中位数）
np.percentile(a, 50)
np.percentile(a, 50, axis=0)

# 求和
t = np.arange(1, 11).reshape(2, 5)
np.sum(t)             # 所有元素求和
np.sum(t, axis=0)     # 每列求和
np.sum(t, axis=1)     # 每行求和

# 平均值
t.mean(axis=None)     # 全局平均值
t.mean(axis=0)        # 每列平均值

# 中位数
np.median(t, axis=0)

# 标准差（越大表示波动越大，越不稳定）
t.std(axis=None)
```

### 5. 排序函数

```python
import numpy as np

x = np.random.randint(1, 11, 12).reshape(3, 4)

# sort 排序
np.sort(x)           # 默认每行排序
np.sort(x, axis=0)   # 按列排序

# argsort：返回排序索引
i = np.argsort(x)
x[i]                 # 用索引重建排序后的数组

# partition：分区
np.partition(x, 3)   # 比第k小的放前面

# argpartition：通过索引找第k小/大的值
y = np.array([46, 57, 23, 39, 1, 10, 0, 120])
y[np.argpartition(y, 2)[2]]    # 第3小的值 → 10
y[np.argpartition(y, -2)[-2]]  # 第2大的值 → 57
```

### 6. 搜索函数

```python
import numpy as np

t = np.arange(1, 11).reshape(2, 5)

# 最大最小值
t.max(axis=0)        # 每列最大值
t.min(axis=1)        # 每行最小值
t.argmax(axis=None)  # 最大值的扁平索引
t.argmin(axis=0)     # 每列最小值的索引

# nonzero：非零元素索引
x = np.array([[30, 40, 0], [0, 20, 10], [50, 0, 60]])
np.nonzero(x)

# where：满足条件的索引
y = np.where(x > 30)
x[y]                 # [40, 50, 60]

# extract：按条件抽取
condition = np.mod(x, 2) == 0   # 偶数条件
np.extract(condition, x)         # 抽取所有偶数
```

---

## 第七部分：nan 和 inf

### nan（Not a Number）

**出现场景：**
- 读取本地 float 文件时有缺失值
- 不合适的计算（如 inf - inf）

```python
import numpy as np
print(type(np.nan))  # <class 'float'>
```

**重要特性：**
```python
# 两个 nan 不相等！
print(np.nan == np.nan)   # False
print(np.nan != np.nan)   # True
```

**判断 nan 的个数：**
```python
b = np.array([1, 2, 3, 4, 5], dtype='float')
b[0] = np.nan
b[1] = np.nan

# 方法1：利用 nan != nan 的特性
count = np.count_nonzero(b != b)

# 方法2：推荐方式
count = np.count_nonzero(np.isnan(b))
```

**处理建议：** 不要把 nan 简单替换为 0（会拉低均值），应替换为均值或中位数，或直接删除缺失行。

### inf（Infinity）

**出现场景：**
- 一个数除以 0（Python 报错，NumPy 返回 inf/-inf）

```python
import numpy as np
print(type(np.inf))  # <class 'float'>
```

### nan 的计算规则

**nan 和任何值计算都为 nan：**
```python
import numpy as np

t = np.array([1, 2, 3, 4, 5], dtype='float')
t[0] = np.nan
print(np.sum(t))  # nan！整个求和结果都是 nan
```

---

> 📝 **学习建议：** 建议边看笔记边在编辑器中逐段敲代码运行，加深理解。NumPy 是数据分析和机器学习的基石，务必熟练掌握。
