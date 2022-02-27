# coding: utf-8
import requests
from PIL import Image
from typing import Optional
from pathlib import Path
from .response_base import ResponseBase
from ..cache.image_cache import ImageCache
from ..common.config import APP_CONFIG
from ..common.log_load import Log
log = Log()

_IMG_CACHE: ImageCache = None

class ResponseImg(ResponseBase):
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
            cache_seconds = APP_CONFIG.cache_duration
        super().__init__(url=url, cache_seconds=cache_seconds, **kwargs)
        self._img: Image.Image = None

    # cache for one week - 604800.0 seconds
    def _get_request_data(self) -> Image.Image:
        global _IMG_CACHE
        allow_cache = self.cache_seconds > 0
        filename = self._url_hash + self._file_ext
        if not _IMG_CACHE:
            _IMG_CACHE = ImageCache(
                tmp_dir=APP_CONFIG.cache_dir, lifetime=self.cache_seconds)
        if allow_cache:
            img = _IMG_CACHE.fetch_from_cache(filename=filename)
            if img:
                log.logger.debug(
                    "ResponseImg._get_request_data() retreived data from Cache")
                return img
        response = requests.get(url=self.url, stream=True)
        if response.status_code != 200:
            raise Exception('bad response code:' + str(response.status_code))
        response.raw.decode_content = True
        _IMG_CACHE.save_in_cache(
            filename=filename, content=response.raw)
        img = _IMG_CACHE.fetch_from_cache(filename=filename)
        if allow_cache:
            log.logger.debug(
                "ResponseImg._get_request_data() Saving to cache as: %s", Path(_IMG_CACHE.path, filename))
        else:
            _IMG_CACHE.del_from_cache(filename=filename)
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
                log.logger.error(e)
                raise e
        return self._img
