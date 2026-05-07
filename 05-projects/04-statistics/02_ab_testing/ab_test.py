# -*- coding: utf-8 -*-
"""
A/B 测试分析模块
提供假设检验、效应量计算、置信区间等功能
"""

import numpy as np
from scipy import stats
from typing import Dict, Optional, Tuple


class ABTest:
    """
    A/B 测试分析器
    
    使用示例:
        test = ABTest(control, treatment)
        result = test.t_test()
    """
    
    def __init__(self, control: np.ndarray, treatment: np.ndarray):
        """
        初始化 A/B 测试
        
        参数:
            control: 对照组数据
            treatment: 实验组数据
        """
        self.control = np.array(control)
        self.treatment = np.array(treatment)
    
    def descriptive_stats(self) -> Dict:
        """描述性统计"""
        return {
            "control": {
                "count": len(self.control),
                "mean": np.mean(self.control),
                "std": np.std(self.control, ddof=1),
                "median": np.median(self.control),
                "min": np.min(self.control),
                "max": np.max(self.control),
            },
            "treatment": {
                "count": len(self.treatment),
                "mean": np.mean(self.treatment),
                "std": np.std(self.treatment, ddof=1),
                "median": np.median(self.treatment),
                "min": np.min(self.treatment),
                "max": np.max(self.treatment),
            }
        }
    
    def t_test(self, alpha: float = 0.05) -> Dict:
        """
        双样本 t 检验
        
        参数:
            alpha: 显著性水平
        
        返回:
            检验结果字典
        """
        t_stat, p_value = stats.ttest_ind(self.control, self.treatment)
        
        return {
            "test_type": "独立双样本 t 检验",
            "t_statistic": t_stat,
            "p_value": p_value,
            "alpha": alpha,
            "significant": p_value < alpha,
            "conclusion": "拒绝零假设，两组有显著差异" if p_value < alpha else "不拒绝零假设，两组无显著差异"
        }
    
    def paired_t_test(self, alpha: float = 0.05) -> Dict:
        """
        配对样本 t 检验
        
        参数:
            alpha: 显著性水平
        
        返回:
            检验结果字典
        """
        if len(self.control) != len(self.treatment):
            raise ValueError("配对 t 检验要求两组数据长度相同")
        
        t_stat, p_value = stats.ttest_rel(self.control, self.treatment)
        
        return {
            "test_type": "配对样本 t 检验",
            "t_statistic": t_stat,
            "p_value": p_value,
            "alpha": alpha,
            "significant": p_value < alpha,
            "conclusion": "拒绝零假设，两组有显著差异" if p_value < alpha else "不拒绝零假设，两组无显著差异"
        }
    
    def cohens_d(self) -> float:
        """
        计算 Cohen's d 效应量
        
        返回:
            效应量值
        """
        n1, n2 = len(self.control), len(self.treatment)
        var1, var2 = np.var(self.control, ddof=1), np.var(self.treatment, ddof=1)
        pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
        d = (np.mean(self.treatment) - np.mean(self.control)) / pooled_std
        return d
    
    def effect_size_interpretation(self, d: float) -> str:
        """
        解释效应量
        
        参数:
            d: Cohen's d 值
        
        返回:
            效应量解释
        """
        abs_d = abs(d)
        if abs_d < 0.2:
            return "无效应"
        elif abs_d < 0.5:
            return "小效应"
        elif abs_d < 0.8:
            return "中效应"
        else:
            return "大效应"
    
    def confidence_interval(self, confidence: float = 0.95) -> Tuple[float, float]:
        """
        计算均值差的置信区间
        
        参数:
            confidence: 置信水平
        
        返回:
            置信区间 (下限, 上限)
        """
        diff = np.mean(self.treatment) - np.mean(self.control)
        se = np.sqrt(np.var(self.control, ddof=1)/len(self.control) + 
                     np.var(self.treatment, ddof=1)/len(self.treatment))
        
        df = len(self.control) + len(self.treatment) - 2
        t_critical = stats.t.ppf((1 + confidence) / 2, df)
        
        margin = t_critical * se
        return diff - margin, diff + margin
    
    def power_analysis(self, alpha: float = 0.05) -> Dict:
        """
        统计功效分析
        
        参数:
            alpha: 显著性水平
        
        返回:
            功效分析结果
        """
        d = self.cohens_d()
        n = min(len(self.control), len(self.treatment))
        
        # 计算功效
        effect_size = abs(d)
        df = 2 * n - 2
        t_critical = stats.t.ppf(1 - alpha/2, df)
        
        # 非中心参数
        ncp = effect_size * np.sqrt(n / 2)
        
        # 功效 = 1 - beta
        power = 1 - stats.nct.cdf(t_critical, df, ncp)
        
        return {
            "effect_size": d,
            "sample_size": n,
            "alpha": alpha,
            "power": power,
            "conclusion": "功效充足" if power >= 0.8 else "功效不足，建议增加样本量"
        }
    
    def generate_report(self) -> Dict:
        """
        生成完整分析报告
        
        返回:
            包含所有分析结果的字典
        """
        d = self.cohens_d()
        ci = self.confidence_interval()
        
        report = {
            "描述性统计": self.descriptive_stats(),
            "t 检验": self.t_test(),
            "效应量": {
                "Cohen's d": d,
                "解释": self.effect_size_interpretation(d),
            },
            "置信区间": {
                "95% CI": ci,
                "解释": f"均值差的 95% 置信区间为 [{ci[0]:.4f}, {ci[1]:.4f}]"
            },
            "功效分析": self.power_analysis(),
        }
        
        return report
    
    def print_report(self):
        """打印分析报告"""
        report = self.generate_report()
        
        print("=" * 60)
        print("  A/B 测试分析报告")
        print("=" * 60)
        
        # 描述性统计
        print("\n[描述性统计]")
        for group, stats in report["描述性统计"].items():
            print(f"\n  {group}:")
            for key, value in stats.items():
                if isinstance(value, float):
                    print(f"    {key}: {value:.4f}")
                else:
                    print(f"    {key}: {value}")
        
        # t 检验
        print("\n[t 检验]")
        t_test = report["t 检验"]
        print(f"  检验类型: {t_test['test_type']}")
        print(f"  t 统计量: {t_test['t_statistic']:.4f}")
        print(f"  p 值: {t_test['p_value']:.4f}")
        print(f"  显著性水平: {t_test['alpha']}")
        print(f"  结论: {t_test['conclusion']}")
        
        # 效应量
        print("\n[效应量]")
        effect = report["效应量"]
        print(f"  Cohen's d: {effect['Cohen\'s d']:.4f}")
        print(f"  解释: {effect['解释']}")
        
        # 置信区间
        print("\n[置信区间]")
        ci = report["置信区间"]
        print(f"  {ci['解释']}")
        
        # 功效分析
        print("\n[功效分析]")
        power = report["功效分析"]
        print(f"  统计功效: {power['power']:.4f}")
        print(f"  结论: {power['conclusion']}")
