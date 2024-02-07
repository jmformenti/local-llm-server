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
  * `MODEL`. One from the [ollama model library](https://ollama.ai/library).

2. Run docker compose.
  ```
  docker compose up -d
  ```

## Access to the services

* UI: http://localhost:3000
* OpenAI API: http://localhost:8000

## Other interesting commands

Common docker compose commands useful in daily execution:
1. Stop.
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

llm = ChatOpenAI(openai_api_base="http://localhost:8000", openai_api_key="ignored", model="mixtral", temperature=0.1)

print(llm.invoke("Who are you?"))
```
