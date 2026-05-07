# -*- coding: utf-8 -*-
"""
数据生成模块
生成模拟销售数据用于可视化分析
"""

import pandas as pd
import numpy as np


def generate_sales_data(num_months=12, num_records=1000):
    """
    生成模拟销售数据
    
    参数:
        num_months: 月份数量
        num_records: 数据记录数量
    
    返回:
        DataFrame: 包含销售数据的 DataFrame
    """
    np.random.seed(42)
    
    # 地区列表
    regions = ["华东", "华南", "华北", "西部"]
    
    # 产品类别
    products = ["电子产品", "服装", "食品", "日用品", "其他"]
    
    # 生成日期范围
    dates = pd.date_range("2024-01-01", periods=num_months, freq="M")
    
    # 生成数据
    data = {
        "日期": np.random.choice(dates, num_records),
        "地区": np.random.choice(regions, num_records),
        "产品类别": np.random.choice(products, num_records),
        "销售额": np.random.uniform(100, 1000, num_records),
        "成本": np.random.uniform(50, 500, num_records),
        "数量": np.random.randint(1, 50, num_records),
        "客户数": np.random.randint(10, 200, num_records)
    }
    
    df = pd.DataFrame(data)
    
    # 计算利润
    df["利润"] = df["销售额"] - df["成本"]
    
    # 计算利润率
    df["利润率"] = (df["利润"] / df["销售额"] * 100).round(2)
    
    # 按日期排序
    df = df.sort_values("日期").reset_index(drop=True)
    
    return df


def generate_monthly_summary(df):
    """
    生成月度汇总数据
    
    参数:
        df: 原始销售数据
    
    返回:
        DataFrame: 月度汇总数据
    """
    df["月份"] = df["日期"].dt.to_period("M")
    
    monthly = df.groupby("月份").agg({
        "销售额": "sum",
        "成本": "sum",
        "利润": "sum",
        "数量": "sum",
        "客户数": "sum"
    }).reset_index()
    
    monthly["月份"] = monthly["月份"].astype(str)
    
    return monthly


def generate_region_summary(df):
    """
    生成地区汇总数据
    
    参数:
        df: 原始销售数据
    
    返回:
        DataFrame: 地区汇总数据
    """
    region = df.groupby("地区").agg({
        "销售额": "sum",
        "成本": "sum",
        "利润": "sum",
        "数量": "sum",
        "客户数": "sum"
    }).reset_index()
    
    return region


def generate_product_summary(df):
    """
    生成产品汇总数据
    
    参数:
        df: 原始销售数据
    
    返回:
        DataFrame: 产品汇总数据
    """
    product = df.groupby("产品类别").agg({
        "销售额": "sum",
        "成本": "sum",
        "利润": "sum",
        "数量": "sum",
        "客户数": "sum"
    }).reset_index()
    
    return product


if __name__ == "__main__":
    # 测试数据生成
    df = generate_sales_data()
    print("原始数据形状:", df.shape)
    print("\n前5行数据:")
    print(df.head())
    
    print("\n月度汇总:")
    print(generate_monthly_summary(df).head())
    
    print("\n地区汇总:")
    print(generate_region_summary(df))
    
    print("\n产品汇总:")
    print(generate_product_summary(df))
