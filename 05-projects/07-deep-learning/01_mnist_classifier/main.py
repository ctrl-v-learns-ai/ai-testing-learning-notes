# -*- coding: utf-8 -*-
"""
MNIST 手写数字分类 - 主程序
演示完整的 CNN 训练流程
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


class CNN(nn.Module):
    """简单的 CNN 模型"""
    
    def __init__(self, num_classes=10):
        super(CNN, self).__init__()
        
        # 卷积层
        self.features = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        
        # 全连接层
        self.classifier = nn.Sequential(
            nn.Linear(64 * 7 * 7, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, num_classes)
        )
    
    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x


def load_data(batch_size=64):
    """加载 MNIST 数据集"""
    transform = transforms.Compose([
        transforms.Resize((28, 28)),
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    
    train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    return train_loader, test_loader


def train(model, train_loader, criterion, optimizer, device, num_epochs=5):
    """训练模型"""
    model.train()
    train_losses = []
    
    for epoch in range(num_epochs):
        running_loss = 0.0
        
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)
            
            # 前向传播
            output = model(data)
            loss = criterion(output, target)
            
            # 反向传播
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()
            
            if batch_idx % 100 == 0:
                print(f"Epoch {epoch+1}/{num_epochs}, Batch {batch_idx}/{len(train_loader)}, Loss: {loss.item():.4f}")
        
        avg_loss = running_loss / len(train_loader)
        train_losses.append(avg_loss)
        print(f"Epoch {epoch+1}/{num_epochs} 完成, 平均 Loss: {avg_loss:.4f}")
    
    return train_losses


def evaluate(model, test_loader, device):
    """评估模型"""
    model.eval()
    correct = 0
    total = 0
    test_losses = []
    criterion = nn.CrossEntropyLoss()
    
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            loss = criterion(output, target)
            test_losses.append(loss.item())
            
            _, predicted = torch.max(output, 1)
            total += target.size(0)
            correct += (predicted == target).sum().item()
    
    accuracy = 100 * correct / total
    avg_loss = sum(test_losses) / len(test_losses)
    
    return accuracy, avg_loss


def plot_results(train_losses, test_losses, accuracies):
    """可视化结果"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # 损失曲线
    axes[0].plot(train_losses, label='训练损失', color='steelblue')
    axes[0].plot(test_losses, label='测试损失', color='orange')
    axes[0].set_title('损失曲线', fontsize=14)
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('损失')
    axes[0].legend()
    axes[0].grid(True, linestyle='--', alpha=0.7)
    
    # 准确率曲线
    axes[1].plot(accuracies, label='测试准确率', color='green')
    axes[1].set_title('准确率曲线', fontsize=14)
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel('准确率 (%)')
    axes[1].legend()
    axes[1].grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('training_results.png', dpi=150)
    plt.close()
    print("已保存: training_results.png")


def visualize_predictions(model, test_loader, device, num_images=10):
    """可视化预测结果"""
    model.eval()
    
    with torch.no_grad():
        data, target = next(iter(test_loader))
        data, target = data.to(device), target.to(device)
        output = model(data)
        _, predicted = torch.max(output, 1)
        
        fig, axes = plt.subplots(2, 5, figsize=(12, 6))
        
        for i, ax in enumerate(axes.flat):
            if i < num_images:
                img = data[i].cpu().squeeze()
                ax.imshow(img, cmap='gray')
                ax.set_title(f'真实: {target[i].item()}\n预测: {predicted[i].item()}',
                            color='green' if target[i] == predicted[i] else 'red')
                ax.axis('off')
        
        plt.tight_layout()
        plt.savefig('predictions.png', dpi=150)
        plt.close()
        print("已保存: predictions.png")


def main():
    """主函数"""
    print("=" * 60)
    print("  MNIST 手写数字分类")
    print("=" * 60)
    
    # 检查设备
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"\n使用设备: {device}")
    
    # 1. 加载数据
    print("\n[1] 加载数据...")
    train_loader, test_loader = load_data(batch_size=64)
    print(f"训练集批次: {len(train_loader)}")
    print(f"测试集批次: {len(test_loader)}")
    
    # 2. 创建模型
    print("\n[2] 创建模型...")
    model = CNN(num_classes=10).to(device)
    print(f"模型结构:\n{model}")
    
    # 3. 定义损失函数和优化器
    print("\n[3] 定义损失函数和优化器...")
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    # 4. 训练模型
    print("\n[4] 训练模型...")
    num_epochs = 5
    train_losses = train(model, train_loader, criterion, optimizer, device, num_epochs)
    
    # 5. 评估模型
    print("\n[5] 评估模型...")
    accuracy, test_loss = evaluate(model, test_loader, device)
    print(f"测试准确率: {accuracy:.2f}%")
    print(f"测试损失: {test_loss:.4f}")
    
    # 6. 可视化
    print("\n[6] 可视化结果...")
    test_losses = [test_loss] * num_epochs
    accuracies = [accuracy] * num_epochs
    plot_results(train_losses, test_losses, accuracies)
    visualize_predictions(model, test_loader, device)
    
    # 7. 保存模型
    print("\n[7] 保存模型...")
    torch.save(model.state_dict(), "mnist_cnn.pth")
    print("模型已保存: mnist_cnn.pth")
    
    # 总结
    print("\n" + "=" * 60)
    print("  总结")
    print("=" * 60)
    print(f"\n测试准确率: {accuracy:.2f}%")
    print(f"模型参数数量: {sum(p.numel() for p in model.parameters()):,}")


if __name__ == "__main__":
    main()
