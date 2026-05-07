# -*- coding: utf-8 -*-
"""
报表生成器模块
提供 SQL 查询和报表生成功能
"""

import sqlite3
import pandas as pd
from typing import List, Dict, Optional


class ReportGenerator:
    """
    报表生成器
    
    使用示例:
        generator = ReportGenerator(db_path)
        report = generator.generate_sales_report()
    """
    
    def __init__(self, db_path: str = ":memory:"):
        """
        初始化报表生成器
        
        参数:
            db_path: 数据库文件路径
        """
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
    
    def close(self):
        """关闭连接"""
        if self.conn:
            self.conn.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    
    def query(self, sql: str, params: Optional[tuple] = None) -> pd.DataFrame:
        """执行查询并返回 DataFrame"""
        if params:
            return pd.read_sql_query(sql, self.conn, params=params)
        return pd.read_sql_query(sql, self.conn)
    
    def generate_sales_summary(self) -> Dict:
        """
        生成销售汇总报表
        
        返回:
            报表数据字典
        """
        # 总销售额
        total_sales = self.query("SELECT SUM(amount) as total FROM sales")
        
        # 按产品统计
        by_product = self.query("""
            SELECT product_name,
                   COUNT(*) as order_count,
                   SUM(amount) as total_amount,
                   AVG(amount) as avg_amount
            FROM sales
            GROUP BY product_name
            ORDER BY total_amount DESC
        """)
        
        # 按地区统计
        by_region = self.query("""
            SELECT region,
                   COUNT(*) as order_count,
                   SUM(amount) as total_amount,
                   AVG(amount) as avg_amount
            FROM sales
            GROUP BY region
            ORDER BY total_amount DESC
        """)
        
        # 按月份统计
        by_month = self.query("""
            SELECT strftime('%Y-%m', sale_date) as month,
                   COUNT(*) as order_count,
                   SUM(amount) as total_amount
            FROM sales
            GROUP BY month
            ORDER BY month
        """)
        
        return {
            "总销售额": total_sales.iloc[0]["total"],
            "按产品统计": by_product,
            "按地区统计": by_region,
            "按月份统计": by_month,
        }
    
    def generate_employee_report(self) -> Dict:
        """
        生成员工报表
        
        返回:
            报表数据字典
        """
        # 员工统计
        employee_stats = self.query("""
            SELECT department,
                   COUNT(*) as employee_count,
                   AVG(salary) as avg_salary,
                   MAX(salary) as max_salary,
                   MIN(salary) as min_salary,
                   SUM(salary) as total_salary
            FROM employees
            GROUP BY department
            ORDER BY total_salary DESC
        """)
        
        # 薪资排名
        salary_ranking = self.query("""
            SELECT name, department, salary,
                   RANK() OVER (ORDER BY salary DESC) as rank
            FROM employees
            ORDER BY salary DESC
            LIMIT 10
        """)
        
        # 年龄分布
        age_distribution = self.query("""
            SELECT 
                CASE 
                    WHEN age < 25 THEN '25岁以下'
                    WHEN age BETWEEN 25 AND 30 THEN '25-30岁'
                    WHEN age BETWEEN 31 AND 35 THEN '31-35岁'
                    ELSE '35岁以上'
                END as age_group,
                COUNT(*) as count
            FROM employees
            GROUP BY age_group
        """)
        
        return {
            "部门统计": employee_stats,
            "薪资排名": salary_ranking,
            "年龄分布": age_distribution,
        }
    
    def format_table(self, df: pd.DataFrame, title: str) -> str:
        """
        格式化表格
        
        参数:
            df: DataFrame
            title: 标题
        
        返回:
            格式化的字符串
        """
        lines = [f"\n{'='*60}"]
        lines.append(f"  {title}")
        lines.append(f"{'='*60}")
        lines.append(df.to_string(index=False))
        lines.append(f"{'='*60}")
        return "\n".join(lines)
    
    def export_to_csv(self, df: pd.DataFrame, filename: str):
        """导出为 CSV 文件"""
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"已导出: {filename}")
    
    def export_to_excel(self, df: pd.DataFrame, filename: str, sheet_name: str = "Sheet1"):
        """导出为 Excel 文件"""
        df.to_excel(filename, index=False, sheet_name=sheet_name)
        print(f"已导出: {filename}")
