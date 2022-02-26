# coding: utf-8
import logging
import os
import tempfile
from pathlib import Path
from typing import Optional, Union
from ..common.config import APP_CONFIG
from abc import ABC, abstractmethod
from ..common.util import Util
from ..common import log_load
# region Logger
logger: logging.Logger = log_load.get_logger()
# endregion Logger

class CacheBase(ABC):
    """
    Caches files and retreives cached files.
    Cached file are in a subfolder of system tmp dir.
    """

    def __init__(self, tmp_dir: str, lifetime: Optional[float] = None) -> None:
        """
        Constructor

        Args:
            tmp_dir (str, optional): Dir name to create in tmp folder. Defaults to 'ooo_uno_tmpl'.
            lifetime (float, optional): Time in seconds that cache is good for. Defaults to 60 seconds.
        """
        t_path = Path(tempfile.gettempdir())
        self._cache_path = t_path / tmp_dir
        Util.mkdirp(self._cache_path)
        self._lifetime = lifetime or APP_CONFIG.cache_duration

    @abstractmethod
    def fetch_from_cache(self, filename: Union[str, Path]):
        """
        Fetches file contents from cache if it exist and is not expired

        Args:
            filename (Union[str, Path]): File to retrieve

        Returns:
            Union[str, None]: File contents if retrieved; Otherwise, ``None``
        """

    @abstractmethod
    def save_in_cache(self, filename: Union[str, Path], content):
        """
        Saves file contents into cache

        Args:
            filename (Union[str, Path]): filename to write.
            content (any): Contents to write into file.
        """

    def del_from_cache(self,  filename: Union[str, Path]) -> None:
        """
        Deletes a file from cache if it exist

        Args:
            filename (Union[str, Path]): file to delete.
        """
        try:
            f = Path(self.path, filename)
            if os.path.exists(f):
                os.remove(f)
        except Exception as e:
            logger.warning(
                'Not able to delete file: %s, error: %s', filename, str(e))

    @property
    def seconds(self) -> float:
        """Gets/Sets cache time in seconds"""
        return self._lifetime

    @seconds.setter
    def seconds(self, value: float) -> None:
        self._lifetime = float(value)

    @property
    def path(self) -> Path:
        """Gets cache path"""
        return self._cache_path