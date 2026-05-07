# -*- coding: utf-8 -*-
"""
Exercise 2: Create Agent
Goal: Learn to create and use agents
Prerequisites: Tool creation, ChatModel
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
    api_key=os.getenv("MIMO_API_KEY"),
    base_url=os.getenv("MIMO_API_URL"),
    temperature=0,
)

# Create tools
@tool
def get_weather(city: str) -> str:
    """Get weather information for a city."""
    # Simulated weather data
    weather_data = {
        "Beijing": "Sunny, 25 degrees",
        "Shanghai": "Cloudy, 22 degrees",
        "Guangzhou": "Rainy, 28 degrees",
    }
    return weather_data.get(city, f"No weather data for {city}")

@tool
def calculator(expression: str) -> str:
    """Calculate a math expression."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

# Create Agent using bind_tools
print("=== Agent with bind_tools ===")

llm_with_tools = llm.bind_tools([get_weather, calculator])

# Test: Ask a question that requires tool use
from langchain_core.messages import HumanMessage

response = llm_with_tools.invoke([HumanMessage(content="What is the weather in Beijing?")])
print(f"Response: {response.content}")

# Check if tool calls were made
if hasattr(response, 'tool_calls') and response.tool_calls:
    print(f"Tool calls: {response.tool_calls}")
else:
    print("No tool calls made")

"""
Questions:
1. What is bind_tools used for?
2. How does the LLM decide which tool to use?
3. What is the difference between bind_tools and create_agent?
"""
