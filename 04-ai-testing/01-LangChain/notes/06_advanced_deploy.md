# Stage 6: Advanced & Deploy

## Streaming Output

### Why Streaming?
- Better UX: show results as they generate
- Lower perceived latency
- Real-time feedback

### How to Use Streaming

```python
# Method 1: stream()
for chunk in chain.stream({"input": "hello"}):
    print(chunk, end="", flush=True)

# Method 2: astream() for async
async for chunk in chain.astream({"input": "hello"}):
    print(chunk, end="", flush=True)
```

### Streaming in FastAPI

```python
from fastapi.responses import StreamingResponse

@app.post("/chat/stream")
async def chat_stream(question: str):
    async def generate():
        async for chunk in chain.astream({"input": question}):
            yield chunk
    return StreamingResponse(generate(), media_type="text/plain")
```

---

## Error Handling

### Retry Mechanism

```python
from langchain_core.runnables import RunnableRetry

# Add retry to any chain
chain_with_retry = chain.with_retry(
    stop_after_attempt=3,
    wait_exponential_jitter=True
)
```

### Fallback Chains

```python
from langchain_core.runnables import RunnableFallback

# Define fallback
fallback_chain = RunnableFallback(
    fallbacks=[backup_chain]
)

# Use fallback
result = fallback_chain.invoke({"input": "hello"})
```

### Try-Except in Chain

```python
from langchain_core.runnables import RunnableLambda

def safe_process(input_data):
    try:
        return chain.invoke(input_data)
    except Exception as e:
        return f"Error: {e}"

safe_chain = RunnableLambda(safe_process)
```

---

## LangServe Deployment

### What is LangServe?
LangServe deploys LangChain chains as REST APIs.

### Basic Deployment

```python
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI()
add_routes(app, chain, path="/chat")

# Run: uvicorn app:app --reload
```

### With Custom Endpoints

```python
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI()

# Add chain routes
add_routes(app, summary_chain, path="/summary")
add_routes(app, qa_chain, path="/qa")

# Custom endpoint
@app.post("/custom")
async def custom_endpoint(input: str):
    return {"result": chain.invoke({"input": input})}
```

---

## LangSmith Monitoring

### What is LangSmith?
- Observability platform for LLM apps
- Trace execution, debug errors, monitor performance

### Setup

```python
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-api-key"
os.environ["LANGCHAIN_PROJECT"] = "my-project"
```

### Trace Example

```python
# All chain calls are automatically traced
result = chain.invoke({"input": "hello"})
# View traces at: https://smith.langchain.com
```

---

## Comprehensive RAG Application

### Features
1. Document upload and processing
2. Vector store with FAISS
3. Conversational memory
4. Streaming responses
5. REST API with FastAPI

### Architecture

```
User -> FastAPI -> RAG Chain -> LLM -> Response
              |
              v
         Vector Store (FAISS)
              |
              v
         Document Loader
```

---

## Common Pitfalls

### 1. Streaming Not Working
```python
# Wrong: Using invoke instead of stream
result = chain.invoke({"input": "hello"})

# Correct: Use stream
for chunk in chain.stream({"input": "hello"}):
    print(chunk, end="")
```

### 2. Error Not Handled
```python
# Wrong: No error handling
result = chain.invoke({"input": "hello"})

# Correct: With retry
chain_with_retry = chain.with_retry(stop_after_attempt=3)
result = chain_with_retry.invoke({"input": "hello"})
```

### 3. LangSmith Not Tracing
```python
# Wrong: Missing environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
# Missing API key

# Correct: Set all required variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-key"
```

---

## Cheatsheet

### Streaming
```python
for chunk in chain.stream(input):
    print(chunk, end="")
```

### Retry
```python
chain.with_retry(stop_after_attempt=3)
```

### LangServe
```python
from langserve import add_routes
add_routes(app, chain, path="/api")
```

### LangSmith
```python
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "key"
```

---

## Quiz

1. **Why use streaming instead of invoke?**
2. **How does retry mechanism work?**
3. **What is LangServe used for?**
4. **How to enable LangSmith tracing?**
5. **What are the key components of a production RAG app?**

---

## Further Reading

- [LangChain Streaming](https://docs.langchain.com/oss/python/langchain/streaming)
- [LangServe Documentation](https://docs.langchain.com/oss/python/langchain/langserve)
- [LangSmith](https://smith.langchain.com)
