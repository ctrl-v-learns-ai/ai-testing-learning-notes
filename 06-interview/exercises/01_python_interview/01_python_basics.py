# -*- coding: utf-8 -*-
"""
练习19：Python 面试基础
练习目标：掌握 Python 面试常见问题
前置知识：Python 基础
"""

# 练习19.1：数据类型
print("=== 练习19.1：数据类型 ===")

# 不可变类型
a = 10          # int
b = 3.14        # float
c = "hello"     # str
d = (1, 2, 3)   # tuple

# 可变类型
e = [1, 2, 3]   # list
f = {"a": 1}    # dict
g = {1, 2, 3}   # set

print(f"int: {type(a)}")
print(f"list: {type(e)}")
print(f"dict: {type(f)}")

# 练习19.2：列表推导式
print("\n=== 练习19.2：列表推导式 ===")

# 基本列表推导式
squares = [x**2 for x in range(10)]
print(f"平方数: {squares}")

# 带条件的列表推导式
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"偶数平方: {even_squares}")

# 练习19.3：装饰器
print("\n=== 练习19.3：装饰器 ===")

import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("函数执行前")
        result = func(*args, **kwargs)
        print("函数执行后")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# 练习19.4：生成器
print("\n=== 练习19.4：生成器 ===")

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")
print()

# 练习19.5：深拷贝和浅拷贝
print("\n=== 练习19.5：深拷贝和浅拷贝 ===")

import copy

# 浅拷贝
a = [[1, 2], [3, 4]]
b = copy.copy(a)
b[0][0] = 99
print(f"浅拷贝 - a: {a}")  # a 也被修改

# 深拷贝
c = copy.deepcopy(a)
c[0][0] = 100
print(f"深拷贝 - a: {a}")  # a 不被修改

# 练习19.6：上下文管理器
print("\n=== 练习19.6：上下文管理器 ===")

class MyContext:
    def __enter__(self):
        print("进入上下文")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出上下文")
        return False

with MyContext() as ctx:
    print("执行中")

# 练习19.7：类型提示
print("\n=== 练习19.7：类型提示 ===")

from typing import List, Dict, Optional

def process(items: List[int]) -> Dict[str, int]:
    return {"sum": sum(items), "count": len(items)}

result = process([1, 2, 3, 4, 5])
print(f"结果: {result}")

# 练习19.8：异常处理
print("\n=== 练习19.8：异常处理 ===")

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"错误：{e}")
except Exception as e:
    print(f"未知错误：{e}")
else:
    print("没有异常")
finally:
    print("总是执行")

# 练习19.9：排序算法
print("\n=== 练习19.9：排序算法 ===")

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

arr = [3, 6, 8, 10, 1, 2, 1]
print(f"排序前: {arr}")
print(f"排序后: {quicksort(arr)}")

"""
思考题：
1. Python 中 is 和 == 的区别？
2. 什么是猴子补丁？
3. 如何实现单例模式？
4. *args 和 **kwargs 的作用？
5. 如何优化 Python 代码性能？
"""
