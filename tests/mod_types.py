# coding: utf-8
from typing import Set
import os
import glob
import re
import json
from pathlib import Path
from rel import mod_rel as RelInfo

def get_module_types(build_dir = None) -> dict:
    if build_dir is None:
        build_dir = ['ooobuild', 'lo']
    uno_obj_dir_name = 'lo'
    s_uno_obj = str(Path(*build_dir)).replace(os.sep, '.')
    module_links_file = 'module_links.json'
    app_root = Path(__file__).parent.parent
    src_uno_obj = app_root / uno_obj_dir_name
    pattern_generic_name = re.compile(r"([a-zA-Z0-9_]+)(<[A-Z, ]+>)")

    def get_clean_classname(input: str) -> str:
        """
        Clean a class name and changes name suah as ``Pair< T, U >`` to ``Pair``

        Args:
            input (str): name

        Returns:
            str: cleaned name
        """
        # convert 'Pair< T, U >' to 'Pair'
        s = pattern_generic_name.sub(r'\g<1>', input)
        s = s.replace(" ", "_")
        return s

    def get_module_link_files() -> Set[str]:
        dirname = src_uno_obj
        # https://stackoverflow.com/questions/20638040/glob-exclude-pattern
        # root module_links.json needs to be remove from listing.
        # it will not need any processing here.
        # using sets and deduct seem the simplist way.
        pattern = str(dirname) + f'/**/{module_links_file}'
        root_json = Path(dirname, module_links_file)
        files = set(glob.glob(pattern, recursive=True))
        ex_files = set()
        ex_files.add(str(root_json))
        # deduct sets:
        return files - ex_files

    def camel_to_snake(name: str) -> str:
        return RelInfo.camel_to_snake(name)

    def get_module_link_details(lnk_path: str, name: str, href: str, ns: str) -> dict:
        m_dir = str(Path(lnk_path).parent)
        s = ns.removeprefix('com.sun.star')
        s = s_uno_obj + s
        c_name = get_clean_classname(name)
        return {
            "dir": m_dir,
            "name": c_name,
            "href": href,
            "ns": s,
            "c_name": camel_to_snake(c_name)
        }

    result: dict = {
        "enum": [],
        "const": [],
        "typedef": [],
        "service": [],
        "struct": [],
        "exception": [],
        "interface": [],
        "singleton": []
    }

    def load_enum(lnk_path: str, j_data: dict):
        ns: str = j_data['namespace']
        lst = j_data['data'].get('enums', [])
        for el in lst:

            result['enum'].append(get_module_link_details(
                lnk_path=lnk_path,
                name=el['name'],
                href=el['href'],
                ns=ns
            ))

    def load_const(lnk_path: str, j_data: dict):
        ns = j_data['namespace']
        lst = j_data['data'].get('constants', [])
        for el in lst:

            result['const'].append(get_module_link_details(
                lnk_path=lnk_path,
                name=el['name'],
                href=el['href'],
                ns=ns
            ))

    def load_typedef(lnk_path: str, j_data: dict):
        ns = j_data['namespace']
        lst = j_data['data'].get('typedef', [])
        for el in lst:

            result['typedef'].append(get_module_link_details(
                lnk_path=lnk_path,
                name=el['name'],
                href=el['href'],
                ns=ns
            ))

    def load_service(lnk_path: str, j_data: dict):
        ns = j_data['namespace']
        lst = j_data['data']['classes'].get('service', [])
        for el in lst:

            result['service'].append(get_module_link_details(
                lnk_path=lnk_path,
                name=el['name'],
                href=el['href'],
                ns=ns
            ))

    def load_struct(lnk_path: str, j_data: dict):
        ns = j_data['namespace']
        lst = j_data['data']['classes'].get('struct', [])
        for el in lst:

            result['struct'].append(get_module_link_details(
                lnk_path=lnk_path,
                name=el['name'],
                href=el['href'],
                ns=ns
            ))

    def load_exception(lnk_path: str, j_data: dict):
        ns = j_data['namespace']
        lst = j_data['data']['classes'].get('exception', [])
        for el in lst:

            result['exception'].append(get_module_link_details(
                lnk_path=lnk_path,
                name=el['name'],
                href=el['href'],
                ns=ns
            ))

    def load_interface(lnk_path: str, j_data: dict):
        ns = j_data['namespace']
        lst = j_data['data']['classes'].get('interface', [])
        for el in lst:

            result['interface'].append(get_module_link_details(
                lnk_path=lnk_path,
                name=el['name'],
                href=el['href'],
                ns=ns
            ))

    def load_singleton(lnk_path: str, j_data: dict):
        ns = j_data['namespace']
        lst = j_data['data']['classes'].get('singleton', [])
        for el in lst:

            result['singleton'].append(get_module_link_details(
                lnk_path=lnk_path,
                name=el['name'],
                href=el['href'],
                ns=ns
            ))

    for j_file in get_module_link_files():
        with open(j_file, 'r') as file:
            j_data = json.load(file)
            load_enum(j_file, j_data)
            load_const(j_file, j_data)
            load_typedef(j_file, j_data)
            load_service(j_file, j_data)
            load_struct(j_file, j_data)
            load_exception(j_file, j_data)
            load_interface(j_file, j_data)
            load_singleton(j_file, j_data)

    return result
