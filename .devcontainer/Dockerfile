FROM dockdock/libreoffice73pyenvpoetry:lo-7.5.3-RELEASE
ARG HOME_DIR=/workspaces/libreoffice-modern-code-editing-py
ENV PYTHONPATH=$HOME_DIR
RUN poetry config virtualenvs.in-project true \
    && git config --global --add safe.directory '*'