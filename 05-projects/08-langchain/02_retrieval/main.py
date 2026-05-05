# -*- coding: utf-8 -*-
"""
个人知识库问答系统 - 主程序入口
"""

import argparse
from rag_bot import RAGBot


def print_welcome():
    """打印欢迎信息"""
    print("=" * 50)
    print("  个人知识库问答系统 - RAG 学习项目")
    print("=" * 50)
    print("命令：")
    print("  /quit   - 退出程序")
    print("  /clear  - 清除对话历史")
    print("=" * 50)


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="个人知识库问答系统")
    parser.add_argument(
        "--docs",
        type=str,
        default="./documents",
        help="文档路径（文件或目录）"
    )
    parser.add_argument(
        "--index",
        type=str,
        default="faiss_index",
        help="向量数据库保存路径"
    )
    args = parser.parse_args()
    
    # 初始化 RAG 机器人
    print("正在初始化...")
    try:
        bot = RAGBot(doc_path=args.docs, index_path=args.index)
    except Exception as e:
        print(f"初始化失败：{e}")
        print("请确保文档路径正确，且已安装所有依赖")
        return
    
    print_welcome()
    print("知识库加载完成！\n")
    
    # 主循环
    while True:
        try:
            question = input("你: ").strip()
            
            if not question:
                continue
            
            if question.startswith("/"):
                cmd = question.lower()
                if cmd == "/quit":
                    print("再见！")
                    break
                elif cmd == "/clear":
                    print(bot.clear_history())
                else:
                    print(f"未知命令：{cmd}")
                continue
            
            # 提问
            print("AI: ", end="", flush=True)
            result = bot.ask(question)
            print(result["answer"])
            
            # 显示来源
            print("\n参考来源：")
            for i, source in enumerate(result["sources"], 1):
                print(f"  {i}. {source}")
            print()
            
        except KeyboardInterrupt:
            print("\n\n再见！")
            break
        except Exception as e:
            print(f"\n错误：{e}")


if __name__ == "__main__":
    main()
