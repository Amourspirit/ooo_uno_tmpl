# coding: utf-8
"""
Reads Module Links Json data.
Writes module_detail and module_info tables in databaase.
"""
import verr
import json
import glob
import re
from pathlib import Path
from typing import List, Dict, Set
from collections import namedtuple
from ...cfg.config import AppConfig
from ..data_class.module_detail import ModuleDetail
from ..data_class.module_info import ModuleInfo
from ..db_class.db_connect import DbConnect
from ..db_class.tbl_module_detail import TblModuleDetail
from ..db_class.tbl_module_info import TblModuleInfo
from ...parser import JSON_ID
from ...model.links.model_module_links import ModelModuleLinks


class ParseModuleLinks:

    def __init__(self, config: AppConfig) -> None:
        self._app_config = config
        self._module_details: List[ModuleDetail] = []
        self._module_infos: List[ModuleInfo] = []
        self._min_ver = verr.Version.parse(config.min_module_links_ver)
        conn = DbConnect(self._app_config)
        self._db_cnn = conn.connection_str
        self._root_dir = conn.root_dir
        self._module_detail_tbl = TblModuleDetail(connect_str=self._db_cnn)
        self._module_info_tbl = TblModuleInfo(connect_str=self._db_cnn)

    def get_module_link_files(self) -> Set[str]:
        dirname = str(self._root_dir / self._app_config.data_dir)
        # https://stackoverflow.com/questions/20638040/glob-exclude-pattern
        # root module_links.json needs to be remove from listing.
        # it will not need any processing here.
        # using sets and deduct seem the simplist way.
        pattern = dirname + f'/**/{self._app_config.module_links_file}'
        root_json = Path(dirname, self._app_config.module_links_file)
        files = set(glob.glob(pattern, recursive=True))
        ex_files = set()
        ex_files.add(str(root_json))
        # deduct sets:
        return files - ex_files

    def get_count_details(self) -> int:
        return self._module_detail_tbl.get_row_count()

    def _write_all(self) -> None:
        self._module_details.clear()
        self._module_infos.clear()
        m_files = self.get_module_link_files()
        for j_file in m_files:
            with open(j_file, 'r') as file:
                j_data = json.load(file)
                links = ModelModuleLinks(**j_data)
            self._validite_json(file=file, links=links)
            self._read(links=links, file=j_file)

        sorted_lst = self._get_detail_lst()

        self._module_detail_tbl.insert(data=sorted_lst)
        self._module_info_tbl.insert(data=self._module_infos)

    def write_all_details(self) -> None:
        self._write_all()

    def update_all_details(self) -> None:
        self._write_all()

    def _get_detail_lst(self) -> List[ModuleDetail]:
        self._module_details
        re_end = re.compile(r".*?([0-9]+)$")
        m_detail = namedtuple('m_detail', [
            'id_namespace',
            'name',
            'namespace',
            'href',
            'component_type',
            'sort',
            'name_part',
            'ver_part'
        ])
        sort_dic = {
            "exception": 1,
            "singleton": 2,
            "service": 3,
            "interface": 4,
            "enum": 20,
            "const": 21,
            "typedef": 22,
            "struct": 23
        }

        # break down name to move version number into seperate field for sorting purposes.
        # this reorders sorting.
        #   Berfore sorting:
        # id_namespace                          name                namespace       href                                                            component_type  sort
        # com.sun.star.io.XTextOutputStream     XTextOutputStream   com.sun.star.io interfacecom_1_1sun_1_1star_1_1io_1_1XTextOutputStream.html     interface       4811
        # com.sun.star.io.XTextOutputStream2    XTextOutputStream2  com.sun.star.io interfacecom_1_1sun_1_1star_1_1io_1_1XTextOutputStream2.html    interface       4813
        #   After Sort
        # id_namespace                          name                namespace       href                                                            component_type  sort
        # com.sun.star.io.XTextOutputStream2    XTextOutputStream2  com.sun.star.io interfacecom_1_1sun_1_1star_1_1io_1_1XTextOutputStream2.html    interface       4811
        # com.sun.star.io.XTextOutputStream     XTextOutputStream   com.sun.star.io interfacecom_1_1sun_1_1star_1_1io_1_1XTextOutputStream.html     interface       4813
        #
        # this sorting results in fewer python mro issues.
        m_details: List[m_detail] = []
        for el in self._module_details:
            m = re_end.match(el.name)
            name_part = el.name
            if m:
                ver_str = m.group(1)
                name_part = name_part[:-len(ver_str)]
                ver_part = -int(ver_str)
            else:
                ver_part = 0
            m_details.append(m_detail(
                id_namespace=el.id_namespace,
                name=el.name,
                namespace=el.namespace,
                href=el.href,
                component_type=el.component_type,
                sort=sort_dic.get(el.component_type, 99),
                name_part=name_part,
                ver_part=ver_part
            ))

        _sorted: List[m_detail] = sorted(m_details,
                                         key=lambda im: (im.sort, im.namespace, im.name_part, im.ver_part))

        lst = []
        i = 1
        for el in _sorted:
            lst.append(ModuleDetail(
                id_namespace=el.id_namespace,
                name=el.name,
                namespace=el.namespace,
                href=el.href,
                component_type=el.component_type,
                sort=i
            ))
            i += 2
        return lst

    # region Read Json into Imports
    def _read(self, links: ModelModuleLinks, file: str) -> None:
        rel = Path(file).relative_to(self._root_dir)
        ns: str = links.namespace
        self._read_classes_ex(ns, links)
        self._read_classes_interface(ns, links)
        self._read_classes_service(ns, links)
        self._read_classes_singleton(ns, links)
        self._read_classes_struct(ns, links)
        self._read_const(ns, links)
        self._read_enums(ns, links)
        self._read_typedef(ns, links)
        self._module_infos.append(ModuleInfo(
            id_module_info=ns,
            url_base=links.url_base,
            file=str(rel)
        ))

    def _read_enums(self, ns: str, links: ModelModuleLinks) -> None:
        for itm in links.data.enums:
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{itm.name}",
                name=itm.name,
                namespace=ns,
                href=itm.href,
                component_type='enum'
            ))

    def _read_const(self, ns: str, links: ModelModuleLinks) -> None:
        for itm in links.data.constants:
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{itm.name}",
                name=itm.name,
                namespace=ns,
                href=itm.href,
                component_type='const'
            ))

    def _read_typedef(self, ns: str, links: ModelModuleLinks) -> None:
        for itm in links.data.typedef:
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{itm.name}",
                name=itm.name,
                namespace=ns,
                href=itm.href,
                component_type='typedef'
            ))

    def _read_classes_service(self, ns: str, links: ModelModuleLinks) -> None:
        if links.data.classes.service is None:
            return None
        for itm in links.data.classes.service:
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{itm.name}",
                name=itm.name,
                namespace=ns,
                href=itm.href,
                component_type='service'
            ))

    def _read_classes_struct(self, ns: str, links: ModelModuleLinks) -> None:
        if links.data.classes.struct is None:
            return None
        for itm in links.data.classes.struct:
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{itm.name}",
                name=itm.name,
                namespace=ns,
                href=itm.href,
                component_type='struct'
            ))

    def _read_classes_ex(self, ns: str, links: ModelModuleLinks) -> None:
        if links.data.classes.exception is None:
            return None
        for itm in links.data.classes.exception:
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{itm.name}",
                name=itm.name,
                namespace=ns,
                href=itm.href,
                component_type='exception'
            ))

    def _read_classes_interface(self, ns: str, links: ModelModuleLinks) -> None:
        if links.data.classes.interface is None:
            return None
        for itm in links.data.classes.interface:
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{itm.name}",
                name=itm.name,
                namespace=ns,
                href=itm.href,
                component_type='interface'
            ))

    def _read_classes_singleton(self, ns: str, links: ModelModuleLinks) -> None:
        if links.data.classes.singleton is None:
            return None
        for itm in links.data.classes.singleton:
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{itm.name}",
                name=itm.name,
                namespace=ns,
                href=itm.href,
                component_type='singleton'
            ))

    # endregion Read Json into Imports

    # region Validation
    def _validite_json(self, file: str, links: ModelModuleLinks):
        if links.ver < self._min_ver:
            _msg = f"{self.__class__.__name__}._validite_json()  Version fail Expect a min version of '{self._min_ver}', got '{links.ver}'. File: {file}"
            raise Exception(_msg)

    # endregion Validation
