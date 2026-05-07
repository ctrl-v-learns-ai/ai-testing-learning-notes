# Pandas 阶段三：数据分析与可视化

## 分组聚合 (GroupBy)

```python
import pandas as pd

df = pd.DataFrame({
    "dept": ["IT", "HR", "IT", "HR", "IT"],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "salary": [5000, 6000, 7000, 5500, 8000],
    "age": [25, 30, 35, 28, 32]
})

# 单列分组
df.groupby("dept")["salary"].mean()

# 多列分组
df.groupby("dept").agg({
    "salary": ["mean", "max", "min"],
    "age": "mean"
})

# 自定义聚合
df.groupby("dept").agg(
    avg_salary=("salary", "mean"),
    max_salary=("salary", "max"),
    count=("name", "count")
)

# 多个聚合函数
df.groupby("dept")["salary"].agg(["mean", "std", "count"])
```

## 透视表 (Pivot Table)

```python
# 创建透视表
pd.pivot_table(
    df,
    values="salary",
    index="dept",
    aggfunc=["mean", "sum", "count"]
)

# 多级透视表
pd.pivot_table(
    df,
    values="salary",
    index=["dept", "age"],
    aggfunc="mean"
)
```

## 数据合并

```python
# concat - 拼接
pd.concat([df1, df2])              # 垂直拼接
pd.concat([df1, df2], axis=1)      # 水平拼接

# merge - 关联合并（类似 SQL JOIN）
pd.merge(df1, df2, on="id")                    # 内连接
pd.merge(df1, df2, on="id", how="left")         # 左连接
pd.merge(df1, df2, on="id", how="right")        # 右连接
pd.merge(df1, df2, on="id", how="outer")        # 外连接
```

## 统计分析

```python
# 相关系数
df.corr()

# 协方差
df.cov()

# 频率统计
df["dept"].value_counts()

# 排名
df["rank"] = df["salary"].rank(ascending=False)
```

## 数据可视化（配合 Matplotlib）

```python
import matplotlib.pyplot as plt

# 折线图
df.plot(x="date", y="sales", kind="line")

# 柱状图
df.groupby("dept")["salary"].mean().plot(kind="bar")

# 直方图
df["salary"].plot(kind="hist", bins=10)

# 散点图
df.plot(x="age", y="salary", kind="scatter")

# 饼图
df["dept"].value_counts().plot(kind="pie")

# 保存图表
plt.savefig("chart.png")
```

## 常见坑

### 坑1：GroupBy 后索引
```python
# GroupBy 后分组列变成索引
result = df.groupby("dept")["salary"].mean()
result.index  # 是 dept

# 重置索引
result = df.groupby("dept")["salary"].mean().reset_index()
```

### 坑2：Merge 重复列名
```python
# 两个 DataFrame 有同名列
df1 = pd.DataFrame({"id": [1], "name": ["A"]})
df2 = pd.DataFrame({"id": [1], "name": ["B"]})

# merge 会自动加后缀
pd.merge(df1, df2, on="id")  # name_x, name_y

# 手动指定后缀
pd.merge(df1, df2, on="id", suffixes=("_left", "_right"))
```

### 坑3：聚合函数命名
```python
# 旧写法（可能有警告）
df.groupby("dept")["salary"].agg(["mean", "count"])

# 新写法（推荐）
df.groupby("dept").agg(
    avg_salary=("salary", "mean"),
    count=("salary", "count")
)
```

## 速查表

| 操作 | 代码 |
|------|------|
| 分组 | `df.groupby("col")` |
| 聚合 | `df.groupby("col").agg(...)` |
| 透视表 | `pd.pivot_table(df, ...)` |
| 垂直拼接 | `pd.concat([df1, df2])` |
| 合并 | `pd.merge(df1, df2, on="col")` |
| 相关系数 | `df.corr()` |
| 频率统计 | `df["col"].value_counts()` |
| 排名 | `df["col"].rank()` |

## 小测验

1. GroupBy 的原理是什么？
2. concat 和 merge 的区别？
3. 如何创建透视表？
4. value_counts 返回什么？
5. 如何计算两列的相关系数？
