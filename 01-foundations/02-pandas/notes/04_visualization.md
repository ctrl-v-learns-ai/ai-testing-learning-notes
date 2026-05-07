# Pandas 阶段四：数据可视化

## Matplotlib 基础

### 图形创建和基本设置

```python
import matplotlib.pyplot as plt

# 创建图形
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
ax.plot(x, y)

# 显示图形
plt.show()
```

### 子图布局

```python
# 2x2 子图布局
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 在第一个子图绘图
axes[0, 0].plot([1, 2, 3], [1, 2, 3])
axes[0, 0].set_title("子图1")

# 在第二个子图绘图
axes[0, 1].bar(["A", "B", "C"], [10, 20, 15])
axes[0, 1].set_title("子图2")

# 调整布局
plt.tight_layout()
plt.show()
```

### 标题、标签、图例

```python
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, y, label="增长趋势")
ax.set_title("数据趋势图", fontsize=16)  # 标题
ax.set_xlabel("时间（天）", fontsize=12)  # X轴标签
ax.set_ylabel("数值", fontsize=12)        # Y轴标签
ax.legend(loc="upper left")               # 图例位置
ax.grid(True, linestyle="--", alpha=0.7)  # 网格线

plt.show()
```

### 颜色、线型、标记

```python
# 颜色：color="red" 或 color="#FF0000" 或 color="r"
# 线型：linestyle="-"（实线）、"--"（虚线）、"-."（点划线）、":"（点线）
# 标记：marker="o"（圆点）、"s"（方块）、"^"（三角）、"*"（星号）

ax.plot(x, y, color="red", linestyle="--", marker="o", markersize=8, label="系列1")
ax.plot(x, y2, color="blue", linestyle="-", marker="s", label="系列2")
```

---

## 常用图表类型

### 折线图（趋势分析）

适用场景：时间序列数据、趋势分析

```python
import pandas as pd
import matplotlib.pyplot as plt

# 创建数据
dates = pd.date_range("2024-01-01", periods=12, freq="M")
sales = [100, 120, 150, 130, 160, 180, 200, 190, 220, 250, 230, 280]

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(dates, sales, marker="o", color="steelblue", linewidth=2)
ax.set_title("月度销售趋势")
ax.set_xlabel("月份")
ax.set_ylabel("销售额（万元）")
ax.grid(True, linestyle="--", alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### 柱状图（对比分析）

适用场景：分类数据对比

```python
categories = ["电子产品", "服装", "食品", "日用品", "其他"]
values = [4500, 3200, 2800, 1500, 800]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(categories, values, color=["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"])

# 在柱子上方显示数值
for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50,
            f"{value}", ha="center", fontsize=10)

ax.set_title("各品类销售额对比")
ax.set_ylabel("销售额（万元）")
plt.show()
```

### 散点图（相关性分析）

适用场景：两个变量之间的关系

```python
import numpy as np

# 模拟广告投入与销售额的关系
np.random.seed(42)
advertising = np.random.uniform(10, 100, 50)
sales = advertising * 2.5 + np.random.normal(0, 20, 50)

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(advertising, sales, alpha=0.6, color="steelblue", edgecolors="white")

# 添加趋势线
z = np.polyfit(advertising, sales, 1)
p = np.poly1d(z)
ax.plot(sorted(advertising), p(sorted(advertising)), "r--", linewidth=2, label="趋势线")

ax.set_title("广告投入与销售额的关系")
ax.set_xlabel("广告投入（万元）")
ax.set_ylabel("销售额（万元）")
ax.legend()
plt.show()
```

### 饼图（占比分析）

适用场景：各部分占整体的比例

```python
categories = ["电子产品", "服装", "食品", "日用品", "其他"]
values = [4500, 3200, 2800, 1500, 800]
colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"]
explode = (0.05, 0, 0, 0, 0)  # 突出显示第一块

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    values, labels=categories, colors=colors, explode=explode,
    autopct="%1.1f%%", startangle=90, pctdistance=0.85
)

