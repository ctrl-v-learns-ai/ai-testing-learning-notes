# -*- coding: utf-8 -*-
"""
Exercise 3: Multi-tool Agent
Goal: Build an agent with multiple tools
Prerequisites: Tool creation, Agent basics
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
    api_key=os.getenv("MIMO_API_KEY"),
    base_url=os.getenv("MIMO_API_URL"),
    temperature=0,
)

# Define multiple tools
@tool
def get_weather(city: str) -> str:
    """Get weather for a city."""
    weather = {"Beijing": "Sunny 25C", "Shanghai": "Cloudy 22C"}
    return weather.get(city, "Unknown city")

@tool
def calculate(expression: str) -> str:
    """Calculate math expression."""
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"

@tool
def search_knowledge(topic: str) -> str:
    """Search knowledge base for a topic."""
    knowledge = {
        "Python": "Python is a popular programming language",
        "testing": "Software testing ensures quality",
        "AI": "AI is artificial intelligence"
    }
    return knowledge.get(topic, f"No info about {topic}")

# Create agent with multiple tools
agent = create_agent(
    llm,
    tools=[get_weather, calculate, search_knowledge],
    system_prompt="You are a helpful assistant with access to weather, calculator, and knowledge tools."
)

# Test multi-tool agent
print("=== Multi-tool Agent ===")

questions = [
    "What is the weather in Beijing?",
    "Calculate 15 * 23 + 7",
    "Tell me about Python",
]

for q in questions:
    print(f"\nQ: {q}")
    result = agent.invoke({"messages": [("human", q)]})
    print(f"A: {result['messages'][-1].content}")

"""
Questions:
1. How does the agent decide which tool to use?
2. Can the agent use multiple tools in one response?
3. What happens if the tool description is unclear?
"""
