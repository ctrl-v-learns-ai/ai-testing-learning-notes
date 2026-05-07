# 深度学习二：神经网络基础

## 什么是神经网络？

神经网络是一种模仿人脑结构的计算模型，由多层神经元组成。

类比理解：
- 神经网络 = 多层决策系统
- 每一层 = 一个特征提取器
- 整个网络 = 一个复杂的函数

## 神经网络结构

```
输入层 → 隐藏层1 → 隐藏层2 → ... → 输出层
```

### 激活函数

```python
import torch
import torch.nn as nn

# ReLU（最常用）
relu = nn.ReLU()
x = torch.tensor([-1.0, 0.0, 1.0, 2.0])
print(relu(x))  # tensor([0., 0., 1., 2.])

# Sigmoid（二分类输出层）
sigmoid = nn.Sigmoid()
print(sigmoid(x))  # tensor([0.2689, 0.5000, 0.7311, 0.8808])

# Tanh
tanh = nn.Tanh()
print(tanh(x))  # tensor([-0.7616, 0.0000, 0.7616, 0.9640])

# Softmax（多分类输出层）
softmax = nn.Softmax(dim=0)
x = torch.tensor([1.0, 2.0, 3.0])
print(softmax(x))  # tensor([0.0900, 0.2447, 0.6652])
```

## PyTorch 构建神经网络

### 定义网络

```python
import torch
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNet, self).__init__()
        
        # 定义层
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        # 前向传播
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# 创建模型
model = SimpleNet(input_size=10, hidden_size=20, output_size=2)
print(model)
```

### 使用 Sequential

```python
# 更简洁的写法
model = nn.Sequential(
    nn.Linear(10, 20),
    nn.ReLU(),
    nn.Linear(20, 2)
)
```

## 训练流程

### 1. 准备数据

```python
from torch.utils.data import DataLoader, TensorDataset

# 创建数据集
X = torch.rand(100, 10)
y = torch.randint(0, 2, (100,))
dataset = TensorDataset(X, y)

# 创建数据加载器
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
```

### 2. 定义损失函数和优化器

```python
# 损失函数
criterion = nn.CrossEntropyLoss()  # 分类
criterion = nn.MSELoss()           # 回归

# 优化器
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
```

### 3. 训练循环

```python
# 训练
num_epochs = 100

for epoch in range(num_epochs):
    for batch_X, batch_y in dataloader:
        # 前向传播
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)
        
        # 反向传播
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    # 打印进度
    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")
```

### 4. 评估模型

```python
# 评估模式
model.eval()

with torch.no_grad():
    outputs = model(X_test)
    _, predicted = torch.max(outputs, 1)
    accuracy = (predicted == y_test).sum().item() / y_test.size(0)
    print(f"准确率: {accuracy:.4f}")
```

## 保存和加载模型

```python
# 保存模型
torch.save(model.state_dict(), "model.pth")

# 加载模型
model = SimpleNet(10, 20, 2)
model.load_state_dict(torch.load("model.pth"))
model.eval()
```

## 常见坑

### 坑1：忘记 model.train() 和 model.eval()

```python
# 训练时
model.train()
for batch_X, batch_y in dataloader:
    # 训练代码
    pass

# 评估时
model.eval()
with torch.no_grad():
    # 评估代码
    pass
```

### 坑2：学习率设置不当

```python
# 学习率太大：loss 震荡不收敛
optimizer = torch.optim.Adam(model.parameters(), lr=1.0)

# 学习率太小：收敛太慢
optimizer = torch.optim.Adam(model.parameters(), lr=0.0000001)

# 合适的学习率
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
```

### 坑3：过拟合

```python
# 解决方案：
# 1. 增加数据量
# 2. 使用正则化（Dropout, L2）
# 3. 早停（Early Stopping）
# 4. 数据增强
```

## 速查表

| 操作 | 代码 |
|------|------|
| 定义网络 | `class Net(nn.Module)` |
| 线性层 | `nn.Linear(in, out)` |
| 激活函数 | `nn.ReLU()`, `nn.Sigmoid()` |
| 损失函数 | `nn.CrossEntropyLoss()` |
| 优化器 | `torch.optim.Adam()` |
| 前向传播 | `output = model(input)` |
| 反向传播 | `loss.backward()` |
| 保存模型 | `torch.save(model.state_dict())` |

## 小测验

1. 神经网络的结构是什么？
2. 激活函数的作用是什么？
3. 什么是前向传播和反向传播？
4. 如何选择学习率？
5. 如何防止过拟合？
