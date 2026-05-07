# -*- coding: utf-8 -*-
"""
Exercise 3: FastAPI Deployment
Goal: Learn to deploy chains as REST API
Prerequisites: FastAPI basics, LCEL chains
"""

# Exercise 3.1: Basic FastAPI with LangServe
print("=== FastAPI Deployment Example ===")

example_code = """
from fastapi import FastAPI
from langserve import add_routes
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

app = FastAPI()

# Create chain
llm = ChatOpenAI(model="gpt-4")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("human", "{input}")
])
chain = prompt | llm | StrOutputParser()

# Add routes
add_routes(app, chain, path="/chat")

# Run: uvicorn main:app --reload
"""

print("Example FastAPI code:")
print(example_code)

# Exercise 3.2: Custom Endpoint
print("=== Custom Endpoint Example ===")

custom_endpoint = """
@app.post("/custom")
async def custom_endpoint(input: str):
    result = chain.invoke({"input": input})
    return {"response": result}
"""

print("Custom endpoint:")
print(custom_endpoint)

# Exercise 3.3: Streaming Endpoint
print("\n=== Streaming Endpoint ===")

streaming_endpoint = """
from fastapi.responses import StreamingResponse

@app.post("/stream")
async def stream_endpoint(input: str):
    async def generate():
        async for chunk in chain.astream({"input": input}):
            yield chunk
    return StreamingResponse(generate(), media_type="text/plain")
"""

print("Streaming endpoint:")
print(streaming_endpoint)

"""
Questions:
1. What is LangServe used for?
2. How to add custom endpoints?
3. How to implement streaming in FastAPI?
"""
