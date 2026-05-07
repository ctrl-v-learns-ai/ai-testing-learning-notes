# -*- coding: utf-8 -*-
"""
练习4：类型提示基础
练习目标：掌握类型提示的使用
前置知识：Python 基础、类
"""

from typing import List, Dict, Tuple, Optional, Union, Callable
from dataclasses import dataclass

# 练习4.1：基本类型提示
print("=== 练习4.1：基本类型提示 ===")

# 变量类型提示
name: str = "Alice"
age: int = 25
height: float = 1.75
is_student: bool = False

print(f"姓名: {name}, 年龄: {age}, 身高: {height}, 是否学生: {is_student}")

# 函数类型提示
def greet(name: str) -> str:
    """问候函数"""
    return f"Hello, {name}!"

print(greet("Bob"))

def add(a: int, b: int = 0) -> int:
    """加法函数"""
    return a + b

print(f"1 + 2 = {add(1, 2)}")

# 练习4.2：复合类型提示
print("\n=== 练习4.2：复合类型提示 ===")

# 列表
numbers: List[int] = [1, 2, 3, 4, 5]
names: List[str] = ["Alice", "Bob", "Charlie"]

print(f"数字: {numbers}")
print(f"姓名: {names}")

# 字典
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
print(f"成绩: {scores}")

# 元组
point: Tuple[int, int] = (10, 20)
print(f"坐标: {point}")

# 可选类型
def find_user(user_id: int) -> Optional[dict]:
    """查找用户，可能返回 None"""
    users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
    return users.get(user_id)

user = find_user(1)
print(f"用户1: {user}")

user = find_user(3)
print(f"用户3: {user}")

# 联合类型
def process(value: Union[int, str]) -> str:
    """处理整数或字符串"""
    if isinstance(value, int):
        return f"处理整数: {value}"
    else:
        return f"处理字符串: {value}"

print(process(42))
print(process("hello"))

# 练习4.3：函数类型提示
print("\n=== 练习4.3：函数类型提示 ===")

# 函数作为参数
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    """应用函数"""
    return func(a, b)

def multiply(a: int, b: int) -> int:
    return a * b

result = apply(multiply, 3, 4)
print(f"3 * 4 = {result}")

# 返回函数
def get_operation(op: str) -> Callable[[int, int], int]:
    """获取操作函数"""
    if op == "+":
        return lambda a, b: a + b
    elif op == "-":
        return lambda a, b: a - b
    else:
        raise ValueError(f"未知操作: {op}")

add_op = get_operation("+")
print(f"10 + 5 = {add_op(10, 5)}")

# 练习4.4：类型别名
print("\n=== 练习4.4：类型别名 ===")

# 类型别名
Vector = List[float]
Matrix = List[Vector]
Point = Tuple[float, float]

def dot_product(v1: Vector, v2: Vector) -> float:
    """计算向量点积"""
    return sum(a * b for a, b in zip(v1, v2))

v1: Vector = [1.0, 2.0, 3.0]
v2: Vector = [4.0, 5.0, 6.0]
print(f"向量点积: {dot_product(v1, v2)}")

# 练习4.5：TypedDict
print("\n=== 练习4.5：TypedDict ===")

from typing import TypedDict

class UserInfo(TypedDict):
    name: str
    age: int
    email: str

user: UserInfo = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
}

print(f"用户信息: {user}")

# 练习4.6：Literal 类型
print("\n=== 练习4.6：Literal 类型 ===")

from typing import Literal

def set_direction(direction: Literal["north", "south", "east", "west"]) -> None:
    """设置方向"""
    print(f"设置方向: {direction}")

set_direction("north")
# set_direction("up")  # 类型检查器会报错

# 练习4.7：数据类
print("\n=== 练习4.7：数据类 ===")

@dataclass
class Student:
    """学生类"""
    name: str
    age: int
    grade: str
    scores: List[int]
    
    def average_score(self) -> float:
        """计算平均分"""
        return sum(self.scores) / len(self.scores)

student = Student("Alice", 20, "A", [90, 85, 95])
print(f"学生: {student.name}")
print(f"平均分: {student.average_score():.1f}")

"""
思考题：
1. 类型提示的作用是什么？
2. Optional 和 Union 的区别是什么？
3. 如何定义类型别名？
4. TypedDict 的作用是什么？
5. @dataclass 的作用是什么？
"""
