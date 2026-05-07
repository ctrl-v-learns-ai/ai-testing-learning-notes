# -*- coding: utf-8 -*-
"""
数据处理管道 - 主程序
演示管道的使用
"""

from pipeline import Pipeline, generate_fibonacci


def main():
    """主函数"""
    print("=" * 50)
    print("  数据处理管道演示")
    print("=" * 50)
    
    # 示例1：基本操作
    print("\n[示例1] 基本操作")
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    result = (Pipeline(data)
        .filter(lambda x: x % 2 == 0)  # 过滤偶数
        .map(lambda x: x * 2)          # 乘以2
        .to_list())
    
    print(f"原始数据: {data}")
    print(f"过滤偶数并乘以2: {result}")
    
    # 示例2：链式操作
    print("\n[示例2] 链式操作")
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    
    result = (Pipeline(data)
        .distinct()                      # 去重
        .sort()                          # 排序
        .take(5)                         # 取前5个
        .to_list())
    
    print(f"原始数据: {data}")
    print(f"去重、排序、取前5: {result}")
    
    # 示例3：字符串处理
    print("\n[示例3] 字符串处理")
    words = ["Hello", "World", "Python", "Generator", "Pipeline"]
    
    result = (Pipeline(words)
        .filter(lambda w: len(w) > 5)    # 过滤长度大于5的
        .map(lambda w: w.upper())        # 转换为大写
        .to_list())
    
    print(f"原始数据: {words}")
    print(f"长度>5并转大写: {result}")
    
    # 示例4：归约操作
    print("\n[示例4] 归约操作")
    data = [1, 2, 3, 4, 5]
    
    total = (Pipeline(data)
        .reduce(lambda a, b: a + b))
    
    product = (Pipeline(data)
        .reduce(lambda a, b: a * b))
    
    print(f"数据: {data}")
    print(f"求和: {total}")
    print(f"求积: {product}")
    
    # 示例5：斐波那契数列
    print("\n[示例5] 斐波那契数列")
    
    result = (Pipeline(generate_fibonacci())
        .take(10)
        .to_list())
    
    print(f"前10个斐波那契数: {result}")
    
    # 示例6：扁平化操作
    print("\n[示例6] 扁平化操作")
    nested = [[1, 2], [3, 4], [5, 6]]
    
    result = (Pipeline(nested)
        .flat_map(lambda x: x)
        .to_list())
    
    print(f"嵌套列表: {nested}")
    print(f"扁平化: {result}")
    
    # 示例7：复杂数据处理
    print("\n[示例7] 复杂数据处理")
    students = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78},
        {"name": "David", "score": 95},
        {"name": "Eve", "score": 88},
    ]
    
    # 找出成绩大于85的学生，并按成绩排序
    result = (Pipeline(students)
        .filter(lambda s: s["score"] > 85)
        .sort(key=lambda s: s["score"], reverse=True)
        .to_list())
    
    print(f"学生数据: {students}")
    print(f"成绩>85并排序: {result}")


if __name__ == "__main__":
    main()
