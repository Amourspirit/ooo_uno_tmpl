# coding: utf-8
import pytest
import logging
import os
import sys
sys.path.append(os.path.realpath('.'))
from logger.log_handle import get_logger

@pytest.fixture(scope='session')
def test_log():
    log = get_logger('test', log_file='test.log', log_level=logging.DEBUG, add_handler_file=False)
    return log
