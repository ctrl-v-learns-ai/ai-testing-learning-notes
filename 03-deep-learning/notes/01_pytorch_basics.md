# 深度学习一：PyTorch 基础

## 什么是深度学习？

深度学习是机器学习的一个分支，使用多层神经网络来学习数据的复杂模式。

类比理解：
- 传统机器学习 = 你告诉计算机找什么特征
- 深度学习 = 计算机自己学习找什么特征

## 深度学习 vs 机器学习

| 特性 | 传统机器学习 | 深度学习 |
|------|-------------|----------|
| 特征工程 | 手动设计 | 自动学习 |
| 数据需求 | 少量数据 | 大量数据 |
| 计算资源 | CPU 即可 | 需要 GPU |
| 可解释性 | 高 | 低 |
| 适用场景 | 结构化数据 | 图像、文本、语音 |

## PyTorch 基础

### 安装

```bash
# CPU 版本
pip install torch torchvision

# GPU 版本（需要 CUDA）
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### 张量（Tensor）

```python
import torch

# 创建张量
x = torch.tensor([1, 2, 3, 4, 5])
print(x)  # tensor([1, 2, 3, 4, 5])

# 创建特殊张量
zeros = torch.zeros(3, 4)  # 全零
ones = torch.ones(3, 4)    # 全一
rand = torch.rand(3, 4)    # 随机数
eye = torch.eye(3)         # 单位矩阵

# 从 NumPy 创建
import numpy as np
np_array = np.array([1, 2, 3])
tensor = torch.from_numpy(np_array)

# 张量属性
x = torch.rand(3, 4)
print(f"形状: {x.shape}")
print(f"数据类型: {x.dtype}")
print(f"设备: {x.device}")
```

### 张量操作

```python
# 基本运算
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

# 加法
z = x + y  # tensor([5, 7, 9])

# 乘法
z = x * y  # tensor([4, 10, 18])

# 矩阵乘法
x = torch.rand(3, 4)
y = torch.rand(4, 5)
z = torch.mm(x, y)  # 或 x @ y

# 形状操作
x = torch.rand(3, 4)
x_reshaped = x.reshape(4, 3)
x_transposed = x.t()
x_flattened = x.view(-1)

# 索引和切片
x = torch.rand(3, 4)
print(x[0, :])      # 第一行
print(x[:, 0])      # 第一列
print(x[0:2, 0:2])  # 子矩阵
```

### 自动求导

```python
# 自动求导是深度学习的核心
x = torch.tensor([2.0], requires_grad=True)
y = x ** 2 + 3 * x + 1

# 反向传播
y.backward()

# 求导结果
print(x.grad)  # dy/dx = 2x + 3 = 7
```

### GPU 加速

```python
# 检查 GPU
print(torch.cuda.is_available())

# 将张量移到 GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.rand(3, 4).to(device)

# 将模型移到 GPU
model = model.to(device)
```

## 常见坑

### 坑1：数据类型不匹配

```python
# 错误：整数和浮点数混合
x = torch.tensor([1, 2, 3])  # 整数
y = torch.tensor([1.0, 2.0, 3.0])  # 浮点数
# z = x + y  # 可能出错

# 正确：统一数据类型
x = torch.tensor([1, 2, 3], dtype=torch.float32)
y = torch.tensor([1.0, 2.0, 3.0])
z = x + y
```

### 坑2：设备不匹配

```python
# 错误：一个在 CPU，一个在 GPU
x = torch.rand(3, 4).to("cuda")
y = torch.rand(3, 4)  # 在 CPU
# z = x + y  # 报错

# 正确：统一设备
x = torch.rand(3, 4).to("cuda")
y = torch.rand(3, 4).to("cuda")
z = x + y
```

### 坑3：梯度累积

```python
# 错误：梯度会累积
for i in range(10):
    y = model(x)
    loss = criterion(y, target)
    loss.backward()  # 梯度会累积

# 正确：每次清零梯度
for i in range(10):
    optimizer.zero_grad()  # 清零梯度
    y = model(x)
    loss = criterion(y, target)
    loss.backward()
    optimizer.step()
```

## 速查表

| 操作 | 代码 |
|------|------|
| 创建张量 | `torch.tensor([1, 2, 3])` |
| 全零张量 | `torch.zeros(3, 4)` |
| 随机张量 | `torch.rand(3, 4)` |
| 矩阵乘法 | `torch.mm(x, y)` 或 `x @ y` |
| 形状操作 | `x.reshape(4, 3)` |
| 移到 GPU | `x.to("cuda")` |
| 自动求导 | `x.backward()` |
| 获取梯度 | `x.grad` |

## 小测验

1. 深度学习和机器学习的区别？
2. PyTorch 中张量和 NumPy 数组的区别？
3. 什么是自动求导？
4. 如何使用 GPU 加速？
5. 为什么需要清零梯度？
