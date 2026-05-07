# Python 进阶三：上下文管理器

## 什么是上下文管理器？

上下文管理器是一种对象，它定义了在执行 with 语句时要运行的代码。主要用于资源管理，确保资源在使用后被正确释放。

类比理解：
- 上下文管理器 = 自动门（进入时自动打开，离开时自动关闭）
- 上下文管理器 = 图书馆借书（借书时登记，还书时注销）

## 基本用法：with 语句

```python
# 文件操作（最常用）
with open("file.txt", "r") as f:
    content = f.read()
# 文件自动关闭，即使发生异常

# 等价于
f = open("file.txt", "r")
try:
    content = f.read()
finally:
    f.close()
```

## 自定义上下文管理器

### 方式一：类实现（__enter__ 和 __exit__）

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """进入 with 语句时调用"""
        print(f"打开文件: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """离开 with 语句时调用"""
        print(f"关闭文件: {self.filename}")
        if self.file:
            self.file.close()
        # 返回 True 会抑制异常，返回 False 会传播异常
        return False

# 使用
with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")
# 输出：
# 打开文件: test.txt
# 关闭文件: test.txt
```

### 方式二：contextlib.contextmanager 装饰器

```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    """使用生成器实现上下文管理器"""
    print(f"打开文件: {filename}")
    f = open(filename, mode)
    try:
        yield f  # yield 的值会赋给 as 后面的变量
    finally:
        print(f"关闭文件: {filename}")
        f.close()

# 使用
with file_manager("test.txt", "w") as f:
    f.write("Hello, World!")
```

## 实际应用场景

### 1. 数据库连接

```python
from contextlib import contextmanager

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

# 使用
with database_connection("localhost", 5432, "mydb") as conn:
    print(f"执行查询，连接状态: {conn['connected']}")
# 输出：
# 连接到数据库: localhost:5432/mydb
# 执行查询，连接状态: True
# 关闭数据库连接: localhost:5432/mydb
```

### 2. 计时器

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(name):
    """计时器上下文管理器"""
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"{name} 耗时: {end - start:.4f}秒")

# 使用
with timer("数据处理"):
    time.sleep(1)
    print("处理完成")
# 输出：
# 处理完成
# 数据处理 耗时: 1.0012秒
```

### 3. 临时修改工作目录

```python
import os
from contextlib import contextmanager

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

# 使用
print(f"当前目录: {os.getcwd()}")
with change_directory("/tmp"):
    print(f"临时目录: {os.getcwd()}")
print(f"恢复目录: {os.getcwd()}")
```

### 4. 临时修改环境变量

```python
import os
from contextlib import contextmanager

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

# 使用
print(f"DEBUG: {os.environ.get('DEBUG')}")
with set_env("DEBUG", "true"):
    print(f"DEBUG: {os.environ.get('DEBUG')}")
print(f"DEBUG: {os.environ.get('DEBUG')}")
```

### 5. 异常处理

```python
from contextlib import contextmanager

@contextmanager
def ignore_errors(*error_types):
    """忽略指定类型的异常"""
    try:
        yield
    except error_types as e:
        print(f"忽略异常: {type(e).__name__}: {e}")

# 使用
with ignore_errors(ValueError, TypeError):
    print("正常代码")
    raise ValueError("这是一个错误")
print("继续执行")
# 输出：
# 正常代码
# 忽略异常: ValueError: 这是一个错误
# 继续执行
```

### 6. 资源池

```python
from contextlib import contextmanager
import threading

class ConnectionPool:
    def __init__(self, max_size=5):
        self.max_size = max_size
        self.connections = []
        self.lock = threading.Lock()
    
    @contextmanager
    def get_connection(self):
        """获取连接"""
        with self.lock:
            if self.connections:
                conn = self.connections.pop()
                print(f"复用连接，剩余: {len(self.connections)}")
            else:
                conn = {"id": id(self), "active": True}
                print(f"创建新连接")
        
        try:
            yield conn
        finally:
            with self.lock:
                self.connections.append(conn)
                print(f"归还连接，剩余: {len(self.connections)}")

# 使用
pool = ConnectionPool(max_size=3)

with pool.get_connection() as conn:
    print(f"使用连接: {conn}")

with pool.get_connection() as conn:
    print(f"使用连接: {conn}")
```

## __enter__ 和 __exit__ 详解

```python
class MyContextManager:
    def __enter__(self):
        """进入 with 语句时调用
        返回值会赋给 as 后面的变量
        """
        print("__enter__ 被调用")
        return self  # 通常返回 self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """离开 with 语句时调用
        
        参数：
        - exc_type: 异常类型（如果没有异常则为 None）
        - exc_val: 异常值（如果没有异常则为 None）
        - exc_tb: 异常追踪信息（如果没有异常则为 None）
        
        返回 True 会抑制异常，返回 False 会传播异常
        """
        print(f"__exit__ 被调用")
        print(f"异常类型: {exc_type}")
        print(f"异常值: {exc_val}")
        
        if exc_type is not None:
            print("发生异常，但被抑制")
            return True  # 抑制异常
        return False

# 没有异常
with MyContextManager() as cm:
    print("正常代码")
# 输出：
# __enter__ 被调用
# 正常代码
# __exit__ 被调用
# 异常类型: None

# 有异常
with MyContextManager() as cm:
    print("正常代码")
    raise ValueError("测试错误")
    print("这行不会执行")
# 输出：
# __enter__ 被调用
# 正常代码
# __exit__ 被调用
# 异常类型: <class 'ValueError'>
# 异常值: 测试错误
# 发生异常，但被抑制
```

## 多个上下文管理器

```python
from contextlib import contextmanager

@contextmanager
def manager_a():
    print("进入 A")
    try:
        yield "A"
    finally:
        print("离开 A")

@contextmanager
def manager_b():
    print("进入 B")
    try:
        yield "B"
    finally:
        print("离开 B")

# 嵌套使用
with manager_a() as a, manager_b() as b:
    print(f"使用 {a} 和 {b}")
# 输出：
# 进入 A
# 进入 B
# 使用 A 和 B
# 离开 B
# 离开 A

# 等价于
with manager_a() as a:
    with manager_b() as b:
        print(f"使用 {a} 和 {b}")
```

## 常见坑

### 坑1：忘记处理异常

```python
# 错误：异常会导致资源泄漏
class BadContextManager:
    def __enter__(self):
        self.resource = acquire_resource()
        return self.resource
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.resource.release()  # 如果 __enter__ 失败，这里会出错

# 正确：使用 try-finally
class GoodContextManager:
    def __enter__(self):
        self.resource = acquire_resource()
        return self.resource
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self, 'resource'):
            self.resource.release()
```

### 坑2：yield 和 return 的区别

```python
from contextlib import contextmanager

@contextmanager
def my_manager():
    print("进入")
    yield 42  # yield 的值会赋给 as 后面的变量
    print("离开")

with my_manager() as value:
    print(value)  # 42
```

### 坑3：__exit__ 返回值

```python
class SuppressErrors:
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return True  # 抑制所有异常

with SuppressErrors():
    raise ValueError("这个异常会被抑制")

print("继续执行")  # 会执行
```

## 速查表

| 操作 | 代码 |
|------|------|
| 类实现 | `class CM: __enter__, __exit__` |
| 生成器实现 | `@contextmanager` |
| 文件操作 | `with open("file") as f:` |
| 多个管理器 | `with a() as x, b() as y:` |
| 抑制异常 | `__exit__` 返回 `True` |

## 小测验

1. __enter__ 和 __exit__ 的作用是什么？
2. @contextmanager 装饰器的作用是什么？
3. yield 在上下文管理器中的作用是什么？
4. __exit__ 返回 True 和 False 有什么区别？
5. 举一个实际应用场景的上下文管理器例子？
