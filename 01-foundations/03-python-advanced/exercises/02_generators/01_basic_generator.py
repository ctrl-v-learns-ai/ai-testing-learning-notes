# -*- coding: utf-8 -*-
"""
练习2：生成器基础
练习目标：掌握生成器的原理和使用
前置知识：Python 函数、迭代器
"""

import sys
import time

# 练习2.1：基本生成器
print("=== 练习2.1：基本生成器 ===")

def count_up_to(n):
    """从1数到n的生成器"""
    i = 1
    while i <= n:
        yield i
        i += 1

# 使用生成器
counter = count_up_to(5)
print(f"第一个值: {next(counter)}")  # 1
print(f"第二个值: {next(counter)}")  # 2
print(f"第三个值: {next(counter)}")  # 3

# 使用 for 循环
print("\n使用 for 循环:")
for num in count_up_to(5):
    print(num, end=" ")
print()

# 练习2.2：生成器表达式
print("\n=== 练习2.2：生成器表达式 ===")

# 列表推导式
squares_list = [x**2 for x in range(1000)]
print(f"列表大小: {sys.getsizeof(squares_list)} bytes")

# 生成器表达式
squares_gen = (x**2 for x in range(1000))
print(f"生成器大小: {sys.getsizeof(squares_gen)} bytes")

# 练习2.3：斐波那契生成器
print("\n=== 练习2.3：斐波那契生成器 ===")

def fibonacci(n):
    """生成前n个斐波那契数"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("前10个斐波那契数:")
for num in fibonacci(10):
    print(num, end=" ")
print()

# 练习2.4：无限生成器
print("\n=== 练习2.4：无限生成器 ===")

def infinite_counter(start=0):
    """无限计数器"""
    current = start
    while True:
        yield current
        current += 1

# 使用 take 函数限制数量
def take(n, generator):
    """从生成器中取前n个值"""
    for _ in range(n):
        yield next(generator)

counter = infinite_counter(10)
print("从10开始的前5个数:")
for num in take(5, counter):
    print(num, end=" ")
print()

# 练习2.5：数据管道
print("\n=== 练习2.5：数据管道 ===")

def read_data():
    """读取数据"""
    for i in range(10):
        yield i

def filter_even(data):
    """过滤偶数"""
    for item in data:
        if item % 2 == 0:
            yield item

def multiply_by_two(data):
    """乘以2"""
    for item in data:
        yield item * 2

# 组合管道
pipeline = multiply_by_two(filter_even(read_data()))
print("数据管道结果:")
for result in pipeline:
    print(result, end=" ")
print()

# 练习2.6：yield from 语法
print("\n=== 练习2.6：yield from 语法 ===")

def chain(*iterables):
    """连接多个可迭代对象"""
    for iterable in iterables:
        yield from iterable

result = list(chain([1, 2], [3, 4], [5, 6]))
print(f"连接结果: {result}")

"""
思考题：
1. 生成器和列表的区别是什么？
2. yield 和 return 的区别是什么？
3. 生成器表达式和列表推导式的区别？
4. yield from 的作用是什么？
5. 生成器只能遍历一次，如何解决？
"""