# 美化文字
for text in autotexts:
    text.set_color("white")
    text.set_fontweight("bold")

ax.set_title("各品类销售占比")
plt.show()
```

### 直方图（分布分析）

适用场景：数据分布情况

```python
np.random.seed(42)
scores = np.random.normal(75, 15, 200)  # 均值75，标准差15

fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(scores, bins=20, color="steelblue", edgecolor="white", alpha=0.7)

# 添加均值线
ax.axvline(scores.mean(), color="red", linestyle="--", linewidth=2, label=f"均值: {scores.mean():.1f}")

ax.set_title("考试成绩分布")
ax.set_xlabel("分数")
ax.set_ylabel("人数")
ax.legend()
plt.show()
```

### 箱线图（异常值检测）

适用场景：数据分布、异常值检测

```python
# 模拟不同地区的销售数据
data = {
    "华东": np.random.normal(200, 30, 100),
    "华南": np.random.normal(180, 40, 100),
    "华北": np.random.normal(220, 35, 100),
    "西部": np.random.normal(150, 50, 100)
}

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(data.values(), labels=data.keys(), patch_artist=True,
           boxprops=dict(facecolor="lightblue"))

ax.set_title("各地区销售数据分布")
ax.set_ylabel("销售额（万元）")
ax.grid(True, linestyle="--", alpha=0.7)
plt.show()
```

---

## Pandas 内置绘图

### df.plot() 基础用法

```python
import pandas as pd

# 创建数据
df = pd.DataFrame({
    "月份": ["1月", "2月", "3月", "4月", "5月", "6月"],
    "销售额": [100, 120, 150, 130, 160, 180],
    "成本": [80, 90, 110, 100, 120, 140]
})

# 折线图
df.plot(x="月份", y=["销售额", "成本"], kind="line", figsize=(10, 6))
plt.title("月度销售与成本趋势")
plt.ylabel("金额（万元）")
plt.show()

# 柱状图
df.plot(x="月份", y=["销售额", "成本"], kind="bar", figsize=(10, 6))
plt.title("月度销售与成本对比")
plt.ylabel("金额（万元）")
plt.show()
```

### 分组绘图

```python
# 创建数据
df = pd.DataFrame({
    "地区": ["华东", "华东", "华南", "华南", "华北", "华北"],
    "季度": ["Q1", "Q2", "Q1", "Q2", "Q1", "Q2"],
    "销售额": [200, 220, 180, 190, 250, 270]
})

# 分组柱状图
pivot_df = df.pivot(index="季度", columns="地区", values="销售额")
pivot_df.plot(kind="bar", figsize=(10, 6))
plt.title("各地区季度销售对比")
plt.ylabel("销售额（万元）")
plt.xticks(rotation=0)
plt.legend(title="地区")
plt.show()
```

---

## Seaborn 统计图表

### 分类图

```python
import seaborn as sns

# 创建数据
df = pd.DataFrame({
    "地区": np.repeat(["华东", "华南", "华北", "西部"], 50),
    "销售额": np.concatenate([
        np.random.normal(200, 30, 50),
        np.random.normal(180, 40, 50),
        np.random.normal(220, 35, 50),
        np.random.normal(150, 50, 50)
    ])
})

# 柱状图（带误差线）
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df, x="地区", y="销售额", ax=ax, palette="Set2")
ax.set_title("各地区平均销售额")
plt.show()

# 箱线图
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x="地区", y="销售额", ax=ax, palette="Set2")
ax.set_title("各地区销售数据分布")
plt.show()
```

### 关系图

```python
# 散点图（带分类颜色）
df = pd.DataFrame({
    "广告投入": np.random.uniform(10, 100, 100),
    "销售额": np.random.uniform(50, 300, 100),
    "地区": np.random.choice(["华东", "华南", "华北"], 100)
})

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x="广告投入", y="销售额", hue="地区", style="地区", s=100, ax=ax)
ax.set_title("广告投入与销售额的关系")
plt.show()
```

### 热力图

```python
# 创建相关性矩阵
df = pd.DataFrame({
    "销售额": [100, 120, 150, 130, 160],
    "成本": [80, 90, 110, 100, 120],
    "利润": [20, 30, 40, 30, 40],
    "广告": [10, 15, 20, 18, 25]
})

