# Python 面试常见问题

## 基础概念

### 1. Python 数据类型

**问题：Python 有哪些常用数据类型？**

```python
# 不可变类型
int, float, str, tuple, frozenset

# 可变类型
list, dict, set

# 区别
a = [1, 2, 3]  # 列表，可变
b = (1, 2, 3)  # 元组，不可变
```

### 2. 列表推导式

**问题：什么是列表推导式？举例说明**

```python
# 列表推导式
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# 等价于
squares = []
for x in range(10):
    squares.append(x**2)
```

### 3. 装饰器

**问题：什么是装饰器？如何使用？**

```python
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
    print("Hello")
```

### 4. 生成器

**问题：生成器和列表的区别？**

```python
# 列表：一次性创建所有元素
my_list = [x**2 for x in range(1000000)]

# 生成器：惰性生成，节省内存
my_gen = (x**2 for x in range(1000000))

# 使用 next() 获取下一个值
print(next(my_gen))  # 0
print(next(my_gen))  # 1
```

### 5. GIL

**问题：什么是 GIL？它有什么影响？**

```python
# GIL (Global Interpreter Lock) 全局解释器锁
# - 同一时刻只能有一个线程执行 Python 字节码
# - 限制了多线程的并行执行
# - 对 I/O 密集型任务影响较小
# - 对 CPU 密集型任务影响较大

# 解决方案
# 1. 使用多进程（multiprocessing）
# 2. 使用 C 扩展
# 3. 使用其他 Python 实现（Jython, PyPy）
```

## 进阶概念

### 6. 深拷贝和浅拷贝

**问题：深拷贝和浅拷贝的区别？**

```python
import copy

# 浅拷贝
a = [[1, 2], [3, 4]]
b = copy.copy(a)
b[0][0] = 99  # a 也会被修改

# 深拷贝
c = copy.deepcopy(a)
c[0][0] = 100  # a 不会被修改
```

### 7. 上下文管理器

**问题：什么是上下文管理器？如何自定义？**

```python
# 使用 with 语句
with open("file.txt", "r") as f:
    content = f.read()

# 自定义上下文管理器
class MyContext:
    def __enter__(self):
        print("进入")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出")
        return False

with MyContext() as ctx:
    print("执行中")
```

### 8. 类型提示

**问题：Python 类型提示的作用？**

```python
# 类型提示
def greet(name: str) -> str:
    return f"Hello, {name}"

# 复合类型
from typing import List, Dict, Optional

def process(items: List[int]) -> Dict[str, int]:
    return {"sum": sum(items), "count": len(items)}

# 可选类型
def find(name: str) -> Optional[str]:
    if name in db:
        return db[name]
    return None
```

### 9. 异常处理

**问题：如何正确处理异常？**

```python
# 基本异常处理
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

# 自定义异常
class MyError(Exception):
    pass

def validate(value):
    if value < 0:
        raise MyError("值不能为负数")
```

### 10. 面向对象

**问题：Python 面向对象的特性？**

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "汪汪"

# 多态
animals = [Dog("小黑"), Dog("小白")]
for animal in animals:
    print(f"{animal.name}: {animal.speak()}")

# 类方法和静态方法
class MyClass:
    count = 0
    
    def __init__(self):
        MyClass.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @staticmethod
    def helper():
        return "辅助函数"
```

## 常见编程题

### 11. 反转字符串

```python
def reverse_string(s):
    return s[::-1]

# 或者
def reverse_string(s):
    return ''.join(reversed(s))
```

### 12. 判断回文

```python
def is_palindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]
```

### 13. 斐波那契数列

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 使用生成器
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

### 14. 排序算法

```python
# 快速排序
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```

## 面试技巧

1. **理解问题**：先确认问题的边界条件
2. **思路清晰**：先说出解题思路，再写代码
3. **代码规范**：使用有意义的变量名，添加注释
4. **测试用例**：写完代码后，用测试用例验证
5. **复杂度分析**：主动分析时间和空间复杂度

## 小测验

1. Python 中 `is` 和 `==` 的区别？
2. 什么是猴子补丁（Monkey Patching）？
3. 如何实现单例模式？
4. `*args` 和 `**kwargs` 的作用？
5. 如何优化 Python 代码性能？
