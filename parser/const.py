#!/usr/bin/env python
# coding: utf-8
"""
Process a link to a page that contains a constant
"""
from enum import IntEnum, auto
import os
import sys
import re
import logging
import argparse
import xerox # requires xclip - sudo apt-get install xclip
import textwrap
from typing import Dict, List, Set, Union
from dataclasses import dataclass, field
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from kwhelp.decorator import AcceptedTypes, DecFuncEnum, TypeCheckKw
from collections import namedtuple
from pathlib import Path
from abc import ABC, abstractmethod, abstractproperty
try:
    import base
except ModuleNotFoundError:
    import parser.base as base
from parser.base import SoupObj, SummaryInfo
from logger.log_handle import get_logger
from parser import __version__, JSON_ID
from parser.type_mod import PythonType

logger = None

def _set_loggers(l: Union[logging.Logger, None]):
    global logger, base
    logger = l
    base.logger = l

_set_loggers(None)

pattern_hex = re.compile(r"0x[0-9A-Fa-f]+")

dataitem = namedtuple(
    'dataitem', ['value', 'raw_value', 'name', 'datatype', 'lines'])

@dataclass
class DataItem:
    name: str
    value: str
    type: str
    lines: List[str] = field(default_factory=list)

# region Rule Engine
class ValTypeEnum(IntEnum):
    STRING = auto()
    INTEGER = auto()


@dataclass
class Val:
    text: str = ''
    identity: str = ''
    is_flags: bool = False
    val_type: ValTypeEnum = ValTypeEnum.INTEGER
    values: List[Union[int, str]] = field(default_factory=list)

class IRule(ABC):
    @abstractmethod
    def __init__(self, rules: 'IRules') -> None:
        """Constructor"""
    @abstractmethod
    def get_is_match(self, tag: Tag) -> bool:
        """
        Gets if rule is a match
        
        Args:
            in_type (str): LibreOffice Api type such as Long.
        """
    @abstractmethod
    def get_val(self) -> Val:
        """Gets a Val if there is a rule match"""
    @abstractproperty
    def identity(self) -> str:
        """Gets id"""

class IRules(ABC):
    @abstractmethod
    def get_rule_instance(self, rule: IRule) -> IRule:
        """Gets a rule instance"""

    @abstractmethod
    def get_val(self, tag: Tag) -> Union[Val, None]:
        """Gets a Val if there is a rule match"""

    @abstractmethod
    def get_summary_by_name(self, name: str) -> Union[base.SummaryInfo, None]:
        """Gets summary info by name"""
    @abstractmethod
    def is_cached(self, sid: str) -> bool:
        """Gets is an id is in the cache"""

    @abstractmethod
    def get_cached(self, sid: str) -> Val:
        """Gets a Val from cache"""

    @abstractmethod
    def set_cached(self, val:Val) -> None:
        """set or updates cached"""

    @abstractproperty
    def summary_block(self) -> base.ApiSummaryBlock:
        """Gets the block that contains summary info for all constants of the current html page."""

    @abstractproperty
    def summaries(self) -> Dict[str, base.SummaryInfo]:
        """All the summaries for a html page"""

    @abstractproperty
    def soup(self) -> SoupObj:
        """Gets the soup object for the page"""

class Rules(IRules):
    def __init__(self, si_dict: Dict[str, base.SummaryInfo], summary_block: base.ApiSummaryBlock) -> None:
        self._summary_block: base.ApiSummaryBlock = summary_block
        self._summaries = si_dict
        self._name_map = {}
        for _, si in si_dict.items():
            self._name_map[si.name] = si.id
        self._rules: List[IRule] = []
        self._cache = {}
        self. _cached_vals = {}
        self._register_known_rules()
        
    # region Methods
    def register_rule(self, rule: IRule) -> None:

        if not issubclass(rule, IRule):
            msg = "Rules.register_rule(), rule arg must be child class of ITypeRule"
            raise TypeError(msg)
        if rule in self._rules:
            msg = "Rules.register_rule() Rule is already registered"
            self._log.warning(msg)
            return
        self._reg_rule(rule=rule)

    def unregister_rule(self,  rule: IRule):
        """
        Unregister a rule

        Args:
            rule (IRule): Rule to unregister
        """
        try:
            self._rules.remove(rule)
        except ValueError as e:
            msg = f"{self.__class__.__name__}.unregister_rule() Unable to unregister rule."
            raise ValueError(msg) from e

    # region Cache
    def is_cached(self, sid: str) -> bool:
        """Gets is an id is in the cache"""
        return sid in self. _cached_vals
    
    def get_cached(self, sid: str) -> Union[Val, None]:
        """Gets a Val from cache"""
        return self. _cached_vals.get(sid, None)
    
    def set_cached(self, val: Val) -> None:
        """set or updates cached"""
        self. _cached_vals[val.identity] = val
    # endregion Cache

    def _reg_rule(self, rule: IRule):
        self._rules.append(rule)

    def _register_known_rules(self):
        self._reg_rule(rule=RuleInt)
        self._reg_rule(rule=RuleHex)
        self._reg_rule(rule=RuleNamedFlags)
        self._reg_rule(rule=RuleDetail)

    def _get_rule(self, tag: Tag) -> Union[IRule, None]:

        match_inst = None
        for rule in self._rules:
            key = str(id(rule))
            if key in self._cache:
                inst = self._cache[key]
            else:
                inst: IRule = rule(self)
                self._cache[key] = inst
            if inst.get_is_match(tag):
                match_inst = inst
                break
        return match_inst

    def get_val(self, tag: Tag) -> Union[Val, None]:
        match = self._get_rule(tag)
        if match:
            return match.get_val()
        return None

    def get_rule_instance(self, rule: IRule) -> IRule:
        if not issubclass(rule, IRule):
            msg = "Rules.get_rule_instance(), rule arg must be child class of ITypeRule"
            self._log.error(msg)
            raise TypeError(msg)
        key = str(id(rule))
        if key in self._cache:
            return self._cache[key]
        else:
            self._cache[key] = rule(self)
        return self._cache[key]
    
    def get_summary_by_name(self, name: str) -> Union[base.SummaryInfo, None]:
        """Gets summary info by name"""
        _id = self._name_map.get(name, None)
        if _id is None:
            return None
        return self._summaries[_id]
    # endregion Methods

    # region Properties
    @property
    def summary_block(self) -> base.ApiSummaryBlock:
        """Gets the block that contains summary info for all constants of the current html page."""
        return self._summary_block

    @property
    def summaries(self) -> Dict[str, base.SummaryInfo]:
        """Gets summaries for a html page. Key is ID."""
        return self._summaries

    @property
    def soup(self) -> SoupObj:
        """Gets the soup object for the page"""
        return self._summary_block.soup
    # endregion Properties
