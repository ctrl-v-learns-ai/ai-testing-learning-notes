# -*- coding: utf-8 -*-
"""
Exercise 2: Error Handling and Retry
Goal: Learn to handle errors and implement retry
Prerequisites: LCEL chains
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
    api_key=os.getenv("MIMO_API_KEY"),
    base_url=os.getenv("MIMO_API_URL"),
    temperature=0.7,
)

# Exercise 2.1: Basic Error Handling
print("=== Basic Error Handling ===")

def safe_invoke(chain, input_data):
    try:
        result = chain.invoke(input_data)
        return {"success": True, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("human", "{input}")
])

chain = prompt | llm | StrOutputParser()

result = safe_invoke(chain, {"input": "Hello"})
print(f"Result: {result}")

# Exercise 2.2: Retry Mechanism
print("\n=== Retry Mechanism ===")

# Add retry to chain
chain_with_retry = chain.with_retry(
    stop_after_attempt=3,
)

print("Chain with retry created")

# Exercise 2.3: Fallback Chain
print("\n=== Fallback Chain ===")

def fallback_response(input_data):
    return "Sorry, I encountered an error. Please try again."

fallback = RunnableLambda(fallback_response)

# Test fallback
try:
    result = chain.invoke({"input": "test"})
    print(f"Success: {result}")
except Exception as e:
    print(f"Error, using fallback: {fallback.invoke({'input': 'test'})}")

"""
Questions:
1. Why is error handling important in production?
2. What is the difference between retry and fallback?
3. How to set appropriate retry attempts?
"""
