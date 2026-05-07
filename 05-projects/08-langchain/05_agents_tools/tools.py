# -*- coding: utf-8 -*-
from langchain_core.tools import tool


@tool
def get_weather(city: str) -> str:
    """Get weather information for a city. Input is the city name."""
    weather_data = {
        "Beijing": "Beijing: Sunny, 25 degrees Celsius",
        "Shanghai": "Shanghai: Cloudy, 22 degrees Celsius",
        "Guangzhou": "Guangzhou: Rainy, 28 degrees Celsius",
        "Shenzhen": "Shenzhen: Partly cloudy, 27 degrees Celsius",
    }
    return weather_data.get(city, f"No weather data available for {city}")


@tool
def calculator(expression: str) -> str:
    """Calculate a math expression. Input should be a valid expression like '2 + 3 * 4'."""
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Calculation error: {e}"


@tool
def search_knowledge(topic: str) -> str:
    """Search the knowledge base for information about a topic."""
    knowledge = {
        "Python": "Python is a high-level programming language known for its readability.",
        "testing": "Software testing is the process of evaluating software to find defects.",
        "AI": "Artificial Intelligence is the simulation of human intelligence by machines.",
        "LangChain": "LangChain is a framework for building LLM-powered applications.",
    }
    return knowledge.get(topic, f"No information found about {topic}")


@tool
def get_current_time() -> str:
    """Get the current date and time."""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


ALL_TOOLS = [get_weather, calculator, search_knowledge, get_current_time]