class RuleBase(IRule):
    def __init__(self, rules: IRules) -> None:
        self._rules = rules
        self._info_tag: Tag = None
        self._info_text: str = None
        self._id: str = None
        self._tag: Tag = None
        self._url = rules.summary_block.url_obj.url
        self._cached: Val = None

    def __set_defaults(self):
        self._info_tag = None
        self._info_text = None
        self._id = None
        self._tag = None
        self._cached = None

    def get_is_match(self, tag: Tag) -> bool:
        self.__set_defaults()
        if not tag:
            return False
        if tag.name != 'tr':
            return False
        _class: List[str] = tag.get('class', [])
        if len(_class) == 0:
            return False
        try:
            self._id = _class[0].split(":")[1]
        except Exception:
            self.__set_defaults()
            return False
        if self._rules.is_cached(self.identity):
            self._cached = self._rules.get_cached(self.identity)
            return True
        info_tag = tag.findChild('td', class_='memItemRight')
        if not info_tag:
            return False
        self._tag = tag
        self._info_tag = info_tag
        info_text = self._info_tag.text.strip()
        # remove extra whitespaces
        self._info_text = ' '.join(info_text.split())
        return True

    @property
    def identity(self) -> str:
        """
        Gets id of current match. This will be the same id used in summary info.

        Raises:
            Exception: If there has not been a successful match then error is raised

        Returns:
            str: id string
        """
        if self._id is None:
            raise Exception(
                "Identity is None: Did you forget to call get_is_match? Identity is only available when there is a sucessfull match.")
        return self._id

class RuleInt(RuleBase):
    def __init__(self, rules: IRules) -> None:
        super().__init__(rules=rules)
        self._val = None

    def get_is_match(self, tag: Tag) -> bool:
        self._val = None
        if not super().get_is_match(tag):
            return False
        if self._cached:
            return True
        parts = self._info_text.split("=")
        if len(parts) != 2:
            return False
        part = parts[1].strip()
        is_match = False
        try:
            self._val = int(part)
            is_match = True
        except ValueError:
            self._val = None
            is_match = False
        return is_match
    
    def get_val(self) -> Val:
        """Gets a Val if there is a rule match"""
        if self._cached:
            return self._cached
        if self._val is None:
            raise Exception(
                f"{self.__class__.__name__}.get_val() Value is missing. Did you run get_is_match() before get_val()?")
        if isinstance(self._val, int):
            si: SummaryInfo = self._rules.summaries[self.identity]
            result = Val(text=si.name,
                identity=self.identity, is_flags=False,
                         val_type=ValTypeEnum.INTEGER, values=[self._val])
            self._val = None
            self._rules.set_cached(result)
            return result
        else:
            raise Exception(
                f"{self.__class__.__name__}.get_val() Something went wrong. expected val was int but got {type(self._val)}")


class RuleHex(RuleBase):
    def __init__(self, rules: IRules) -> None:
        super().__init__(rules=rules)
        self._val = None

    def get_is_match(self, tag: Tag) -> bool:
        self._val = None
        if not super().get_is_match(tag):
            return False
        if self._cached:
            return True
        parts = self._info_text.split("=")
        if len(parts) != 2:
            return False
        part = parts[1].strip()
        is_match = False
        try:
            self._val = int(part, base=16)
            is_match = True
        except ValueError:
            self._val = None
            is_match = False
        return is_match

    def get_val(self) -> Val:
        """Gets a Val if there is a rule match"""
        if self._cached:
            return self._cached
        if self._val is None:
            raise Exception(
                f"{self.__class__.__name__}.get_val() Value is missing. Did you run get_is_match() before get_val()?")
        if isinstance(self._val, int):
            si: SummaryInfo = self._rules.summaries[self.identity]
            result = Val(text=si.name,
                         identity=self.identity, is_flags=False,
                         val_type=ValTypeEnum.INTEGER, values=[self._val])
            self._val = None
            self._rules.set_cached(result)
            return result
        else:
            raise Exception(
                f"{self.__class__.__name__}.get_val() Something went wrong. expected val was int but got {type(self._val)}")


