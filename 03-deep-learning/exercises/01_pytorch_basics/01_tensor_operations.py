# -*- coding: utf-8 -*-
"""
练习11：PyTorch 基础
练习目标：掌握 PyTorch 张量操作和自动求导
前置知识：NumPy
"""

import torch
import numpy as np

# 练习11.1：创建张量
print("=== 练习11.1：创建张量 ===")

# 从列表创建
x = torch.tensor([1, 2, 3, 4, 5])
print(f"从列表创建: {x}")

# 创建特殊张量
zeros = torch.zeros(3, 4)
ones = torch.ones(3, 4)
rand = torch.rand(3, 4)
eye = torch.eye(3)

print(f"全零张量:\n{zeros}")
print(f"全一张量:\n{ones}")
print(f"随机张量:\n{rand}")
print(f"单位矩阵:\n{eye}")

# 从 NumPy 创建
np_array = np.array([1, 2, 3])
tensor = torch.from_numpy(np_array)
print(f"从 NumPy 创建: {tensor}")

# 练习11.2：张量属性
print("\n=== 练习11.2：张量属性 ===")

x = torch.rand(3, 4)
print(f"形状: {x.shape}")
print(f"数据类型: {x.dtype}")
print(f"设备: {x.device}")
print(f"维度: {x.dim()}")

# 练习11.3：张量操作
print("\n=== 练习11.3：张量操作 ===")

# 基本运算
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

print(f"加法: {x + y}")
print(f"乘法: {x * y}")
print(f"矩阵乘法: {torch.mm(x.reshape(1, 3), y.reshape(3, 1))}")

# 形状操作
x = torch.rand(3, 4)
print(f"原始形状: {x.shape}")
print(f"转置形状: {x.t().shape}")
print(f"展平形状: {x.view(-1).shape}")
print(f"重塑形状: {x.reshape(4, 3).shape}")

# 练习11.4：索引和切片
print("\n=== 练习11.4：索引和切片 ===")

x = torch.rand(3, 4)
print(f"张量:\n{x}")
print(f"第一行: {x[0, :]}")
print(f"第一列: {x[:, 0]}")
print(f"子矩阵:\n{x[0:2, 0:2]}")

# 练习11.5：自动求导
print("\n=== 练习11.5：自动求导 ===")

x = torch.tensor([2.0], requires_grad=True)
y = x ** 2 + 3 * x + 1

# 反向传播
y.backward()

print(f"x = {x.item()}")
print(f"y = x^2 + 3x + 1 = {y.item()}")
print(f"dy/dx = 2x + 3 = {x.grad.item()}")

# 练习11.6：GPU 加速
print("\n=== 练习11.6：GPU 加速 ===")

print(f"CUDA 可用: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    device = torch.device("cuda")
    x = torch.rand(3, 4).to(device)
    print(f"张量设备: {x.device}")
else:
    print("CUDA 不可用，使用 CPU")

"""
思考题：
1. PyTorch 中张量和 NumPy 数组的区别？
2. 什么是自动求导？
3. 如何使用 GPU 加速？
4. requires_grad 参数的作用是什么？
5. view 和 reshape 的区别？
"""
