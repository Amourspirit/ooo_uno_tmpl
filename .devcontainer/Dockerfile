FROM dockdock/libreoffice-api-dev:LO-7.5 as builder

USER root

WORKDIR /workspace/ooo_uno_tmpl

COPY ./pyproject.toml ./poetry.lock ./poetry.toml ./

RUN poetry install --no-root


FROM dockdock/libreoffice-api-dev:LO-7.5 as runner

ARG PY_VER=3.10
ARG GIT_AUTHOR_NAME=""
ARG GIT_AUTHOR_EMAIL=""

USER root
ENV HOME /root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    nano \
    git \
    gnupg \
    jq \
    make \
    openssh-client \
    unzip \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace/ooo_uno_tmpl

COPY --from=builder /workspace/ooo_uno_tmpl/.venv ./.venv


ENV VIRTUAL_ENV=/workspace/ooo_uno_tmpl/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN if [ x"$GIT_AUTHOR_NAME" != "x" ]; then git config --global user.name "$GIT_AUTHOR_NAME" || true; fi \
    && if [ x"$GIT_AUTHOR_EMAIL" != "x" ]; then git config --global user.email $GIT_AUTHOR_EMAIL || true; fi

WORKDIR $HOME

COPY ./.devcontainer/custom_bash.txt ./.bashrc_custom

ARG WD=/workspace/ooo_uno_tmpl/.venv/lib/python$PY_VER/site-packages

WORKDIR ${WD}

RUN ln -s /usr/lib/python3/dist-packages/uno.py uno.py \
    && ln -s /usr/lib/python3/dist-packages/unohelper.py unohelper.py \
    && echo "/workspace/ooo_uno_tmpl" >> ooo_dev_tools.pth
# Enable venv
# ENV PATH="/opt/venv/bin:$PATH"

