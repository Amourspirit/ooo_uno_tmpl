# coding: utf-8
import pytest
import logging
import os
import sys
from pathlib import Path
sys.path.append(os.path.realpath('.'))
from src.logger.log_handle import get_logger

@pytest.fixture(scope='session')
def test_log():
    log = get_logger('test', log_file='test.log', log_level=logging.DEBUG, add_handler_file=False)
    return log

@pytest.fixture(scope="session")
def scrtch_uno_path() -> Path:
    return Path('scratch') / 'uno_obj'

@pytest.fixture(scope='session')
def app_root() -> Path:
    return Path(__file__).parent.parent



