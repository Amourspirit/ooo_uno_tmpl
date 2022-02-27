# coding: utf-8
import re
import logging
from typing import Union, Set, List
from bs4.element import Tag
from .api_proto_block import ApiProtoBlock
from ..dataclass.name_info import NameInfo
from ..dataclass.param_info import ParamInfo
from ..dataclass.summary_info import SummaryInfo
from ..web.block_obj import BlockObj
from ..mod_type import PythonType
from ..common.util import Util
from ..common.log_load import Log
log = Log()

re_dir_pattern = re.compile(r"\[((?:in)|(?:out))\]", re.IGNORECASE)


class ApiMethodPramsInfo(BlockObj):
    """Gets List of Parameter information for a funciton"""

    def __init__(self, block: ApiProtoBlock, name_info: NameInfo, ns: str, long_names: bool = False) -> None:
        self._block: ApiProtoBlock = block
        super().__init__(self._block.soup)
        self._requires_typing = False
        self._imports: Set[str] = set()
        self._ns = ns
        self._long_names = long_names
        self._name_info = name_info
        self._data = None

    def get_obj(self) -> List[ParamInfo]:
        if not self._data is None:
            return self._data
        self._data = []
        proto = self._block.get_obj()
        if not proto:
            return self._data
        p_type_tag = proto.find_all('td', class_='paramtype')
        p_name_tag = proto.find_all('td', class_='paramname')
        if not p_type_tag and not p_name_tag:
            if log.logger.level <= logging.DEBUG:
                log.logger.debug(
                    'ApiInterfacePramsInfoget_obj() No Parmas for %s', self._block.summary_info.name)
            return self._data

        try:
            if len(p_type_tag) != len(p_name_tag):
                if len(p_type_tag) == 0 and len(p_name_tag) == 1:
                    # no params. p_name_tag will usually be 1
                    # when there are not paramters.
                    return self._data
                raise Exception
        except Exception as e:
            msg = "ApiFnPramsInfo.get_obj(), Parameter Name and Parameter Types do not have the same length. Function Summary: %s Url: %s" % (str(
                self._block.summary_info), self.url_obj.url)
            log.logger.error(msg)
            raise Exception(msg)
        p_info = zip(p_name_tag, p_type_tag)
        self._data = self._process_params(params=p_info)
        return self._data

    def _process_name_tag(self, name_tag: Tag, pinfo: ParamInfo):
        name = name_tag.text
        pinfo.name = Util.get_clean_name(name)

    def _get_type_from_inner_link(self, paramtype: Tag, name: str) -> Union[str, None]:
        log.logger.debug(
            'ApiFnPramsInfo._get_type_from_inner_link() Searching for %s link.', name)
        if not paramtype:
            return None
        a_tag = paramtype.findChild('a')
        if not a_tag:
            return None
        a_name = a_tag.text.strip()
        if a_name != name:
            return None
        s = Util.get_ns_from_a_tag(a_tag=a_tag)
        log.logger.debug(
            'ApiFnPramsInfo._get_type_from_inner_link() found: %s', s)
        return s

    def _process_type_tag(self, type_tag: Tag, pinfo: ParamInfo):
        pinfo.direction = 'in'
        # dir_tag: NavigableString = type_tag.find(text=True, recursive=False)
        # dir_str could be in format of: [in] sequence< ::
        dir_str: str = type_tag.text.strip()
        m = re_dir_pattern.match(dir_str)
        if m:
            g_dir = m.group(1).lower()
            pinfo.direction = g_dir  # in or out
            dir_str = dir_str.split(maxsplit=1)[1]
        _type = dir_str.replace("::", '.').lstrip('.')
        t_info: PythonType = Util.get_python_type(
            in_type=_type,
            ns=self._ns,
            name_info=self._name_info,
            long_names=self._long_names
        )
        if t_info.is_default():
            log.logger.debug(
                'ApiFnPramsInfo._process_type_tag() %s type is Default. Looking for %s', pinfo.name, _type)
            t2_type = self._get_type_from_inner_link(type_tag, _type)
            if t2_type:
                t2_info = Util.get_python_type(
                    t2_type,
                    ns=self._ns,
                    name_info=self._name_info,
                    long_names=self._long_names
                )
                if not t2_info.is_default():
                    t_info = t2_info
        log.logger.debug(
            "ApiFnPramsInfo._process_type_tag() param '%s' type '%s' converted to '%s'", pinfo.name, _type, t_info.type)
        pinfo.type = t_info.type
        pinfo.p_type = t_info
        if t_info.requires_typing:
            self._requires_typing = True
        self._imports.update(t_info.get_all_imports())
        return

    def _process_params(self, params: zip) -> List[ParamInfo]:
        results = []
        for p_name_tag, p_type_tag in params:
            p_info = ParamInfo()
            self._process_name_tag(name_tag=p_name_tag, pinfo=p_info)
            if not p_info.name:
                msg = f"ApiFnPramsInfo: unable to find parameter name for method {self.summary_info.name!r}. Url: {self.url_obj.url}"
                log.logger.error(msg)
                raise Exception(msg)
            self._process_type_tag(type_tag=p_type_tag, pinfo=p_info)
            if not p_info.type:
                msg = f"ApiFnPramsInfo: unable to find parameter type for method {self.summary_info.name!r} with param name of {p_info.name!r}. Url: {self.url_obj.url}"
                log.logger.error(msg)
                raise Exception(msg)
            results.append(p_info)
        return results

    @property
    def requires_typing(self) -> bool:
        """Gets require_typing value"""
        return self._requires_typing

    @property
    def imports(self) -> Set[str]:
        """Gets imports value"""
        return self._imports

    @property
    def summary_info(self) -> SummaryInfo:
        """Gets summary_info value"""
        return self._block.summary_info