class RuleNamedFlags(RuleBase):
    def __init__(self, rules: IRules) -> None:
        super().__init__(rules=rules)
        self._names: List[str] = None
        self._infos: List[SummaryInfo] = None
        self._recursive_mode = False

    def get_is_match(self, tag: Tag) -> bool:
        # if self._recursive_mode:
        #     return False
        self._set_defaults()
        if not super().get_is_match(tag):
            return False
        if self._cached:
            return True
        if self._info_text.find('|') < 0:
            # no 'or' found
            return False
        parts = self._info_text.split("=")
        if len(parts) != 2:
            return False
        self._names = [s.strip() for s in parts[1].split('|')]
        self._infos: List[SummaryInfo] = []
        for name in self._names:
            si = self._rules.get_summary_by_name(name)
            if not si:
                self._set_defaults()
                return False
            self._infos.append(si)
        return True

    def get_val(self) -> Val:
        """Gets a Val if there is a rule match"""
        if self._cached:
            return self._cached
        if not self._is_valid():
            raise Exception(
                f"{self.__class__.__name__}.get_val() Values are missing. Did you run get_is_match() before get_val()?: Url: {self._url}")
        vals: List[Val] = []
        for si in self._infos:
            try:
                tag = self._get_from_block(si)
            except Exception:
                self._set_defaults()
                raise

            val = self._get_recursive_match(tag=tag)
            if not val:
                self._set_defaults()
                raise Exception(
                    f"{self.__class__.__name__}.get_val() Fail to find a match during recursive search for {si.name} with id: '{si.id}' Url: {self._url}")
            vals.append(val)
        try:
            result = self._get_val_from_vals(vals)
        except Exception:
            raise
        finally:
            self._set_defaults()
        self._rules.set_cached(result)
        return result

    # region Private Methods
    def _set_defaults(self):
        self._names = None
        self._infos = None

    def _is_valid(self) -> bool:
        if self._names is None:
            return False
        if self._infos is None:
            return False
        return True

    def _get_val_from_vals(self, vals: List[Val]) -> Val:
        if len(vals) == 0:
            raise Exception(
                    f"{self.__class__.__name__}._get_val_from_vals() There are no values! Url: {self._url}")
    
        flags: List[str] = []
        for val in vals:
            if val.val_type == ValTypeEnum.INTEGER:
                flags.append(val.text)
            else:
                flags.extend(val.values)
        result = Val(
            identity=self.identity,
            is_flags=True,
            val_type=ValTypeEnum.STRING,
            values=flags
        )
        return result

    def _get_from_block(self, si: SummaryInfo) -> Tag:
        _id = 'memitem:' + si.id
        tag = self._rules.summary_block.get_obj()
        if not tag:
            raise Exception(
                f"{self.__class__.__name__}._get_from_block() Summary block did not yield a result! Url: {self._url}")
        tag_row = tag.find('tr', class_=_id)
        if not tag_row:
            raise Exception(
                f"{self.__class__.__name__}._get_from_block() Summary block did not find a row with class matching: '{_id}'! Url: {self._url}")
        return tag_row

    def _get_recursive_match(self, tag: Tag) -> Union[Val, None]:
        try:
            self._recursive_mode = True
            return self._rules.get_val(tag)
        except:
            raise
        finally:
            self._recursive_mode = False
    # endregion Private Methods


class RuleDetail(RuleBase):
    """Gets value from details section"""
    def __init__(self, rules: IRules) -> None:
        super().__init__(rules=rules)
        self._text: str = None

    def _set_defaults(self) -> None:
        self._text = None

    def get_is_match(self, tag: Tag) -> bool:
        self._set_defaults()
        # ignore super is match but run to set id and cached
        super().get_is_match(tag)
        if self._cached:
            return True
        parts = self._info_text.split("=")
        if len(parts) != 1:
            return False
        # single name only. Now have to get value from body.
        try:
            # = UNI_DIGIT | UNI_LETTER_NUMBER | UNI_OTHER_NUMBER
            text = self._get_text()
            parts = text.split(sep='=')
            if len(parts) != 2:
                return False
            self._text = parts[1]
        except Exception:
            self._set_defaults()
            return False
        return True

    def get_val(self) -> Val:
        """Gets a Val if there is a rule match"""
        if self._cached:
            return self._cached
        if self._text is None:
            raise Exception(
                f"{self.__class__.__name__}.get_val() Value is missing. Did you run get_is_match() before get_val()?")
        # text could be hex or int.
        val = self._get_from_int()
        if val:
            self._rules.set_cached(val)
            return val
        names = [s.strip() for s in self._text.split('|')]
        # confirm name and return them.
        
        if len(names) == 0:
            raise Exception(
                f"{self.__class__.__name__}.get_val() There are no names found from details section!")
        try:
            self._validate_names(names=names)
        except Exception:
            self._set_defaults()
            raise
        result = Val(identity=self.identity, is_flags=True, val_type=ValTypeEnum.STRING, values=names)
        
        self._set_defaults()
        self._rules.set_cached(result)
        return result


    def _validate_names(self, names: List[str]) -> None:
        for name in names:
            si: SummaryInfo = self._rules.get_summary_by_name(name)
            if not si:
                raise Exception(
                    f"{self.__class__.__name__}.get_val() Name '{name}' did not match any summary info!")
        return None

    def _get_from_int(self) -> Union[Val, None]:
        """Convert text to int if possible"""
        si: SummaryInfo = self._rules.summaries[self.identity]
        try:
            i = None
            try:
                i = int(self._text)
            except ValueError:
                i = None
                pass
            if i is None:
                i = int(self._text, 16)
            val = Val(text=si.name,identity=self.identity, is_flags=False,val_type=ValTypeEnum.INTEGER ,values=[i])
            return val
        except ValueError:
            return None

    def _get_details_block(self) -> base.ApiDescBlock:
        return base.ApiDetailBlock(self._rules.soup, self.identity)
    
    def _get_text(self) -> str:
        block = self._get_details_block()
        tag = block.get_obj()
        if not tag:
            raise Exception
        f_tag = tag.find('div', class_='fragment')
        if not f_tag:
            raise Exception
        lines: ResultSet = f_tag.find_all('div', class_='line')
        if not lines:
            raise Exception
        text: str = None
        for i, line in enumerate(lines):
            if i == 0:
                text = ''
            else:
                text += ' '
            text += line.text
        if not text:
            raise Exception
        # replace \n with space
        text = " ".join(text.splitlines())
        # remove extra whitespace
        return " ".join(text.split())

# endregion Rule Engine

# region API classes
class ApiConstBlock(base.ApiSummaryBlock):
    def _get_match_name(self) -> str:
        return 'var-members'

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

class ApiSummaries(base.BlockObj):
    def __init__(self, block: base.ApiSummaryRows) -> None:
        self._block: base.ApiSummaryRows = block
        super().__init__(self._block.soup)
        self._requires_typing = False
        self._imports: Set[str] = set()
        self._data = None
    
    def get_obj(self) -> Dict[str, SummaryInfo]:
        """
        Gets a dictionary of summary info. Key is ID.

        Raises:
            Exception: If error parsing info.

        Returns:
            Dict[str, base.SummaryInfo]: summary info dictionary.
        """
        if not self._data is None:
            return self._data
        self._data: Dict[str, SummaryInfo] = {}
        # get all rows
        tags: List[Tag] = self._block.get_obj()
        if len(tags) == 0:
            msg = f"{self.__class__.__name__}.get_obj() no table rows that can be used to parse const info."
            msg += f" Url: {self.url_obj.url}"
            logger.error(msg)
            raise Exception(msg)
        
        for tag in tags:
            # parse out type, name, id
            sid = self._get_id(tag)
            name = self._get_name(tag)
            p_type = self._get_type(tag, name)
            si = SummaryInfo(
                id = sid,
                name = name,
                type = p_type.type,
                p_type=p_type
            )
            if p_type.requires_typing:
                self._requires_typing = True
            self._imports.update(p_type.get_all_imports())
            self._data[si.id] = si
        return self._data

    def _get_name(self, tr:Tag) -> str:
        # name should be in first a tag.
        tag: Tag = tr.findChild('td', class_='memItemRight')
        if not tag:
            msg = f"{self.__class__.__name__}._get_name() No data found to get name from. Url: {self.url_obj.url}"
            logger.error(msg)
            raise Exception(msg)
        a_tag = tag.findChild('a')
        if a_tag:
            return a_tag.text.strip()
        # for some reason a_tag not found. Let try straight text
        text = tag.text.strip()
        # text: ASC_UPALPHA = 0x00000001
        parts = text.split(sep="=", maxsplit=1)
        if len(parts) == 1:
            msg = f"{self.__class__.__name__}._get_name() No valid name can be parsed. Url: {self.url_obj.url}"
            logger.error(msg)
            raise Exception(msg)
        return parts[0]

    def _get_type(self, tr: Tag, name: str) -> PythonType:
        # select first cell
        tag: Tag = tr.findChild('td', class_='memItemLeft')
        # tag.text 'const long ' format
        if not tag:
            msg = f"{self.__class__.__name__}._get_type() {name}, No data found to get type for. Url: {self.url_obj.url}"
            logger.error(msg)
            raise Exception(msg)
        text = tag.text.strip()
        parts = text.split()
        type_name = parts.pop()
        p_type = base.Util.get_python_type(type_name)
        logger.debug(
            "%s._get_type(), found type: %s for name: %s",
            self.__class__.__name__, p_type.type, name)
        return p_type
    
    def _get_id(self, tr:Tag) -> str:
        result = None
        classes: List[str] = tr.get('class', [])
        if len(classes) == 0:
            msg = f"{self.__class__.__name__}._get_id() No valid class that can be parsed. Url: {self.url_obj.url}"
            logger.error(msg)
            raise Exception(msg)
        
        for c in classes:
            if c.startswith('memitem:'):
                result = base.Util.get_last_part(input=c, sep=":")
                break
        if result is None:
            msg = f"{self.__class__.__name__}._get_id() Failed to get id. Url: {self.url_obj.url}"
            logger.error(msg)
            raise Exception(msg)
        return result

class ApiValues(base.BlockObj):
    def __init__(self, summary_block: base.ApiSummaryBlock, api_summaries: ApiSummaries) -> None:
        self._summary_block: base.ApiSummaryBlock = summary_block
        self._api_summaries: ApiSummaries = api_summaries
        super().__init__(self._summary_block.soup)
        self._data = None

    def _get_tag(self, si: SummaryInfo, block_tag: Tag) -> Tag:
        _id = "memitem:" + si.id
        tag: Tag = block_tag.find('tr', class_=_id)
        if not tag:
            msg = f"{self.__class__.__name__} Failed in finding data for {si.name} with class: '{_id}'. Url: {self.url_obj.url}"
            raise Exception(msg)
        return tag

    def get_obj(self) -> Dict[str, Val]:
        if not self._data is None:
            return self._data
        sum_block_tag = self._summary_block.get_obj()
        if not sum_block_tag:
            msg = f"{self.__class__.__name__} instance of ApiSummaryBlock failed to get any data. Url: {self.url_obj.url}"
            logger.error(msg)
            raise Exception(msg)
        api_summaries: Dict[str, SummaryInfo] = self._api_summaries.get_obj()
        keys = list(api_summaries.keys())
        if len(keys) == 0:
            msg = f"{self.__class__.__name__} instance of ApiSummaries failed to get any data. Url: {self.url_obj.url}"
            logger.error(msg)
            raise Exception(msg)
        self._data = {}
        rules = Rules(si_dict=api_summaries, summary_block=self._summary_block)
        for k in keys:
            si: SummaryInfo = api_summaries[k]
            try:
                t: Tag = self._get_tag(si=si, block_tag=sum_block_tag)
                val = rules.get_val(t)
                if not val:
                    msg = f"{self.__class__.__name__} Failed to get data from rules engine for {si.name} with id of '{si.id}'."
                    raise Exception(msg)
                self._data[si.id] = val
            except Exception as e:
                msg = str(e) + '\nUrl: ' + self.url_obj.url
                logger.exception(msg, exc_info=True)
                raise Exception(msg) from e
        return self._data


class ApiData(base.APIData):
    def __init__(self, url_soup: Union[str, base.SoupObj], allow_cache: bool):
        super().__init__(url_soup=url_soup, allow_cache=allow_cache)
        self._ns: ApiNs = None
        self._api_const_block: ApiConstBlock = None
        self._api_const_summary_rows: base.ApiSummaryRows = None
        self._api_summaries: ApiSummaries = None
        self._api_values: ApiValues = None
        self._cache: Dict[str, object] = {}

    # region Methods  
    def get_data_items(self) -> List[DataItem]:
        key = 'get_data_items'
        if key in self._cache:
            return self._cache[key]
        def build_val(val: Val) -> str:
            if not val.is_flags:
                return str(val.values[0])
            return " | ".join([str(v) for v in val.values])
        
        summaries = self.api_summaries.get_obj()
        values = self.api_values.get_obj()
        keys = summaries.keys()
        results: List[DataItem] = []
        for k in keys:
            si = summaries[k]
            val =values[k]
            desc = self.get_desc_detail(si.id).get_obj()
            di = DataItem(
                name=si.name,
                value = build_val(val),
                type=si.p_type.type,
                lines=desc
            )
            results.append(di)
        self._cache[key] = results
        return self._cache[key]

    # endregion Methods

    # region Properties

    @property
    def ns(self) -> ApiNs:
        """Gets the interface Description object"""
        if self._ns is None:
            self._ns = ApiNs(
                self.soup_obj)
        return self._ns

    @property
    def api_const_block(self):
        """Get Block containd all const types, names and values"""
        if self._api_const_block is None:
            self._api_const_block = ApiConstBlock(self.public_members)
        return self._api_const_block

    @property
    def api_summary_rows(self) -> base.ApiSummaryRows:
        """Gets the summary rows for api_const_block"""
        if self._api_const_summary_rows is None:
            self._api_const_summary_rows = base.ApiSummaryRows(self.api_const_block)
        return self._api_const_summary_rows
    @property
    def api_summaries(self) -> ApiSummaries:
        """
        Get the summaries. This classes get_object() returns a list of SummaryInfo
        """
        if self._api_summaries is None:
            self._api_summaries = ApiSummaries(self.api_summary_rows)
        return self._api_summaries

    @property
    def api_values(self) -> ApiValues:
        if self._api_values is None:
            self._api_values = ApiValues(self.api_const_block, self.api_summaries)
        return self._api_values
    # endregion Properties
# endregion API classes

class Parser(base.ParserBase):
    
    # region init
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._soup = base.SoupObj(url=self.url, allow_cache=self.allow_cache)
        self._cache = {
            "python_types": []
        }

    # endregion init

    # region Info
    def get_info(self) -> Dict[str, str]:
        """
        Gets info

        Returns:
            Dict[str, str]: {
                "name": "name of constant",
                "fullname": "full name such as com.sun.star.awt.Command"
                "desc": "description of constant",
                "url": "Url to LibreOffice of constant",
                "namespace": "Namespace such as com.sun.star.awt.Command"
            }
        """
        key = 'get_info'
        if key in self._cache:
            return self._cache[key]
        self._cache[key] = {}
        try:
            if not self._url:
                raise ValueError('URL is not set')
            soup = self._soup.soup
            full_name = self._get_full_name(soup=soup)
            name = self._get_name(soup=soup)
            desc = self._get_desc(soup=soup)
            ns = base.UrlObj(self.url)
            info = {
                "name": name,
                "fullname": full_name,
                "desc": desc,
                "url": self.url,
                "namespace": ns.namespace_str
            }
            self._cache[key].update(info)
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        return self._cache[key]

    def get_parser_args(self) -> dict:
        args = {
            "sort": self.sort
        }
        return args
    # endregion Info
    # region Data
    def get_dict_data(self) -> dict:
        info = self.get_info()
        items = self._get_data_items()
        # set to list for json
        info['items'] = items
        return info


    def get_data(self) -> List[dataitem]:
        """
        Gets constants data

        Returns:
            List: list of tuple (value:number|str, raw_value:str, name:str, type:str, lines:[])

        Raises:
            ValueError: If url is not set.
        """
        key = 'get_data'
        if key in self._cache:
            return self._cache[key]
        try:
            if not self._url:
                raise ValueError('URL is not set')
            soup = BeautifulSoup(self.get_raw_html(), 'lxml')

            items = self._get_memitems(soup=soup)
            const_info = self._get_const_details(memitetms=items)
            self._cache[key] = const_info
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        return self._cache[key]

    def get_formated_data(self):
        key = 'get_formated_data'
        if key in self._cache:
            return self._cache[key]
        try:
            data = self.get_data()
            lines = []
            for itm in data:
                s = f'"{itm.name}": ["{itm.raw_value}"'
                if len(itm.lines) > 0:
                    s_ln = ', [\n'
                    for j, line in enumerate(itm.lines):
                        if j > 0:
                            s_ln += ',\n    "",\n'
                        s_ln += f'    "{self._clean_str(line)}"'
                    s_ln += '\n]'
                    s += s_ln
                s += ']'
                lines.append(s)
            result = ',\n'.join(lines)
            self._cache[key] = result
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        return self._cache[key]
    
    def get_is_flags(self) -> bool:
        """
        Gets if const has values that can be Flags Enum.
        This is a calculated result.

        Returns:
            bool: ``True`` if can be flags; Otherwise, ``False``
        """
        key = 'get_is_flags'
        if key in self._cache:
            return self._cache[key]
        self._cache[key] = False
        data = self.get_data()
        nums = []
        try:
            for itm in data:
                nums.append(int(itm.value))
        except:
            return self._cache[key]
        if len(nums) == 0:
            return self._cache[key]
        self._cache[key] = base.Util.is_enum_nums(*nums)
        return self._cache[key]

    def get_is_hex(self) -> bool:
        """
        Gets if the parsed data is in hex format of 0x12AB

        Returns:
            bool: ``True`` if hex is matched; Otherwise, ``False``
        """
        key = 'get_is_hex'
        if key in self._cache:
            return self._cache[key]
        self._cache[key] = False
        data = self.get_data()
        if len(data) == 0:
            return self._cache[key]
        m = pattern_hex.match(data[0].raw_value)
        if m:
            self._cache[key] = True
        return self._cache[key]
        
        
    def _get_data_items(self) -> List[dict]:
        key = '_get_data_items'
        if key in self._cache:
            return self._cache[key]
        result = []
        data = self.get_data()
        p_names: Set[str] = set()
        try:
            for itm in data:
                p_type = base.Util.get_python_type(itm.datatype)
                if not p_type.type in p_names:
                    self._cache['python_types'].append(p_type)
                    p_names.add(p_type.type)
                d_itm = {
                    "name": itm.name,
                    "type": p_type.type,
                    "value": itm.value,
                    "lines": itm.lines
                }
                result.append(d_itm)
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        self._cache[key] = result
        return self._cache[key]

    def _get_const_details(self, memitetms: ResultSet) -> List[dataitem]:
        results = []
        def get_doc_lines(item_tag:Tag) -> list:
            docs = item_tag.find('div', class_='memdoc')
            lines = []
            if docs:
                doc_lines = docs.find_all('p')
                if doc_lines:
                    for ln in doc_lines:
                        lines.append(ln.text)
            return lines

        for itm in memitetms:
            text: str = itm.find("td", class_='memname',
                                 recursive=True).text.replace(' ', ',').replace('=,', '').replace('=', '')
            logger.debug("Parser._get_const_details() Processing: %s", text)
            try:
                parts = text.rsplit(',', maxsplit=3)
                raw_value = parts.pop()
                name = parts.pop() # parts[2]
                _type = parts.pop() # parts[1]
            except Exception as e:
                logger.warning('Failed to process Line: %s', text)
                continue
            value = self._get_number(raw_value)
            lines = get_doc_lines(itm)
            di = dataitem(value=value, raw_value=raw_value, name=name,
                          datatype=_type, lines=lines)
            results.append(di)
        if self.sort:
            results.sort()
        return results

        

    def _get_tbl(self, soup: BeautifulSoup) -> ResultSet:
        return soup.find('table', class_='memberdecls')

    def _get_rows_memitem(self, tbl: ResultSet) -> ResultSet:
        def check_row(tag: Tag) -> bool:
            if tag.has_attr('class'):
                _class = tag['class']
                if isinstance(_class, str):
                    return _class.startswith('memitem')
                else:
                    return _class[0].startswith('memitem')
            return False

        return tbl.find_all(check_row)
    # endregion Data

    # region Properties
    @property
    def python_types(self) -> List[PythonType]:
        """Gets a list of PythonTypes for this instance"""
        if not '_get_data_items' in self._cache:
            # raise Exception("Parser._get_data_items() must be called before python_types can be accessed.")
            self._get_data_items()
        return self._cache['python_types']
    # endregion Properties


class ConstWriter(base.WriteBase):
    # region Constructor
    @TypeCheckKw(arg_info={
        "hex": 0,
        "sort": 0,
        "flags": 1,
        "copy_clipboard": 0,
        "write_template": 0,
        "print_template": 0,
        "print_json": 0,
        "write_json": 0,
        "write_template_long": 0
        },
        types=[bool, (bool, type(None))],
        ftype=DecFuncEnum.METHOD)
    def __init__(self, parser:Parser, **kwargs):
        super().__init__(**kwargs)
        self._parser = parser
        self._hex = kwargs.get('hex', False)
        self._sort = kwargs.get('sort', True)
        self._flags = kwargs.get('flags', None)
        self._copy_clipboard = kwargs.get('copy_clipboard', False)
        self._print_template = kwargs.get('print_template', True)
        self._write_file = kwargs.get('write_template', False)
        self._print_json = kwargs.get('print_json', True)
        self._write_json = kwargs.get('write_json', False)
        self._write_template_long: bool = kwargs.get(
            'write_template_long', False)
        self._indent_amt = 4
        self._file_full_path = None
        self._p_name = None
        self._p_namespace = None
        self._p_fullname = None
        self._p_url = None
        self._p_desc = None
        self._p_requires_typing = False
        self._p_from_imports = set()
        self._p_typing_imports = set()
        self._path_dir = Path(os.path.dirname(__file__))
        t_file = 'const'
        if not self._write_template_long:
            t_file += '_stub'
        t_file += '.tmpl'
        _path = Path(self._path_dir, 'template', t_file)
        if not _path.exists():
            raise FileNotFoundError(f"unable to find templae file '{_path}'")
        self._template_file = _path
        self._template: str = self._get_template()
        self._cache = {}
        self._set_flags()
    # endregion Constructor
    def _set_flags(self):
        # if flags is not specifically set in constructor then get flags from parser
        if self._flags is None:
            self._flags = self._parser.get_is_flags()


    def _get_template(self):
        with open(self._template_file) as f:
            contents = f.read()
        return contents

    def write(self):
        self._set_info()
        self._set_template_data()
        logger.info("Processing %s", self._p_fullname)
        try:
            if self._print_template or self._print_json:
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
        key = '_get_json'
        if key in self._cache:
            return self._cache[key]
        p_dict = {
            "name": 'place holder',
            "namespace": 'place holder',
            "url": 'place holder',
            'flags': self._flags,
            "base_class": self._get_const_base_class(),
            "quote": [],
            "typings": []
        }
        p_dict['quote'] = self._get_quote_flat()
        p_dict['typings'] = self._get_typings()
        p_dict['requires_typing'] = self._p_requires_typing
        p_dict['from_imports'] = self._get_from_imports()
        p_dict['from_imports_typing'] = self._get_from_imports_typing()
        # ConstIntFlagsBase
        p_dict.update(self._parser.get_dict_data())
        
        
        json_dict = {
            "id": JSON_ID,
            "version": __version__,
            "timestamp": str(base.Util.get_timestamp_utc()),
            "name": p_dict['name'],
            "type": "const",
            "namespace": p_dict['namespace'],
            "parser_args": self._parser.get_parser_args(),
            "writer_args": {
                "hex": self._hex,
                "sort": self._sort,
                "flags": self._flags
            },
            "data": p_dict
        }
        str_jsn = base.Util.get_formated_dict_list_str(obj=json_dict, indent=2)
        self._cache[key] = str_jsn
        return self._cache[key]

    def _get_const_base_class(self) -> str:
        if self._flags:
            const_base_cls = base.APP_CONFIG.base_const_int_flags
        else:
            const_base_cls = base.APP_CONFIG.base_const_int
        return const_base_cls

    def _get_from_imports(self) -> List[List[str]]:
        key = '_get_from_imports'
        if key in self._cache:
            return self._cache[key]
        lst = [
            [base.APP_CONFIG.base_const, self._get_const_base_class()]
        ]
        self._cache[key] = lst
        return self._cache[key]

    def _get_from_imports_typing(self) -> List[List[str]]:
        key = '_get_from_imports_typing'
        if key in self._cache:
            return self._cache[key]
        t_set: Set[str] = set()
        p_lst = self._parser.python_types
        for t in p_lst:
            t_set.update(t.get_all_imports())
        self._cache[key] = list(t_set)
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
        
    def _set_template_data(self):
        if self._write_template_long is False:
            return
        self._template = self._template.replace('{hex}', str(self._hex))
        self._template = self._template.replace('{sort}', str(self._sort))
        self._template = self._template.replace('{flags}', str(self._flags))
        self._template = self._template.replace('{name}', self._p_name)
        self._template = self._template.replace('{ns}', self._p_namespace)
        self._template = self._template.replace('{link}', self._p_url)
        self._template = self._template.replace('{base_class}', self._get_const_base_class())
        self._template = self._template.replace(
            '{requires_typing}', str(self._p_requires_typing))
        self._template = self._template.replace(
            '{from_imports}',
            base.Util.get_formated_dict_list_str(self._get_from_imports())
            )
        self._template = self._template.replace(
            '{from_typing_imports}',
            base.Util.get_formated_dict_list_str(self._get_from_imports_typing())
        )
        indent = ' ' * self._indent_amt
        str_json_desc = base.Util.get_formated_dict_list_str(self._p_desc)
        self._template = self._template.replace('{desc}', str_json_desc)
        # indented = textwrap.indent(self._p_desc, indent).lstrip()
        # self._template = self._template.replace('{desc}', indented)
        indented = textwrap.indent(self._p_data, indent)
        # indented = indented.lstrip()
        self._template = self._template.replace('{data}', indented)

    def _set_info(self):
        data = self._parser.get_info()
        self._p_name = data['name']
        self._p_namespace = data['namespace']
        self._p_desc = data['desc']
        self._p_url = data['url']
        self._p_fullname = data['fullname']
        self._p_data = self._parser.get_formated_data()
        if self._write_file or self._write_json:
            self._file_full_path = self._get_uno_obj_path()
        # prime cache and set other params such as self._p_requires_typing
        self._get_quote_flat()
        self._get_typings()

    # region quote/typings
    def _get_quote_flat(self) -> List[str]:
        key = '_get_quote_flat'
        if key in self._cache:
            return self._cache[key]
        t_set: Set[str] = set()
        p_lst = self._parser.python_types
        for t in p_lst:
            if t.requires_typing or t.is_py_type is False:
                t_set.add(t.type)
                self._p_requires_typing = True
        self._cache[key] = list(t_set)
        return self._cache[key]

    def _get_typings(self) -> List[str]:
        key = '_get_typings'
        if key in self._cache:
            return self._cache[key]
        t_set: Set[str] = set()
        p_lst = self._parser.python_types
        for t in p_lst:
            if t.requires_typing:
                t_set.add(t.type)
        self._cache[key] = list(t_set)
        return self._cache[key]

    # endregion quote/typing

    def _get_uno_obj_path(self) -> Path:
        key = '_get_uno_obj_path'
        if key in self._cache:
            return self._cache[key]
        uno_obj_path = Path(self._path_dir.parent, base.APP_CONFIG.uno_base_dir)
        name_parts = self._p_fullname.split('.')
        # ignore com, sun, star
        path_parts = name_parts[3:]
        index = len(path_parts) -1
        if not path_parts[index]:
            try:
                raise Exception(
                    "ConstWriter._get_uno_obj_path() parsing path yielded an empty string")
            except Exception as e:
                logger.error(e, exc_info=True)
                raise e
        path_parts[index] = path_parts[index] + '.tmpl'
        obj_path = uno_obj_path.joinpath(*path_parts)
        self._mkdirp(obj_path.parent)
        self._cache[key] = obj_path
        return self._cache[key]

# region Parse method


def _get_parsed_kwargs(**kwargs) -> Dict[str, str]:
    required = ("url",)
    lookups = {
        "u": "url",
        "url": "url",
        "L": "log_file",
        "log_file": "log_file"
    }
    result = {}
    for k, v in kwargs.items():
        if not isinstance(k, str):
            continue
        if k in lookups:
            key = lookups[k]
            result[key] = v
    for k in required:
        if not k in result:
            # k is missing from kwargs
            raise base.RequiredError(f"Missing required arg {k}.")
    return result


def _get_parsed_args(*args) -> Dict[str, bool]:
    # key, value and value is a key into defaults
    defaults = {
        'no_sort': True,
        "no_cache": True,
        "long_template": False,
        "clipboard": False,
        "print_json": False,
        "print_template": False,
        "write_template": False,
        "write_json": False,
        "verbose": False,
        "flags": False,
        "hex": False
    }
    found = {
        'no_sort': False,
        "no_cache": False,
        "long_template": True,
        "clipboard": True,
        "print_json": True,
        "print_template": True,
        "write_template": True,
        "write_json": True,
        "verbose": True,
        "flags": True,
        "hex": False
    }
    lookups = {
        "s": "no_sort",
        "no_sort": "no_sort",
        "x": "no_cache",
        "no_cache": "no_cache",
        "g": "long_template",
        "long_template": "long_template",
        "c": "clipboard",
        "clipboard": "clipboard",
        "n": "print_json",
        "print_json": "print_json",
        "m": "print_template",
        "print_template": "print_template",
        "t": "write_template",
        "write_template": "write_template",
        "j": "write_json",
        "write_json": "write_json",
        "v": "verbose",
        "verbose": "verbose",
        "f": "flags",
        "flags": "flags",
        "y": "hex",
        "hex": "hex"
    }
    result = {k: v for k, v in defaults.items()}
    for arg in args:
        if not isinstance(arg, str):
            continue
        if arg in lookups:
            key = lookups[arg]
            result[key] = found[key]
    return result


