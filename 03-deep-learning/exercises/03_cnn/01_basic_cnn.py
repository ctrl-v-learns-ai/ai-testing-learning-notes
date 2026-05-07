# -*- coding: utf-8 -*-
"""
练习13：卷积神经网络
练习目标：掌握 CNN 的构建和使用
前置知识：神经网络基础
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 练习13.1：定义 CNN
print("=== 练习13.1：定义 CNN ===")

class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10):
        super(SimpleCNN, self).__init__()
        
        # 卷积层
        self.features = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        
        # 全连接层
        self.classifier = nn.Sequential(
            nn.Linear(32 * 7 * 7, 128),
            nn.ReLU(),
            nn.Linear(128, num_classes)
        )
    
    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)  # 展平
        x = self.classifier(x)
        return x

model = SimpleCNN()
print(f"模型结构:\n{model}")

# 练习13.2：测试前向传播
print("\n=== 练习13.2：测试前向传播 ===")

# 创建测试输入
x = torch.rand(1, 1, 28, 28)  # (batch, channels, height, width)
output = model(x)
print(f"输入形状: {x.shape}")
print(f"输出形状: {output.shape}")

# 练习13.3：卷积层参数
print("\n=== 练习13.3：卷积层参数 ===")

conv = nn.Conv2d(1, 16, kernel_size=3, padding=1)
print(f"卷积层权重形状: {conv.weight.shape}")
print(f"卷积层偏置形状: {conv.bias.shape}")

# 练习13.4：池化层
print("\n=== 练习13.4：池化层 ===")

x = torch.rand(1, 16, 32, 32)
max_pool = nn.MaxPool2d(kernel_size=2, stride=2)
avg_pool = nn.AvgPool2d(kernel_size=2, stride=2)

print(f"输入形状: {x.shape}")
print(f"最大池化后: {max_pool(x).shape}")
print(f"平均池化后: {avg_pool(x).shape}")

# 练习13.5：加载 MNIST 数据集
print("\n=== 练习13.5：加载 MNIST 数据集 ===")

transform = transforms.Compose([
    transforms.Resize((28, 28)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

try:
    train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)
    
    print(f"训练集大小: {len(train_dataset)}")
    print(f"测试集大小: {len(test_dataset)}")
    print(f"训练批次数: {len(train_loader)}")
except Exception as e:
    print(f"数据集加载失败: {e}")
    print("跳过数据集加载练习")

# 练习13.6：训练 CNN（简化版）
print("\n=== 练习13.6：训练 CNN ===")

# 使用模拟数据
X_train = torch.rand(100, 1, 28, 28)
y_train = torch.randint(0, 10, (100,))

# 训练
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

model.train()
for epoch in range(5):
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 1 == 0:
        print(f"Epoch [{epoch+1}/5], Loss: {loss.item():.4f}")

# 练习13.7：评估模型
print("\n=== 练习13.7：评估模型 ===")

model.eval()
with torch.no_grad():
    outputs = model(X_train)
    _, predicted = torch.max(outputs, 1)
    accuracy = (predicted == y_train).sum().item() / y_train.size(0)
    print(f"训练准确率: {accuracy:.4f}")

"""
思考题：
1. CNN 和全连接网络的区别？
2. 卷积层的作用是什么？
3. 池化层的作用是什么？
4. 什么是迁移学习？
5. 如何防止 CNN 过拟合？
"""
