# Python 进阶一：装饰器

## 什么是装饰器？

装饰器是一个函数，它接收一个函数作为参数，返回一个新的函数。它可以在不修改原函数代码的情况下，给函数添加额外的功能。

类比理解：
- 装饰器 = 手机壳（不改变手机本身，但增加了保护功能）
- 装饰器 = 包装纸（不改变礼物本身，但增加了美观）

## 基本装饰器

```python
def my_decorator(func):
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# 调用
say_hello()
# 输出：
# 函数执行前
# Hello!
# 函数执行后
```

## 带参数的装饰器

```python
def repeat(n):
    def decorator(func):
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
```

## 常用装饰器

### 1. 日志装饰器

```python
import functools
import time

def log(func):
    @functools.wraps(func)  # 保留原函数的元信息
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
```

### 2. 计时装饰器

```python
import functools
import time

def timer(func):
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
    time.sleep(1)
    return "完成"

slow_function()
# 输出：slow_function 执行时间: 1.0012秒
```

### 3. 缓存装饰器

```python
import functools

def cache(func):
    cached_results = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cached_results:
            cached_results[args] = func(*args)
        return cached_results[args]
    
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))  # 快速计算
```

### 4. 权限检查装饰器

```python
import functools

def require_auth(func):
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
user = {"name": "Alice", "is_authenticated": True}
print(get_user_data(user))  # 正常

user = {"name": "Bob", "is_authenticated": False}
try:
    print(get_user_data(user))  # 抛出异常
except PermissionError as e:
    print(f"错误: {e}")
```

## 类装饰器

```python
class Timer:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"{self.func.__name__} 执行时间: {end - start:.4f}秒")
        return result

@Timer
def slow_function():
    time.sleep(1)
    return "完成"

slow_function()
```

## 多个装饰器叠加

```python
def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # <b><i>Hello, Alice!</i></b>
```

## 实际应用场景

### 1. 重试机制

```python
import functools
import time

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"第 {attempt + 1} 次尝试失败: {e}")
                    if attempt < max_attempts - 1:
                        time.sleep(delay)
            raise Exception(f"函数 {func.__name__} 在 {max_attempts} 次尝试后仍然失败")
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("随机错误")
    return "成功"
```

### 2. 参数验证

```python
import functools

def validate_types(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg, expected_type in zip(args, types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"参数 {arg} 应该是 {expected_type.__name__} 类型")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(int, int)
def add(a, b):
    return a + b

print(add(1, 2))      # 正常
try:
    print(add(1, "2"))  # 抛出异常
except TypeError as e:
    print(f"错误: {e}")
```

### 3. 单例模式

```python
import functools

def singleton(cls):
    instances = {}
    
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("创建数据库连接")

db1 = Database()  # 创建数据库连接
db2 = Database()  # 不会再次创建
print(db1 is db2)  # True
```

## 常见坑

### 坑1：忘记使用 functools.wraps

```python
# 错误：丢失原函数信息
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """问候函数"""
    return f"Hello, {name}!"

print(greet.__name__)   # wrapper（错误）
print(greet.__doc__)    # None（错误）

# 正确：使用 functools.wraps
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """问候函数"""
    return f"Hello, {name}!"

print(greet.__name__)   # greet（正确）
print(greet.__doc__)    # 问候函数（正确）
```

### 坑2：装饰器参数传递错误

```python
# 错误：忘记返回装饰器
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)  # 正确：repeat(3) 返回 decorator
def greet(name):
    print(f"Hello, {name}!")

# 错误写法
@repeat  # 错误：repeat 是装饰器工厂，不是装饰器
def greet(name):
    print(f"Hello, {name}!")
```

## 速查表

| 场景 | 代码 |
|------|------|
| 基本装饰器 | `@my_decorator` |
| 带参数装饰器 | `@decorator(arg)` |
| 保留元信息 | `@functools.wraps(func)` |
| 类装饰器 | `class Decorator: __call__` |
| 多装饰器叠加 | `@decorator1`<br>`@decorator2` |

## 小测验

1. 装饰器的作用是什么？
2. functools.wraps 的作用是什么？
3. 如何创建带参数的装饰器？
4. 多个装饰器叠加时，执行顺序是什么？
5. 举一个实际应用场景的装饰器例子？
