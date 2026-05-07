# -*- coding: utf-8 -*-
"""
重试装饰器 - 主程序
演示重试装饰器的使用
"""

import random
from retry import retry


# 示例1：基本重试
@retry(max_attempts=3, delay=1)
def unstable_function():
    """不稳定函数，随机失败"""
    if random.random() < 0.7:
        raise ValueError("随机错误")
    return "成功"


# 示例2：指定异常类型
@retry(max_attempts=3, delay=0.5, exceptions=(ValueError, TypeError))
def validate_input(data):
    """验证输入数据"""
    if not isinstance(data, dict):
        raise TypeError("输入必须是字典")
    if "name" not in data:
        raise ValueError("缺少 name 字段")
    return f"验证通过: {data['name']}"


# 示例3：指数退避
@retry(max_attempts=4, delay=1, backoff=2)
def api_call():
    """模拟 API 调用"""
    if random.random() < 0.8:
        raise ConnectionError("API 连接失败")
    return {"status": "success", "data": [1, 2, 3]}


# 示例4：带回调函数
def on_retry_callback(attempt, error):
    """重试回调函数"""
    print(f"  -> 回调：第 {attempt} 次重试，错误: {error}")


@retry(max_attempts=3, delay=0.5, on_retry=on_retry_callback)
def process_data():
    """处理数据"""
    if random.random() < 0.6:
        raise RuntimeError("处理失败")
    return "处理完成"


def main():
    """主函数"""
    print("=" * 50)
    print("  重试装饰器演示")
    print("=" * 50)
    
    # 示例1
    print("\n[示例1] 基本重试")
    try:
        result = unstable_function()
        print(f"结果: {result}")
    except Exception as e:
        print(f"最终失败: {e}")
    
    # 示例2
    print("\n[示例2] 指定异常类型")
    try:
        result = validate_input({"name": "Alice"})
        print(f"结果: {result}")
    except Exception as e:
        print(f"最终失败: {e}")
    
    # 示例3
    print("\n[示例3] 指数退避")
    try:
        result = api_call()
        print(f"结果: {result}")
    except Exception as e:
        print(f"最终失败: {e}")
    
    # 示例4
    print("\n[示例4] 带回调函数")
    try:
        result = process_data()
        print(f"结果: {result}")
    except Exception as e:
        print(f"最终失败: {e}")


if __name__ == "__main__":
    main()
