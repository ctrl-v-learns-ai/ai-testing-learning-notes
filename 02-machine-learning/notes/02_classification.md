# 机器学习二：分类算法

## 什么是分类？

分类是预测离散类别的监督学习任务。

类比理解：
- 回归 = 预测具体数值（房价、温度）
- 分类 = 预测类别（垃圾邮件/正常邮件、猫/狗）

## 逻辑回归

### 原理

逻辑回归虽然名字有"回归"，但实际上是分类算法。

```python
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 生成数据
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=100, n_features=2, n_classes=2, random_state=42)

# 划分数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建模型
model = LogisticRegression()

# 训练
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 评估
print(f"准确率: {accuracy_score(y_test, y_pred):.4f}")
print(f"\n分类报告:\n{classification_report(y_test, y_pred)}")
```

## 决策树

### 原理

决策树通过一系列规则进行分类，像一棵树一样分支。

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# 创建模型
dt = DecisionTreeClassifier(max_depth=3, random_state=42)

# 训练
dt.fit(X_train, y_train)

# 预测
y_pred = dt.predict(X_test)

# 评估
print(f"准确率: {accuracy_score(y_test, y_pred):.4f}")

# 可视化
plt.figure(figsize=(12, 8))
tree.plot_tree(dt, filled=True, feature_names=["特征1", "特征2"])
plt.savefig("decision_tree.png", dpi=150)
plt.close()
```

## 随机森林

### 原理

随机森林是多个决策树的集成，通过投票决定最终分类。

```python
from sklearn.ensemble import RandomForestClassifier

# 创建模型
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# 训练
rf.fit(X_train, y_train)

# 预测
y_pred = rf.predict(X_test)

# 评估
print(f"准确率: {accuracy_score(y_test, y_pred):.4f}")

# 特征重要性
print(f"特征重要性: {rf.feature_importances_}")
```

## 支持向量机（SVM）

### 原理

SVM 找到一个超平面来最大化类别之间的间隔。

```python
from sklearn.svm import SVC

# 创建模型
svm = SVC(kernel='rbf', C=1.0, random_state=42)

# 训练
svm.fit(X_train, y_train)

# 预测
y_pred = svm.predict(X_test)

# 评估
print(f"准确率: {accuracy_score(y_test, y_pred):.4f}")
```

## K近邻（KNN）

### 原理

KNN 根据最近的 K 个邻居进行分类。

```python
from sklearn.neighbors import KNeighborsClassifier

# 创建模型
knn = KNeighborsClassifier(n_neighbors=5)

# 训练
knn.fit(X_train, y_train)

# 预测
y_pred = knn.predict(X_test)

# 评估
print(f"准确率: {accuracy_score(y_test, y_pred):.4f}")
```

## 模型评估

### 混淆矩阵

```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# 计算混淆矩阵
cm = confusion_matrix(y_test, y_pred)
print(f"混淆矩阵:\n{cm}")

# 可视化
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.savefig("confusion_matrix.png", dpi=150)
plt.close()
```

### 分类报告

```python
from sklearn.metrics import classification_report

# 生成分类报告
report = classification_report(y_test, y_pred, target_names=["类别0", "类别1"])
print(f"分类报告:\n{report}")
```

### ROC 曲线

```python
from sklearn.metrics import roc_curve, auc

# 获取概率
y_prob = model.predict_proba(X_test)[:, 1]

# 计算 ROC 曲线
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

# 绘制 ROC 曲线
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f}')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.savefig("roc_curve.png", dpi=150)
plt.close()
```

## 模型选择

### 网格搜索

```python
from sklearn.model_selection import GridSearchCV

# 定义参数网格
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10]
}

# 网格搜索
grid_search = GridSearchCV(RandomForestClassifier(random_state=42), 
                           param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

print(f"最佳参数: {grid_search.best_params_}")
print(f"最佳分数: {grid_search.best_score_:.4f}")

# 使用最佳模型
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
```

## 常见坑

### 坑1：类别不平衡

```python
# 问题：类别样本数量差异大
# 解决方案：
# 1. 过采样（SMOTE）
# 2. 欠采样
# 3. 调整类别权重

from sklearn.utils.class_weight import compute_class_weight

# 计算类别权重
weights = compute_class_weight('balanced', classes=np.unique(y), y=y)
print(f"类别权重: {weights}")
```

### 坑2：特征缩放

```python
# 某些算法需要特征缩放
# 需要缩放：SVM、KNN、逻辑回归
# 不需要缩放：决策树、随机森林
```

### 坑3：模型选择

```python
# 选择建议：
# - 数据量小：逻辑回归、KNN
# - 数据量大：随机森林、SVM
# - 需要解释性：决策树、逻辑回归
# - 追求准确率：随机森林、SVM
```

## 速查表

| 算法 | 代码 | 适用场景 |
|------|------|----------|
| 逻辑回归 | `LogisticRegression()` | 二分类、线性可分 |
| 决策树 | `DecisionTreeClassifier()` | 需要解释性 |
| 随机森林 | `RandomForestClassifier()` | 追求准确率 |
| SVM | `SVC()` | 小数据集、高维特征 |
| KNN | `KNeighborsClassifier()` | 小数据集、简单任务 |

## 小测验

1. 分类和回归的区别？
2. 混淆矩阵的四个值分别代表什么？
3. 精确率和召回率的区别？
4. 什么是过拟合？如何解决？
5. 如何选择合适的分类算法？
