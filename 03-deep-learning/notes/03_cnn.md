# 深度学习三：卷积神经网络（CNN）

## 什么是 CNN？

CNN 是专门用于处理图像数据的神经网络，通过卷积操作提取图像特征。

类比理解：
- 全连接网络 = 把图像展平成一维，丢失了空间信息
- CNN = 保留图像的二维结构，用卷积核提取特征

## CNN 核心组件

### 卷积层（Convolutional Layer）

```python
import torch
import torch.nn as nn

# 2D 卷积
conv = nn.Conv2d(
    in_channels=3,      # 输入通道数（RGB=3）
    out_channels=16,    # 输出通道数（滤波器数量）
    kernel_size=3,      # 卷积核大小
    stride=1,           # 步长
    padding=1           # 填充
)

# 输入：(batch_size, channels, height, width)
x = torch.rand(1, 3, 32, 32)
output = conv(x)
print(output.shape)  # torch.Size([1, 16, 32, 32])
```

### 池化层（Pooling Layer）

```python
# 最大池化
max_pool = nn.Max2d(kernel_size=2, stride=2)
x = torch.rand(1, 16, 32, 32)
output = max_pool(x)
print(output.shape)  # torch.Size([1, 16, 16, 16])

# 平均池化
avg_pool = nn.AvgPool2d(kernel_size=2, stride=2)
```

### 批归一化（Batch Normalization）

```python
# 批归一化
bn = nn.BatchNorm2d(16)  # 通道数
x = torch.rand(1, 16, 32, 32)
output = bn(x)
```

### Dropout

```python
# Dropout（防止过拟合）
dropout = nn.Dropout(p=0.5)  # 50% 的概率丢弃
x = torch.rand(1, 16)
output = dropout(x)
```

## 经典 CNN 架构

### LeNet（入门级）

```python
class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        
        self.features = nn.Sequential(
            nn.Conv2d(1, 6, kernel_size=5),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(6, 16, kernel_size=5),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        
        self.classifier = nn.Sequential(
            nn.Linear(16 * 5 * 5, 120),
            nn.ReLU(),
            nn.Linear(120, 84),
            nn.ReLU(),
            nn.Linear(84, 10)
        )
    
    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)  # 展平
        x = self.classifier(x)
        return x

model = LeNet()
print(model)
```

### 图像分类示例

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# 数据预处理
transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# 加载 MNIST 数据集
train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# 创建模型
model = LeNet()

# 损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 训练
num_epochs = 5
for epoch in range(num_epochs):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        
        if batch_idx % 100 == 0:
            print(f"Epoch {epoch+1}, Batch {batch_idx}, Loss: {loss.item():.4f}")

# 评估
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for data, target in test_loader:
        output = model(data)
        _, predicted = torch.max(output, 1)
        total += target.size(0)
        correct += (predicted == target).sum().item()

print(f"准确率: {100 * correct / total:.2f}%")
```

## 迁移学习

### 使用预训练模型

```python
from torchvision import models

# 加载预训练的 ResNet
model = models.resnet18(pretrained=True)

# 冻结所有层
for param in model.parameters():
    param.requires_grad = False

# 替换最后一层
num_classes = 10
model.fc = nn.Linear(model.fc.in_features, num_classes)

# 只训练最后一层
optimizer = optim.Adam(model.fc.parameters(), lr=0.001)
```

## 常见坑

### 坑1：输入形状不匹配

```python
# 错误：输入形状不对
x = torch.rand(1, 32, 32)  # 缺少通道维度

# 正确：添加通道维度
x = torch.rand(1, 1, 32, 32)  # 灰度图
x = torch.rand(1, 3, 32, 32)  # RGB 图
```

### 坑2：忘记展平

```python
# 错误：卷积后直接接全连接层
x = conv(x)  # (batch, channels, height, width)
x = fc(x)    # 报错

# 正确：先展平
x = conv(x)
x = x.view(x.size(0), -1)  # 展平
x = fc(x)
```

### 坑3：GPU 内存不足

```python
# 解决方案：
# 1. 减小 batch_size
# 2. 使用更小的模型
# 3. 使用梯度累积
# 4. 使用混合精度训练
```

## 速查表

| 操作 | 代码 |
|------|------|
| 2D 卷积 | `nn.Conv2d(in_channels, out_channels, kernel_size)` |
| 最大池化 | `nn.MaxPool2d(kernel_size, stride)` |
| 批归一化 | `nn.BatchNorm2d(num_channels)` |
| Dropout | `nn.Dropout(p=0.5)` |
| 展平 | `x.view(x.size(0), -1)` |
| 迁移学习 | `models.resnet18(pretrained=True)` |

## 小测验

1. CNN 和全连接网络的区别？
2. 卷积层的作用是什么？
3. 池化层的作用是什么？
4. 什么是迁移学习？
5. 如何防止 CNN 过拟合？
