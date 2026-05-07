# -*- coding: utf-8 -*-
"""
客服机器人类
"""

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

from config import API_KEY, API_URL, MODEL_NAME, TEMPERATURE
from prompts import CUSTOMER_SERVICE_PROMPT


class CustomerServiceBot:
    """客服机器人类"""
    
    def __init__(self):
        # 初始化 LLM
        self.llm = ChatOpenAI(
            model=MODEL_NAME,
            api_key=API_KEY,
            base_url=API_URL,
            temperature=TEMPERATURE,
        )
        
        # 创建基础链
        chain = CUSTOMER_SERVICE_PROMPT | self.llm | StrOutputParser()
        
        # 会话存储
        self.store = {}
        
        # 包装链，添加记忆功能
        self.chain = RunnableWithMessageHistory(
            chain,
            self._get_session_history,
            input_messages_key="input",
            history_messages_key="history"
        )
    
    def _get_session_history(self, session_id: str):
        """获取或创建会话历史"""
        if session_id not in self.store:
            self.store[session_id] = InMemoryChatMessageHistory()
        return self.store[session_id]
    
    def chat(self, user_input: str, user_id: str = "default") -> str:
        """
        处理用户输入
        
        Args:
            user_input: 用户输入
            user_id: 用户ID（用于区分不同用户的历史）
        
        Returns:
            AI 回复
        """
        config = {"configurable": {"session_id": user_id}}
        response = self.chain.invoke({"input": user_input}, config=config)
        return response
    
    def get_history(self, user_id: str = "default") -> list:
        """
        获取用户对话历史
        
        Args:
            user_id: 用户ID
        
        Returns:
            消息列表
        """
        if user_id not in self.store:
            return []
        return self.store[user_id].messages
    
    def clear_history(self, user_id: str = "default"):
        """
        清除用户对话历史
        
        Args:
            user_id: 用户ID
        """
        if user_id in self.store:
            self.store[user_id].clear()
        return "历史已清除"
