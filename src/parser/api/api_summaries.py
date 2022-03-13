# coding: utf-8
import logging
from typing import Union, Optional, Set, List
from bs4.element import Tag
from ..web.block_obj import BlockObj
from .api_summary_rows import ApiSummaryRows
from ..dataclass.name_info import NameInfo
from ..dataclass.summary_info import SummaryInfo
from ..common.util import Util
from ..rules.summary.i_rules_summary_info import IRulesSummaryInfo
from ..common.log_load import Log
log = Log()


class ApiSummaries(BlockObj):
    """Gets summary information for a public member block"""

    def __init__(self, block: ApiSummaryRows, name_info: NameInfo, ns: str, rule_engine: Optional[IRulesSummaryInfo] = None, long_names: bool = False
                 ) -> None:
        """
        [summary]

        Args:
            block (ApiSummaryRows): Block of html that contains summary rows.
            rule_engine (IRulesSummaryInfo, optional): Rules engine to process each found Summary Info. Defaults to None.
        """
        self._block: ApiSummaryRows = block
        super().__init__(self._block.soup)
        self._requires_typing = False
        self._imports: Set[str] = set()
        self._rule_engine = rule_engine
        self._ns = ns
        self._long_names = long_names
        self._name_info = name_info
        self._data = None

    def _get_type_from_inner_link(self, mem_item_left: Tag, name: str) -> Union[str, None]:
        log.logger.debug(
            'ApiSummaries._get_type_from_inner_link() Searching for %s link.', name)
        if not mem_item_left:
            return None
        a_tag = mem_item_left.findChild('a')
        if not a_tag:
            return None
        a_name = a_tag.text.strip()
        if a_name != name:
            return None
        s = Util.get_ns_from_a_tag(a_tag=a_tag)
        log.logger.debug(
            'ApiSummaries._get_type_from_inner_link() found: %s', s)
        return s

    def get_obj(self) -> List[SummaryInfo]:
        """
        Get list of Summary Info from html page.

        Returns:
            List[SummaryInfo]: summary info.

        Note:
            If a rules engine is present then each summary info will have any relevant rules applied.
        """
        if not self._data is None:
            return self._data
        self._data = []
        rows = self._block.get_obj()
        for row in rows:
            cls_name = row.get('class')[0]
            id_str = cls_name.rsplit(sep=':', maxsplit=1)[1]
            itm_lft = row.find('td', class_='memItemLeft')
            r_type = ''
            name = ''
            if itm_lft:
                r_type = itm_lft.text.strip().replace('::', '.').lstrip('.')
            itm_rgt = row.find('td', class_='memItemRight')
            if itm_rgt:
                itm_name = itm_rgt.select_one('a')
                if itm_name:
                    name = itm_name.text.strip()
                    name = Util.get_clean_method_name(name)
            # log.logger.debug('ApiSummaries.get_obj() r_type in: %s', r_type)
            p_type = Util.get_python_type(
                in_type=r_type,
                name_info=self._name_info,
                ns=self._ns,
                long_names=self._long_names
            )
            # log.logger.debug('ApiSummaries.get_obj() p_type in: %s', p_type.type)
            if p_type.is_default():
                log.logger.debug(
                    'ApiSummaries.get_obj() %s: p_type is Default. Looking for %s', name, r_type)
                # defaulted to object.
                # this could be an object in the same namespace.
                # test for link and namespace and try again.
                r2_type = self._get_type_from_inner_link(itm_lft, r_type)
                if r2_type:
                    p2_type = Util.get_python_type(
                        in_type=r2_type,
                        name_info=self._name_info,
                        ns=self._ns,
                        long_names=self._long_names
                    )
                    if not p2_type.is_default():
                        p_type = p2_type
                        log.logger.debug(
                            'ApiSummaries.get_obj() %s: p_type is now %s', name, r_type)
            else:
                log.logger.debug(
                    'ApiSummaries.get_obj() %s: p_type is %s for %s', name, p_type.type, r_type)
            si = SummaryInfo(id=id_str, name=name,
                             type=p_type.type, p_type=p_type)
            if p_type.requires_typing:
                self._requires_typing = True
            im = p_type.get_all_imports()
            self._imports.update(im)
            self._data.append(si)

        if self._rule_engine:
            for si in self._rule_engine:
                self._rule_engine.process_summary_info(si)
        return self._data

    @property
    def requires_typing(self) -> bool:
        """Gets requires_typing value"""
        return self._requires_typing

    @property
    def imports(self) -> Set[str]:
        """Gets imports value"""
        return self._imports
