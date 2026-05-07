# 机器学习一：线性回归

## 什么是机器学习？

机器学习是让计算机从数据中学习规律，而不需要显式编程的方法。

类比理解：
- 传统编程 = 你告诉计算机规则，计算机按规则执行
- 机器学习 = 你给计算机数据和结果，计算机自己找规则

## 机器学习分类

| 类型 | 说明 | 例子 |
|------|------|------|
| 监督学习 | 有标签数据 | 预测房价、分类邮件 |
| 无监督学习 | 无标签数据 | 聚类、降维 |
| 强化学习 | 通过奖励学习 | 游戏AI、机器人 |

## 线性回归

### 什么是线性回归？

线性回归是最简单的监督学习算法，用于预测连续值。

公式：y = wx + b

类比理解：
- 线性回归 = 找一条最拟合数据的直线

### Scikit-learn 使用

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 生成数据
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 2 * X.squeeze() + 3 + np.random.randn(100) * 2

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建模型
model = LinearRegression()

# 训练模型
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 评估
print(f"斜率: {model.coef_[0]:.4f}")
print(f"截距: {model.intercept_:.4f}")
print(f"MSE: {mean_squared_error(y_test, y_pred):.4f}")
print(f"R²: {r2_score(y_test, y_pred):.4f}")
```

### 模型评估指标

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# MSE（均方误差）
mse = mean_squared_error(y_test, y_pred)

# RMSE（均方根误差）
rmse = np.sqrt(mse)

# MAE（平均绝对误差）
mae = mean_absolute_error(y_test, y_pred)

# R²（决定系数）
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R²: {r2:.4f}")
```

### 多元线性回归

```python
import numpy as np
from sklearn.linear_model import LinearRegression

# 多个特征
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([5, 7, 9, 11, 13])

model = LinearRegression()
model.fit(X, y)

print(f"系数: {model.coef_}")
print(f"截距: {model.intercept_}")

# 预测
new_X = np.array([[6, 7]])
prediction = model.predict(new_X)
print(f"预测值: {prediction[0]}")
```

### 正则化

```python
from sklearn.linear_model import Ridge, Lasso

# Ridge 回归（L2 正则化）
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)

# Lasso 回归（L1 正则化）
lasso = Lasso(alpha=1.0)
lasso.fit(X_train, y_train)

# 比较系数
print(f"线性回归系数: {model.coef_}")
print(f"Ridge 系数: {ridge.coef_}")
print(f"Lasso 系数: {lasso.coef_}")
```

### 特征缩放

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# 标准化（均值为0，标准差为1）
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 归一化（缩放到0-1之间）
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)
```

### 交叉验证

```python
from sklearn.model_selection import cross_val_score

# 5折交叉验证
scores = cross_val_score(model, X, y, cv=5, scoring='r2')
print(f"交叉验证 R²: {scores.mean():.4f} (+/- {scores.std() * 2:.4f})")
```

## 常见坑

### 坑1：数据泄露

```python
# 错误：先标准化再划分数据
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # 用了全部数据
X_train, X_test = train_test_split(X_scaled, ...)

# 正确：先划分再标准化
X_train, X_test = train_test_split(X, ...)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # 用训练集的参数
```

### 坑2：过拟合

```python
# 过拟合：训练集表现好，测试集表现差
# 解决方案：
# 1. 增加数据量
# 2. 使用正则化
# 3. 减少特征
# 4. 使用交叉验证
```

### 坑3：特征工程

```python
# 错误：直接使用原始特征
# 正确：进行特征工程
# - 处理缺失值
# - 编码分类变量
# - 特征缩放
# - 特征选择
```

## 速查表

| 操作 | 代码 |
|------|------|
| 创建模型 | `model = LinearRegression()` |
| 训练 | `model.fit(X_train, y_train)` |
| 预测 | `model.predict(X_test)` |
| 评估 | `r2_score(y_test, y_pred)` |
| 交叉验证 | `cross_val_score(model, X, y, cv=5)` |
| 特征缩放 | `StandardScaler().fit_transform(X)` |

## 小测验

1. 线性回归的公式是什么？
2. MSE、RMSE、MAE、R² 的区别？
3. 什么是正则化？Ridge 和 Lasso 的区别？
4. 什么是数据泄露？如何避免？
5. 什么是过拟合？如何解决？
