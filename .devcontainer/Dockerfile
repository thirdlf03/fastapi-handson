FROM ubuntu:latest

RUN apt update && apt upgrade -y  \
    && apt install -y curl git \
    && curl -LsSf https://astral.sh/uv/install.sh | sh

RUN mkdir -p ./opt/workspace


