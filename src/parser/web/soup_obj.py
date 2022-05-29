# coding: utf-8
from bs4 import BeautifulSoup
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw
from kwhelp import rules
from .response_obj import ResponseObj
from .url_obj import UrlObj


class SoupObj:
    """Wrapper for BeautifulSoup"""
    @RuleCheckAllKw(
        arg_info={
            'url': rules.RuleStrNotNullEmptyWs,
            'allow_cache': rules.RuleBool
        },
        ftype=DecFuncEnum.METHOD
    )
    def __init__(self, url: str, allow_cache: bool = True, **kwargs) -> None:
        """
        Constructor

        Args:
            url (str): Url of http page
            allow_cache (bool, optional): If ``True`` html contents are cached. Defaults to ``True``.

        Keyword Arguments:
            has_name (bool, optional): If ``True`` name is extracted from
                url and namespace excludes name. Default ``True``.
                This applies to ``url_obj`` property
        """
        if allow_cache:
            self._response = ResponseObj(url=url, **kwargs)
        else:
            self._response = ResponseObj(url=url, cache_seconds=0, **kwargs)
        self._soup = None

    @property
    def soup(self) -> BeautifulSoup:
        """Gets soup for this instance"""
        if not self._soup:
            # clean up whitespace
            # https://stackoverflow.com/questions/4270742/how-to-remove-whitespace-in-beautifulsoup
            html = "".join(line.strip()
                           for line in self._response.raw_html.split("\n"))
            self._soup = BeautifulSoup(html, 'lxml')
        return self._soup

    @property
    def response(self) -> ResponseObj:
        """Gets this instance response"""
        return self._response

    @property
    def url(self) -> str:
        """Specifies url"""
        return self._response.url

    @property
    def url_obj(self) -> 'UrlObj':
        """Specifies url"""
        return self._response.url_obj

    @property
    def allow_cache(self) -> bool:
        """Specifies allow_cache

            :getter: Gets allow_cache value.
            :setter: Sets allow_cache value.
        """
        return self._response.allow_cache

    @allow_cache.setter
    def allow_cache(self, value: bool):
        self._response.allow_cache = value
