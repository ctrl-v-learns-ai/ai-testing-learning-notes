# Pandas 阶段一：基础数据结构

## 什么是 Pandas？
Pandas 是 Python 数据分析的核心库，提供 DataFrame 和 Series 两种数据结构。

类比理解：
- Series = Excel 的一列
- DataFrame = Excel 的一个表格

## 安装与导入
```python
pip install pandas
import pandas as pd
```

## Series（一维数据）

```python
# 从列表创建
s = pd.Series([1, 2, 3, 4, 5])
print(s)

# 指定索引
s = pd.Series([10, 20, 30], index=["a", "b", "c"])

# 从字典创建
s = pd.Series({"name": "Alice", "age": 25, "city": "Beijing"})

# 访问元素
s["name"]      # 通过标签
s.iloc[0]      # 通过位置

# Series 属性
s.index        # 索引
s.values       # 值
s.dtype        # 数据类型
s.shape        # 形状
```

## DataFrame（二维数据）

```python
# 从字典创建
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["Beijing", "Shanghai", "Guangzhou"]
}
df = pd.DataFrame(data)

# 从嵌套列表创建
data = [
    ["Alice", 25, "Beijing"],
    ["Bob", 30, "Shanghai"],
    ["Charlie", 35, "Guangzhou"]
]
df = pd.DataFrame(data, columns=["name", "age", "city"])

# DataFrame 属性
df.shape       # (3, 3) - 形状
df.columns     # 列名
df.index       # 索引
df.dtypes      # 数据类型
df.info()      # 摘要信息
df.describe()  # 统计摘要
```

## 数据读写

```python
# CSV
df = pd.read_csv("data.csv")
df.to_csv("output.csv", index=False)

# Excel
df = pd.read_excel("data.xlsx")
df.to_excel("output.xlsx", index=False)

# JSON
df = pd.read_json("data.json")
df.to_json("output.json")
```

## 基本操作

```python
# 查看数据
df.head()      # 前5行
df.tail()      # 后5行
df.sample(5)   # 随机5行

# 选择列
df["name"]           # 单列（Series）
df[["name", "age"]]  # 多列（DataFrame）

# 选择行
df.iloc[0]       # 第1行（位置）
df.iloc[0:3]     # 前3行
df.loc[0]        # 第1行（标签）

# 选择行列
df.iloc[0:2, 0:3]  # 前2行，前3列
df.loc[0:2, "name":"age"]  # 标签切片

# 添加列
df["salary"] = [5000, 6000, 7000]

# 删除列
df.drop("salary", axis=1, inplace=True)
```

## 常见坑

### 坑1：链式索引
```python
# 警告：链式索引可能出问题
df["name"][0] = "New"  # 可能有警告

# 正确：使用 loc
df.loc[0, "name"] = "New"
```

### 坑2：数据类型
```python
# CSV 读取后类型可能不对
df = pd.read_csv("data.csv")
df.dtypes  # 可能都是 object

# 需要转换
df["age"] = pd.to_numeric(df["age"])
```

### 坑3：索引重置
```python
# 筛选后索引不连续
filtered = df[df["age"] > 25]
filtered.index  # 可能是 [1, 2]

# 重置索引
filtered = filtered.reset_index(drop=True)
```

## 速查表

| 操作 | 代码 |
|------|------|
| 创建Series | `pd.Series([1,2,3])` |
| 创建DataFrame | `pd.DataFrame(data)` |
| 读CSV | `pd.read_csv("file.csv")` |
| 写CSV | `df.to_csv("file.csv")` |
| 查看前5行 | `df.head()` |
| 形状 | `df.shape` |
| 列名 | `df.columns` |
| 选择列 | `df["col"]` |
| 选择行 | `df.iloc[0]` |
| 统计摘要 | `df.describe()` |

## 小测验

1. Series 和 DataFrame 的区别？
2. iloc 和 loc 的区别？
3. 如何读取 CSV 文件？
4. 如何选择多列数据？
5. head() 和 tail() 的作用？
