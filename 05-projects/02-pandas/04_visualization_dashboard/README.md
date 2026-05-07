# Pandas Project 04: 数据可视化仪表板

## 项目简介

一个完整的数据可视化仪表板，用于分析销售数据并生成多种图表。

## 功能特性

- 生成模拟销售数据（12个月、4个地区、5种产品）
- 时间趋势分析（折线图）
- 地区对比分析（柱状图）
- 产品占比分析（饼图）
- 价格分布分析（直方图 + 箱线图）
- 相关性分析（散点图 + 热力图）
- 图表美化和导出

## 运行方式

```bash
# 安装依赖
pip install -r requirements.txt

# 运行程序
python main.py
```

## 项目结构

```
04_visualization_dashboard/
├── main.py           # 主程序入口
├── data_generator.py # 生成模拟数据
├── charts.py         # 图表生成函数
├── requirements.txt  # 依赖包
└── README.md         # 项目说明
```

## 核心知识点

1. Matplotlib 子图布局
2. Pandas 数据分析 + 可视化
3. Seaborn 统计图表
4. 多图表组合
5. 图表美化和导出

## 输出文件

运行后会生成以下图表文件：

- `01_monthly_trend.png` - 月度销售趋势
- `02_region_comparison.png` - 地区销售对比
- `03_product_pie.png` - 产品销售占比
- `04_price_distribution.png` - 价格分布
- `05_correlation_scatter.png` - 相关性散点图
- `06_correlation_heatmap.png` - 相关性热力图
- `07_dashboard.png` - 综合仪表板
