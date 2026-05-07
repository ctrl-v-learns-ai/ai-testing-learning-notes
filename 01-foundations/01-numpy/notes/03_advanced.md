# NumPy 阶段三：高级应用

## 线性代数

```python
import numpy as np

# 矩阵创建
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 矩阵乘法
np.dot(A, B)        # 矩阵乘法
A @ B               # 矩阵乘法（运算符）

# 转置
A.T                 # 转置

# 行列式
np.linalg.det(A)    # 行列式

# 逆矩阵
np.linalg.inv(A)    # 逆矩阵

# 特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)

# 解线性方程组 Ax = b
b = np.array([5, 6])
x = np.linalg.solve(A, b)

# 矩阵的秩
np.linalg.matrix_rank(A)
```

## 随机数生成

```python
# 设置随机种子（可重复）
np.random.seed(42)

# 均匀分布 [0, 1)
np.random.rand(3, 3)

# 正态分布
np.random.normal(loc=0, scale=1, size=(3, 3))

# 随机整数
np.random.randint(0, 10, size=(3, 3))

# 随机选择
np.random.choice([1, 2, 3, 4, 5], size=3)

# 打乱顺序
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)  # 原地打乱
np.random.permutation(arr)  # 返回新数组
```

## 性能优化

```python
# 向量化 vs 循环
import time

# 慢：Python 循环
start = time.time()
result = 0
for i in range(1000000):
    result += i
print(f"Loop: {time.time() - start:.3f}s")

# 快：NumPy 向量化
start = time.time()
result = np.sum(np.arange(1000000))
print(f"Vectorized: {time.time() - start:.3f}s")

# 内存效率
# 使用适当的数据类型
arr = np.array([1, 2, 3], dtype=np.int8)  # 节省内存
```

## 实用技巧

```python
# 唯一值和计数
arr = np.array([1, 2, 2, 3, 3, 3])
unique, counts = np.unique(arr, return_counts=True)
# unique: [1, 2, 3], counts: [1, 2, 3]

# 条件筛选
np.argwhere(arr > 2)  # 满足条件的索引
np.argsort(arr)       # 排序索引

# 保存和加载
np.save("data.npy", arr)
loaded = np.load("data.npy")

# 文本格式
np.savetxt("data.txt", arr)
loaded = np.loadtxt("data.txt")
```

## 常见坑

### 坑1：矩阵乘法混淆
```python
# 逐元素乘法 vs 矩阵乘法
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

A * B     # 逐元素乘法
A @ B     # 矩阵乘法
```

### 坑2：随机种子
```python
# 不设种子，每次结果不同
np.random.rand(3)

# 设种子，结果可重复
np.random.seed(42)
np.random.rand(3)
```

### 坑3：内存视图
```python
# 某些操作返回视图
arr = np.array([1, 2, 3])
view = arr.reshape(3, 1)  # 视图
copy = arr.copy()          # 副本
```

## 速查表

| 操作 | 代码 |
|------|------|
| 矩阵乘法 | `A @ B` |
| 逆矩阵 | `np.linalg.inv(A)` |
| 行列式 | `np.linalg.det(A)` |
| 特征值 | `np.linalg.eig(A)` |
| 解方程 | `np.linalg.solve(A, b)` |
| 正态分布 | `np.random.normal(0, 1, 100)` |
| 随机选择 | `np.choice(arr, 3)` |
| 唯一值 | `np.unique(arr)` |
| 保存 | `np.save("file.npy", arr)` |

## 小测验

1. @ 运算符和 * 的区别？
2. 如何让随机数可重复？
3. 向量化为什么比循环快？
4. 如何解线性方程组？
5. 视图和副本的区别？
