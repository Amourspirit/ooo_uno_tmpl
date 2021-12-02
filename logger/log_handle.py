# coding: utf-8
import logging
import sys
from pathlib import Path
# from logging.handlers import TimedRotatingFileHandler

FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = Path(__file__).parent.parent / 'app.log'
LOG_LEVEL = logging.DEBUG

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
