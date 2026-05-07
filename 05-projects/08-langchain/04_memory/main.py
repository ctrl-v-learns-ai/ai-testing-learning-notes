# -*- coding: utf-8 -*-
"""
带上下文记忆的客服机器人 - 主程序入口
"""

import argparse
from chat_bot import CustomerServiceBot


def print_welcome():
    """打印欢迎信息"""
    print("=" * 50)
    print("  客服机器人 - Memory 学习项目")
    print("=" * 50)
    print("命令：")
    print("  /quit     - 退出程序")
    print("  /history  - 查看对话历史")
    print("  /clear    - 清除对话历史")
    print("=" * 50)


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="客服机器人")
    parser.add_argument(
        "--user-id",
        type=str,
        default="user_001",
        help="用户ID（默认：user_001）"
    )
    args = parser.parse_args()
    
    # 初始化机器人
    print("正在初始化客服机器人...")
    bot = CustomerServiceBot()
    
    print_welcome()
    print(f"当前用户：{args.user_id}")
    print("您好！我是客服小助，有什么可以帮您的吗？\n")
    
    # 主循环
    while True:
        try:
            user_input = input("您: ").strip()
            
            if not user_input:
                continue
            
            if user_input.startswith("/"):
                cmd = user_input.lower()
                if cmd == "/quit":
                    print("感谢您的咨询，再见！")
                    break
                elif cmd == "/history":
                    history = bot.get_history(args.user_id)
                    if not history:
                        print("暂无对话历史")
                    else:
                        print("\n对话历史：")
                        for msg in history:
                            role = "用户" if msg.type == "human" else "客服"
                            print(f"  [{role}] {msg.content}")
                    print()
                elif cmd == "/clear":
                    print(bot.clear_history(args.user_id))
                else:
                    print(f"未知命令：{cmd}")
                continue
            
            # 处理用户输入
            response = bot.chat(user_input, args.user_id)
            print(f"小助: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\n感谢您的咨询，再见！")
            break
        except Exception as e:
            print(f"\n错误：{e}")


if __name__ == "__main__":
    main()
