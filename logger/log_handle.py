# coding: utf-8
import logging
import sys
import re
from pathlib import Path
from typing import Dict
# from logging.handlers import TimedRotatingFileHandler

FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = 'app.log'
LOG_LEVEL = logging.INFO

def _parse_log_options():
    global LOG_FILE, LOG_LEVEL
    if len(sys.argv) <= 1:
        LOG_LEVEL = logging.DEBUG
        LOG_FILE = Path(__file__).parent.parent / 'debug.log'
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
    LOG_FILE = Path(__file__).parent.parent / "app.log"

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


def get_file_handler():
    """
    Gets a file handler for usage with logger

    Raises:
        ValueError: If ``globals.LOG_PATH`` is not set.

    Returns:
        TimedRotatingFileHandler: Handler that rotates log every Monday.
    """
    # https://docs.python.org/3/library/logging.handlers.html#timedrotatingfilehandler
    # W0 rotate every monday.
    # file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name):
    """
    Gets a logger

    Args:
        logger_name (str): name of logger

    Returns:
        Logger: A logger for the curren name.
    """
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
    logger.setLevel(LOG_LEVEL)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False
    return logger
