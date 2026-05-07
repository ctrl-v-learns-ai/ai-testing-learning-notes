# 机器学习面试常见问题

## 基础概念

### 1. 监督学习 vs 无监督学习

**问题：监督学习和无监督学习的区别？**

```
监督学习：
- 有标签数据
- 目标：预测未知数据的标签
- 例子：分类、回归

无监督学习：
- 无标签数据
- 目标：发现数据中的模式
- 例子：聚类、降维
```

### 2. 偏差-方差权衡

**问题：什么是偏差-方差权衡？**

```
偏差（Bias）：
- 模型预测值与真实值的差异
- 高偏差 = 欠拟合

方差（Variance）：
- 模型对训练数据变化的敏感度
- 高方差 = 过拟合

权衡：
- 简单模型：高偏差，低方差
- 复杂模型：低偏差，高方差
- 目标：找到平衡点
```

### 3. 过拟合和欠拟合

**问题：如何解决过拟合和欠拟合？**

```python
# 过拟合解决方案
# 1. 增加数据量
# 2. 正则化（L1, L2）
# 3. Dropout（神经网络）
# 4. 早停（Early Stopping）
# 5. 特征选择

# 欠拟合解决方案
# 1. 增加模型复杂度
# 2. 增加特征
# 3. 减少正则化
# 4. 训练更长时间
```

## 常见算法

### 4. 线性回归

**问题：线性回归的假设是什么？**

```
假设：
1. 线性关系：y = wx + b
2. 独立性：样本之间独立
3. 同方差性：误差方差恒定
4. 正态性：误差服从正态分布

评估指标：
- MSE（均方误差）
- RMSE（均方根误差）
- R²（决定系数）
```

### 5. 逻辑回归

**问题：逻辑回归和线性回归的区别？**

```
线性回归：
- 预测连续值
- 输出范围：(-∞, +∞)
- 损失函数：MSE

逻辑回归：
- 预测概率（分类）
- 输出范围：[0, 1]
- 损失函数：交叉熵
- 使用 Sigmoid 函数
```

### 6. 决策树

**问题：决策树如何选择分裂点？**

```
分裂标准：
1. 信息增益（ID3）
2. 信息增益比（C4.5）
3. 基尼系数（CART）

剪枝：
- 预剪枝：限制树的深度、最小样本数
- 后剪枝：先生成完整树，再剪枝
```

### 7. 随机森林

**问题：随机森林的原理？**

```
原理：
1. 从训练数据中有放回地抽样（Bagging）
2. 随机选择特征子集
3. 构建多棵决策树
4. 投票（分类）或平均（回归）得到最终结果

优点：
- 减少过拟合
- 处理高维数据
- 可以评估特征重要性
```

### 8. SVM

**问题：SVM 的核心思想？**

```
核心思想：
- 找到一个超平面，最大化分类间隔
- 使用核函数处理非线性问题

核函数：
- 线性核：K(x,y) = x·y
- 多项式核：K(x,y) = (x·y + c)^d
- RBF核：K(x,y) = exp(-γ||x-y||²)
```

## 评估指标

### 9. 分类指标

**问题：精确率和召回率的区别？**

```
混淆矩阵：
              预测正    预测负
实际正        TP        FN
实际负        FP        TN

精确率（Precision）= TP / (TP + FP)
- 预测为正的样本中，实际为正的比例

召回率（Recall）= TP / (TP + FN)
- 实际为正的样本中，被正确预测的比例

F1 分数 = 2 * Precision * Recall / (Precision + Recall)
- 精确率和召回率的调和平均
```

### 10. 回归指标

**问题：MSE、RMSE、MAE 的区别？**

```
MSE（均方误差）= Σ(y - ŷ)² / n
- 对异常值敏感

RMSE（均方根误差）= √MSE
- 与原始数据单位一致

MAE（平均绝对误差）= Σ|y - ŷ| / n
- 对异常值不敏感

R²（决定系数）= 1 - Σ(y - ŷ)² / Σ(y - ȳ)²
- 越接近 1 越好
```

## 特征工程

### 11. 特征缩放

**问题：为什么需要特征缩放？**

```python
# 标准化（StandardScaler）
# 均值为 0，标准差为 1
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 归一化（MinMaxScaler）
# 缩放到 [0, 1] 范围
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

# 适用场景：
# - 需要缩放：SVM、KNN、逻辑回归
# - 不需要缩放：决策树、随机森林
```

### 12. 缺失值处理

**问题：如何处理缺失值？**

```python
# 删除缺失值
df.dropna()

# 填充缺失值
df.fillna(df.mean())  # 均值填充
df.fillna(df.median())  # 中位数填充
df.fillna(df.mode()[0])  # 众数填充

# 使用模型预测
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=5)
X_imputed = imputer.fit_transform(X)
```

### 13. 特征选择

**问题：如何选择特征？**

```python
# 过滤法
from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(f_classif, k=10)
X_selected = selector.fit_transform(X, y)

# 包装法
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
selector = RFE(LogisticRegression(), n_features_to_select=10)
X_selected = selector.fit_transform(X, y)

# 嵌入法
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X, y)
importances = model.feature_importances_
```

## 模型选择

### 14. 交叉验证

**问题：什么是交叉验证？**

```python
from sklearn.model_selection import cross_val_score

# 5折交叉验证
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"平均准确率: {scores.mean():.4f} (+/- {scores.std() * 2:.4f})")

# 作用：
# 1. 评估模型泛化能力
# 2. 防止过拟合
# 3. 选择最佳模型
```

### 15. 网格搜索

**问题：如何调参？**

```python
from sklearn.model_selection import GridSearchCV

# 定义参数网格
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10]
}

# 网格搜索
grid_search = GridSearchCV(
    RandomForestClassifier(),
    param_grid,
    cv=5,
    scoring='accuracy'
)
grid_search.fit(X_train, y_train)

print(f"最佳参数: {grid_search.best_params_}")
print(f"最佳分数: {grid_search.best_score_:.4f}")
```

## 深度学习

### 16. 激活函数

**问题：常用激活函数有哪些？**

```
ReLU：
- f(x) = max(0, x)
- 优点：计算简单，缓解梯度消失
- 缺点：Dead ReLU

Sigmoid：
- f(x) = 1 / (1 + e^(-x))
- 优点：输出范围 [0, 1]
- 缺点：梯度消失

Tanh：
- f(x) = (e^x - e^(-x)) / (e^x + e^(-x))
- 优点：输出范围 [-1, 1]
- 缺点：梯度消失
```

### 17. 优化器

**问题：常用优化器有哪些？**

```
SGD：
- 随机梯度下降
- 学习率需要手动调整

Adam：
- 自适应学习率
- 结合动量和 RMSprop
- 通常效果最好

RMSprop：
- 自适应学习率
- 适合非平稳目标
```

## 面试技巧

1. **理解算法原理**：不只是会用，还要理解为什么
2. **知道适用场景**：什么情况下用什么算法
3. **掌握评估指标**：如何评估模型好坏
4. **实践经验**：能举出实际应用的例子
5. **最新进展**：了解最新的技术趋势

## 小测验

1. 什么是梯度消失？如何解决？
2. Batch Normalization 的作用？
3. Dropout 的原理？
4. 迁移学习是什么？
5. 如何处理类别不平衡？
