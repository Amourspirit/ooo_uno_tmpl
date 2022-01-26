# coding: utf-8
import verr
import json
import glob
import re
from pathlib import Path
from typing import List, Dict, Set
from config import AppConfig
from ..data_class.module_detail import ModuleDetail
from ..data_class.module_info import ModuleInfo
from ..db_class.db_connect import DbConnect
from ..db_class.tbl_module_detail import TblModuleDetail
from ..db_class.tbl_module_info import TblModuleInfo
from parser import JSON_ID
from collections import namedtuple
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
            self._validite_json(file=file, data=j_data)
            self._read(json_data=j_data, file=j_file)

        sorted_lst = self._get_detail_lst()

        self._module_detail_tbl.insert(data=sorted_lst)
        self._module_info_tbl.insert(data=self._module_infos)

    def write_all_details(self) -> None:
        # if self._module_detail_tbl.has_data():
        #     msg = f"{self.__class__.__name__}.write_all_details() Can not write because there is already data in the database for {self._module_detail_tbl.get_table_name()}"
        #     raise Exception(msg)
        # if self._module_info_tbl.has_data():
        #     msg = f"{self.__class__.__name__}.write_all_details() Can not write because there is already data in the database for {self._module_detail_tbl.get_table_name()}"
        #     raise Exception(msg)
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
    def _read(self, json_data: dict, file: str) -> None:
        rel = Path(file).relative_to(self._root_dir)
        ns: str = json_data['namespace']
        self._read_classes_ex(ns, json_data)
        self._read_classes_interface(ns, json_data)
        self._read_classes_service(ns, json_data)
        self._read_classes_singleton(ns, json_data)
        self._read_classes_struct(ns, json_data)
        self._read_const(ns, json_data)
        self._read_enums(ns, json_data)
        self._read_typedef(ns, json_data)
        self._module_infos.append(ModuleInfo(
            id_module_info=ns,
            url_base=json_data['url_base'],
            file=str(rel)
        ))

    def _read_enums(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data'].get('enums', [])
        for itm in lst:
            name: str = itm['name']
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{name}",
                name=name,
                namespace=ns,
                href=itm['href'],
                component_type='enum'
            ))

    def _read_const(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data'].get('constants', [])
        for itm in lst:
            name: str = itm['name']
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{name}",
                name=name,
                namespace=ns,
                href=itm['href'],
                component_type='const'
            ))

    def _read_typedef(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data'].get('typedef', [])
        for itm in lst:
            name: str = itm['name']
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{name}",
                name=name,
                namespace=ns,
                href=itm['href'],
                component_type='typedef'
            ))

    def _read_classes_service(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data']['classes'].get(
            'service', [])
        for itm in lst:
            name: str = itm['name']
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{name}",
                name=name,
                namespace=ns,
                href=itm['href'],
                component_type='service'
            ))

    def _read_classes_struct(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data']['classes'].get(
            'struct', [])
        for itm in lst:
            name: str = itm['name']
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{name}",
                name=name,
                namespace=ns,
                href=itm['href'],
                component_type='struct'
            ))

    def _read_classes_ex(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data']['classes'].get(
            'exception', [])
        for itm in lst:
            name: str = itm['name']
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{name}",
                name=name,
                namespace=ns,
                href=itm['href'],
                component_type='exception'
            ))

    def _read_classes_interface(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data']['classes'].get(
            'interface', [])
        for itm in lst:
            name: str = itm['name']
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{name}",
                name=name,
                namespace=ns,
                href=itm['href'],
                component_type='interface'
            ))

    def _read_classes_singleton(self, ns: str, json_data: dict) -> None:
        lst: List[Dict[str, str]] = json_data['data']['classes'].get(
            'singleton', [])
        for itm in lst:
            name: str = itm['name']
            self._module_details.append(ModuleDetail(
                id_namespace=f"{ns}.{name}",
                name=name,
                namespace=ns,
                href=itm['href'],
                component_type='singleton'
            ))

    # endregion Read Json into Imports

    # region Validation
    def _validite_json(self, file: str, data: dict):
        msg = f"{self.__class__.__name__}._validite_json() "

        key = 'id'
        if not key in data:
            _msg = f"{msg} Json missing id field. File: {file}"
            raise Exception(_msg)
        if data[key] != JSON_ID:
            _msg = f"{msg} Json data bad id field. Expected: {JSON_ID}, Got: {data[key]}. File: {file}"
            raise Exception(_msg)
        key = 'type'
        if not key in data:
            _msg = f"{msg} Json missing type field. File: {file}"
            raise Exception(_msg)
        if data[key] != 'module_links':
            _msg = f"{msg} Json data bad id field. Expected: module_links, Got: {data[key]}. File: {file}"
            raise Exception(_msg)
        key = 'url_base'
        if not key in data:
            _msg = f"{msg} Json missing url_base field. File: {file}"
            raise Exception(_msg)
        key = 'version'
        if not key in data:
            _msg = f"{msg} Json missing version field. File: {file}"
            raise Exception(_msg)
        json_ver = verr.Version.parse(data[key])
        if json_ver < self._min_ver:
            _msg = f"{msg} Version fail Expect a min version of '{self._min_ver}', got '{json_ver}'. File: {file}"
            raise Exception(_msg)
        key = 'data'
        if not key in data:
            _msg = f"{msg} Json missing data field. File: {file}"
            raise Exception(_msg)
        if not isinstance(data[key], dict):
            _msg = f"{msg} Json data field is not a dictionary. File: {file}"
            raise Exception(_msg)
    # endregion Validation
