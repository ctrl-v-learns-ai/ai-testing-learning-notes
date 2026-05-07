# Pandas 阶段二：数据处理与清洗

## 缺失值处理

```python
import pandas as pd
import numpy as np

# 创建含缺失值的数据
df = pd.DataFrame({
    "A": [1, 2, np.nan, 4, 5],
    "B": [np.nan, 2, 3, np.nan, 5],
    "C": [1, 2, 3, 4, 5]
})

# 检测缺失值
df.isnull()          # 布尔矩阵
df.isnull().sum()    # 每列缺失数量
df.isnull().sum().sum()  # 总缺失数

# 删除缺失值
df.dropna()          # 删除有缺失的行
df.dropna(axis=1)    # 删除有缺失的列
df.dropna(subset=["A"])  # 只看A列

# 填充缺失值
df.fillna(0)         # 填充0
df.fillna(df.mean()) # 填充均值
df.fillna(method="ffill")  # 前向填充
df.fillna(method="bfill")  # 后向填充
```

## 数据筛选

```python
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 28],
    "salary": [5000, 6000, 7000, 5500]
})

# 条件筛选
df[df["age"] > 28]           # 年龄大于28
df[df["salary"] >= 6000]     # 薪资>=6000

# 多条件筛选
df[(df["age"] > 25) & (df["salary"] > 5500)]  # 且
df[(df["age"] < 25) | (df["salary"] > 6000)]  # 或

# isin 筛选
df[df["name"].isin(["Alice", "Bob"])]

# 字符串筛选
df[df["name"].str.startswith("A")]
df[df["name"].str.contains("li")]
```

## 排序

```python
# 单列排序
df.sort_values("age")                # 升序
df.sort_values("age", ascending=False)  # 降序

# 多列排序
df.sort_values(["age", "salary"], ascending=[True, False])

# 索引排序
df.sort_index()
```

## 类型转换

```python
# 转换类型
df["age"] = df["age"].astype(int)
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["date"] = pd.to_datetime(df["date"])

# 类型检查
df.dtypes
```

## 重复值处理

```python
# 检测重复
df.duplicated()              # 布尔 Series
df.duplicated().sum()        # 重复行数

# 删除重复
df.drop_duplicates()         # 删除完全重复的行
df.drop_duplicates(subset=["name"])  # 指定列去重
df.drop_duplicates(keep="last")      # 保留最后一个
```

## 字符串操作

```python
# 字符串方法
df["name"].str.lower()       # 小写
df["name"].str.upper()       # 大写
df["name"].str.strip()       # 去空格
df["name"].str.replace("a", "A")  # 替换
df["name"].str.split(" ")    # 分割
df["name"].str.len()         # 长度
```

## 常见坑

### 坑1：SettingWithCopyWarning
```python
# 警告：在切片上赋值
filtered = df[df["age"] > 25]
filtered["new_col"] = 1  # 警告！

# 正确：使用 loc
df.loc[df["age"] > 25, "new_col"] = 1
```

### 坑2：fillna 不原地修改
```python
# fillna 返回新 DataFrame
df_filled = df.fillna(0)  # df 不变

# 原地修改
df.fillna(0, inplace=True)
```

### 坑3：布尔索引括号
```python
# 错误：没有括号
df[df.age > 25 & df.salary > 5000]

# 正确：每个条件加括号
df[(df.age > 25) & (df.salary > 5000)]
```

## 速查表

| 操作 | 代码 |
|------|------|
| 检测缺失 | `df.isnull().sum()` |
| 删除缺失 | `df.dropna()` |
| 填充缺失 | `df.fillna(0)` |
| 条件筛选 | `df[df["col"] > 5]` |
| 多条件 | `df[(c1) & (c2)]` |
| 排序 | `df.sort_values("col")` |
| 去重 | `df.drop_duplicates()` |
| 类型转换 | `df["col"].astype(int)` |
| 字符串操作 | `df["col"].str.upper()` |

## 小测验

1. dropna 和 fillna 的区别？
2. 如何同时满足多个条件筛选？
3. SettingWithCopyWarning 怎么解决？
4. 如何检测和删除重复值？
5. str 方法可以做哪些字符串操作？
