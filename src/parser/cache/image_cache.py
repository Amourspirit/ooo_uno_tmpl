# coding: utf-8
import logging
import time
from pathlib import Path
from typing import Union, Any
from PIL import Image
import shutil  # to save it locally
from .cache_base import CacheBase
from ..common import log_load
# region Logger
logger: logging.Logger = log_load.get_logger()
# endregion Logger


class ImageCache(CacheBase):
    """
    Caches files and retreives cached files.
    Cached file are in a subfolder of system tmp dir.
    """

    def fetch_from_cache(self, filename: Union[str, Path]) -> Union[Image.Image, None]:
        """
        Fetches file contents from cache if it exist and is not expired

        Args:
            filename (Union[str, Path]): File to retrieve

        Returns:
            Union[str, None]: File contents if retrieved; Otherwise, ``None``
        """
        if self.seconds <= 0:
            return None
        f = Path(self.path, filename)
        if not f.exists():
            return None

        f_stat = f.stat()
        if f_stat.st_size == 0:
            # shoud not be zero byte file.
            try:
                self.del_from_cache(f)
            except Exception as e:
                logger.warning(
                    'Not able to delete 0 byte file: %s, error: %s', filename, str(e))
            return None
        ti_m = f_stat.st_mtime
        age = time.time() - ti_m
        if age >= self.seconds:
            return None

        try:
            # Check if we have this file locally
            with Image.open(f) as img:
                img.load()
                return img
        except IOError:
            return None

    def save_in_cache(self, filename: Union[str, Path], content: Any):
        """
        Saves file contents into cache

        Args:
            filename (Union[str, Path]): filename to write.
            content (str): Contents to write into file.
        """
        f = Path(self.path, filename)
        # print('Saving a copy of {} in the cache'.format(filename))
        with open(f, 'wb') as file:
            shutil.copyfileobj(content, file)
