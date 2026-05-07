# -*- coding: utf-8 -*-
"""
重试装饰器模块
支持配置重试次数、延迟时间、异常类型等
"""

import functools
import time
from typing import Type, Callable, Optional, Tuple


def retry(
    max_attempts: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
    on_retry: Optional[Callable] = None
):
    """
    重试装饰器
    
    参数:
        max_attempts: 最大重试次数
        delay: 初始延迟时间（秒）
        backoff: 退避倍数
        exceptions: 需要重试的异常类型
        on_retry: 重试时的回调函数
    
    使用示例:
        @retry(max_attempts=3, delay=1, exceptions=(ValueError,))
        def unstable_function():
            ...
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    attempt_num = attempt + 1
                    
                    if attempt_num < max_attempts:
                        print(f"第 {attempt_num} 次尝试失败: {type(e).__name__}: {e}")
                        print(f"等待 {current_delay:.1f} 秒后重试...")
                        
                        if on_retry:
                            on_retry(attempt_num, e)
                        
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        print(f"第 {attempt_num} 次尝试失败，已达到最大重试次数")
            
            raise last_exception
        
        return wrapper
    return decorator


def async_retry(
    max_attempts: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
):
    """
    异步重试装饰器
    
    参数:
        max_attempts: 最大重试次数
        delay: 初始延迟时间（秒）
        backoff: 退避倍数
        exceptions: 需要重试的异常类型
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            import asyncio
            
            current_delay = delay
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    attempt_num = attempt + 1
                    
                    if attempt_num < max_attempts:
                        print(f"第 {attempt_num} 次尝试失败: {type(e).__name__}: {e}")
                        print(f"等待 {current_delay:.1f} 秒后重试...")
                        await asyncio.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        print(f"第 {attempt_num} 次尝试失败，已达到最大重试次数")
            
            raise last_exception
        
        return wrapper
    return decorator
