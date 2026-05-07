# -*- coding: utf-8 -*-
"""
房价预测项目 - 主程序
演示完整的机器学习流程
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


def generate_data(n_samples=500):
    """生成模拟房价数据"""
    np.random.seed(42)
    
    # 特征
    area = np.random.uniform(50, 200, n_samples)  # 面积
    bedrooms = np.random.randint(1, 6, n_samples)  # 卧室数
    age = np.random.uniform(0, 30, n_samples)  # 房龄
    distance = np.random.uniform(1, 20, n_samples)  # 距市中心距离
    
    # 生成房价（带噪声）
    price = (area * 2 + bedrooms * 50 - age * 2 - distance * 10 + 
             np.random.randn(n_samples) * 50 + 100)
    
    # 创建 DataFrame
    data = pd.DataFrame({
        '面积': area,
        '卧室数': bedrooms,
        '房龄': age,
        '距市中心距离': distance,
        '房价': price
    })
    
    return data


def preprocess_data(data):
    """数据预处理"""
    # 分离特征和目标
    X = data.drop('房价', axis=1)
    y = data['房价']
    
    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # 特征缩放
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


def train_models(X_train, y_train):
    """训练多个模型"""
    models = {
        '线性回归': LinearRegression(),
        'Ridge回归': Ridge(alpha=1.0),
        'Lasso回归': Lasso(alpha=1.0),
        '随机森林': RandomForestRegressor(n_estimators=100, random_state=42)
    }
    
    trained_models = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        trained_models[name] = model
        print(f"训练完成: {name}")
    
    return trained_models


def evaluate_models(models, X_test, y_test):
    """评估模型"""
    results = {}
    
    for name, model in models.items():
        y_pred = model.predict(X_test)
        
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        results[name] = {
            'MSE': mse,
            'RMSE': rmse,
            'MAE': mae,
            'R²': r2
        }
        
        print(f"\n{name}:")
        print(f"  MSE: {mse:.4f}")
        print(f"  RMSE: {rmse:.4f}")
        print(f"  MAE: {mae:.4f}")
        print(f"  R²: {r2:.4f}")
    
    return results


def cross_validate_models(models, X, y):
    """交叉验证"""
    print("\n[交叉验证结果]")
    
    for name, model in models.items():
        scores = cross_val_score(model, X, y, cv=5, scoring='r2')
        print(f"{name}: R² = {scores.mean():.4f} (+/- {scores.std() * 2:.4f})")


def plot_results(results, y_test, y_pred):
    """可视化结果"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # 模型对比
    model_names = list(results.keys())
    r2_scores = [results[name]['R²'] for name in model_names]
    
    bars = axes[0].bar(model_names, r2_scores, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
    axes[0].set_title('模型 R² 对比', fontsize=14)
    axes[0].set_ylabel('R²')
    axes[0].set_ylim(0, 1)
    
    # 在柱子上显示数值
    for bar, score in zip(bars, r2_scores):
        axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                     f'{score:.3f}', ha='center', fontsize=10)
    
    # 预测 vs 实际
    axes[1].scatter(y_test, y_pred, alpha=0.5, color='steelblue')
    axes[1].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 
                 'r--', linewidth=2, label='理想预测线')
    axes[1].set_title('预测值 vs 实际值', fontsize=14)
    axes[1].set_xlabel('实际值')
    axes[1].set_ylabel('预测值')
    axes[1].legend()
    
    plt.tight_layout()
    plt.savefig('prediction_results.png', dpi=150)
    plt.close()
    print("\n已保存: prediction_results.png")


def main():
    """主函数"""
    print("=" * 60)
    print("  房价预测项目")
    print("=" * 60)
    
    # 1. 生成数据
    print("\n[1] 生成数据...")
    data = generate_data(500)
    print(f"数据形状: {data.shape}")
    print(f"\n数据预览:")
    print(data.head())
    
    # 2. 数据预处理
    print("\n[2] 数据预处理...")
    X_train, X_test, y_train, y_test, scaler = preprocess_data(data)
    print(f"训练集大小: {X_train.shape[0]}")
    print(f"测试集大小: {X_test.shape[0]}")
    
    # 3. 训练模型
    print("\n[3] 训练模型...")
    models = train_models(X_train, y_train)
    
    # 4. 评估模型
    print("\n[4] 评估模型...")
    results = evaluate_models(models, X_test, y_test)
    
    # 5. 交叉验证
    print("\n[5] 交叉验证...")
    X = data.drop('房价', axis=1)
    y = data['房价']
    X_scaled = scaler.transform(X)
    cross_validate_models(models, X_scaled, y)
    
    # 6. 可视化
    print("\n[6] 可视化结果...")
    best_model_name = max(results, key=lambda x: results[x]['R²'])
    best_model = models[best_model_name]
    y_pred = best_model.predict(X_test)
    plot_results(results, y_test, y_pred)
    
    # 7. 总结
    print("\n" + "=" * 60)
    print("  总结")
    print("=" * 60)
    print(f"\n最佳模型: {best_model_name}")
    print(f"R²: {results[best_model_name]['R²']:.4f}")
    print(f"RMSE: {results[best_model_name]['RMSE']:.4f}")


if __name__ == "__main__":
    main()
