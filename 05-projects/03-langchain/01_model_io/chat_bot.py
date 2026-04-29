# -*- coding: utf-8 -*-
"""
聊天机器人核心类
封装 ChatModel、PromptTemplate、LCEL 链
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from config import API_KEY, API_URL, MODEL_NAME, TEMPERATURE
from prompts import get_system_prompt


class ChatBot:
    """命令行聊天机器人类"""
    
    def __init__(self, role_id: str = "test_engineer"):
        """
        初始化聊天机器人
        
        Args:
            role_id: 角色ID，对应 prompts.py 中的角色定义
        """
        self.role_id = role_id
        self.system_prompt = get_system_prompt(role_id)
        
        # 初始化模型
        self.llm = ChatOpenAI(
            model=MODEL_NAME,
            api_key=API_KEY,
            base_url=API_URL,
            temperature=TEMPERATURE,
        )
        
        # 创建提示模板
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", "{input}")
        ])
        
        # 创建 LCEL 链
        self.chain = self.prompt | self.llm | StrOutputParser()
        
        # 对话历史
        self.history = []
    
    def chat(self, user_input: str) -> str:
        """
        处理用户输入并返回响应
        
        Args:
            user_input: 用户输入的文本
            
        Returns:
            AI 的回复文本
        """
        # 调用链
        response = self.chain.invoke({"input": user_input})
        
        # 保存到历史
        self.history.append({"role": "user", "content": user_input})
        self.history.append({"role": "assistant", "content": response})
        
        return response
    
    def chat_stream(self, user_input: str):
        """
        流式输出版本的 chat 方法
        
        Args:
            user_input: 用户输入的文本
            
        Yields:
            逐个 token 的响应片段
        """
        full_response = ""
        for chunk in self.chain.stream({"input": user_input}):
            full_response += chunk
            yield chunk
        
        # 保存到历史
        self.history.append({"role": "user", "content": user_input})
        self.history.append({"role": "assistant", "content": full_response})
    
    def clear_history(self):
        """清除对话历史"""
        self.history = []
        return "对话历史已清除"
    
    def switch_role(self, new_role_id: str):
        """
        切换角色
        
        Args:
            new_role_id: 新的角色ID
        """
        self.role_id = new_role_id
        self.system_prompt = get_system_prompt(new_role_id)
        
        # 重新创建提示模板和链
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", "{input}")
        ])
        self.chain = self.prompt | self.llm | StrOutputParser()
        
        return f"已切换到角色：{new_role_id}"
    
    def get_history_count(self) -> int:
        """获取对话历史条数"""
        return len(self.history)
