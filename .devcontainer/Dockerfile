FROM dockdock/libreoffice73pyenvpoetry:lo-7.5.3-RELEASE

# Set Python version
ARG PYTHON_VERSION='3.8.15'
ARG HOME_DIR=/workspaces/ooo_uno_tmpl
ENV PYTHONPATH=$HOME_DIR

RUN pyenv install $PYTHON_VERSION \
    && pyenv global $PYTHON_VERSION

RUN pip install --upgrade pip \
    && pyenv rehash \
    && rm -rf ~/.cache/pip \
    && poetry config virtualenvs.in-project true \
    && poetry config virtualenvs.prefer-active-python true \
    && git config --global --add safe.directory '*'

ENV PYENV_SHIMS="$HOME/.pyenv/shims/python"