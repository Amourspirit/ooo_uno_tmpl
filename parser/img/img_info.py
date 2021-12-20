# coding: utf-8
"""
Module for getting and processing image data.
Module logger must be set before calling any class or function.
eg: import img_info
    img_info.logger = mylogger
"""
import os
import sys
import requests
import logging
import shutil  # to save it locally
from pathlib import Path
from typing import Any, Awaitable, Dict, List, Optional, Tuple, Union
import asyncio
import time
from PIL import Image
APP_ROOT:str = os.environ.get('project_root', str(Path(__file__).parent.parent.parent))
if not APP_ROOT in sys.path:
    sys.path.insert(0, APP_ROOT)
from parser import base

RESPONSE_IMG_CACHE: 'ImageCache' = None
logger: logging.Logger = None

# region Cache
class ImageCache(base.CacheBase):
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
        f = Path(self.path, filename)
        if not f.exists():
            return None

        if self.seconds > 0:
            f_stat = f.stat()
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
        with open(filename, 'wb') as f:
            shutil.copyfileobj(content, f)

# endregion Cache

# region Response
class ResponseImg(base.ResponseBase):
    """Gets response data for an image"""

    def __init__(self, url: str, cache_seconds: Optional[float] = None, **kwargs):
        """
        Constructor

        Args:
            url (str): Url to retrieve html
            allow_cache (bool, optional): Determins if caching is used.
                If ``True`` html will be written to cache. Defaults to True.
            cache_seconds (float, optional): The number of seconds that html
                contents will be cached for. Default is ``604800.0`` ( one week )

        Keyword Arguments:
            has_name (bool, optional): If ``True`` name is extracted from
                url and namespace excludes name. Default ``True``.
                This applies to ``url_obj`` property
            file_ext (str, optional): Extension if file. Default is empty str.
                Format must prepend ``.`` such as ``.png``
        """
        if cache_seconds is None:
            cache_seconds = base.APP_CONFIG.cache_duration
        super().__init__(url=url, cache_seconds=cache_seconds, **kwargs)
        self._img: Image = None

    # cache for one week - 604800.0 seconds
    def _get_request_data(self) -> Image:
        global RESPONSE_IMG_CACHE
        allow_cache = self.cache_seconds > 0
        filename = self._url_hash + self._file_ext
        if allow_cache:
            if not RESPONSE_IMG_CACHE:
                RESPONSE_IMG_CACHE = ImageCache(
                    tmp_dir=base.APP_CONFIG.cache_dir, lifetime=self.cache_seconds)
            img = RESPONSE_IMG_CACHE.fetch_from_cache(filename=filename)
            if img:
                logger.debug(
                    "ResponseImg._get_request_data() retreived data from Cache")
                return img
        response = requests.get(url=self.url, stream=True)
        if response.status_code != 200:
            raise Exception('bad response code:' + str(response.status_code))
        response.raw.decode_content = True
        RESPONSE_IMG_CACHE.save_in_cache(
            filename=filename, content=response.raw)
        img = RESPONSE_IMG_CACHE.fetch_from_cache(filename=filename)
        if allow_cache:
            logger.debug(
                "ResponseImg._get_request_data() Saving to cache as: %s", filename)
        else:
            RESPONSE_IMG_CACHE.del_from_cache(filename=filename)
        return img

    @property
    def img(self) -> Image:
        """
        Gets image
        """
        if self._img is None:
            try:
                self._img = self._get_request_data()
            except Exception as e:
                logger.error(e)
                raise e
        return self._img
# endregion Response
