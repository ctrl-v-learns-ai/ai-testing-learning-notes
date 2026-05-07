# Agent 与 Tool

## Agent
Agent = LLM + Tools + 决策循环

类比：Agent 像一个有工具箱的助手，能根据问题选择合适的工具。

## ReAct 流程
1. 用户提问
2. LLM 思考需要做什么
3. LLM 选择工具并执行
4. 获取结果，判断是否完成
5. 未完成则继续，完成则返回答案

## 创建 Tool
```python
from langchain_core.tools import tool

@tool
def search_web(query: str) -> str:
    # Tool description is the function docstring
    return f"Search results for: {query}"
```

## 创建 Agent
```python
from langchain.agents import create_agent

agent = create_agent(
    model="openai:gpt-4",
    tools=[search_web, calculator],
    system_prompt="You are a helpful assistant"
)
```

## 调用 Agent
```python
result = agent.invoke({
    "messages": [("human", "What is the weather today?")]
})
print(result["messages"][-1].content)
```

## 注意事项
1. Tool 描述要清晰（LLM 根据描述选择工具）
2. Tool 返回字符串
3. 设置 max_iterations 防止无限循环
