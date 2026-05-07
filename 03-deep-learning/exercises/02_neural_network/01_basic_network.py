# -*- coding: utf-8 -*-
"""
练习12：神经网络基础
练习目标：掌握 PyTorch 构建和训练神经网络
前置知识：PyTorch 基础
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# 练习12.1：定义简单网络
print("=== 练习12.1：定义简单网络 ===")

class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNet, self).__init__()
        
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

model = SimpleNet(10, 20, 2)
print(f"模型结构:\n{model}")

# 练习12.2：使用 Sequential
print("\n=== 练习12.2：使用 Sequential ===")

model_seq = nn.Sequential(
    nn.Linear(10, 20),
    nn.ReLU(),
    nn.Linear(20, 2)
)
print(f"Sequential 模型:\n{model_seq}")

# 练习12.3：准备数据
print("\n=== 练习12.3：准备数据 ===")

# 生成模拟数据
X = torch.rand(100, 10)
y = torch.randint(0, 2, (100,))

# 创建数据集和数据加载器
dataset = TensorDataset(X, y)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

print(f"数据集大小: {len(dataset)}")
print(f"批次数: {len(dataloader)}")

# 练习12.4：定义损失函数和优化器
print("\n=== 练习12.4：定义损失函数和优化器 ===")

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

print(f"损失函数: {criterion}")
print(f"优化器: {optimizer}")

# 练习12.5：训练循环
print("\n=== 练习12.5：训练循环 ===")

num_epochs = 10

for epoch in range(num_epochs):
    total_loss = 0
    
    for batch_X, batch_y in dataloader:
        # 前向传播
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)
        
        # 反向传播
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
    
    avg_loss = total_loss / len(dataloader)
    if (epoch + 1) % 2 == 0:
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {avg_loss:.4f}")

# 练习12.6：评估模型
print("\n=== 练习12.6：评估模型 ===")

model.eval()
with torch.no_grad():
    outputs = model(X)
    _, predicted = torch.max(outputs, 1)
    accuracy = (predicted == y).sum().item() / y.size(0)
    print(f"准确率: {accuracy:.4f}")

# 练习12.7：保存和加载模型
print("\n=== 练习12.7：保存和加载模型 ===")

# 保存模型
torch.save(model.state_dict(), "model.pth")
print("模型已保存: model.pth")

# 加载模型
loaded_model = SimpleNet(10, 20, 2)
loaded_model.load_state_dict(torch.load("model.pth"))
loaded_model.eval()
print("模型已加载")

"""
思考题：
1. 神经网络的结构是什么？
2. 激活函数的作用是什么？
3. 什么是前向传播和反向传播？
4. 如何选择学习率？
5. 如何防止过拟合？
"""
