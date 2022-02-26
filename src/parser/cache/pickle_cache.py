# coding: utf-8
import pickle
import time
from pathlib import Path
from typing import Union
from .cache_base import CacheBase
from ..common.log_load import Log
log = Log()

PICKLE_CACHE: 'PickleCache' = None

class PickleCache(CacheBase):
    """
    Caches files and retreives cached files.
    Cached file are in a subfolder of system tmp dir.
    """

    def fetch_from_cache(self, filename: Union[str, Path]) -> Union[object, None]:
        """
        Fetches file contents from cache if it exist and is not expired

        Args:
            filename (Union[str, Path]): File to retrieve

        Returns:
            Union[object, None]: File contents if retrieved; Otherwise, ``None``
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
            # Open the file in binary mode
            with open(f, 'rb') as file:
                # Call load method to deserialze
                content = pickle.load(file)
            return content
        except IOError:
            return None
        except Exception as e:
            log.logger.exception(e, exc_info=True)
            raise e

    def save_in_cache(self, filename: Union[str, Path], content: object):
        """
        Saves file contents into cache

        Args:
            filename (Union[str, Path]): filename to write.
            content (object): Contents to write into file.
        """
        f = Path(self.path, filename)
        with open(f, 'wb') as file:
            pickle.dump(content, file)
