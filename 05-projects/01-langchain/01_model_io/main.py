# -*- coding: utf-8 -*-
"""
命令行聊天机器人 - 主程序入口
支持角色切换、多轮对话、流式输出
"""

import argparse
import sys

from chat_bot import ChatBot
from prompts import list_roles


def print_welcome():
    """打印欢迎信息"""
    print("=" * 50)
    print("  AI 聊天机器人 - Model I/O 学习项目")
    print("=" * 50)
    print("命令：")
    print("  /quit      - 退出程序")
    print("  /clear     - 清除对话历史")
    print("  /role xxx  - 切换角色")
    print("  /roles     - 列出所有角色")
    print("  /history   - 查看历史条数")
    print("=" * 50)


def main():
    """主函数"""
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="AI 聊天机器人")
    parser.add_argument(
        "--role",
        type=str,
        default="test_engineer",
        help="初始角色 (default: test_engineer)"
    )
    parser.add_argument(
        "--stream",
        action="store_true",
        default=True,
        help="使用流式输出"
    )
    args = parser.parse_args()
    
    # 初始化机器人
    bot = ChatBot(role_id=args.role)
    print_welcome()
    print(f"当前角色：{args.role}")
    print()
    
    # 主循环
    while True:
        try:
            user_input = input("你: ").strip()
            
            # 跳过空输入
            if not user_input:
                continue
            
            # 处理命令
            if user_input.startswith("/"):
                cmd = user_input.lower().split()
                
                if cmd[0] == "/quit":
                    print("再见！")
                    break
                elif cmd[0] == "/clear":
                    print(bot.clear_history())
                elif cmd[0] == "/role":
                    if len(cmd) > 1:
                        print(bot.switch_role(cmd[1]))
                    else:
                        print("请指定角色，如：/role product_manager")
                elif cmd[0] == "/roles":
                    roles = list_roles()
                    print("可用角色：")
                    for role_id in roles:
                        print(f"  - {role_id}")
                elif cmd[0] == "/history":
                    print(f"历史消息条数：{bot.get_history_count()}")
                else:
                    print(f"未知命令：{cmd[0]}")
                continue
            
            # 正常对话
            print("AI: ", end="", flush=True)
            
            if args.stream:
                # 流式输出
                for chunk in bot.chat_stream(user_input):
                    print(chunk, end="", flush=True)
                print()
            else:
                # 非流式
                response = bot.chat(user_input)
                print(response)
            
            print()
            
        except KeyboardInterrupt:
            print("\n\n再见！")
            break
        except Exception as e:
            print(f"\n错误：{e}")
            print("请检查 API 配置是否正确")


if __name__ == "__main__":
    main()
