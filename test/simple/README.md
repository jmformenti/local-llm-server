# README

Use your local LLM as Open AI replacement.

Run it with [uv](https://github.com/astral-sh/uv):
```
export MODEL=qwen3:0.6b
docker compose exec ollama-gpu ollama pull $MODEL
uv run --with langchain[openai] test/simple/simple.py
```
