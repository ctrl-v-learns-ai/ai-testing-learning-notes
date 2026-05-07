# -*- coding: utf-8 -*-
"""
数据处理管道模块
基于生成器的惰性处理管道
"""

from typing import Generator, Callable, Any, Iterable
import functools


class Pipeline:
    """
    数据处理管道
    
    使用示例:
        result = (Pipeline(data)
            .filter(lambda x: x > 0)
            .map(lambda x: x * 2)
            .take(10)
            .to_list())
    """
    
    def __init__(self, data: Iterable):
        """初始化管道"""
        self._data = iter(data)
    
    def __iter__(self):
        """支持迭代"""
        return self._data
    
    def map(self, func: Callable) -> 'Pipeline':
        """映射操作"""
        self._data = (func(item) for item in self._data)
        return self
    
    def filter(self, func: Callable) -> 'Pipeline':
        """过滤操作"""
        self._data = (item for item in self._data if func(item))
        return self
    
    def take(self, n: int) -> 'Pipeline':
        """取前 n 个元素"""
        def _take():
            for i, item in enumerate(self._data):
                if i >= n:
                    break
                yield item
        self._data = _take()
        return self
    
    def skip(self, n: int) -> 'Pipeline':
        """跳过前 n 个元素"""
        def _skip():
            for i, item in enumerate(self._data):
                if i >= n:
                    yield item
        self._data = _skip()
        return self
    
    def flat_map(self, func: Callable) -> 'Pipeline':
        """扁平化映射"""
        def _flat_map():
            for item in self._data:
                result = func(item)
                if hasattr(result, '__iter__'):
                    yield from result
                else:
                    yield result
        self._data = _flat_map()
        return self
    
    def distinct(self) -> 'Pipeline':
        """去重"""
        def _distinct():
            seen = set()
            for item in self._data:
                if item not in seen:
                    seen.add(item)
                    yield item
        self._data = _distinct()
        return self
    
    def sort(self, key: Callable = None, reverse: bool = False) -> 'Pipeline':
        """排序"""
        self._data = iter(sorted(self._data, key=key, reverse=reverse))
        return self
    
    def to_list(self) -> list:
        """转换为列表"""
        return list(self._data)
    
    def to_set(self) -> set:
        """转换为集合"""
        return set(self._data)
    
    def reduce(self, func: Callable, initial: Any = None) -> Any:
        """归约操作"""
        if initial is None:
            return functools.reduce(func, self._data)
        return functools.reduce(func, self._data, initial)
    
    def for_each(self, func: Callable) -> None:
        """遍历执行"""
        for item in self._data:
            func(item)
    
    def count(self) -> int:
        """计数"""
        return sum(1 for _ in self._data)
    
    def first(self, default: Any = None) -> Any:
        """获取第一个元素"""
        try:
            return next(self._data)
        except StopIteration:
            return default
    
    def last(self, default: Any = None) -> Any:
        """获取最后一个元素"""
        result = default
        for item in self._data:
            result = item
        return result


def read_lines(file_path: str) -> Generator[str, None, None]:
    """逐行读取文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()


def read_csv(file_path: str, delimiter: str = ',') -> Generator[dict, None, None]:
    """逐行读取 CSV 文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        headers = f.readline().strip().split(delimiter)
        for line in f:
            values = line.strip().split(delimiter)
            yield dict(zip(headers, values))


def generate_range(start: int, end: int, step: int = 1) -> Generator[int, None, None]:
    """生成范围"""
    current = start
    while current < end:
        yield current
        current += step


def generate_fibonacci() -> Generator[int, None, None]:
    """生成斐波那契数列"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
