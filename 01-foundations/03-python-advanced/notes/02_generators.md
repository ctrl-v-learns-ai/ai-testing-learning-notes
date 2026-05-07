# Python 进阶二：生成器

## 什么是生成器？

生成器是一种特殊的迭代器，它使用 yield 关键字来产生值，而不是 return。生成器可以暂停和恢复执行，节省内存。

类比理解：
- 列表 = 一次性把所有书买回家（占用空间）
- 生成器 = 去图书馆借一本看一本（节省空间）

## 基本生成器

```python
def count_up_to(n):
    """从1数到n的生成器"""
    i = 1
    while i <= n:
        yield i  # 暂停执行，返回值
        i += 1

# 使用生成器
counter = count_up_to(5)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3

# 使用 for 循环
for num in count_up_to(5):
    print(num)  # 1, 2, 3, 4, 5
```

## 生成器表达式

```python
# 列表推导式（占用内存）
squares_list = [x**2 for x in range(1000000)]

# 生成器表达式（节省内存）
squares_gen = (x**2 for x in range(1000000))

# 内存对比
import sys
print(sys.getsizeof(squares_list))  # 约 8MB
print(sys.getsizeof(squares_gen))   # 约 200字节
```

## 生成器的工作原理

```python
def simple_generator():
    print("第一次 yield")
    yield 1
    print("第二次 yield")
    yield 2
    print("第三次 yield")
    yield 3

gen = simple_generator()

print("开始调用")
print(next(gen))  # 输出：第一次 yield，返回 1
print("继续执行")
print(next(gen))  # 输出：第二次 yield，返回 2
print("继续执行")
print(next(gen))  # 输出：第三次 yield，返回 3
```

## 实际应用场景

### 1. 读取大文件

```python
def read_large_file(file_path):
    """逐行读取大文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

# 使用
for line in read_large_file("huge_file.txt"):
    process(line)  # 每次只处理一行，不会占用大量内存
```

### 2. 无限序列

```python
def fibonacci():
    """无限斐波那契数列"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 使用
fib = fibonacci()
for _ in range(10):
    print(next(fib))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

### 3. 数据管道

```python
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
for result in pipeline:
    print(result)  # 0, 4, 8, 12, 16
```

### 4. 分页处理

```python
def paginate(data, page_size=10):
    """分页生成器"""
    for i in range(0, len(data), page_size):
        yield data[i:i + page_size]

# 使用
data = list(range(100))
for page in paginate(data, page_size=10):
    print(f"处理页面: {page[:3]}...")  # 处理每页数据
```

## 生成器方法

### send() 方法

```python
def accumulator():
    """累加器生成器"""
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)           # 启动生成器
print(acc.send(10)) # 10
print(acc.send(20)) # 30
print(acc.send(30)) # 60
```

### throw() 方法

```python
def my_generator():
    try:
        yield 1
        yield 2
        yield 3
    except ValueError:
        print("捕获到 ValueError")
        yield "错误处理后的值"

gen = my_generator()
print(next(gen))  # 1
print(gen.throw(ValueError))  # 捕获到 ValueError，返回 "错误处理后的值"
```

### close() 方法

```python
def my_generator():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("生成器被关闭")

gen = my_generator()
print(next(gen))  # 1
gen.close()       # 输出：生成器被关闭
```

## yield from 语法

```python
def chain(*iterables):
    """连接多个可迭代对象"""
    for iterable in iterables:
        yield from iterable

# 使用
result = list(chain([1, 2], [3, 4], [5, 6]))
print(result)  # [1, 2, 3, 4, 5, 6]
```

## 生成器与迭代器的区别

```python
# 迭代器
class Counter:
    def __init__(self, n):
        self.n = n
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        self.current += 1
        return self.current

# 生成器（更简洁）
def counter(n):
    current = 0
    while current < n:
        current += 1
        yield current

# 两者功能相同，但生成器更简洁
```

## 常见坑

### 坑1：生成器只能遍历一次

```python
gen = (x for x in range(5))

# 第一次遍历
for x in gen:
    print(x)  # 0, 1, 2, 3, 4

# 第二次遍历（没有输出）
for x in gen:
    print(x)  # 空！

# 解决：重新创建生成器
gen = (x for x in range(5))
```

### 坑2：生成器中的 return

```python
def my_generator():
    yield 1
    yield 2
    return "结束"  # return 的值会作为 StopIteration 的参数
    yield 3  # 不会执行

gen = my_generator()
print(next(gen))  # 1
print(next(gen))  # 2
try:
    print(next(gen))  # 抛出 StopIteration: 结束
except StopIteration as e:
    print(f"生成器结束: {e.value}")
```

### 坑3：生成器的惰性求值

```python
def expensive_function(x):
    print(f"计算 {x}")
    return x * 2

# 列表推导式（立即执行）
results = [expensive_function(x) for x in range(5)]
# 输出：计算 0, 计算 1, 计算 2, 计算 3, 计算 4

# 生成器表达式（惰性执行）
results = (expensive_function(x) for x in range(5))
# 没有输出！

# 需要遍历时才执行
for r in results:
    print(r)
```

## 性能对比

```python
import sys
import time

# 列表方式
def get_squares_list(n):
    return [x**2 for x in range(n)]

# 生成器方式
def get_squares_gen(n):
    return (x**2 for x in range(n))

n = 1000000

# 内存对比
list_squares = get_squares_list(n)
gen_squares = get_squares_gen(n)

print(f"列表内存: {sys.getsizeof(list_squares)} bytes")  # 约 8MB
print(f"生成器内存: {sys.getsizeof(gen_squares)} bytes")  # 约 200 bytes

# 时间对比
start = time.time()
sum(get_squares_list(n))
print(f"列表耗时: {time.time() - start:.4f}秒")

start = time.time()
sum(get_squares_gen(n))
print(f"生成器耗时: {time.time() - start:.4f}秒")
```

## 速查表

| 操作 | 代码 |
|------|------|
| 创建生成器 | `def gen(): yield value` |
| 生成器表达式 | `(x for x in range(10))` |
| 获取下一个值 | `next(gen)` |
| 遍历生成器 | `for x in gen:` |
| 连接生成器 | `yield from iterable` |
| 发送值 | `gen.send(value)` |
| 抛出异常 | `gen.throw(Exception)` |
| 关闭生成器 | `gen.close()` |

## 小测验

1. 生成器和列表的区别是什么？
2. yield 和 return 的区别是什么？
3. 生成器表达式和列表推导式的区别？
4. yield from 的作用是什么？
5. 生成器只能遍历一次，如何解决？
