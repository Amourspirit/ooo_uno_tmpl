# coding: utf-8
import logging
import hashlib
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw
from kwhelp import rules
from abc import ABC
from .url_obj import UrlObj
from ..common import log_load
# region Logger
logger: logging.Logger = log_load.get_logger()
# endregion Logger




class ResponseBase(ABC):
    """Gets response data"""
    @RuleCheckAllKw(
        arg_info={
            "url": rules.RuleStrNotNullEmptyWs,
            "cache_seconds": rules.RuleNumber,
            "file_ext": rules.RuleStr
        },
        ftype=DecFuncEnum.METHOD
    )
    def __init__(self, url: str, cache_seconds: float, **kwargs):
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
            file_ext (str, optional): Extension if file. Default is read from url.
                Format must prepend ``.`` such as ``.png``
        """
        self._url = url
        self._url_obj = UrlObj(url=self._url, **kwargs)
        self._lifetime = cache_seconds
        self._url_hash = hashlib.md5(
            self._url_obj.url_only.encode('utf-8')).hexdigest()

        self._file_ext = kwargs.get('file_ext', None)
        if self._file_ext is None:
            self._file_ext = self._url_obj.ext

    @property
    def url(self) -> str:
        """Specifies url"""
        return self._url

    @property
    def url_obj(self) -> 'UrlObj':
        """Gets url_obj value"""
        return self._url_obj

    @property
    def url_hash(self) -> str:
        """Gets url_hash value"""
        return self._url_hash

    @property
    def cache_seconds(self) -> float:
        """Specifies allow_cache

            :getter: Gets cache_seconds value.
            :setter: Sets cache_seconds value.
        """
        return self._lifetime

    @cache_seconds.setter
    def cache_seconds(self, value: float):
        self._lifetime = value
        logger.debug('ResponseBase: caching is set to: %d', value)
