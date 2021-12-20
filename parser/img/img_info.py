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
import numpy
from pathlib import Path
from typing import Any, Awaitable, Dict, List, Optional, Tuple, Union
import asyncio
import time
from PIL import Image
APP_ROOT:str = os.environ.get('project_root', str(Path(__file__).parent.parent.parent))
if not APP_ROOT in sys.path:
    sys.path.insert(0, APP_ROOT)
from parser import base

IMG_CACHE: 'ImageCache' = None
RESPONSE_IMG: 'ResponseImg' = None
TEXT_CACHE: base.TextCache = None
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
        with open(f, 'wb') as file:
            shutil.copyfileobj(content, file)

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
            file_ext (str, optional): Extension if file. Default ext of url.
                Format must prepend ``.`` such as ``.png``
        """
        if cache_seconds is None:
            cache_seconds = base.APP_CONFIG.cache_duration
        super().__init__(url=url, cache_seconds=cache_seconds, **kwargs)
        self._img: Image.Image = None

    # cache for one week - 604800.0 seconds
    def _get_request_data(self) -> Image.Image:
        global IMG_CACHE
        allow_cache = self.cache_seconds > 0
        filename = self._url_hash + self._file_ext
        if not IMG_CACHE:
            IMG_CACHE = ImageCache(
                tmp_dir=base.APP_CONFIG.cache_dir, lifetime=self.cache_seconds)
        if allow_cache:
            img = IMG_CACHE.fetch_from_cache(filename=filename)
            if img:
                logger.debug(
                    "ResponseImg._get_request_data() retreived data from Cache")
                return img
        response = requests.get(url=self.url, stream=True)
        if response.status_code != 200:
            raise Exception('bad response code:' + str(response.status_code))
        response.raw.decode_content = True
        IMG_CACHE.save_in_cache(
            filename=filename, content=response.raw)
        img = IMG_CACHE.fetch_from_cache(filename=filename)
        if allow_cache:
            logger.debug(
                "ResponseImg._get_request_data() Saving to cache as: %s", Path(IMG_CACHE.path, filename))
        else:
            IMG_CACHE.del_from_cache(filename=filename)
        return img

    @property
    def img(self) -> Image.Image:
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


def get_image_pixels_by_mode(image: Image.Image):
    """Get a numpy array of an image so that one can access values[x][y]."""
    # https://stackoverflow.com/questions/138250/how-to-read-the-rgb-value-of-a-given-pixel-in-python
    width, height = image.size
    if image.mode == "RGB":
        channels = 3
    elif image.mode == "L":
        channels = 1
    elif image.mode == "P":
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    pixel_values = numpy.array(list(image.getdata())).reshape(
        (height, width, channels))
    # pixel_values = numpy.array(pixel_values).reshape((width, height))
    return pixel_values


def get_image_pixels(image: Image.Image):
    """Get a numpy array of an image so that one can access values[x][y]."""
    width, height = image.size
    lst = list(image.getdata())
    pixel_values = numpy.array(lst).reshape((height, width))
    return pixel_values

def is_inherit_img(url:str) -> bool:
    global RESPONSE_IMG, TEXT_CACHE
    if RESPONSE_IMG is None:
        # no reason to cache image. caching result instead
        RESPONSE_IMG = ResponseImg(url=url,cache_seconds=0)
    if TEXT_CACHE is None:
        TEXT_CACHE = base.TextCache(tmp_dir=base.APP_CONFIG.cache_dir)
    try:
        filename = RESPONSE_IMG.url_hash + '.txt'
        result = -1
        txt = TEXT_CACHE.fetch_from_cache(filename=filename)
        if txt:
            result = int(txt)
            return result == base.APP_CONFIG.pixel_inherit
        pix = get_image_pixels(RESPONSE_IMG.img)
        row = pix[0, :] # row 0
        # images are expected to be indexed png files
        # find the first pixel that does not have index of 0
        # if first pixes is 1 then not inherited, if 3 inherited
        for px in row:
            if px != 0:
                result = px
                break
        if result == -1:
            msg = f"Failed to find colored pixel in first row of image pixels. Url: {url}"
            raise Exception(msg)
        content = str(result)
        TEXT_CACHE.save_in_cache(filename=filename, content=content)
        return result == base.APP_CONFIG.pixel_inherit
    except Exception as e:
        logger.error(e)
        raise e
