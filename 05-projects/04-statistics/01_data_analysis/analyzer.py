# -*- coding: utf-8 -*-
"""
数据分析器模块
提供描述性统计、异常值检测、相关性分析等功能
"""

import numpy as np
import pandas as pd
from scipy import stats
from typing import Dict, List, Optional, Tuple


class DataAnalyzer:
    """
    数据分析器
    
    使用示例:
        analyzer = DataAnalyzer(data)
        report = analyzer.generate_report()
    """
    
    def __init__(self, data: pd.DataFrame):
        """初始化分析器"""
        self.data = data
        self.numeric_columns = data.select_dtypes(include=[np.number]).columns.tolist()
    
    def descriptive_stats(self) -> Dict:
        """
        描述性统计
        
        返回:
            包含各种统计量的字典
        """
        stats_dict = {}
        
        for col in self.numeric_columns:
            series = self.data[col].dropna()
            stats_dict[col] = {
                "count": len(series),
                "mean": np.mean(series),
                "median": np.median(series),
                "std": np.std(series, ddof=1),
                "min": np.min(series),
                "max": np.max(series),
                "q1": np.percentile(series, 25),
                "q3": np.percentile(series, 75),
                "iqr": np.percentile(series, 75) - np.percentile(series, 25),
                "skewness": stats.skew(series),
                "kurtosis": stats.kurtosis(series),
            }
        
        return stats_dict
    
    def detect_outliers(self, method: str = "iqr", threshold: float = 1.5) -> Dict:
        """
        异常值检测
        
        参数:
            method: 检测方法 ("iqr" 或 "zscore")
            threshold: 阈值
        
        返回:
            包含异常值信息的字典
        """
        outliers_dict = {}
        
        for col in self.numeric_columns:
            series = self.data[col].dropna()
            
            if method == "iqr":
                q1 = np.percentile(series, 25)
                q3 = np.percentile(series, 75)
                iqr = q3 - q1
                lower_bound = q1 - threshold * iqr
                upper_bound = q3 + threshold * iqr
                outlier_mask = (series < lower_bound) | (series > upper_bound)
            elif method == "zscore":
                z_scores = np.abs(stats.zscore(series))
                outlier_mask = z_scores > threshold
                lower_bound = np.mean(series) - threshold * np.std(series)
                upper_bound = np.mean(series) + threshold * np.std(series)
            else:
                raise ValueError(f"不支持的方法: {method}")
            
            outliers_dict[col] = {
                "outlier_count": outlier_mask.sum(),
                "outlier_ratio": outlier_mask.mean(),
                "lower_bound": lower_bound,
                "upper_bound": upper_bound,
                "outlier_values": series[outlier_mask].tolist()
            }
        
        return outliers_dict
    
    def correlation_analysis(self) -> pd.DataFrame:
        """
        相关性分析
        
        返回:
            相关系数矩阵
        """
        if len(self.numeric_columns) < 2:
            return pd.DataFrame()
        
        return self.data[self.numeric_columns].corr()
    
    def distribution_analysis(self) -> Dict:
        """
        分布分析
        
        返回:
            包含分布信息的字典
        """
        dist_dict = {}
        
        for col in self.numeric_columns:
            series = self.data[col].dropna()
            
            # 正态性检验
            if len(series) >= 8:
                stat, p_value = stats.shapiro(series[:5000])  # Shapiro-Wilk 检验
                is_normal = p_value > 0.05
            else:
                is_normal = None
                p_value = None
            
            dist_dict[col] = {
                "is_normal": is_normal,
                "p_value": p_value,
                "skewness": stats.skew(series),
                "kurtosis": stats.kurtosis(series),
            }
        
        return dist_dict
    
    def generate_report(self) -> Dict:
        """
        生成完整分析报告
        
        返回:
            包含所有分析结果的字典
        """
        report = {
            "数据概览": {
                "行数": len(self.data),
                "列数": len(self.data.columns),
                "数值列数": len(self.numeric_columns),
                "缺失值": self.data.isnull().sum().to_dict(),
            },
            "描述性统计": self.descriptive_stats(),
            "异常值检测": self.detect_outliers(),
            "相关性分析": self.correlation_analysis().to_dict() if len(self.numeric_columns) >= 2 else {},
            "分布分析": self.distribution_analysis(),
        }
        
        return report
    
    def print_report(self):
        """打印分析报告"""
        report = self.generate_report()
        
        print("=" * 60)
        print("  数据分析报告")
        print("=" * 60)
        
        # 数据概览
        print("\n[数据概览]")
        for key, value in report["数据概览"].items():
            print(f"  {key}: {value}")
        
        # 描述性统计
        print("\n[描述性统计]")
        for col, stats in report["描述性统计"].items():
            print(f"\n  {col}:")
            for key, value in stats.items():
                if isinstance(value, float):
                    print(f"    {key}: {value:.4f}")
                else:
                    print(f"    {key}: {value}")
        
        # 异常值检测
        print("\n[异常值检测]")
        for col, info in report["异常值检测"].items():
            print(f"\n  {col}:")
            print(f"    异常值数量: {info['outlier_count']}")
            print(f"    异常值比例: {info['outlier_ratio']:.2%}")
        
        # 相关性分析
        if report["相关性分析"]:
            print("\n[相关性分析]")
            corr_df = pd.DataFrame(report["相关性分析"])
            print(corr_df.round(4))
