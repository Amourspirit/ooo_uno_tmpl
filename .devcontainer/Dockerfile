FROM mcr.microsoft.com/devcontainers/base:jammy

# Configure Poetry
ENV POETRY_VERSION=1.5.1


# Install poetry separated from system interpreter
RUN apt-get update \
    && apt-get -y install python3-cheetah \
    && apt-get -y install python3-pip \
    && apt-get -y install python3.10-venv \
    && python3 -m pip install "poetry==$POETRY_VERSION"
    # && python3 -m pip install pipx \
    # && python3 -m pipx ensurepath

# Add `pipx` to PATH
# ENV PATH="${PATH}:/root/.local/bin"

# RUN pipx install poetry==${POETRY_VERSION}

# Copy only requirements to cache them in docker layer
# WORKDIR /code
# COPY poetry.lock pyproject.toml /code/

# Creating folders, and files for a project:
# COPY . /code

