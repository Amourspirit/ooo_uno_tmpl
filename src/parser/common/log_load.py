# coding: utf-8
import logging
from typing import Union
from ...logger import log_handle
# region Logger
_logger: logging.Logger = None

def get_logger() -> logging.Logger:
    global _logger
    if _logger is None:
        _logger = log_handle.get_logger('parse.log')
    return _logger


def set_logger(l: Union[logging.Logger, None]):
    global _logger
    _logger = l
