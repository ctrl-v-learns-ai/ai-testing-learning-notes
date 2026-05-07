# -*- coding: utf-8 -*-
"""
A/B 测试分析工具 - 主程序
演示 A/B 测试的使用
"""

import numpy as np
from ab_test import ABTest


def main():
    """主函数"""
    print("=" * 50)
    print("  A/B 测试分析工具演示")
    print("=" * 50)
    
    # 生成模拟数据
    np.random.seed(42)
    
    # 场景1：有显著差异
    print("\n[场景1] 有显著差异")
    control = np.random.normal(100, 15, 100)
    treatment = np.random.normal(110, 15, 100)  # 实验组均值高10
    
    test = ABTest(control, treatment)
    test.print_report()
    
    # 场景2：无显著差异
    print("\n\n[场景2] 无显著差异")
    control = np.random.normal(100, 15, 100)
    treatment = np.random.normal(102, 15, 100)  # 实验组均值只高2
    
    test = ABTest(control, treatment)
    test.print_report()
    
    # 场景3：配对样本
    print("\n\n[场景3] 配对样本")
    before = np.random.normal(70, 10, 30)
    after = before + np.random.normal(5, 3, 30)  # 培训后提高5分
    
    test = ABTest(before, after)
    test.print_report()


if __name__ == "__main__":
    main()
