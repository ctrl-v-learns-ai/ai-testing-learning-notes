# 阶段项目：命令行聊天机器人

## 项目简介
一个具有角色设定和格式化输出的命令行聊天机器人，用于巩固 Model I/O 的所有知识点。

## 功能特性
- 支持多种AI角色（测试工程师、产品经理、开发工程师）
- 多轮对话，保持上下文记忆
- 流式输出，实时显示生成过程
- 支持特殊命令（退出、清除历史、切换角色）

## 运行方式
```bash
# 安装依赖
pip install -r requirements.txt

# 运行程序
python main.py

# 指定角色启动
python main.py --role test_engineer
```

## 核心知识点
1. ChatModel 初始化与调用
2. ChatPromptTemplate 构建多轮对话提示
3. StrOutputParser 解析输出
4. LCEL 链式调用（invoke、stream）
5. 消息历史管理

## 项目结构
```
05-projects/01_model_io/
  main.py        # 程序入口
  chat_bot.py    # 聊天机器人核心类
  config.py      # 配置管理
  prompts.py     # 角色提示模板
  requirements.txt
  README.md
```
