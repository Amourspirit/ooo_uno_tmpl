# coding: utf-8
import pytest
from pathlib import Path

@pytest.fixture(scope='session')
def app_root() -> Path:
    return Path(__file__).parent
