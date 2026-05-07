# 阶段项目：带上下文记忆的客服机器人

## 项目简介
一个具有上下文记忆能力的客服机器人，能够记住用户的历史对话，提供连贯的服务体验。

## 功能特性
- 多轮对话，记住用户历史
- 支持多个用户同时对话（独立历史）
- 客服角色设定
- 支持查看对话历史
- 支持清除历史重新开始

## 运行方式
```bash
# 安装依赖
pip install -r requirements.txt

# 运行程序
python main.py

# 指定用户ID
python main.py --user-id user_001
```

## 核心知识点
1. ConversationBufferMemory 的使用
2. MessagesPlaceholder 的作用
3. RunnableWithMessageHistory 实现多用户记忆
4. 对话历史管理

## 项目结构
```
05-projects/04_memory/
  main.py           # 程序入口
  chat_bot.py       # 客服机器人类
  prompts.py        # 提示模板
  config.py         # 配置管理
  requirements.txt
  README.md
```
