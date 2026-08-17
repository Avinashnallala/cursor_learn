# MCP Multi-Server AI Agent

A hands-on AI Agent project demonstrating how **Model Context Protocol (MCP)** can connect a LangChain agent with multiple external tools using different MCP transports.

## 🚀 Project Overview

This project demonstrates a multi-server MCP architecture where an AI agent can discover and execute tools exposed by different MCP servers.

The application integrates:

* Model Context Protocol (MCP)
* LangChain
* Groq
* FastMCP
* Async Python
* stdio transport
* Streamable HTTP transport

## 🏗️ Architecture

```text
                    User
                      |
                      v
               LangChain Agent
                      |
                      v
                  Groq LLM
                      |
                      v
             MultiServerMCPClient
                  /          \
                 /            \
                v              v
         Math MCP Server   Weather MCP Server
             stdio         Streamable HTTP
                |               |
                v               v
        add / multiply      get_weather
```

## 🧠 How It Works

The MCP client connects to multiple MCP servers and retrieves the tools exposed by them.

These tools are provided to the LangChain agent.

When the user submits a question, the LLM determines whether a tool is required and selects the appropriate MCP tool.

Example:

```text
User
 |
 | "What is (3+5)*12?"
 v
AI Agent
 |
 v
Math MCP Server
 |
 +--> add(3,5)
 |
 +--> multiply(8,12)
 |
 v
96
```

## 🛠️ Math MCP Server

The Math MCP server exposes mathematical operations as MCP tools.

Available tools:

* `add(a, b)`
* `multiply(a, b)`

Transport:

```text
stdio
```

## 🌦️ Weather MCP Server

The Weather MCP server demonstrates exposing a weather function through MCP.

Available tool:

* `get_weather(location)`

Transport:

```text
streamable-http
```

## 🤖 AI Agent

The AI agent is built using LangChain and Groq.

The agent receives all tools discovered through the MCP client and determines which tool should be executed based on the user's request.

## 📂 Project Structure

```text
mcp-project/
│
├── client.py
├── mathserver.py
├── weather.py
├── main.py
├── requirements.txt
├── pyproject.toml
├── uv.lock
├── .python-version
├── .env
└── .gitignore
```

## 📦 Main Dependencies

```text
langchain
langchain-groq
langchain-mcp-adapters
langgraph
mcp
```

## ▶️ Running the Project

Install the dependencies:

```bash
uv sync
```

Start the Weather MCP server:

```bash
uv run python weather.py
```

Then open another terminal and run:

```bash
uv run python client.py
```

The Math MCP server uses `stdio`, so the MCP client launches it as a subprocess.

The Weather MCP server runs separately using Streamable HTTP.

## 🧪 Example Queries

### Math

```text
What is (3+5)*12?
```

### Weather

```text
What is the weather in California?
```

## 🎯 What I Learned

Through this project, I explored:

* Model Context Protocol fundamentals
* Creating MCP servers using FastMCP
* Creating custom MCP tools
* Connecting multiple MCP servers
* stdio transport
* Streamable HTTP transport
* LangChain agent development
* LLM tool calling
* Groq LLM integration
* Async Python programming
* Modular AI agent architecture

## 🔮 Future Improvements

The architecture can be extended with additional MCP servers such as:

```text
AI Agent
   |
   +-- Math MCP Server
   |
   +-- Weather MCP Server
   |
   +-- Database MCP Server
   |
   +-- Files MCP Server
   |
   +-- REST API MCP Server
   |
   +-- RAG MCP Server
```

Future versions can integrate real weather APIs, SQL databases, vector databases, document retrieval, and enterprise APIs.

## ⭐ Technologies

`Python` `MCP` `FastMCP` `LangChain` `LangGraph` `Groq` `AsyncIO` `AI Agents` `LLM Tool Calling`

---

If you find this project useful, feel free to ⭐ the repository.
