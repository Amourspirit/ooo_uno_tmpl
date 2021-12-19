import os
import sys
import argparse
import glob
import logging
import json
from pathlib import Path
from typing import Any, Awaitable, Dict, List, Tuple
import asyncio
APP_ROOT:str = os.environ.get('project_root', str(Path(__file__).parent.parent.parent))
if not APP_ROOT in sys.path:
    sys.path.insert(0, APP_ROOT)
from parser import base


async def run_sequence(*functions: Awaitable[Any]) -> None:
    for function in functions:
        await function


async def run_parallel(*functions: Awaitable[Any]) -> None:
    await asyncio.gather(*functions)
    
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


class _FileWorker:
    def __init__(self, file: str) -> None:
        self._file = file
        self._data = {}
        self._ns: str = None
        self._build_data()

    def _load_file(self, file):
        with open(file, 'r') as f:
            data = json.load(f)
        return data
    # region Process

    def _process(self, d_in: dict):
        if not self._ns in self._data:
            self._data[self._ns] = []
        self._data[self._ns].append(d_in['name'])

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

    def _process_enums(self,j_data: dict):
        values = self._get_enums(j_data)
        for d in values:
            self._process(d_in=d)
    # endregion Process Enums
    # region process Typedef

    def _get_typedef(self, j_data: dict) -> List[dict]:
        try:
            return j_data['typedef']
        except Exception:
            return []

    def _process_typedef(self, j_data: dict):
        values = self._get_typedef(j_data)
        for d in values:
            self._process(d_in=d)
    # endregion process Typedef
    # region Process Service

    def _process_service(self, j_data: dict):
        values = self._get_class_section(j_data, 'service')
        for d in values:
            self._process(d_in=d)
    # endregion Process Service
    # region Process Struct

    def _process_struct(self, j_data: dict):
        values = self._get_class_section(j_data, 'struct')
        for d in values:
            self._process(d_in=d)
    # endregion Process Struct
    # region Process Exception

    def _process_exception(self, j_data: dict):
        values = self._get_class_section(j_data, 'exception')
        for d in values:
            self._process(d_in=d)
    # endregion Process Exception
    # region Process Interface

    def _process_interface(self, j_data: dict):
        values = self._get_class_section(j_data, 'interface')
        for d in values:
            self._process(d_in=d)
    # endregion Process Interface
    # endregion Process

    def _build_data(self):
        j_data_raw = self._load_file(self._file)
        self._ns = j_data_raw['namespace']
        j_data = j_data_raw['data']
        self._process_enums(j_data=j_data)
        self._process_typedef(j_data=j_data, )
        self._process_service(j_data=j_data)
        self._process_struct(j_data=j_data)
        self._process_exception(j_data=j_data)
        self._process_interface(j_data=j_data)

    @property
    def ns_data(self) -> Dict[str, str]:
        """Gets ns_data value"""
        return self._data

    @property
    def namespace(self) -> str:
        """Gets namespace value"""
        return self._ns

def process_file(file:str) -> Tuple[str, str]:
    fw = _FileWorker(file=file)
    return fw.namespace, fw.ns_data

def main() -> None:
    files = list(get_module_link_files())
    files.sort()
    ns, data = process_file(files[0])
    print(data)
    print(ns)


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
