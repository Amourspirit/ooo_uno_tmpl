# coding: utf-8
import requests
from typing import Optional
from pathlib import Path
from .response_base import ResponseBase
from ..common.config import APP_CONFIG
from ..cache.text_cache import TextCache
from ..common.log_load import Log
log = Log()

_TEXT_CACHE: TextCache = None


class ResponseObj(ResponseBase):
    """Gets response data"""

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
            file_ext (str, optional): Extension if file. Default is empty ``.html``.
                Format must prepend ``.`` such as ``.png``
        """
        if cache_seconds is None:
            cache_seconds = APP_CONFIG.cache_duration
        super().__init__(url=url, cache_seconds=cache_seconds, **kwargs)
        self._text = None
        if not 'file_ext' in kwargs:
            self._file_ext = '.html'

    # cache for one week - 604800.0 seconds
    def _get_request_text(self) -> str:
        global _TEXT_CACHE
        allow_cache = self.cache_seconds > 0
        filename = self._url_hash + self._file_ext
        if allow_cache:
            if not _TEXT_CACHE:
                _TEXT_CACHE = TextCache(
                    tmp_dir=APP_CONFIG.cache_dir, lifetime=self.cache_seconds)
            html_text = _TEXT_CACHE.fetch_from_cache(filename=filename)
            if html_text:
                log.logger.debug(
                    "ResponseObj._get_request_text() retreived data from Cache")
                return html_text
        response = requests.get(url=self.url)
        if response.status_code != 200:
            raise Exception('bad response code:' + str(response.status_code))
        html_text = response.text
        if allow_cache:
            _TEXT_CACHE.save_in_cache(filename=filename, content=html_text)
            log.logger.debug(
                "ResponseObj._get_request_text() Saving to cache as: %s", Path(_TEXT_CACHE.path, filename))
        return html_text

    @property
    def raw_html(self) -> str:
        """
        Gets raw html of url
        """
        if self._text is None:
            try:
                self._text = self._get_request_text()
            except Exception as e:
                log.logger.error(e)
                raise e
        return self._text
