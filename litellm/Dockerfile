FROM ghcr.io/berriai/litellm:main-latest

WORKDIR /app

RUN apt-get update && \
    apt-get install -y gettext jq && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /app/entrypoint.sh
COPY litellm-config.yaml.template /app/litellm-config.yaml.template

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["--config", "/app/proxy_server_config.yaml"]
