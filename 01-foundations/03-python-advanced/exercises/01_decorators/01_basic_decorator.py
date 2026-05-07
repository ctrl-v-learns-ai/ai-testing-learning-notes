# -*- coding: utf-8 -*-
"""
练习1：装饰器基础
练习目标：掌握装饰器的基本原理和使用
前置知识：Python 函数基础
"""

import functools
import time

# 练习1.1：基本装饰器
print("=== 练习1.1：基本装饰器 ===")

def my_decorator(func):
    """简单装饰器：在函数执行前后打印信息"""
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# 输出：
# 函数执行前
# Hello!
# 函数执行后

# 练习1.2：带参数的装饰器
print("\n=== 练习1.2：带参数的装饰器 ===")

def repeat(n):
    """重复执行 n 次的装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# 输出：
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!

# 练习1.3：日志装饰器
print("\n=== 练习1.3：日志装饰器 ===")

def log(func):
    """记录函数调用信息的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        print(f"参数: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"返回值: {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

add(1, 2)
# 输出：
# 调用函数: add
# 参数: args=(1, 2), kwargs={}
# 返回值: 3

# 练习1.4：计时装饰器
print("\n=== 练习1.4：计时装饰器 ===")

def timer(func):
    """记录函数执行时间的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行时间: {end - start:.4f}秒")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.5)
    return "完成"

result = slow_function()
# 输出：slow_function 执行时间: 0.5012秒

# 练习1.5：权限检查装饰器
print("\n=== 练习1.5：权限检查装饰器 ===")

def require_auth(func):
    """检查用户是否登录的装饰器"""
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("is_authenticated"):
            raise PermissionError("用户未登录")
        return func(user, *args, **kwargs)
    return wrapper

@require_auth
def get_user_data(user):
    return f"用户数据: {user['name']}"

# 测试
user1 = {"name": "Alice", "is_authenticated": True}
print(get_user_data(user1))  # 正常

user2 = {"name": "Bob", "is_authenticated": False}
try:
    print(get_user_data(user2))  # 抛出异常
except PermissionError as e:
    print(f"错误: {e}")

"""
思考题：
1. functools.wraps 的作用是什么？
2. 带参数的装饰器和普通装饰器有什么区别？
3. *args 和 **kwargs 在装饰器中的作用是什么？
4. 如何实现一个缓存装饰器？
5. 多个装饰器叠加时，执行顺序是什么？
"""
