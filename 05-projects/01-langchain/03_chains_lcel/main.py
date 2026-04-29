# -*- coding: utf-8 -*-
"""
多步文档分析管道 - 主程序入口
"""

import argparse
from analysis_chain import DocumentAnalyzer


def print_welcome():
    """打印欢迎信息"""
    print("=" * 50)
    print("  多步文档分析管道 - LCEL 学习项目")
    print("=" * 50)
    print("命令：")
    print("  /quit   - 退出程序")
    print("  /batch  - 批量分析模式")
    print("=" * 50)


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="多步文档分析管道")
    parser.add_argument(
        "--doc",
        type=str,
        help="文档路径（可选）"
    )
    args = parser.parse_args()
    
    # 初始化分析器
    print("正在初始化分析器...")
    analyzer = DocumentAnalyzer()
    
    print_welcome()
    
    # 如果指定了文档，直接分析
    if args.doc:
        try:
            with open(args.doc, "r", encoding="utf-8") as f:
                text = f.read()
            print(f"\n正在分析文档：{args.doc}")
            print("=" * 50)
            
            result = analyzer.analyze(text)
            
            print(f"\n【摘要】{result['summary']}")
            print(f"\n【关键词】{result['keywords']}")
            print(f"\n【情感倾向】{result['sentiment']}")
            print(f"\n【分析报告】\n{result['report']}")
        except Exception as e:
            print(f"读取文档失败：{e}")
        return
    
    # 交互模式
    print("\n请输入要分析的文本（输入 /quit 退出）\n")
    
    while True:
        try:
            text = input("请输入文本：").strip()
            
            if not text:
                continue
            
            if text.startswith("/"):
                cmd = text.lower()
                if cmd == "/quit":
                    print("再见！")
                    break
                elif cmd == "/batch":
                    print("批量分析模式（输入多行文本，空行结束）：")
                    texts = []
                    while True:
                        line = input()
                        if not line:
                            break
                        texts.append(line)
                    if texts:
                        results = analyzer.batch_analyze(texts)
                        for i, r in enumerate(results, 1):
                            print(f"\n--- 文本 {i} ---")
                            print(f"摘要：{r['summary']}")
                            print(f"关键词：{r['keywords']}")
                else:
                    print(f"未知命令：{cmd}")
                continue
            
            print("\n正在分析...")
            result = analyzer.analyze(text)
            
            print(f"\n【摘要】{result['summary']}")
            print(f"【关键词】{result['keywords']}")
            print(f"【情感倾向】{result['sentiment']}")
            print(f"\n【分析报告】\n{result['report']}")
            print()
            
        except KeyboardInterrupt:
            print("\n\n再见！")
            break
        except Exception as e:
            print(f"\n错误：{e}")


if __name__ == "__main__":
    main()
