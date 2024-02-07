#!/bin/bash

OLLAMA_API_URL=http://ollama:11434/api

export MODEL_NAME=${MODEL%%:*}
envsubst < /app/litellm-config.yaml.template > /app/proxy_server_config.yaml

if ! curl -s $OLLAMA_API_URL/tags | jq --arg model "$MODEL" --arg model_latest "$MODEL_NAME:latest" '.models[].name == $model or .models[].name == $model_latest' | grep -q true; then
  echo "Pulling $MODEL .."
  curl -s $OLLAMA_API_URL/pull -d "{ \"name\": \"$MODEL\", \"stream\": false }"
  echo "done."
fi

litellm "$@"
