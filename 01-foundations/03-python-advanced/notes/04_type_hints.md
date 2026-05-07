# Python 进阶四：类型提示

## 什么是类型提示？

类型提示是 Python 3.5+ 引入的功能，用于标注变量、函数参数和返回值的类型。它不会影响程序运行，但可以提高代码可读性和 IDE 支持。

类比理解：
- 类型提示 = 路牌（不改变道路，但帮助你找到正确方向）
- 类型提示 = 说明书标签（不改变产品，但帮助你理解用途）

## 基本类型提示

```python
# 变量类型提示
name: str = "Alice"
age: int = 25
height: float = 1.75
is_student: bool = False

# 函数类型提示
def greet(name: str) -> str:
    return f"Hello, {name}!"

# 带默认值的参数
def add(a: int, b: int = 0) -> int:
    return a + b
```

## 复合类型提示

```python
from typing import List, Dict, Tuple, Set, Optional, Union

# 列表
numbers: List[int] = [1, 2, 3, 4, 5]
names: List[str] = ["Alice", "Bob", "Charlie"]

# 字典
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# 或者使用更具体的类型
from typing import Dict
scores: Dict[str, List[int]] = {"Alice": [90, 85, 95]}

# 元组
point: Tuple[int, int] = (10, 20)
# 或者使用更具体的类型
rgb: Tuple[int, int, int] = (255, 128, 0)

# 集合
unique_numbers: Set[int] = {1, 2, 3, 4, 5}

# 可选类型（可以是 None）
name: Optional[str] = None  # 等价于 Union[str, None]

# 联合类型（多种类型）
value: Union[int, str] = 42
value = "hello"  # 也可以
```

## Python 3.10+ 新语法

```python
# Python 3.10+ 可以使用 | 代替 Union
def process(value: int | str) -> None:
    if isinstance(value, int):
        print(f"处理整数: {value}")
    else:
        print(f"处理字符串: {value}")

# 可选类型
name: str | None = None

# 列表类型
numbers: list[int] = [1, 2, 3]  # 不需要从 typing 导入 List
```

## 函数类型提示

```python
from typing import Callable, Awaitable

# 函数作为参数
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def add(a: int, b: int) -> int:
    return a + b

result = apply(add, 1, 2)  # 3

# 返回函数
def get_operation(op: str) -> Callable[[int, int], int]:
    if op == "+":
        return lambda a, b: a + b
    elif op == "-":
        return lambda a, b: a - b
    else:
        raise ValueError(f"未知操作: {op}")

# 异步函数
async def fetch_data() -> str:
    return "data"
```

## 类型别名

```python
from typing import List, Dict, Tuple

# 类型别名
Vector = List[float]
Matrix = List[Vector]
Point = Tuple[float, float]
ScoreMap = Dict[str, List[int]]

# 使用
def dot_product(v1: Vector, v2: Vector) -> float:
    return sum(a * b for a, b in zip(v1, v2))

def create_matrix(rows: int, cols: int) -> Matrix:
    return [[0.0] * cols for _ in range(rows)]
```

## 泛型

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)
    
    def pop(self) -> T:
        if not self.items:
            raise IndexError("栈为空")
        return self.items.pop()
    
    def peek(self) -> T:
        if not self.items:
            raise IndexError("栈为空")
        return self.items[-1]

# 使用
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
print(int_stack.pop())  # 2

str_stack: Stack[str] = Stack()
str_stack.push("hello")
str_stack.push("world")
print(str_stack.pop())  # world
```

## TypedDict

```python
from typing import TypedDict

class UserInfo(TypedDict):
    name: str
    age: int
    email: str

# 使用
user: UserInfo = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
}

# 访问
print(user["name"])  # Alice
```

## Literal 类型

```python
from typing import Literal

def set_direction(direction: Literal["north", "south", "east", "west"]) -> None:
    print(f"设置方向: {direction}")

set_direction("north")  # 正确
# set_direction("up")   # 类型检查器会报错
```

## Protocol（结构化子类型）

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        ...

class Circle:
    def draw(self) -> None:
        print("绘制圆形")

class Square:
    def draw(self) -> None:
        print("绘制正方形")

def draw_shape(shape: Drawable) -> None:
    shape.draw()

# Circle 和 Square 都实现了 Drawable 协议
draw_shape(Circle())  # 正确
draw_shape(Square())  # 正确
```

## 实际应用场景

### 1. API 参数类型

```python
from typing import Optional, List

def search_users(
    keyword: str,
    limit: int = 10,
    offset: int = 0,
    fields: Optional[List[str]] = None
) -> List[dict]:
    """搜索用户
    
    Args:
        keyword: 搜索关键词
        limit: 返回数量限制
        offset: 偏移量
        fields: 返回的字段列表
    
    Returns:
        用户列表
    """
    # 实现
    pass
```

### 2. 配置类

```python
from typing import Optional
from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    host: str
    port: int
    username: str
    password: str
    database: str
    pool_size: int = 10
    timeout: Optional[int] = None

# 使用
config = DatabaseConfig(
    host="localhost",
    port=5432,
    username="admin",
    password="password",
    database="mydb"
)
```

### 3. 响应类型

```python
from typing import Generic, TypeVar, Optional
from dataclasses import dataclass

T = TypeVar('T')

@dataclass
class ApiResponse(Generic[T]):
    code: int
    message: str
    data: Optional[T] = None

# 使用
def get_user(user_id: int) -> ApiResponse[dict]:
    return ApiResponse(
        code=200,
        message="success",
        data={"id": user_id, "name": "Alice"}
    )
```

## 使用 mypy 进行类型检查

```bash
# 安装 mypy
pip install mypy

# 检查单个文件
mypy script.py

# 检查整个项目
mypy src/

# 配置 mypy (mypy.ini)
[mypy]
python_version = 3.10
warn_return_any = True
warn_unused_configs = True
```

## 常见坑

### 坑1：类型提示不影响运行

```python
def add(a: int, b: int) -> int:
    return a + b

# 以下调用不会报错（类型提示只用于检查）
result = add("hello", " world")  # 运行时不会报错
print(result)  # hello world
```

### 坑2：None 的处理

```python
# 错误：没有处理 None 的情况
def get_name(user: dict) -> str:
    return user.get("name")  # 返回值可能是 None

# 正确：明确处理 None
def get_name(user: dict) -> Optional[str]:
    return user.get("name")

# 或者提供默认值
def get_name(user: dict) -> str:
    return user.get("name", "未知")
```

### 坑3：循环引用

```python
# 错误：循环引用
class Node:
    def __init__(self, value: int, next: Node):  # NameError: name 'Node' is not defined
        self.value = value
        self.next = next

# 正确：使用字符串或 TYPE_CHECKING
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .node import Node

class Node:
    def __init__(self, value: int, next: 'Node'):
        self.value = value
        self.next = next
```

## 速查表

| 类型 | 代码 |
|------|------|
| 基本类型 | `int`, `str`, `float`, `bool` |
| 列表 | `List[int]` 或 `list[int]` |
| 字典 | `Dict[str, int]` 或 `dict[str, int]` |
| 元组 | `Tuple[int, str]` |
| 可选 | `Optional[str]` 或 `str \| None` |
| 联合 | `Union[int, str]` 或 `int \| str` |
| 函数 | `Callable[[int], str]` |
| 泛型 | `Generic[T]` |
| 类型别名 | `Vector = List[float]` |

## 小测验

1. 类型提示的作用是什么？
2. Optional 和 Union 的区别是什么？
3. 如何定义类型别名？
4. Generic 的作用是什么？
5. 如何使用 mypy 进行类型检查？
