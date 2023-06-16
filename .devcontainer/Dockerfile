FROM mcr.microsoft.com/devcontainers/base:jammy

# Configure Poetry
ENV POETRY_VERSION=1.5.1


# Install poetry separated from system interpreter
RUN apt-get update && apt-get -y install \
    python3-cheetah \
    python3-pip \
    python3.10-venv \
    && python3 -m pip install "poetry==$POETRY_VERSION"
    # && python3 -m pip install pipx \
    # && python3 -m pipx ensurepath

RUN poetry config virtualenvs.in-project true

