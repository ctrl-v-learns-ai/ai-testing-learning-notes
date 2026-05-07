# -*- coding: utf-8 -*-
"""
Exercise 1: Create Tool
Goal: Learn to create tools using @tool decorator
Prerequisites: Python functions, type hints
"""

import os
from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()

# Exercise 1.1: Basic Tool
print("=== Basic Tool ===")

@tool
def calculator(expression: str) -> str:
    """Calculate a math expression. Input should be a valid math expression like '2 + 3 * 4'."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

# Test the tool
result = calculator.invoke({"expression": "2 + 3 * 4"})
print(f"2 + 3 * 4 = {result}")

# Exercise 1.2: Tool with multiple parameters
print("\n=== Tool with Multiple Parameters ===")

@tool
def search_database(query: str, limit: int = 5) -> str:
    """Search a database. query is the search term, limit is max results."""
    # Simulated database search
    fake_results = [
        {"id": i, "title": f"Result {i} for {query}"}
        for i in range(1, limit + 1)
    ]
    return str(fake_results)

result = search_database.invoke({"query": "python", "limit": 3})
print(f"Search results: {result}")

# Exercise 1.3: Check tool metadata
print("\n=== Tool Metadata ===")
print(f"Tool name: {calculator.name}")
print(f"Tool description: {calculator.description}")
print(f"Tool args: {calculator.args_schema.model_json_schema() if calculator.args_schema else 'None'}")

"""
Questions:
1. What is the purpose of the docstring in @tool?
2. What happens if the tool returns None?
3. Why should tool descriptions be clear?
"""
