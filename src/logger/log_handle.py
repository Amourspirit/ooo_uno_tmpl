# coding: utf-8
"""
Module responsible for getting and managing logging.
"""
import logging
import sys
import re
from pathlib import Path
from typing import Union
from ..utilities import util
# from logging.handlers import TimedRotatingFileHandler

FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = 'app.log'
LOG_LEVEL = logging.INFO
LOG_FILE_HANDLER = None
"""
This is the last file handler created using ``get_file_handler()`` method
"""
    
def _parse_log_options():
    global LOG_FILE, LOG_LEVEL
    if len(sys.argv) <= 1:
        LOG_LEVEL = logging.INFO
        # LOG_FILE = Path(__file__).parent.parent / 'app.log'
        LOG_FILE = Path(util.get_root()) / 'app.log'
        return

    args_str = " ".join(sys.argv[1:])
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    if any(map(lambda v: v in opts, ("-v", '--verbose'))):
        LOG_LEVEL = logging.DEBUG

    p = LOG_FILE
    regex = r"((?:-L|--log-file)\s(?P<LOG_FILE>.*?)(?:\s|$))"
    matches = re.search(regex, args_str)
    if matches:
        # print(m)
        p = matches.group('LOG_FILE').strip()
    try:
        if p == LOG_FILE:
            LOG_FILE = Path(__file__).parent.parent / p
            return
        tmp_p = Path(p)
        if tmp_p.is_file():
            return
        if tmp_p.is_absolute():
            LOG_FILE = tmp_p
            return
        LOG_FILE = Path(Path(__file__).parent.parent, tmp_p)
        return
    except Exception:
        pass
    # LOG_FILE = Path(__file__).parent.parent / "app.log"
    LOG_FILE = Path(util.get_root()) / 'app.log'

_parse_log_options()

def get_console_handler():
    """
    Gets a terminal handler

    Returns:
        StreamHandler: Stream Handler
    """
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler(log_file: Union[str, Path, None] = None):
    """
    Gets a file handler for usage with logger.
    The file handler created in this method will be stored in LOG_FILE_HANDLER.

    Arguments:
        log_file (StrPath, optional): name of file for the handler.
        Default is the value of global var ``LOG_FILE``

    Returns:
        FileHandler: File Handler
    """
    # https://docs.python.org/3/library/logging.handlers.html#timedrotatingfilehandler
    # W0 rotate every monday.
    # file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    global LOG_FILE_HANDLER
    if not log_file:
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(FORMATTER)
    else:
        p_log: Path = log_file
        if isinstance(log_file, str):
            p_log = Path(Path(util.get_root()), log_file)
        file_handler = logging.FileHandler(p_log)
        file_handler.setFormatter(FORMATTER)
    LOG_FILE_HANDLER = file_handler
    return LOG_FILE_HANDLER


def get_logger(logger_name, **kwargs):
    """
    Gets a logger

    Args:
        logger_name (str): name of logger
    
    Keyword Args:
        log_file (str, Path, optional): Log file to use. Default is valie of ``LOG_FILE``
        level (int, optional): Logger logging level. Default is value of ``LOG_LEVEL``
        add_handler_file (bool, optional): If ``True`` a default file handler is added. Default ``True``
        add_handler_console (bool, optional): If ``True`` a default console handler is added. Default ``True``

    Returns:
        Logger: A logger for the curren name.
    """
    add_file_handler = bool(kwargs.get('add_handler_file', True))
    add_console_handler = bool(kwargs.get('add_handler_console', True))
    _level = int(kwargs.get('level', LOG_LEVEL))
    _file = kwargs.get('log_file', None)
    try:
        # https://stackoverflow.com/questions/53129716/how-to-check-if-a-logger-exists
        # Undocumneted method so wrap in try to future proof
        logger = logging.Logger.manager.loggerDict.get(logger_name, False)
        if logger:
            return logger
    except:
        pass
    logger = logging.getLogger(logger_name)
    # better to have too much log than not enough
    logger.setLevel(_level)
    if add_console_handler:
        logger.addHandler(get_console_handler())
    if add_file_handler:
        logger.addHandler(get_file_handler(log_file=_file))
    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False
    return logger
