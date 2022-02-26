# coding: utf-8
import logging
from typing import Union, List
from bs4.element import Tag, ResultSet
from .api_proto_block import ApiProtoBlock
from ..dataclass.summary_info import SummaryInfo
from ..web.block_obj import BlockObj
from ..web.soup_obj import SoupObj
from ..common import log_load
# region Logger
logger: logging.Logger = log_load.get_logger()
# endregion Logger


class ApiInherited(BlockObj):

    def __init__(self, soup: SoupObj, area_filter_rules_engine: IRulesArea, ns: str, class_name: str, **kwargs) -> None:
        """
        Constructor

        Args:
            soup (SoupObj): Soup object
            area_filter_rules_engine (IRulesArea): Rules engine for procesing area data.
            ni (NameInfo): Contains name of current class being processed.

        Keyword Arguments:
            raise_error (bool, optional): Determines if errors will be raised when they occur: Default ``False``
        """
        super().__init__(soup)
        self._api_dy_content: ApiDyContent = ApiDyContent(self.soup)
        self._ns: str = ns
        self._class_name = class_name
        self._data = None
        self._raise_errors = bool(kwargs.get('raise_error', False))
        self._area_fileter_rules_engine = area_filter_rules_engine
        self._ai: AreaInfo = None
        self._allow_cache = bool(kwargs.get('allow_cache', True))

    def _log_missing(self, for_str: Optional[str] = None, raise_error: bool = False):
        if for_str:
            f_str = f" for {for_str}"
        else:
            f_str = ''
        msg = f"ApiInherited.get_obj() Failed to get find data{f_str}. Url: {self.url_obj.url}"
        if raise_error:
            logger.error(msg)
            raise Exception(msg)
        logger.warning(msg)

    def get_obj(self) -> List[Ns]:
        """
        Gets a list of Ns objects. Sorting is dertimined by IRulesArea

        Returns:
            List[Ns]: List of Ns objects for class inherites
        """
        if not self._data is None:
            return self._data
        known = get_known_extends(ns=self._ns, class_name=self._class_name)
        if known:
            logger.info('%s: Found Known inherits for %s.%s',
                        self.__class__.__name__, self._ns, self._class_name)
            self._data = known
            return self._data
        self._data = []
        ai = ApiImage(self._api_dy_content)
        image_url = ai.get_obj()
        if not image_url:
            self._log_missing(for_str='image url',
                              raise_error=self._raise_errors)
            return self._data
        self._ai = ImageInfo.get_area_info(
            url=image_url, allow_cache=self._allow_cache)
        if not self._ai.is_inherited:
            return self._data
        ab: ApiAreaBlock = ApiAreaBlock(self._api_dy_content)
        api_area: ApiArea = ApiArea(ab)
        lst = api_area.get_obj()
        filter = AreaFilter(lst, area_info=self._ai,
                            rules_engine=self._area_fileter_rules_engine)
        extends = filter.get_as_ns()
        if not extends:
            return self._data
        self._data = extends
        return self._data

    @property
    def area_info(self) -> AreaInfo:
        """Gets the area info containing inherited and cordinates info."""
        if self._ai is None:
            raise Exception(
                'ApiInherited.area_info can not be called before get_obj()')
        return self._ai

    @property
    def allow_cache(self) -> bool:
        """Specifies allow_cache

            :getter: Gets allow_cache value.
            :setter: Sets allow_cache value.
        """
        return self._allow_cache

    @allow_cache.setter
    def allow_cache(self, value: bool):
        self._allow_cache = value
