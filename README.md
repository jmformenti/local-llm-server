# Run LLM in local for development

Run easily a LLM in local as backend for development along with a Chat UI.

Using [Ollama](https://github.com/ollama/ollama) and [Open WebUI](https://github.com/open-webui/open-webui).

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

* UI: http://localhost:3003
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
5. Update all the containers.
```
docker compose up --build -d
```

## Code examples

* [Simple](./test/simple). Using your local LLM as Open AI replacement.
* [Multi MCP client](./test/mcp_demo). Using a multi MCP client with your local LLM.