corr_matrix = df.corr()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", center=0,
            square=True, linewidths=1, ax=ax)
ax.set_title("变量相关性热力图")
plt.show()
```

---

## 图表美化和导出

### 主题和样式设置

```python
# 使用内置样式
plt.style.use("seaborn-v0_8")  # 推荐
# plt.style.use("ggplot")
# plt.style.use("bmh")

# 全局设置
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 中文显示
plt.rcParams["axes.unicode_minus"] = False     # 负号显示
plt.rcParams["figure.figsize"] = (10, 6)       # 默认图形大小
plt.rcParams["font.size"] = 12                 # 默认字体大小
```

### 保存图表

```python
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y)
ax.set_title("数据趋势图")

# 保存为 PNG
plt.savefig("chart.png", dpi=300, bbox_inches="tight")

# 保存为 PDF
plt.savefig("chart.pdf", bbox_inches="tight")

# 保存为 SVG
plt.savefig("chart.svg", bbox_inches="tight")
```

---

## 常见坑

### 坑1：中文显示乱码

```python
# 问题：中文显示为方块
# 解决：设置字体
plt.rcParams["font.sans-serif"] = ["SimHei"]  # Windows
# plt.rcParams["font.sans-serif"] = ["Arial Unicode Mac"]  # Mac
plt.rcParams["axes.unicode_minus"] = False
```

### 坑2：图表重叠

```python
# 问题：多个图表重叠在一起
# 解决：使用 tight_layout()
plt.tight_layout()

# 或者手动调整
plt.subplots_adjust(hspace=0.5, wspace=0.3)
```

### 坑3：颜色搭配

```python
# 问题：颜色搭配不美观
# 解决：使用 seaborn 调色板
sns.set_palette("Set2")  # 柔和色调
sns.set_palette("husl")  # 彩虹色调
sns.set_palette("muted") # 柔和色调

# 或者自定义颜色
colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"]
```

### 坑4：图例位置

```python
# 问题：图例遮挡数据
# 解决：调整图例位置
ax.legend(loc="upper right")   # 右上角
ax.legend(loc="lower left")    # 左下角
ax.legend(loc="center right")  # 右侧居中
ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")  # 图形外部
```

---

## 速查表

| 图表类型 | 适用场景 | Pandas 代码 | Matplotlib 代码 |
|----------|----------|-------------|-----------------|
| 折线图 | 趋势分析 | `df.plot(kind="line")` | `ax.plot(x, y)` |
| 柱状图 | 分类对比 | `df.plot(kind="bar")` | `ax.bar(x, y)` |
| 散点图 | 相关性 | `df.plot(kind="scatter")` | `ax.scatter(x, y)` |
| 饼图 | 占比 | `df.plot(kind="pie")` | `ax.pie(values)` |
| 直方图 | 分布 | `df.plot(kind="hist")` | `ax.hist(data)` |
| 箱线图 | 异常值 | `df.plot(kind="box")` | `ax.boxplot(data)` |

| Seaborn 图表 | 适用场景 | 代码 |
|--------------|----------|------|
| barplot | 分类对比（带误差线） | `sns.barplot(data=df, x="col1", y="col2")` |
| boxplot | 数据分布 | `sns.boxplot(data=df, x="col1", y="col2")` |
| scatterplot | 相关性（带分类） | `sns.scatterplot(data=df, x="col1", y="col2", hue="col3")` |
| heatmap | 相关性矩阵 | `sns.heatmap(df.corr(), annot=True)` |

---

## 小测验

1. 折线图和柱状图分别适合什么场景？
2. 如何解决中文乱码问题？
3. Pandas 的 df.plot() 和 Matplotlib 的 ax.plot() 有什么区别？
4. Seaborn 和 Matplotlib 的关系是什么？
5. 如何保存图表为图片文件？
