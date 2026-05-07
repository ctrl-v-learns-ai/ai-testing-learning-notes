# -*- coding: utf-8 -*-
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from config import API_KEY, API_URL, MODEL_NAME, TEMPERATURE
from tools import ALL_TOOLS


class MultiToolAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=MODEL_NAME,
            api_key=API_KEY,
            base_url=API_URL,
            temperature=TEMPERATURE,
        )

        self.agent = create_agent(
            self.llm,
            tools=ALL_TOOLS,
            system_prompt="""You are a helpful AI assistant with access to these tools:
- get_weather: Get weather for a city
- calculator: Calculate math expressions
- search_knowledge: Search knowledge base
- get_current_time: Get current time

Use these tools to help answer user questions."""
        )

        self.history = []

    def chat(self, user_input: str) -> str:
        result = self.agent.invoke({
            "messages": [("human", user_input)]
        })
        response = result["messages"][-1].content

        self.history.append({"role": "user", "content": user_input})
        self.history.append({"role": "assistant", "content": response})

        return response

    def clear_history(self):
        self.history = []
        return "History cleared"
