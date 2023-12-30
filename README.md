# Run LLM in local for development

Run quickly a LLM in local as backend for development along with a Chat UI.

Main points:
 - Using the [Mistral 8x7b (MoE)](https://mistral.ai/news/mixtral-of-experts/) model, in particular [the variant GGUF](https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF) published in HuggingFace.
 - API server using [llama-cpp-python](https://github.com/abetlen/llama-cpp-python), that you can use it as a replacement for Open AI.
 - [Chat UI from HuggingFace](https://github.com/huggingface/chat-ui).

All installed using docker compose.

## Requirements

* Assumption that you have GPU installed (not tested only with CPU).
* docker compose (recommended V2).
* [nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) installed.

## Install

1. Download the model.
```
mkdir model
wget https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF/resolve/main/mixtral-8x7b-instruct-v0.1.Q5_K_M.gguf?download=true -O ./model/mixtral-8x7b-instruct-v0.1.Q5_K_M.gguf
```
3. Adapt the settings to your environment: `chatui.env` and `llm.env`.
	* IMPORTANT: Adapt `N_GPU_LAYERS` parameter to your GPU memory (default 22 layers, assuming 24GB).
	* In llm.env you can add more configuration parameters as environment variables, check TODO.
4. Run docker compose.
```
docker compose up -d
```

## Access to the services

After start the services, you can access to the UI: http://localhost:3000
The API is exposed in: http://localhost:8000

## Other interesting commands

Common docker composer commands useful in daily execution:
1. Stop.
```
docker compose stop
```
3. Show logs.
```
docker compose logs -f
```
4. Remove.
```
docker compose down -v
```

## Use you local LLM as Open AI replacement

Example using langchain:
```
from langchain.llms import OpenAI

llm = OpenAI(openai_api_base="http://localhost:8000/v1", openai_api_key="dummy")

print(llm("[INST] Who are you? [/INST]"))
```
Note that the prompt is enclosed by *[INST]* because we are using an instruction model trained this way, check the [model card](https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF).