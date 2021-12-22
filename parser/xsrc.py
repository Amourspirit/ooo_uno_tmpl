#!/usr/bin/env python
# coding: utf-8
"""
Process a link to a page that contains an interface
"""
from abc import abstractmethod
import os
import sys
import argparse
import logging
import textwrap
import xerox  # requires xclip - sudo apt-get install xclip
import re
import base
from typing import Dict, List, Optional, Set, Union
from bs4.element import NavigableString, PageElement, ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, TypeCheck, TypeCheckKw
from pathlib import Path
from logger.log_handle import get_logger
from parser.enm import main
from dataclasses import dataclass
from parser import __version__, JSON_ID

logger = None


def _set_loggers(l: Union[logging.Logger, None]):
    global logger, base
    logger = l
    base.logger = l


_set_loggers(None)

re_component_start = re.compile(r"(interface.*){", re.DOTALL)
re_name_info_start = re.compile(r"(interface)\s*[a-zA-Z0-9]+[ :]+")
re_name_info_name = re.compile(r"interface\s*(?P<NAME>[a-zA-Z0-9_]+)")
# region SDK API Reference
re_ln_pattern = re.compile(r"\A\s*(:?[0-9]*)\s*")
# https://regex101.com/r/xAqRAU/1/
re_args_pattern = re.compile(r"\s*(?:\[(\S{2,3})\])?\s*(\S*)\s(\S*)")
# https://regex101.com/r/HU09ZZ/1
re_method_pattern = re.compile(
    r"(\S*)\s*(?:(\S*)\()(?:\s(.*)\))|(\S*)\s*([0-9A-Z-a-z]*)")
# https://regex101.com/r/BdDT4u/1
re_raises_pattern = re.compile(r"\s*(raises\s*\(.*\))")

re_interface_pattern = re.compile(r"interface\s*([a-zA-Z0-9.]*)\s*;")
re_property_pattern = re.compile(r"(?:\[attribute[ ,a-z]*\])(?:[ ]+)([a-zA-Z0-9. {}()]*);")
re_comment_start_pattern = re.compile(r"(?:(\/\*)|(?:\*)\s)")
re_dir_pattern = re.compile(r"\[((?:in)|(?:out))\]", re.IGNORECASE)
# endregion SDK API Reference

# region Data Classes
@dataclass
class ParamInfo:
    direction: str = ''
    name: str = ''
    type: str =''

@dataclass
class MethodBlockInfo:
    tag_id: Tag
    tag_title: Tag
    tag_main: Tag


@dataclass(frozen=True)
class SummaryInfo:
    id: str
    name: str
    return_type: str
# endregion Data Classes

# region API Interface classes

class ApiPublicMembers(base.BlockObj):
    """Gets all blocks with condensed info such as Public Member Functions"""
    @TypeCheck(base.SoupObj, ftype=DecFuncEnum.METHOD)
    def __init__(self, soup: base.SoupObj):
        self._soup = soup
        super().__init__(soup)
        self._data = False
    
    def get_obj(self) -> Union[ResultSet, None]:
        if not self._data is False:
            return self._data
        self._data = None
        soup = self.soup.soup
        rs = soup.find_all('table', class_='memberdecls')
        self._data = rs
        return self._data

class ApiSummaryBlock(base.BlockObj):
    def __init__(self, block: ApiPublicMembers):
        self._block: ApiPublicMembers = block
        super().__init__(self._block.soup)
        self._data = False
    @abstractmethod
    def _get_match_name(self) -> str:
        pass

    def get_obj(self) -> Union[Tag, None]:
        if not self._data is False:
            return self._data
        self._data = None
        rs = self._block.get_obj()
        if not rs:
            return self._data
        match_name = self._get_match_name()
        for tag in rs:
            # tag is a table
            # body > div.contents > table > tbody > tr.heading > td > h2 > a
            t: Tag = tag
            a_lnk = t.select_one('tr.heading > td > h2 > a')
            if a_lnk:
                name = a_lnk.get('name', None)
                if name == match_name:
                    self._data = tag
                    break
        return self._data


class ApiFunctionsBlock(ApiSummaryBlock):
    def _get_match_name(self) -> str:
        return 'pub-methods'


class ApiPropertiesBlock(ApiSummaryBlock):
    def _get_match_name(self) -> str:
        return 'pub-attribs'

class ApiInterfacesBlock(ApiSummaryBlock):
    """Gets Block object for Exported Interfaces"""
    def _get_match_name(self) -> str:
        return 'interfaces'

class ApiSummaryRows(base.BlockObj):
    """Gets the rows that contain short details and desc for a Function/properyty block"""
    def __init__(self, block: ApiSummaryBlock):
        self._block: ApiSummaryBlock = block
        super().__init__(self._block.soup)
        self._data = None

    def get_obj(self) -> List[Tag]:
        if not self._data is None:
            return self._data
        self._data = []
        tbl_tag: Tag = self._block.get_obj()
        if not tbl_tag:
            return self._data
        rs_rows: ResultSet = tbl_tag.find_all('tr')
        if not rs_rows:
            return self._data
        for row in rs_rows:
            r: Tag = row
            _class = r.get('class', [])
            if len(_class) == 0:
                continue
            class_str = _class[0]
            if class_str == 'inherit_header':
                # Public Member Functions inherited from ...
                break
            if class_str.startswith('memitem:'):
                self._data.append(row)
        return self._data

class ApiSummaries(base.BlockObj):
    def __init__(self, block: ApiSummaryRows) -> None:
        self._block: ApiSummaryRows = block
        super().__init__(self._block.soup)
        self._requires_typing = False
        self._imports: Set[str] = set()
        self._data = None

    def get_obj(self) -> List[SummaryInfo]:
        if not self._data is None:
            return self._data
        self._data = []
        rows = self._block.get_obj()
        for row in rows:
            cls_name = row.get('class')[0]
            id_str = cls_name.rsplit(sep=':',maxsplit=1)[1]
            itm_lft = row.find('td', class_='memItemLeft')
            r_type = ''
            name = ''
            if itm_lft:
                r_type = itm_lft.text.strip().replace('::', '.')
            itm_rgt = row.find('td', class_='memItemRight')
            if itm_rgt:
                itm_name = itm_rgt.select_one('a')
                if itm_name:
                    name = itm_name.text.strip()
                    name = base.Util.get_clean_method_name(name)
            p_type = base.Util.get_python_type(in_type=r_type)
            si = SummaryInfo(id=id_str,name=name,return_type=p_type.type)
            if p_type.requires_typing:
                self._requires_typing = True
            for im in p_type.imports:
                self._imports.add(im)
            self._data.append(si)
        return self._data

    @property
    def requires_typing(self) -> bool:
        """Gets requires_typing value"""
        return self._requires_typing

    @property
    def imports(self) -> Set[str]:
        """Gets imports value"""
        return self._imports

class ApiDetailBlock(base.BlockObj):
    def __init__(self, soup: base.SoupObj, si: SummaryInfo) -> None:
        super().__init__(soup)
        self._si = si
        self._data = False
    
    def get_obj(self) -> Union[Tag, None]:
        if not self._data is False:
            return self._data
        self._data = None
        soup = self.soup.soup
        a_tag: Tag = soup.find('a', id=self._si.id)
        if not a_tag:
            return self._data
        self._data = a_tag.find_next('div', class_='memitem')
        return self._data
    @property
    def summary_info(self) -> SummaryInfo:
        """Gets summary_info value"""
        return self._si


class ApiProtoBlock(base.BlockObj):
    """Gets Detailed Method data block"""

    def __init__(self, block: ApiDetailBlock) -> None:
        self._block: ApiDetailBlock = block
        super().__init__(self._block.soup)
        self._data = False
    
    def get_obj(self) -> Union[Tag, None]:
        if not self._data is False:
            return self._data
        self._data = None
        tag = self._block.get_obj()
        if not tag:
            return self._data
        proto = tag.findChild('div', class_='memproto')
        self._data = proto
        self._data

    @property
    def summary_info(self) -> SummaryInfo:
        """Gets summary_info value"""
        return self._block.summary_info


class ApiDescBlock(base.BlockObj):
    """Gets Detailed Method description block"""

    def __init__(self, block: ApiDetailBlock) -> None:
        self._block: ApiDetailBlock = block
        super().__init__(self._block.soup)
        self._data = False

    def get_obj(self) -> Union[Tag, None]:
        if not self._data is False:
            return self._data
        self._data = None
        tag = self._block.get_obj()
        if not tag:
            return self._data
        desc = tag.findChild('div', class_='memdoc')
        self._data = desc
        return self._data

    @property
    def summary_info(self) -> SummaryInfo:
        """Gets summary_info value"""
        return self._block.summary_info

class ApiFnPramsInfo(base.BlockObj):
    """Gets List of Parameter information for a funciton"""
    def __init__(self, block: ApiProtoBlock) -> None:
        self._block: ApiProtoBlock = block
        super().__init__(self._block.soup)
        self._requires_typing = False
        self._imports: Set[str] = set()
        self._data = None

    def get_obj(self) -> List[ParamInfo]:
        if not self._data is None:
            return self._data
        self._data = []
        proto = self._block.get_obj()
        if not proto:
            return self._data
        p_type_tag = proto.find_all('td', class_='paramtype')
        p_name_tag= proto.find_all('td', class_='paramname')
        if not p_type_tag and not p_name_tag:
            if logger.level <= logging.DEBUG:
                logger.debug('ApiInterfacePramsInfoget_obj() No Parmas for %s', self._block.summary_info.name)
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
            logger.error(msg)
            raise Exception(msg)
        p_info = zip(p_name_tag, p_type_tag)
        self._data = self._process_params(params=p_info)
        return self._data
    
    def _process_name_tag(self, name_tag: Tag, pinfo:ParamInfo):
        name = name_tag.text
        pinfo.name = base.Util.get_clean_name(name)
    
    def _process_type_tag(self, type_tag: Tag, pinfo: ParamInfo):
        pinfo.direction = 'in'
        # dir_tag: NavigableString = type_tag.find(text=True, recursive=False)
        # dir_str could be in format of: [in] sequence< ::
        dir_str: str = type_tag.text.strip()
        m = re_dir_pattern.match(dir_str)
        if m:
            g_dir = m.group(1).lower()
            pinfo.direction = g_dir # in or out
            dir_str = dir_str.split(maxsplit=1)[1]
        _type = dir_str.replace("::", '.').lstrip('.')
        t_info: base.PythonType = base.Util.get_python_type(in_type=_type)
        pinfo.type = t_info.type
        if t_info.requires_typing:
            self._requires_typing = True
        for im in t_info.imports:
            self._imports.add(im)
        return

    def _process_params(self, params:zip) -> List[ParamInfo]:
        results = []
        for p_name_tag, p_type_tag in params:
            p_info = ParamInfo()
            self._process_name_tag(name_tag=p_name_tag, pinfo=p_info)
            if not p_info.name:
                msg = f"ApiFnPramsInfo: unable to find parameter name for method {self.summary_info.name!r}. Url: {self.url_obj.url}"
                logger.error(msg)
                raise Exception(msg)
            self._process_type_tag(type_tag=p_type_tag, pinfo=p_info)
            if not p_info.type:
                msg = f"ApiFnPramsInfo: unable to find parameter type for method {self.summary_info.name!r} with param name of {p_info.name!r}. Url: {self.url_obj.url}"
                logger.error(msg)
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


class ApiMethodException(base.BlockObj):
    """Gets errors for a funciton"""
    # have not found an example with more than one exception so assuming
    # singular excpetion
    def __init__(self, block: ApiProtoBlock) -> None:
        self._block: ApiProtoBlock = block
        super().__init__(self._block.soup)
        self._data = False

    def _get_raises_row(self):
        proto = self._block.get_obj()
        rows: ResultSet = proto.find_all('tr')
        result = None
        for row in rows:
            td: Tag = row.select_one('td')
            if td.text.strip().lower() == 'raises':
                result = row
                break
        return result
    
    def _get_raises_text(self, row:Tag):
        if not row:
            return None
        s: str = row.text.rsplit(maxsplit=1)[1] # drop raises
        s = s.replace('(', '').replace(')', '').replace('::', '.').strip().lstrip('.')
        return s
    
    def get_obj(self) -> Union[str, None]:
        """
        Get name of error that is raises

        Returns:
            Union[str, None]: String containing type of error if it exist; Otherwise, ``None``
        """
        if not self._data is False:
            return self._data
        self._data = None
        row = self._get_raises_row()
        if not row:
            return self._data
        self._data = self._get_raises_text(row)        
        return self._data

    @property
    def summary_info(self) -> SummaryInfo:
        """Gets summary_info value"""
        return self._block.summary_info


class ApiDescDetail(base.BlockObj):
    def __init__(self, block: ApiDescBlock) -> None:
        self._block: ApiDescBlock = block
        super().__init__(self._block.soup)
        self._data = None
        self._cls = 'memdoc'
        self._el = 'div'

    def get_obj(self) -> List[str]:
        if not self._data is None:
            return self._data
        self._data = []
        tag = self._block.get_obj()
        if not tag:
            return self._data
        lines_found: ResultSet = tag.select(f'{self._el}.{self._cls} > p')
        if not lines_found:
            return self._data
        p_obj = base.TagsStrObj(tags=lines_found)
        self._data = p_obj.get_lines()
        since_obj = ApiDescDetailSince(self._block)
        since = since_obj.get_obj()
        if since:
            self._data.append('')
            self._data.append('**since**')
            self._data.append('')
            self._data.append(f"    {since}")
        return self._data

class ApiDescDetailSince(base.BlockObj):
    def __init__(self, block: ApiDescBlock) -> None:
        self._block: ApiDescBlock = block
        super().__init__(self._block.soup)
        self._data = False
    
    def get_obj(self) -> Union[str, None]:
        if not self._data is False:
            return self._data
        self._data = None
        tag: Tag = self._block.get_obj()
        if not tag:
            return self._data
        dl_tag = tag.select_one('dl.section.since')
        if not dl_tag:
            return self._data
        dd_tag = dl_tag.find('dd')
        if not dd_tag:
            return self._data
        self._data = dd_tag.text.strip()
        return self._data

class ApiInterfaceName(base.ApiName):
    """Get the Name object for the interface"""
class ApiNs(base.ApiNamespace):
    """Get the Name object for the interface"""
    def __init__(self, soup: base.SoupObj):
        super().__init__(soup)
        self._namespace_str = None
        self._namespace = None
    
    @property
    def namespace(self) -> List[str]:
        """Gets namespace value"""
        if self._namespace is None:
            self._namespace = self.get_obj()[:-1]
        return self._namespace
    
    
    @property
    def namespace_str(self) -> str:
        if self._namespace_str is None:
            self._namespace_str = '.'.join(self.namespace)
        return self._namespace_str

class ApiDesc(base.BlockObj):
    """Gets the description"""

    def __init__(self, soup: base.SoupObj):
        super().__init__(soup)
        self._data = None

    def get_obj(self) -> List[str]:
        """
        Gets description as list of str

        Returns:
            List[str]: description lines
        """
        if self._data:
            return self._data
        lines_found: ResultSet = self.soup.soup.select(
            'body > div.contents > div.textblock > p')
        p_obj = base.TagsStrObj(tags=lines_found)
        self._data = p_obj.get_lines()
        since_obj = ApiDescSince(self.soup)
        since = since_obj.get_obj()
        if since:
            self._data.append('')
            self._data.append('**since**')
            self._data.append('')
            self._data.append(f"    {since}")
        #.. deprecated::
        dep_obj = ApiDepreciated(self.soup)
        dep = dep_obj.get_obj()
        if dep:
            self._data.append('')
            self._data.append('.. deprecated::')
            self._data.append('')
            self._data.append('    Interface is deprecated.')
        return self._data

    @property
    def summary_info(self) -> SummaryInfo:
        """Gets summary_info value"""
        return self._block.summary_info

class ApiDescSince(base.BlockObj):
    """Gets the Since if it exist"""

    def __init__(self, soup: base.SoupObj):
        super().__init__(soup)
        self._data = False

    def get_obj(self) -> Union[str, None]:
        """
        Gets See alos of Interface

        Returns:
            str: See also. if it exist; Otherwise empty string.
        """
        if not self._data is False:
            return self._data
        self._data = None
        dl_tag = self._soup.soup.select_one('dl.section.since')
        if not dl_tag:
            return self._data
        dd_tag = dl_tag.find('dd')
        if not dd_tag:
            return self._data
        self._data = dd_tag.text.strip()
        return self._data

class ApiDepreciated(base.BlockObj):
    """Gets if an interface is deprecated"""
    # eg: https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XVclContainerPeer.html
    def __init__(self, soup: base.SoupObj):
        super().__init__(soup)
        self._data = None

    def get_obj(self) -> bool:
        """
        Gets See alos of Interface

        Returns:
            str: See also. if it exist; Otherwise empty string.
        """
        if not self._data is None:
            return self._data
        soup = self.soup.soup
        tag = soup.select_one('div.textblock > dl.deprecated')
        if tag:
            self._data = True
        else:
            self._data = False
        return self._data


class ApiInterfaceData:
    def __init__(self, url_soup: Union[str, base.SoupObj], allow_cache: bool):
        if isinstance(url_soup, str):
            self._url = url_soup
            self._soup_obj = base.SoupObj(
                url=url_soup, allow_cache=allow_cache)
        else:
            self._url = url_soup.url
            self._soup_obj = url_soup
            self._soup_obj.allow_cache = allow_cache
        self._si_key = 'summeries'
        self._detail_block_key = 'detail_block'
        self._name: ApiInterfaceName = None
        self._ns: ApiNs = None
        self._public_members: ApiPublicMembers = None
        self._properties_block: ApiPropertiesBlock = None
        self._func_block: ApiFunctionsBlock = None
        self._interfaces_block: ApiInterfacesBlock = None
        self._func_summary_rows: ApiSummaryRows = None
        self._property_summary_rows: ApiSummaryRows = None
        self._export_summary_rows: ApiSummaryRows = None
        self._func_summaries: ApiSummaries = None
        self._property_summaries: ApiSummaries = None
        self._exported_summaries: ApiSummaries = None
        self._desc: ApiDesc = None
        self._inherited: base.ApiInherited = None
        self._cache = {
            self._si_key: {},
            self._detail_block_key: {}
        }
    # region Methods

    def get_cached_summary(self, si_id: Union[str, SummaryInfo]) -> SummaryInfo:
        """
        Gets a method summary info cache.

        Args:
            si (SummaryInfo): Summary info

        Raises:
            KeyError if summary does not exist in cache

        Returns:
            SummaryInfo: Summary info
        """
        if isinstance(si_id, SummaryInfo):
            return si_id
        if self._func_summaries is None:
            # set up the cache
            _ = self.func_summaries
        if self._property_summaries is None:
            # set up the cache
            _ = self.property_summaries
        return self._cache[self._si_key][si_id]
    
    def get_detail_block(self, si_id: Union[str, SummaryInfo]) -> ApiDetailBlock:
        """
        Gets detail block of a function.
        Gets the 

        Args:
            si (SummaryInfo): Function summary Info to get the details block for.

        Returns:
            ApiDetailBlock: object
        """
        if isinstance(si_id, SummaryInfo):
            id = si_id.id
        else:
            id = si_id
        key = f"get_detail_block_{id}"
        if key in self._cache:
            return self._cache[key]
        si = self.get_cached_summary(si_id=si_id)
        result = ApiDetailBlock(soup=self.soup_obj, si=si)
        self._cache[key] = result
        return result
    
    def get_proto_block(self, si_id: Union[str, SummaryInfo]) -> ApiProtoBlock:
        """Gets the block for a method information"""
        if isinstance(si_id, SummaryInfo):
            id = si_id.id
        else:
            id = si_id
        key = f"get_proto_block_{id}"
        if key in self._cache:
            return self._cache[key]
        detail_block = self.get_detail_block(si_id)
        result = ApiProtoBlock(block=detail_block)
        self._cache[key] = result
        return self._cache[key]
    
    def get_desc_block(self, si_id: Union[str, SummaryInfo]) -> ApiDescBlock:
        """Gets the block for a method description"""
        if isinstance(si_id, SummaryInfo):
            id = si_id.id
        else:
            id = si_id
        key = f"get_desc_block_{id}"
        if key in self._cache:
            return self._cache[key]
        detail_block = self.get_detail_block(si_id)
        result = ApiDescBlock(block=detail_block)
        self._cache[key] = result
        return self._cache[key]
    
    def get_prams_info(self, si_id: Union[str, SummaryInfo]) -> ApiFnPramsInfo:
        """Gets parameter info for all parameters of a a method"""
        block = self.get_proto_block(si_id=si_id)
        result = ApiFnPramsInfo(block=block)
        return result
    
    def get_method_ex(self, si_id: Union[str, SummaryInfo]) -> ApiMethodException:
        """Gets raises info for method"""
        block = self.get_proto_block(si_id=si_id)
        result = ApiMethodException(block=block)
        return result
    
    def get_desc_detail(self, si_id: Union[str, SummaryInfo]) -> ApiDescDetail:
        """Gets Description obj for method or property"""
        block = self.get_desc_block(si_id=si_id)
        result = ApiDescDetail(block=block)
        return result
    
    def get_import_info_method(self, si_id: Union[str, SummaryInfo]) -> base.ImportInfo:
        """
        Gets imports for method params and return type

        Args:
            si_id (str): Function summary Info

        Returns:
            base.ImportInfo: Import info
        """
        info = base.ImportInfo()
        params_info = self.get_prams_info(si_id=si_id)
        fn_info = self.func_summaries
        # ensure data is primed
        fn_info.get_obj()
        info.requires_typing = params_info.requires_typing or fn_info.requires_typing
        info.imports.update(params_info.imports)
        info.imports.update(fn_info.imports)
        return info
    
    def get_import_info_property(self) -> base.ImportInfo:
        """
        Gets imports for properties

        Args:
            si_id (str): Property summary Info

        Returns:
            base.ImportInfo: Import info
        """
        info = base.ImportInfo()
        p_info = self.property_summaries
        # ensure data is primed
        p_info.get_obj()
        info.requires_typing = p_info.requires_typing
        info.imports.update(p_info.imports)
        return info
    # endregion Methods
    # region Properties
    
    @property
    def name(self) -> ApiInterfaceName:
        if self._name is None:
            self._name = ApiInterfaceName(
                self._soup_obj)
        return self._name

    @property
    def ns(self) -> ApiNs:
        """Gets the interface Description object"""
        if self._ns is None:
            self._ns = ApiNs(
                self.soup_obj)
        return self._ns

    @property
    def public_members(self) -> ApiPublicMembers:
        if self._public_members is None:
            self._public_members = ApiPublicMembers(self._soup_obj)
        return self._public_members
    
    @property
    def func_block(self) -> ApiFunctionsBlock:
        """Gets Summary Functions block"""
        if self._func_block is None:
            self._func_block = ApiFunctionsBlock(
                self.public_members)
        return self._func_block
    
    @property
    def properties_block(self) -> ApiPropertiesBlock:
        """Gets Summary Properties block"""
        if self._properties_block is None:
            self._properties_block = ApiPropertiesBlock(
                self.public_members)
        return self._properties_block
    
    @property
    def interfaces_block(self) -> ApiInterfacesBlock:
        """Gets Summary Exported Interfaces block"""
        if self._interfaces_block is None:
            self._interfaces_block = ApiInterfacesBlock(
                self.public_members)
        return self._interfaces_block
    
    @property
    def func_summary_rows(self) -> ApiSummaryRows:
        """Get Summary rows for functions"""
        if self._func_summary_rows is None:
            self._func_summary_rows = ApiSummaryRows(
                self.func_block)
        return self._func_summary_rows
    
    @property
    def property_summary_rows(self) -> ApiSummaryRows:
        """Get Summary rows for Properties"""
        if self._property_summary_rows is None:
            self._property_summary_rows = ApiSummaryRows(
                self.properties_block)
        return self._property_summary_rows
    
    @property
    def export_summary_rows(self) -> ApiSummaryRows:
        """Get Summary rows for Exported Interfaces"""
        if self._export_summary_rows is None:
            self._export_summary_rows = ApiSummaryRows(
                self.interfaces_block)
        return self._export_summary_rows
    
    @property
    def func_summaries(self) -> ApiSummaries:
        """Get Summary info list for functions"""
        if self._func_summaries is None:
            self._func_summaries = ApiSummaries(
                self.func_summary_rows)
            d = {}
            summaries = self._func_summaries.get_obj()
            for si in summaries:
                d[si.id] = si
            self._cache[self._si_key].update(d)
        return self._func_summaries
    
    @property
    def property_summaries(self) -> ApiSummaries:
        """Get Summary info list for Properties"""
        if self._property_summaries is None:
            self._property_summaries = ApiSummaries(
                self.property_summary_rows)
            d = {}
            summaries = self._property_summaries.get_obj()
            for si in summaries:
                d[si.id] = si
            self._cache[self._si_key].update(d)
        return self._property_summaries
    
    @property
    def exported_summaries(self) -> ApiSummaries:
        """Get Summary info list for Exported Interfaces"""
        if self._exported_summaries is None:
            self._exported_summaries = ApiSummaries(
                self.export_summary_rows)
        return self._exported_summaries

    @property
    def desc(self) -> ApiDesc:
        """Gets the interface Description object"""
        if self._desc is None:
            self._desc = ApiDesc(self.soup_obj)
        return self._desc
    
    @property
    def inherited(self) -> base.ApiInherited:
        """Gets class that get all inherited value"""
        if self._inherited is None:
            self._inherited = base.ApiInherited(self.soup_obj)
        return self._inherited

    @property
    def soup_obj(self) -> base.SoupObj:
        """Gets soup_obj value"""
        return self._soup_obj

    @property
    def url_obj(self) -> base.UrlObj:
        return self._soup_obj.url_obj
    # endregion Properties
# endregion API Interface classes

# region Parse
class ParserInterface(base.ParserBase):

    # region Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._allow_caching = bool(kwargs.get('allow_cache', True))
        self._api_data = ApiInterfaceData(url_soup=self.url, allow_cache=self._allow_cache)
        self._requires_typing = False
        self._imports: Set[str] = set()
        self._cache = {}
    # endregion Constructor

    def get_dict_data(self) -> dict:
        info = self.get_info()
        items = self._get_data_items()
        info['items'] = items
        return info
    
    def get_parser_args(self) -> dict:
        args = {
            "sort": self.sort
        }
        return args
        
    def get_info(self) -> Dict[str, object]:
        """
        Gets info

        Returns:
            Dict[str, object]: {
                "name": "str, class name",
                "imports": "List[str], imports",
                "namespace": "str, Namespace",
                "extends": "List[str], class extends",
                "desc": "List[str], class description",
                "url": "str, api url"
            }
        """
        key = 'get_info'
        if key in self._cache:
            return self._cache[key]
        ex = []
        for el in self._api_data.inherited.get_obj():
            ex.append(el.fullns)
        # im = self._sdk_data.imports
        result = {
            # 'name': ni.name,
            'name': self._api_data.name.get_obj(),
            # convert set to list for json
            # 'imports': list(im.get_obj()),
            'imports': [],
            'namespace': self._api_data.ns.namespace_str,
            'extends': ex,
            'desc': self._api_data.desc.get_obj(),
            "url": self._api_data.url_obj.url
        }
        logger.debug('ParserInterface.get_info() name: %s', result['name'])
        logger.debug('ParserInterface.get_info() namespace: %s',
                     result['namespace'])
        self._cache[key] = result
        return self._cache[key]
    
    def get_formated_data(self) -> str:
        key = 'get_formated_data'
        if key in self._cache:
            return self._cache[key]
        attribs = self._get_data_items()
        str_lst = base.Util.get_formated_dict_list_str(obj=attribs, indent=4)
        self._cache[key] = str_lst
        return self._cache[key]

    def _get_data_items(self) -> dict:
        key = '_get_data_items'
        if key in self._cache:
            return self._cache[key]
        attribs = {}
        methods = self._get_methods_data()
        prop = self._get_properties_data()
        if 'methods' in methods:
            attribs.update(methods)
        if 'properties' in prop:
            attribs.update(prop)
        self._cache[key] = attribs
        return self._cache[key]
        
    def _get_methods_data(self):
        attribs = {}
        si_lst  = self._api_data.func_summaries.get_obj()
        for i, si in enumerate(si_lst):
            import_info = self._api_data.get_import_info_method(si)
            params_info = self._api_data.get_prams_info(si)
            lst_info = params_info.get_obj()
            if i == 0:
                attribs['methods'] = []
            if import_info.requires_typing:
                self._requires_typing = True
            self._imports.update(import_info.imports)
            args = []
            attrib = {
                "name": si.name,
                "returns": si.return_type,
                "desc": self._api_data.get_desc_detail(si).get_obj(),
                "raises": self._api_data.get_method_ex(si).get_obj() or ''
            }
            for pi in lst_info:
                args.append((pi.name, pi.type, pi.direction))
            attrib['args'] = args
            attribs['methods'].append(attrib)

        if self.sort:
            if 'methods' in attribs:
                newlist = sorted(attribs['methods'], key=lambda d: d['name'])
                attribs['methods'] = newlist
        return attribs
    
    def _get_properties_data(self):
        attribs = {}
        si_lst = self._api_data.property_summaries.get_obj()
        for i, si in enumerate(si_lst):
            if i == 0:
                attribs['properties'] = []
            if not si.name:
                continue
            attrib = {
                "name": si.name,
                "returns": si.return_type,
                "desc": self._api_data.get_desc_detail(si).get_obj(),
                "raises_get": '',
                "raises_set": ''
            }
            attribs['properties'].append(attrib)
        import_info = self._api_data.get_import_info_property()
        if import_info.requires_typing:
            self._requires_typing = True
        self._imports.update(import_info.imports)

        if self.sort:
            if 'properties' in attribs:
                newlist = sorted(attribs['properties'], key=lambda d: d['name'])
                attribs['properties'] = newlist
        return attribs

    @property
    def imports(self) -> Set[str]:
        """Gets imports value"""
        try:
            key = 'get_formated_data'
            if not key in self._cache:
                msg = "ParserInterface.get_formated_data() method must be called before accessing imports"
                raise Exception(msg)
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        return self._imports
    @property
    def requires_typing(self) -> bool:
        """Gets requires typing value"""
        try:
            key = 'get_formated_data'
            if not key in self._cache:
                msg = "ParserInterface.get_formated_data() method must be called before accessing requires_typing"
                raise Exception(msg)
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        return self._requires_typing
# endregion Parse

# region Writer


class InterfaceWriter(base.WriteBase):
    # region Constructor
    @TypeCheckKw(arg_info={
        "write_file": 0, "write_json": 0,
        "copy_clipboard": 0, "print_template": 0,
        "print_json": 0, "clear_on_print": 0,
        "write_template_long": 0
        },
        types=[bool],
        ftype=DecFuncEnum.METHOD)
    def __init__(self, parser: ParserInterface, **kwargs):
        super().__init__(**kwargs)
        self._parser: ParserInterface = parser
        self._copy_clipboard: bool = kwargs.get('copy_clipboard', False)
        self._print_template: bool = kwargs.get('print_template', False)
        self._write_file: bool = kwargs.get('write_template', False)
        self._print_json: bool = kwargs.get('print_json', True)
        self._write_json: bool = kwargs.get('write_json', False)
        self._clear_on_print: bool = kwargs.get('clear_on_print', True)
        self._write_template_long: bool = kwargs.get('write_template_long', False)
        self._indent_amt = 4
        self._json_str = None
        self._p_name: str = None
        self._p_imports: Set[str] = set()
        self._p_imports_typing: Set[str] = set()
        self._p_namespace: str = None
        self._p_extends: List[str] = None
        self._p_desc: List[str] = None
        self._p_data: str = None
        self._p_url: str = None
        self._p_requires_typing = False
        self._path_dir = Path(__file__).parent
        self._cache: Dict[str, object] = {}
        
        t_file = 'interface'
        if not self._write_template_long:
            t_file += '_stub'
        t_file += '.tmpl'
        _path = Path(self._path_dir, 'template', t_file)
        try:
            if not _path.exists():
                raise FileNotFoundError(f"unable to find templae file '{_path}'")
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        self._template_file = _path
        self._template: str = self._get_template()
    # endregion Constructor

    def write(self):
        self._set_info()
        self._set_template_data()
        logger.info("Processing %s.%s", self._p_namespace, self._p_name)
        try:
            if self._clear_on_print and (self._print_template or self._print_json):
                logger.debug('Printing to terminal')
                os.system('cls' if os.name == 'nt' else 'clear')
            if self._copy_clipboard:
                xerox.copy(self._template)
                logger.debug('copied to clipbord')
            if self._print_template:
                print(self._template)
            if self._print_json:
                print(self._get_json())
            if self._write_file:
                self._write_to_file()
            if self._write_json:
                self._write_to_json()
        except Exception as e:
            logger.exception(e)
    
    def _get_json(self) -> str:
        if not self._json_str is None:
            return self._json_str
        p_dict = {}
        p_dict['from_imports'] = self._get_from_imports()
        p_dict['from_imports_typing'] = self._get_from_imports_typing()
        p_dict.update(self._parser.get_dict_data())
        
        json_dict = {
            "id": JSON_ID,
            "version": __version__,
            "timestamp": str(base.Util.get_timestamp_utc()),
            "name": p_dict['name'],
            "type": "interface",
            "namespace": p_dict['namespace'],
            "parser_args": self._parser.get_parser_args(),
            "writer_args": {},
            "data": p_dict
        }
        str_jsn = base.Util.get_formated_dict_list_str(obj=json_dict, indent=2)
        self._json_str = str_jsn
        return self._json_str
    
    def _get_template(self):
        with open(self._template_file) as f:
            contents = f.read()
        return contents

    # region get Imports
    def _get_from_imports(self) -> List[List[str]]:
        key = '_get_from_imports'
        if key in self._cache:
            return self._cache[key]
        lst = []
        for ns in self._p_imports:
            f, n = base.Util.get_rel_import(
                i_str=ns, ns=self._p_namespace
            )
            lst.append([f, n])
        self._cache[key] = lst
        return self._cache[key]

    def _get_from_imports_typing(self) -> List[List[str]]:
        key = '_get_from_imports_typing'
        if key in self._cache:
            return self._cache[key]
        lst = []
        for ns in self._p_imports_typing:
            f, n = base.Util.get_rel_import(
                i_str=ns, ns=self._p_namespace
            )
            # lst.append(f)
            # lst.append(n)
            lst.append([f, n])
        self._cache[key] = lst
        return self._cache[key]
    # endregion get Imports
    
    def _set_template_data(self):
        if self._write_template_long is False:
            return
        self._template = self._template.replace('{name}', self._p_name)
        self._template = self._template.replace('{ns}', str(self._p_namespace))
        self._template = self._template.replace('{link}', self._p_url)
        self._template = self._template.replace(
            '{requires_typing}', str(self._p_requires_typing))
        self._template = self._template.replace(
            '{inherits}', base.Util.get_string_list(lines=self._p_extends))
        self._template = self._template.replace(
            '{imports}', "[]")
        self._template = self._template.replace(
            '{from_imports}',
            base.Util.get_formated_dict_list_str(self._get_from_imports())
        )
        self._template = self._template.replace(
            '{from_imports_typing}',
            base.Util.get_formated_dict_list_str(
                self._get_from_imports_typing())
        )
        if len(self._p_desc) > 0:
            desc = base.Util.get_formated_dict_list_str(self._p_desc, indent=4)
        else:
            desc = "[]"
        self._template = self._template.replace('{desc}', desc)
        if self._indent_amt > 0:
            indent = ' ' * self._indent_amt
            indented = textwrap.indent(self._p_data, indent).lstrip()
        else:
            indented = self._p_data.lstrip()
        self._template = self._template.replace('{data}', indented)

    def _set_info(self):
        def get_extends(lst:List[str]) -> List[str]:
            return [base.Util.get_last_part(s) for s in lst]
            # return [s.rsplit('.', 1)[1] for s in lst]
        data = self._parser.get_info()
        self._p_name = data['name']
        self._p_namespace = data['namespace']
        self._p_extends = get_extends(data['extends'])
        self._p_desc = data['desc']
        self._p_url = data['url']
        self._p_data = self._parser.get_formated_data()
        self._validate_p_info()
        _imports = data['imports']
        self._p_imports.update(_imports)
        self._p_imports.update(data['extends'])
        self._p_imports_typing.update(self._parser.imports)
        if len(self._p_imports_typing) > 0:
            self._p_requires_typing = True
        if not self._p_requires_typing:
            self._p_requires_typing = self._parser.requires_typing
        if self._write_file or self._write_json:
            self._file_full_path = self._get_uno_obj_path()
    
    def _validate_p_info(self):
        try:
            if not self._p_name:
                raise Exception(
                    "InterfaceWriter: validation fail: name is an empty string.")
            if not self._p_url:
                raise Exception(
                    "InterfaceWriter: validation fail: url is an empty string.")
            if not self._p_namespace:
                raise Exception(
                    "InterfaceWriter: validation fail: namespace is an empty string.")
        except Exception as e:
            logger.error(e)
            raise e
    
    def _get_uno_obj_path(self) -> Path:
        key = '_get_uno_obj_path'
        if key in self._cache:
            return self._cache[key]
        if not self._p_name:
            try:
                raise Exception("InterfaceWriter._get_uno_obj_path() Parser provided a name that is an empty string.")
            except Exception as e:
                logger.error(e, exc_info=True)
                raise e
            
        uno_obj_path = Path(self._path_dir.parent,
                            base.APP_CONFIG.uno_base_dir)
        name_parts: List[str] = self._p_namespace.split('.')
        # ignore com, sun, star
        path_parts = name_parts[3:]
        path_parts.append(self._p_name + '.tmpl')
        obj_path = uno_obj_path.joinpath(*path_parts)
        self._mkdirp(obj_path.parent)
        self._cache[key] = obj_path
        return self._cache[key]

    def _write_to_file(self):
        with open(self._file_full_path, 'w') as f:
            f.write(self._template)
        logger.info("Created file: %s", self._file_full_path)
    
    def _write_to_json(self):
        p = self._file_full_path.parent
        jsn_p = p / (str(self._file_full_path.stem) + '.json')
        jsn_str = self._get_json()
        with open(jsn_p, 'w') as f:
            f.write(jsn_str)
        logger.info("Created file: %s", jsn_p)
# endregion Writer


def _main():
   
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1graphic_1_1XSvgParser.html'
    url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1office_1_1XAnnotation.html'
    # url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XItemList.html'
    sys.argv.extend(['--log-file', 'debug.log', '-v', '-n', '-u', url])
    main()

def main():
    global logger
    # region Parser
    parser = argparse.ArgumentParser(description='interface')
    parser.add_argument(
        '-u', '--url',
        help='Source Url',
        type=str,
        required=True)
    parser.add_argument(
        '-s', '--no-sort',
        help='No sorting of results',
        action='store_false',
        dest='sort',
        default=True)
    parser.add_argument(
        '-x', '--no-cache',
        help='No caching',
        action='store_false',
        dest='cache',
        default=True)
    parser.add_argument(
        '-p', '--no-print-clear',
        help='No clearing of terminal when output to terminal.',
        action='store_false',
        dest='no_print_clear',
        default=True)
    parser.add_argument(
        '-g', '--long-template',
        help='Writes a long format template. Requires --write-template is set. No Autoload',
        action='store_true',
        dest='long_format',
        default=False)
    parser.add_argument(
        '-c', '--clipboard',
        help='Copy to clipboard',
        action='store_true',
        dest='clipboard',
        default=False)
    parser.add_argument(
        '-n', '--print-json',
        help='Print json to terminal',
        action='store_true',
        dest='print_json',
        default=False)
    parser.add_argument(
        '-m', '--print-template',
        help='Print template to terminal',
        action='store_true',
        dest='print_template',
        default=False)
    parser.add_argument(
        '-t', '--write-template',
        help='Write template file into obj_uno subfolder',
        action='store_true',
        dest='write_template',
        default=False)
    parser.add_argument(
        '-j', '--write-json',
        help='Write json file into obj_uno subfolder',
        action='store_true',
        dest='write_json',
        default=False)
    parser.add_argument(
        '-v', '--verbose',
        help='verbose logging',
        action='store_true',
        dest='verbose',
        default=False)
    parser.add_argument(
        '-L', '--log-file',
        help='Log file to use. Defaults to interface.log',
        type=str,
        required=False)

    args = parser.parse_args()
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'interface.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    # endregion Parser
    if not args.no_print_clear:
        os.system('cls' if os.name == 'nt' else 'clear')
    logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing Url %s' % args.url)
    
    p = ParserInterface(
        url=args.url,
        sort=args.sort,
        cache=args.cache
    )
    w = InterfaceWriter(
        parser=p,
        print_template=args.print_template,
        print_json=args.print_json,
        copy_clipboard=args.clipboard,
        write_template=args.write_template,
        write_json=args.write_json,
        clear_on_print=(not args.no_print_clear),
        write_template_long=args.long_format
        )
    if args.print_template is False and args.print_json is False:
        print('')
    w.write()



if __name__ == '__main__':
    _main()
