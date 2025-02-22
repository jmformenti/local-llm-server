# Run LLM in local for development

Run quickly a LLM in local as backend for development along with a Chat UI.

Using [Ollama](https://github.com/ollama/ollama) and [LiteLLM](https://github.com/BerriAI/litellm).

All installed via docker compose.

## Requirements

* docker compose (recommended V2).
* [nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) installed if you have gpu.

## Install

1. Configure `.env`.
  * `COMPOSE_PROFILES`. `gpu` (you need nvidia-container-toolkit installed) or `cpu`.

2. Run docker compose.
  ```
  docker compose up -d
  ```

## Access to the services

* UI: http://localhost:3000
* OpenAI API: http://localhost:11434

## Other interesting commands

Common docker compose commands useful in daily execution:
1. Download a [ollama model](https://ollama.com/library) from cli:
```
docker compose exec ollama-gpu ollama pull <model_name>
```
2. Stop.
```
docker compose stop
```
3. Show logs.
```
docker compose logs -f
```
4. Remove all.
```
docker compose down -v
```

## Use your local LLM as Open AI replacement

Example using Langchain:
```
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(openai_api_base="http://localhost:11434/v1", openai_api_key="ignored", model=<model>)

print(llm.invoke("Who are you?"))
```

Run it with [uv](https://github.com/astral-sh/uv):
```
export MODEL=qwen2.5:0.5b
docker compose exec ollama-gpu ollama pull $MODEL
uv run --with langchain[openai] test/simple.py
```