def parse(*args, **kwargs):
    """
    Parses data, alternative to running on command line.

    Other Arguments:
        'no_sort' (str, optional): Short form ``'s'``. No sorting of results. Default ``False``
        'no_cache' (str, optional): Short form ``'x'``. No caching. Default ``False``
        'no_print_clear (str, optional): Short form ``'p'``. No clearing of terminal
            when otuput to terminal. Default ``False``
        'long_template' (str, optional): Short form ``'g'``. Writes a long format template.
            Requires write_template is set. Default ``False``
        'clipboard' (str, optional): Short form ``'c'``. Copy to clipboard. Default ``False``
        'flags' (str, optional): Short form ``'f'``. Treat as flags. Default ``False``
        'hex' (str, optional): Short form ``'y```. Treat as hex. Default ``False``
        'print_json' (str, optional): Short form ``'n'``. Print json to termainl. Default ``False``
        'print_template' (str, optional): Short form ``'m'``. Print template to terminal. Default ``False``
        'write_template' (str, optional): Short form ``'t'``. Write template file into obj_uno subfolder. Default ``False``
        'write_json' (str, optional): Short form ``'j'``. Write json file into obj_uno subfolder. Default ``False``
        'verbose' (str, optional): Short form ``'v'``. Verobose output.

    Keyword Arguments:
        url (str): Short form ``u``. url to parse
        log_file (str, optional): Short form ``L``. Log File
    """
    global logger
    pkwargs = _get_parsed_kwargs(**kwargs)
    pargs = _get_parsed_args(*args)
    if logger is None:
        log_args = {}
        if 'log_file' in pkwargs:
            log_args['log_file'] = pkwargs['log_file']
        else:
            log_args['log_file'] = 'const.log'
        if pargs['verbose']:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    p = Parser(
        url=pkwargs['url'],
        sort=pargs['no_sort'],
        cache=pargs['no_cache']
    )
    w = ConstWriter(
        parser=p,
        copy_clipboard=pargs['clipboard'],
        print_template=pargs['print_template'],
        print_json=pargs['print_json'],
        flags=pargs['flags'],
        hex=pargs['hex'],
        write_template=pargs['write_template'],
        write_json=pargs['write_json'],
        write_template_long=pargs['long_template']
    )
    w.write()
# endregion Parse method

def _api():
    global logger
    if logger is None:
        log_args = {
            "log_file": "const_api.log",
            "level": logging.DEBUG
        }
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))
    url = 'https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1KParseTokens.html'
    api = ApiData(url_soup=url, allow_cache=True)
    data = api.get_data_items()
    for itm in data:
        print(itm)
    
def _main():
    # for debugging
    url = 'https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1KParseTokens.html'
    # sys.argv.extend(['--log-file', 'debug.log', '-v', '-n', '-u', url])
    # main()
    args = ('v', 'n')
    kwargs = {
        "u": url,
        "log_file": "debug.log"
    }
    parse(*args, **kwargs)

def main():
    global logger
    
    parser = argparse.ArgumentParser(description='const')
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
        '-f', '--flags',
        help='Treat as flags',
        action='store_true',
        dest='flags',
        default=None)
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
        '-y', '--hex',
        help='Treat as hex',
        action='store_true',
        dest='hex',
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
        '-g', '--long-template',
        help='Writes a long format template. Requires --write-template is set. No Autoload',
        action='store_true',
        dest='long_format',
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
        help='Log file to use. Defaults to const.log',
        type=str,
        required=False)

    args = parser.parse_args()
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'const.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        _set_loggers(get_logger(logger_name=Path(__file__).stem, **log_args))

    if not args.no_print_clear:
        os.system('cls' if os.name == 'nt' else 'clear')

    logger.info('Executing command: %s', sys.argv[1:])
    logger.info('Parsing Url %s' % args.url)

    p = Parser(
        url=args.url,
        sort=args.sort,
        cache=args.cache
    )
    if not args.print_json and not args.print_template:
        print('')
    w = ConstWriter(
        parser=p,
        copy_clipboard=args.clipboard,
        print_template=args.print_template,
        print_json=args.print_json,
        flags=args.flags,
        hex=args.hex,
        write_template=args.write_template,
        write_json=args.write_json,
        write_template_long=args.long_format
        )
    w.write()
 
if __name__ == '__main__':
    _api()
