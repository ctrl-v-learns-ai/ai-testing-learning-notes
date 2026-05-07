# -*- coding: utf-8 -*-
"""
练习3：上下文管理器基础
练习目标：掌握上下文管理器的原理和使用
前置知识：Python 类、with 语句
"""

from contextlib import contextmanager
import time
import os

# 练习3.1：文件上下文管理器
print("=== 练习3.1：文件上下文管理器 ===")

class FileManager:
    """文件管理器上下文管理器"""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"打开文件: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"关闭文件: {self.filename}")
        if self.file:
            self.file.close()
        return False

# 使用
with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")

print(f"文件内容: {open('test.txt').read()}")
os.remove("test.txt")

# 练习3.2：计时器上下文管理器
print("\n=== 练习3.2：计时器上下文管理器 ===")

@contextmanager
def timer(name):
    """计时器上下文管理器"""
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"{name} 耗时: {end - start:.4f}秒")

with timer("数据处理"):
    time.sleep(0.5)
    print("处理完成")

# 练习3.3：临时修改工作目录
print("\n=== 练习3.3：临时修改工作目录 ===")

@contextmanager
def change_directory(path):
    """临时修改工作目录"""
    old_dir = os.getcwd()
    print(f"切换到目录: {path}")
    os.chdir(path)
    try:
        yield
    finally:
        print(f"切换回目录: {old_dir}")
        os.chdir(old_dir)

print(f"当前目录: {os.getcwd()}")
with change_directory("/tmp"):
    print(f"临时目录: {os.getcwd()}")
print(f"恢复目录: {os.getcwd()}")

# 练习3.4：临时修改环境变量
print("\n=== 练习3.4：临时修改环境变量 ===")

@contextmanager
def set_env(key, value):
    """临时设置环境变量"""
    old_value = os.environ.get(key)
    os.environ[key] = value
    try:
        yield
    finally:
        if old_value is None:
            del os.environ[key]
        else:
            os.environ[key] = old_value

print(f"DEBUG: {os.environ.get('DEBUG')}")
with set_env("DEBUG", "true"):
    print(f"DEBUG: {os.environ.get('DEBUG')}")
print(f"DEBUG: {os.environ.get('DEBUG')}")

# 练习3.5：异常处理上下文管理器
print("\n=== 练习3.5：异常处理上下文管理器 ===")

@contextmanager
def ignore_errors(*error_types):
    """忽略指定类型的异常"""
    try:
        yield
    except error_types as e:
        print(f"忽略异常: {type(e).__name__}: {e}")

with ignore_errors(ValueError, TypeError):
    print("正常代码")
    raise ValueError("这是一个错误")
print("继续执行")

# 练习3.6：数据库连接模拟
print("\n=== 练习3.6：数据库连接模拟 ===")

@contextmanager
def database_connection(host, port, db_name):
    """数据库连接上下文管理器"""
    print(f"连接到数据库: {host}:{port}/{db_name}")
    connection = {
        "host": host,
        "port": port,
        "db_name": db_name,
        "connected": True
    }
    try:
        yield connection
    finally:
        print(f"关闭数据库连接: {host}:{port}/{db_name}")
        connection["connected"] = False

with database_connection("localhost", 5432, "mydb") as conn:
    print(f"执行查询，连接状态: {conn['connected']}")

"""
思考题：
1. __enter__ 和 __exit__ 的作用是什么？
2. @contextmanager 装饰器的作用是什么？
3. yield 在上下文管理器中的作用是什么？
4. __exit__ 返回 True 和 False 有什么区别？
5. 举一个实际应用场景的上下文管理器例子？
"""
