# -*- coding: utf-8 -*-
"""
Exercise 1: Streaming Output
Goal: Learn to implement streaming responses
Prerequisites: LCEL chains
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("MIMO_MODEL", "mimo-v2-flash"),
    api_key=os.getenv("MIMO_API_KEY"),
    base_url=os.getenv("MIMO_API_URL"),
    temperature=0.7,
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("human", "{input}")
])

chain = prompt | llm | StrOutputParser()

# Exercise 1.1: Basic Streaming
print("=== Basic Streaming ===")
print("Response: ", end="", flush=True)

for chunk in chain.stream({"input": "Explain what is software testing in 3 sentences"}):
    print(chunk, end="", flush=True)

print()

# Exercise 1.2: Collect chunks
print("\n=== Collect Chunks ===")
chunks = []
for chunk in chain.stream({"input": "List 3 programming languages"}):
    chunks.append(chunk)

full_response = "".join(chunks)
print(f"Full response ({len(chunks)} chunks): {full_response}")

"""
Questions:
1. What is the difference between stream() and invoke()?
2. When should you use streaming?
3. How to handle streaming errors?
"""
