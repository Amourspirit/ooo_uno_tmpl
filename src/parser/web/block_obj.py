# coding: utf-8
from abc import ABC, abstractmethod
from bs4.element import Tag
from ..web.soup_obj import SoupObj
from ..web.url_obj import UrlObj


class BlockObj(ABC):
    """
    Abstract Class.

    Represents a Html Block.
    """

    def __init__(self, soup: SoupObj):
        """
        Constructor

        Args:
            soup (SoupObj): soup for this instance
        """
        self._soup = soup
        self._url = soup.url
        self._urlobj = self._get_url_obj()

    def _get_url_obj(self):
        return UrlObj(self._url)

    @abstractmethod
    def get_obj(self) -> Tag:
        """Get object"""

    @property
    def url(self) -> str:
        """Gets Url"""
        return self._url

    @property
    def soup(self) -> SoupObj:
        """Gets SoupObj instance for this instance"""
        return self._soup

    @property
    def url_obj(self) -> UrlObj:
        """Gets UrlObj instance for this instance"""
        return self._urlobj
