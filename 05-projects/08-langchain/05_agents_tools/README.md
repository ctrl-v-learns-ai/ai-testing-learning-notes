# Multi-function AI Assistant

## Project Overview
An AI assistant with multiple tools: weather lookup, calculator, and knowledge base search.

## Features
- Weather lookup for cities
- Math calculation
- Knowledge base search
- Multi-turn conversation with memory

## How to Run
```bash
pip install -r requirements.txt
python main.py
```

## Core Concepts
1. Tool creation with @tool decorator
2. Agent creation with create_agent
3. Multi-tool agent execution
4. Conversation memory integration

## Project Structure
```
05-projects/05_agents_tools/
  main.py           # Entry point
  agent.py          # Agent class
  tools.py          # Tool definitions
  config.py         # Configuration
  requirements.txt
  README.md
```
