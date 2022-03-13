# coding: utf-8
import os
import pytest
from pathlib import Path


@pytest.fixture(scope='session')
def root_path(app_root) -> Path:
    os.environ['project_root'] = str(app_root)
    return app_root
