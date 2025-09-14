# README

Simple example for a multi MCP client using Langchain, based on [Model Context Protocol (MCP) LangChain docs](https://docs.langchain.com/oss/python/langchain/mcp).

Three examples:
1. Using an MCP server with `stdio`.
2. Using an MCP server for web search from [Claude MCP](https://www.claudemcp.com/servers/open-websearch) running locally.
3. Creating a simple `http` MCP server and runing it locally.

## Run

1. Prepare the environment using [uv](https://github.com/astral-sh/uv).
```
uv sync
```
1. Run the web search MCP server.
```
docker run -d --name web-search -p 3003:3000 -e ENABLE_CORS=true -e CORS_ORIGIN=* -e DEFAULT_SEARCH_ENGINE=duckduckgo -e ALLOWED_SEARCH_ENGINES=duckduckgo ghcr.io/aas-ee/open-web-search:latest
```
2. Run our HTTP MCP server.
```
uv run weather_server.py
```
3. Run the client.
```
uv run multi_client.py
```
