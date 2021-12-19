import os
import sys
import argparse
import glob
import logging
import json
from pathlib import Path
from typing import List
APP_ROOT:str = os.environ.get('project_root', str(Path(__file__).parent.parent.parent))
if not APP_ROOT in sys.path:
    sys.path.insert(0, APP_ROOT)
from parser import base

def get_module_link_files(exclude_root: bool = False) -> List[str]:
    dirname = str(Path(APP_ROOT, base.APP_CONFIG.uno_base_dir))
    # https://stackoverflow.com/questions/20638040/glob-exclude-pattern
    # exclude files that start with _
    pattern = dirname + f'/**/{base.APP_CONFIG.module_links_file}'
    files = set(glob.glob(pattern, recursive=True))
    if exclude_root is False:
        # print(files)
        return files
    root_json = Path(dirname, base.APP_CONFIG.module_links_file)
    ex_files = set()
    ex_files.add(str(root_json))
    # deduct sets:
    return files - ex_files


class NamespaceBuild:
    def __init__(self) -> None:
        self._link_files = list(get_module_link_files())
        self._link_files.sort()
        self._data = []
        self._build_data()

    def _load_file(self, file):
        with open(file, 'r') as f:
            data = json.load(f)
        return data
    # region Process

    def _process(self, ns: str, d_in: dict, d_out: dict):
        if not ns in d_out:
            d_out[ns] = []
        d_out[ns].append(d_in['name'])

    def _get_class_section(self, j_data: dict, key: str) -> List[dict]:
        result = []
        try:
            values: List[dict] = j_data['classes'][key]
            result = [d for d in values]
        except Exception:
            pass
        return result

    # region Process Enums
    def _get_enums(self, j_data: dict) -> List[dict]:
        try:
            return j_data['enums']
        except Exception:
            return []

    def _process_enums(self, ns: str, j_data: dict, d_out: dict):
        values = self._get_enums(j_data)
        for d in values:
            self._process(ns=ns, d_in=d, d_out=d_out)
    # endregion Process Enums
    # region process Typedef

    def _get_typedef(self, j_data: dict) -> List[dict]:
        try:
            return j_data['typedef']
        except Exception:
            return []

    def _process_typedef(self, ns: str, j_data: dict, d_out: dict):
        values = self._get_typedef(j_data)
        for d in values:
            self._process(ns=ns, d_in=d, d_out=d_out)
    # endregion process Typedef
    # region Process Service

    def _process_service(self, ns: str, j_data: dict, d_out: dict):
        values = self._get_class_section(j_data, 'service')
        for d in values:
            self._process(ns=ns, d_in=d, d_out=d_out)
    # endregion Process Service
    # region Process Struct

    def _process_struct(self, ns: str, j_data: dict, d_out: dict):
        values = self._get_class_section(j_data, 'struct')
        for d in values:
            self._process(ns=ns, d_in=d, d_out=d_out)
    # endregion Process Struct
    # region Process Exception

    def _process_exception(self, ns: str, j_data: dict, d_out: dict):
        values = self._get_class_section(j_data, 'exception')
        for d in values:
            self._process(ns=ns, d_in=d, d_out=d_out)
    # endregion Process Exception
    # region Process Interface

    def _process_interface(self, ns: str, j_data: dict, d_out: dict):
        values = self._get_class_section(j_data, 'interface')
        for d in values:
            self._process(ns=ns, d_in=d, d_out=d_out)
    # endregion Process Interface
    # endregion Process

    def _build_data(self):
        d_ns = {}
        j_data_raw = self._load_file(self._link_files[0])
        j_ns = j_data_raw['namespace']
        j_data = j_data_raw['data']
        self._process_enums(ns=j_ns, j_data=j_data, d_out=d_ns)
        self._process_typedef(ns=j_ns, j_data=j_data, d_out=d_ns)
        self._process_service(ns=j_ns, j_data=j_data, d_out=d_ns)
        self._process_struct(ns=j_ns, j_data=j_data, d_out=d_ns)
        self._process_exception(ns=j_ns, j_data=j_data, d_out=d_ns)
        self._process_interface(ns=j_ns, j_data=j_data, d_out=d_ns)
        print(d_ns)


def main() -> None:
    ns = NamespaceBuild()


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
