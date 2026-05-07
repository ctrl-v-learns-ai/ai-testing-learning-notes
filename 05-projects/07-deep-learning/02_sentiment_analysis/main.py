# -*- coding: utf-8 -*-
"""
情感分析项目 - 主程序
演示使用 LSTM 进行情感分析
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


class LSTMModel(nn.Module):
    """LSTM 情感分析模型"""
    
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim, n_layers, dropout):
        super(LSTMModel, self).__init__()
        
        # 词嵌入层
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        
        # LSTM 层
        self.lstm = nn.LSTM(
            embedding_dim,
            hidden_dim,
            num_layers=n_layers,
            dropout=dropout,
            batch_first=True
        )
        
        # 全连接层
        self.fc = nn.Linear(hidden_dim, output_dim)
        
        # Dropout
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, x):
        # 词嵌入
        embedded = self.embedding(x)
        
        # LSTM
        output, (hidden, cell) = self.lstm(embedded)
        
        # 取最后一个时间步的输出
        hidden = self.dropout(hidden[-1])
        
        # 全连接层
        output = self.fc(hidden)
        
        return output


def generate_sample_data(num_samples=1000, max_length=50, vocab_size=1000):
    """生成模拟数据"""
    # 生成随机序列
    X = np.random.randint(0, vocab_size, (num_samples, max_length))
    
    # 生成标签（0=负面，1=正面）
    y = np.random.randint(0, 2, num_samples)
    
    # 转换为张量
    X = torch.LongTensor(X)
    y = torch.LongTensor(y)
    
    return X, y


def create_data_loader(X, y, batch_size=32):
    """创建数据加载器"""
    dataset = TensorDataset(X, y)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    return loader


def train(model, train_loader, criterion, optimizer, device, num_epochs=10):
    """训练模型"""
    model.train()
    train_losses = []
    train_accuracies = []
    
    for epoch in range(num_epochs):
        running_loss = 0.0
        correct = 0
        total = 0
        
        for batch_X, batch_y in train_loader:
            batch_X, batch_y = batch_X.to(device), batch_y.to(device)
            
            # 前向传播
            output = model(batch_X)
            loss = criterion(output, batch_y)
            
            # 反向传播
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()
            
            # 计算准确率
            _, predicted = torch.max(output, 1)
            total += batch_y.size(0)
            correct += (predicted == batch_y).sum().item()
        
        avg_loss = running_loss / len(train_loader)
        accuracy = 100 * correct / total
        
        train_losses.append(avg_loss)
        train_accuracies.append(accuracy)
        
        if (epoch + 1) % 2 == 0:
            print(f"Epoch {epoch+1}/{num_epochs}, Loss: {avg_loss:.4f}, Accuracy: {accuracy:.2f}%")
    
    return train_losses, train_accuracies


def evaluate(model, test_loader, criterion, device):
    """评估模型"""
    model.eval()
    test_loss = 0.0
    correct = 0
    total = 0
    
    with torch.no_grad():
        for batch_X, batch_y in test_loader:
            batch_X, batch_y = batch_X.to(device), batch_y.to(device)
            
            output = model(batch_X)
            loss = criterion(output, batch_y)
            
            test_loss += loss.item()
            
            _, predicted = torch.max(output, 1)
            total += batch_y.size(0)
            correct += (predicted == batch_y).sum().item()
    
    avg_loss = test_loss / len(test_loader)
    accuracy = 100 * correct / total
    
    return avg_loss, accuracy


def plot_results(train_losses, train_accuracies, test_losses, test_accuracies):
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
    axes[1].plot(train_accuracies, label='训练准确率', color='steelblue')
    axes[1].plot(test_accuracies, label='测试准确率', color='orange')
    axes[1].set_title('准确率曲线', fontsize=14)
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel('准确率 (%)')
    axes[1].legend()
    axes[1].grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('training_results.png', dpi=150)
    plt.close()
    print("已保存: training_results.png")


def main():
    """主函数"""
    print("=" * 60)
    print("  情感分析项目")
    print("=" * 60)
    
    # 检查设备
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"\n使用设备: {device}")
    
    # 1. 生成数据
    print("\n[1] 生成数据...")
    X_train, y_train = generate_sample_data(800, max_length=50, vocab_size=1000)
    X_test, y_test = generate_sample_data(200, max_length=50, vocab_size=1000)
    
    train_loader = create_data_loader(X_train, y_train, batch_size=32)
    test_loader = create_data_loader(X_test, y_test, batch_size=32)
    
    print(f"训练集大小: {len(X_train)}")
    print(f"测试集大小: {len(X_test)}")
    
    # 2. 创建模型
    print("\n[2] 创建模型...")
    model = LSTMModel(
        vocab_size=1000,
        embedding_dim=64,
        hidden_dim=128,
        output_dim=2,
        n_layers=2,
        dropout=0.5
    ).to(device)
    
    print(f"模型结构:\n{model}")
    
    # 3. 定义损失函数和优化器
    print("\n[3] 定义损失函数和优化器...")
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    # 4. 训练模型
    print("\n[4] 训练模型...")
    num_epochs = 10
    train_losses, train_accuracies = train(model, train_loader, criterion, optimizer, device, num_epochs)
    
    # 5. 评估模型
    print("\n[5] 评估模型...")
    test_loss, test_accuracy = evaluate(model, test_loader, criterion, device)
    print(f"测试损失: {test_loss:.4f}")
    print(f"测试准确率: {test_accuracy:.2f}%")
    
    # 6. 可视化
    print("\n[6] 可视化结果...")
    test_losses = [test_loss] * num_epochs
    test_accuracies = [test_accuracy] * num_epochs
    plot_results(train_losses, train_accuracies, test_losses, test_accuracies)
    
    # 7. 保存模型
    print("\n[7] 保存模型...")
    torch.save(model.state_dict(), "sentiment_lstm.pth")
    print("模型已保存: sentiment_lstm.pth")
    
    # 总结
    print("\n" + "=" * 60)
    print("  总结")
    print("=" * 60)
    print(f"\n测试准确率: {test_accuracy:.2f}%")
    print(f"模型参数数量: {sum(p.numel() for p in model.parameters()):,}")


if __name__ == "__main__":
    main()
