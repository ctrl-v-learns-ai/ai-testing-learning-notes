# -*- coding: utf-8 -*-
"""
数据可视化仪表板 - 主程序
生成模拟销售数据并创建多种图表
"""

import os
from data_generator import (
    generate_sales_data,
    generate_monthly_summary,
    generate_region_summary,
    generate_product_summary
)
from charts import (
    plot_monthly_trend,
    plot_region_comparison,
    plot_product_pie,
    plot_price_distribution,
    plot_correlation_scatter,
    plot_correlation_heatmap,
    create_dashboard
)


def main():
    """主函数"""
    print("=" * 60)
    print("  数据可视化仪表板")
    print("=" * 60)
    
    # 创建输出目录
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # 第1步：生成数据
    print("\n[第1步] 生成模拟销售数据...")
    df = generate_sales_data(num_months=12, num_records=1000)
    print(f"  数据形状: {df.shape}")
    print(f"  数据列: {list(df.columns)}")
    print(f"\n  前5行数据:")
    print(df.head())
    
    # 第2步：生成汇总数据
    print("\n[第2步] 生成汇总数据...")
    monthly_df = generate_monthly_summary(df)
    region_df = generate_region_summary(df)
    product_df = generate_product_summary(df)
    
    print(f"  月度汇总: {len(monthly_df)} 条记录")
    print(f"  地区汇总: {len(region_df)} 条记录")
    print(f"  产品汇总: {len(product_df)} 条记录")
    
    # 第3步：生成图表
    print("\n[第3步] 生成图表...")
    
    # 3.1 月度趋势图
    print("\n  3.1 月度趋势图")
    plot_monthly_trend(monthly_df, os.path.join(output_dir, "01_monthly_trend.png"))
    
    # 3.2 地区对比图
    print("  3.2 地区对比图")
    plot_region_comparison(region_df, os.path.join(output_dir, "02_region_comparison.png"))
    
    # 3.3 产品占比图
    print("  3.3 产品占比图")
    plot_product_pie(product_df, os.path.join(output_dir, "03_product_pie.png"))
    
    # 3.4 价格分布图
    print("  3.4 价格分布图")
    plot_price_distribution(df, os.path.join(output_dir, "04_price_distribution.png"))
    
    # 3.5 相关性散点图
    print("  3.5 相关性散点图")
    plot_correlation_scatter(df, os.path.join(output_dir, "05_correlation_scatter.png"))
    
    # 3.6 相关性热力图
    print("  3.6 相关性热力图")
    plot_correlation_heatmap(df, os.path.join(output_dir, "06_correlation_heatmap.png"))
    
    # 3.7 综合仪表板
    print("  3.7 综合仪表板")
    create_dashboard(df, monthly_df, region_df, product_df, 
                     os.path.join(output_dir, "07_dashboard.png"))
    
    # 第4步：显示统计信息
    print("\n[第4步] 数据统计信息...")
    print(f"\n  总销售额: {df['销售额'].sum():,.2f} 万元")
    print(f"  总成本: {df['成本'].sum():,.2f} 万元")
    print(f"  总利润: {df['利润'].sum():,.2f} 万元")
    print(f"  平均利润率: {df['利润率'].mean():.2f}%")
    
    print(f"\n  销售额最高的地区: {region_df.loc[region_df['销售额'].idxmax(), '地区']}")
    print(f"  销售额最高的产品: {product_df.loc[product_df['销售额'].idxmax(), '产品类别']}")
    
    # 第5步：显示文件列表
    print("\n[第5步] 生成的图表文件:")
    for file in sorted(os.listdir(output_dir)):
        if file.endswith(".png"):
            print(f"  - {os.path.join(output_dir, file)}")
    
    print("\n" + "=" * 60)
    print("  可视化仪表板生成完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
