# coding: utf-8
import time
from pathlib import Path
from typing import Union
from .cache_base import CacheBase
from ..common.log_load import Log
log = Log()

TEXT_CACHE: 'TextCache' = None

class TextCache(CacheBase):
    """
    Caches files and retreives cached files.
    Cached file are in a subfolder of system tmp dir.
    """

    def fetch_from_cache(self, filename: Union[str, Path]) -> Union[str, None]:
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
                log.logger.warning(
                    'Not able to delete 0 byte file: %s, error: %s', filename, str(e))
            return None
        ti_m = f_stat.st_mtime
        age = time.time() - ti_m
        if age >= self.seconds:
            return None

        try:
            # Check if we have this file locally

            with open(f) as fin:
                content = fin.read()
            # If we have it, let's send it
            return content
        except IOError:
            return None

    def save_in_cache(self, filename: Union[str, Path], content: str):
        """
        Saves file contents into cache

        Args:
            filename (Union[str, Path]): filename to write.
            content (str): Contents to write into file.
        """
        f = Path(self.path, filename)
        # print('Saving a copy of {} in the cache'.format(filename))
        with open(f, 'w') as cached_file:
            cached_file.write(content)
