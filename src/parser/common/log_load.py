# coding: utf-8
import logging
from typing import Union
from ...logger import log_handle
# region Logger
_logger: logging.Logger = None

def get_logger(use_default: bool = False) -> logging.Logger:
    """
    Get global logger

    Args:
        use_default (bool, optional): If True a default logger will be returned
            if global logger is ``None``. Defaults to ``False``.

    Returns:
        logging.Logger: logger
    """
    global _logger
    if use_default is True and _logger is None:
        _logger = log_handle.get_logger('parse.log')
    return _logger


def set_logger(l: Union[logging.Logger, None]):
    """
    Sets global logger

    Args:
        l (Union[logging.Logger, None]): logger that is assiged to global logger.
    """
    global _logger
    _logger = l
