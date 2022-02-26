# coding: utf-8
import logging
from typing import Union
from ...logger import log_handle
# region Logger
logger: logging.Logger = None

class Log:
    """Singleton Class Log helper for parsers"""
    _instance = None
    _logger: logging.Logger = None

    def __new__(cls, *args, **kwargs):
        # single instance only allowed
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    @property
    def logger(self) -> logging.Logger:
        return self._logger
    
    @logger.setter
    def logger(self, value: logging.Logger) -> None:
        self._logger = value

__all__ = ['Log']