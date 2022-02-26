# coding: utf-8
import logging
from typing import Union

# region Logger
_logger: logging.Logger = None

def get_logger() -> logging.Logger:
    global _logger
    return _logger


def set_loggers(l: Union[logging.Logger, None]):
    global _logger
    _logger = l
