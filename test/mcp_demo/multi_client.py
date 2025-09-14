import asyncio

from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent


def print_response(response):
    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"
    LIGHT_GRAY = "\033[90m"

    messages = response.get('messages', [])
    
    if not messages:
        print("No messages.")
        return

    for idx, msg in enumerate(messages):
        msg = msg.content
        if idx == 0:
            print(f"\n\n{LIGHT_GRAY}Input:\n{RED}{msg}{RESET}")
        elif idx == len(messages) - 1:
            print(f"\n{LIGHT_GRAY}Final output:\n{GREEN}{msg}{RESET}")
        else:
            print(f'\n{LIGHT_GRAY}Message {idx}:{RESET}\n{msg}')


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "transport": "stdio",
                "command": "python",
                "args": ["math_server.py"],
            },
            "weather": {
                "transport": "streamable_http",
                "url": "http://localhost:8000/mcp",
            },
            "web-search": {
                "transport": "streamable_http",
                "url": "http://localhost:3003/mcp",
            }
        })

    model = ChatOpenAI(openai_api_base="http://localhost:11434/v1", openai_api_key="ignored", model='qwen3:0.6b')
    tools = await client.get_tools()

    agent = create_react_agent(model, tools, prompt="Use the addition and multiplication tools to perform basic arithmetic calculations.")

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12 ?"}]}
    )
    print_response(math_response)

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in Terrassa?"}]}
    )
    print_response(weather_response)

    web_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "can you search the web for Paul Graham?"}]}
    )
    print_response(web_response)


if __name__ == "__main__":
    asyncio.run(main())
