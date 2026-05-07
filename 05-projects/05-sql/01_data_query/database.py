# -*- coding: utf-8 -*-
"""
数据库操作模块
提供 SQLite 数据库的增删改查功能
"""

import sqlite3
import pandas as pd
from typing import List, Dict, Optional, Tuple


class Database:
    """
    SQLite 数据库操作类
    
    使用示例:
        db = Database("test.db")
        db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
        db.execute("INSERT INTO users VALUES (1, 'Alice')")
        result = db.query("SELECT * FROM users")
    """
    
    def __init__(self, db_path: str = ":memory:"):
        """
        初始化数据库连接
        
        参数:
            db_path: 数据库文件路径，":memory:" 表示内存数据库
        """
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row  # 返回字典格式
        self.cursor = self.conn.cursor()
    
    def close(self):
        """关闭数据库连接"""
        if self.conn:
            self.conn.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    
    def execute(self, sql: str, params: Optional[Tuple] = None) -> sqlite3.Cursor:
        """
        执行 SQL 语句
        
        参数:
            sql: SQL 语句
            params: 参数
        
        返回:
            游标对象
        """
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor
    
    def executemany(self, sql: str, params_list: List[Tuple]) -> sqlite3.Cursor:
        """
        批量执行 SQL 语句
        
        参数:
            sql: SQL 语句
            params_list: 参数列表
        
        返回:
            游标对象
        """
        self.cursor.executemany(sql, params_list)
        self.conn.commit()
        return self.cursor
    
    def query(self, sql: str, params: Optional[Tuple] = None) -> List[Dict]:
        """
        执行查询并返回结果
        
        参数:
            sql: SQL 查询语句
            params: 参数
        
        返回:
            查询结果列表
        """
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        
        columns = [description[0] for description in self.cursor.description]
        results = []
        
        for row in self.cursor.fetchall():
            results.append(dict(zip(columns, row)))
        
        return results
    
    def query_to_dataframe(self, sql: str, params: Optional[Tuple] = None) -> pd.DataFrame:
        """
        执行查询并返回 DataFrame
        
        参数:
            sql: SQL 查询语句
            params: 参数
        
        返回:
            DataFrame
        """
        if params:
            return pd.read_sql_query(sql, self.conn, params=params)
        return pd.read_sql_query(sql, self.conn)
    
    def create_table(self, table_name: str, columns: Dict[str, str]) -> None:
        """
        创建表
        
        参数:
            table_name: 表名
            columns: 列定义字典 {"列名": "类型"}
        """
        columns_def = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})"
        self.execute(sql)
    
    def insert(self, table_name: str, data: Dict) -> None:
        """
        插入单条数据
        
        参数:
            table_name: 表名
            data: 数据字典
        """
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data])
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.execute(sql, tuple(data.values()))
    
    def insert_many(self, table_name: str, data_list: List[Dict]) -> None:
        """
        批量插入数据
        
        参数:
            table_name: 表名
            data_list: 数据字典列表
        """
        if not data_list:
            return
        
        columns = ", ".join(data_list[0].keys())
        placeholders = ", ".join(["?" for _ in data_list[0]])
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        params_list = [tuple(row.values()) for row in data_list]
        self.executemany(sql, params_list)
    
    def get_tables(self) -> List[str]:
        """获取所有表名"""
        result = self.query("SELECT name FROM sqlite_master WHERE type='table'")
        return [row["name"] for row in result]
    
    def get_table_info(self, table_name: str) -> List[Dict]:
        """获取表结构信息"""
        return self.query(f"PRAGMA table_info({table_name})")
    
    def table_to_dataframe(self, table_name: str) -> pd.DataFrame:
        """将表导出为 DataFrame"""
        return self.query_to_dataframe(f"SELECT * FROM {table_name}")
    
    def dataframe_to_table(self, df: pd.DataFrame, table_name: str, if_exists: str = "replace") -> None:
        """
        将 DataFrame 导入为表
        
        参数:
            df: DataFrame
            table_name: 表名
            if_exists: 如果表存在，处理方式 ("replace", "append", "fail")
        """
        df.to_sql(table_name, self.conn, if_exists=if_exists, index=False)
