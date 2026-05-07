# -*- coding: utf-8 -*-
"""
数据分析工具 - 主程序
演示数据分析器的使用
"""

import numpy as np
import pandas as pd
from analyzer import DataAnalyzer


def main():
    """主函数"""
    print("=" * 50)
    print("  数据分析工具演示")
    print("=" * 50)
    
    # 生成模拟数据
    np.random.seed(42)
    data = pd.DataFrame({
        "销售额": np.random.normal(1000, 200, 100),
        "成本": np.random.normal(600, 100, 100),
        "利润": np.random.normal(400, 150, 100),
        "数量": np.random.randint(10, 100, 100),
    })
    
    # 添加一些异常值
    data.loc[95, "销售额"] = 2000
    data.loc[96, "成本"] = 1000
    data.loc[97, "利润"] = -100
    
    print("\n数据预览:")
    print(data.head())
    
    # 创建分析器
    analyzer = DataAnalyzer(data)
    
    # 打印报告
    analyzer.print_report()
    
    # 单独调用各功能
    print("\n" + "=" * 60)
    print("  单独功能演示")
    print("=" * 60)
    
    # 描述性统计
    print("\n[描述性统计]")
    stats = analyzer.descriptive_stats()
    for col, col_stats in stats.items():
        print(f"\n{col}:")
        print(f"  均值: {col_stats['mean']:.2f}")
        print(f"  中位数: {col_stats['median']:.2f}")
        print(f"  标准差: {col_stats['std']:.2f}")
    
    # 异常值检测
    print("\n[异常值检测 - IQR 方法]")
    outliers = analyzer.detect_outliers(method="iqr")
    for col, info in outliers.items():
        if info["outlier_count"] > 0:
            print(f"{col}: {info['outlier_count']} 个异常值")
    
    # 相关性分析
    print("\n[相关性分析]")
    corr = analyzer.correlation_analysis()
    print(corr.round(4))


if __name__ == "__main__":
    main()
