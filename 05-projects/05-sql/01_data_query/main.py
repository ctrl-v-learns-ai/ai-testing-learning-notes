# -*- coding: utf-8 -*-
"""
数据查询工具 - 主程序
演示数据库操作
"""

import pandas as pd
from database import Database


def main():
    """主函数"""
    print("=" * 50)
    print("  数据查询工具演示")
    print("=" * 50)
    
    # 创建内存数据库
    with Database(":memory:") as db:
        # 创建员工表
        db.create_table("employees", {
            "id": "INTEGER PRIMARY KEY",
            "name": "TEXT",
            "age": "INTEGER",
            "department": "TEXT",
            "salary": "REAL"
        })
        
        # 创建部门表
        db.create_table("departments", {
            "id": "INTEGER PRIMARY KEY",
            "name": "TEXT",
            "location": "TEXT"
        })
        
        # 插入部门数据
        departments = [
            {"id": 1, "name": "技术部", "location": "北京"},
            {"id": 2, "name": "市场部", "location": "上海"},
            {"id": 3, "name": "人事部", "location": "广州"},
        ]
        db.insert_many("departments", departments)
        
        # 插入员工数据
        employees = [
            {"id": 1, "name": "张三", "age": 25, "department": "技术部", "salary": 8000},
            {"id": 2, "name": "李四", "age": 30, "department": "市场部", "salary": 7000},
            {"id": 3, "name": "王五", "age": 28, "department": "技术部", "salary": 9000},
            {"id": 4, "name": "赵六", "age": 35, "department": "人事部", "salary": 7500},
            {"id": 5, "name": "钱七", "age": 22, "department": "技术部", "salary": 6500},
        ]
        db.insert_many("employees", employees)
        
        # 查询所有员工
        print("\n[查询1] 所有员工")
        result = db.query("SELECT * FROM employees")
        for row in result:
            print(f"  {row}")
        
        # 条件查询
        print("\n[查询2] 技术部员工")
        result = db.query("SELECT * FROM employees WHERE department = ?", ("技术部",))
        for row in result:
            print(f"  {row}")
        
        # 聚合查询
        print("\n[查询3] 各部门平均薪资")
        result = db.query("""
            SELECT department, 
                   COUNT(*) as count,
                   AVG(salary) as avg_salary,
                   MAX(salary) as max_salary,
                   MIN(salary) as min_salary
            FROM employees 
            GROUP BY department
        """)
        for row in result:
            print(f"  {row['department']}: 人数={row['count']}, "
                  f"平均薪资={row['avg_salary']:.2f}, "
                  f"最高={row['max_salary']}, "
                  f"最低={row['min_salary']}")
        
        # 排序查询
        print("\n[查询4] 按薪资降序排列")
        result = db.query("SELECT * FROM employees ORDER BY salary DESC")
        for row in result:
            print(f"  {row['name']}: {row['salary']}")
        
        # 连接查询
        print("\n[查询5] 员工和部门信息")
        result = db.query("""
            SELECT e.name, e.age, e.salary, d.location
            FROM employees e
            LEFT JOIN departments d ON e.department = d.name
        """)
        for row in result:
            print(f"  {row['name']}: 年龄={row['age']}, "
                  f"薪资={row['salary']}, 地点={row['location']}")
        
        # 导出为 DataFrame
        print("\n[查询6] 导出为 DataFrame")
        df = db.table_to_dataframe("employees")
        print(df)
        
        # 统计信息
        print("\n[查询7] 统计信息")
        print(f"  总人数: {len(df)}")
        print(f"  平均薪资: {df['salary'].mean():.2f}")
        print(f"  薪资标准差: {df['salary'].std():.2f}")


if __name__ == "__main__":
    main()
