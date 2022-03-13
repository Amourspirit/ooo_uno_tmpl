# coding: utf-8
import json
from pathlib import Path
from typing import Union, List, Dict
from ..dataclass.ns import Ns
from ...utilities import util as utils
from ..common.util import Util

# region CONST

_KNOWN_EXTENDS: Dict[str, List[str]] = None
_KNOWN_JSON: Dict[str, List[str]] = None
# endregion CONST




# region Known Extends


def get_known_extends(ns: str, class_name: str) -> Union[List[Ns], None]:
    global _KNOWN_EXTENDS
    key = ns + '.' + class_name
    if _KNOWN_EXTENDS is None:
        json_file = Path(utils.get_root())/ 'src' / 'parser' / 'config' / 'known_extends.json'
        with open(json_file, 'r') as file:
            _KNOWN_EXTENDS = json.load(file)
    if not key in _KNOWN_EXTENDS:
        return None
    results = []
    known = _KNOWN_EXTENDS[key]
    for s in known:
        parts = s.rsplit(sep='.', maxsplit=1)
        if parts[1] == '_':
            # python import such as Exception
            results.append(Ns(name=parts[0], namespace='', python_import=True))
        else:
            results.append(Ns(name=parts[1], namespace=parts[0]))
    return results

# endregion Known Extends

# region Known Extends


def get_known_json(full_ns: str) -> Union[str, None]:
    global _KNOWN_JSON
    key = full_ns
    if _KNOWN_JSON is None:
        json_file = Path(utils.get_root())/ 'src' / 'parser' / 'config' / 'known_json.json'
        with open(json_file, 'r') as file:
            _KNOWN_JSON = json.load(file)
    if not key in _KNOWN_JSON:
        return None
    file = _KNOWN_JSON[full_ns]
    json_file = Path(utils.get_root())/ 'src' / 'parser' / 'known_json' / file
    with open(json_file, 'r') as file:
        j_data = json.load(file)
    return Util.get_formated_dict_list_str(j_data, indent=2)

# endregion Known Extends
