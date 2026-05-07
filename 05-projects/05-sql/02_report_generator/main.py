# -*- coding: utf-8 -*-
"""
报表生成器 - 主程序
演示报表生成
"""

import numpy as np
import pandas as pd
from report import ReportGenerator


def create_sample_data(conn):
    """创建示例数据"""
    cursor = conn.cursor()
    
    # 创建销售表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            product_name TEXT,
            region TEXT,
            salesperson TEXT,
            amount REAL,
            sale_date TEXT
        )
    """)
    
    # 创建员工表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            department TEXT,
            salary REAL
        )
    """)
    
    # 插入销售数据
    np.random.seed(42)
    products = ["笔记本电脑", "手机", "平板电脑", "显示器", "键盘"]
    regions = ["华东", "华南", "华北", "西部"]
    salespersons = ["张三", "李四", "王五", "赵六", "钱七"]
    
    sales_data = []
    for i in range(100):
        sales_data.append((
            i + 1,
            np.random.choice(products),
            np.random.choice(regions),
            np.random.choice(salespersons),
            np.random.uniform(500, 5000),
            f"2024-{np.random.randint(1, 13):02d}-{np.random.randint(1, 29):02d}"
        ))
    
    cursor.executemany(
        "INSERT INTO sales (id, product_name, region, salesperson, amount, sale_date) VALUES (?, ?, ?, ?, ?, ?)",
        sales_data
    )
    
    # 插入员工数据
    employees_data = [
        (1, "张三", 25, "技术部", 8000),
        (2, "李四", 30, "市场部", 7000),
        (3, "王五", 28, "技术部", 9000),
        (4, "赵六", 35, "人事部", 7500),
        (5, "钱七", 22, "技术部", 6500),
        (6, "孙八", 29, "市场部", 7200),
        (7, "周九", 32, "技术部", 9500),
        (8, "吴十", 27, "人事部", 6800),
        (9, "郑十一", 24, "技术部", 7200),
        (10, "王十二", 31, "市场部", 8500),
    ]
    
    cursor.executemany(
        "INSERT INTO employees (id, name, age, department, salary) VALUES (?, ?, ?, ?, ?)",
        employees_data
    )
    
    conn.commit()


def main():
    """主函数"""
    print("=" * 50)
    print("  报表生成器演示")
    print("=" * 50)
    
    with ReportGenerator(":memory:") as generator:
        # 创建示例数据
        create_sample_data(generator.conn)
        
        # 生成销售汇总报表
        print("\n[销售汇总报表]")
        sales_report = generator.generate_sales_summary()
        
        print(f"\n总销售额: {sales_report['总销售额']:,.2f}")
        
        print(generator.format_table(sales_report['按产品统计'], "按产品统计"))
        print(generator.format_table(sales_report['按地区统计'], "按地区统计"))
        print(generator.format_table(sales_report['按月份统计'], "按月份统计"))
        
        # 生成员工报表
        print("\n[员工报表]")
        employee_report = generator.generate_employee_report()
        
        print(generator.format_table(employee_report['部门统计'], "部门统计"))
        print(generator.format_table(employee_report['薪资排名'], "薪资排名 Top 10"))
        print(generator.format_table(employee_report['年龄分布'], "年龄分布"))


if __name__ == "__main__":
    main()
