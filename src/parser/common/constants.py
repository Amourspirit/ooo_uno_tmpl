# coding: utf-8
from ...utilities import util

URL_SPLIT = '_1_1'
"""Default stirng for splitting url string into it parts"""
APP_ROOT: str = util.get_root()
util.set_os_root_path()

# region Type Map
# TYPE_MAP and TYPE_MAP_EX are only used with deprecated method get_py_type


TYPE_MAP = {
    "any": "object",
    "short": "int",
    "long": "int",
    "float": "float",
    "double": "float",
    "string": "str",
    "char": "str",
    "boolean": "bool",
    "sequence": "list",
    "aDXArray": "list",
    "void": "None",
    'type': 'object',
    'T': 'object',
    'U': 'object'
}
TYPE_MAP_EX = {
    "com.sun.star.beans.Pair": {
        "replace": "typing.Tuple[{0}, {1}]",
        "regex": r".*<[ ]*([a-zA-Z]+),[ ]*([a-zA-Z]+)",
        "is_typing": True,
        "is_wrapper": False,
        "is_py_type": True
    }
}
# endregion Type Map
