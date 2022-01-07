# coding: utf-8
import enum
import os
import sys
import re
import importlib
import logging
import time
import calendar
from datetime import datetime, timezone
from types import ModuleType
from typing import Dict, Iterable, Tuple, List, Union
from Cheetah.Template import Template

# set up path for importing modules from main app
_project_root = os.environ.get('project_root', None)
if _project_root:
    if not _project_root in sys.path:
        sys.path.insert(0, _project_root)

py_name_pattern = re.compile('[\W_]+')

RESERVER_WORDS = {
    'and', 'as', 'assert', 'break', 'class',
    'continue', 'def', 'del', 'elif', 'else',
    'except', 'False', 'finally', 'for',
    'from', 'global', 'if', 'import', 'in',
    'is', 'lambda', 'None', 'nonlocal',
    'not', 'or', 'pass', 'raise', 'return',
    'True', 'try', 'while', 'with', 'yield'
    }
class BaseTpml(Template):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._is_class_init = True
        self._is_class_data = False
        self._logger = None
        get_logger = None
        if not hasattr(self, "extends_map"):
            setattr(self, 'extends_map', {})
        self._logger: logging.Logger = None
        try:
            _, get_logger = self.dynamic_imp(
                'logger', 'log_handle', 'get_logger')
        except Exception as e:
            # print("# Error importing logger:", e)
            pass

        if get_logger:
            self._logger: logging.Logger = get_logger(
                logger_name="Template — " + self.__class__.__name__,
                add_handler_console=False
                )

    def init_data(self):
        self._is_class_init = True

    def load_data(self):
        self._is_class_data = True

    # region Logger
    def _log_to_logger(self, level: int, msg: object, *args, **kwargs):
        if not self._logger:
            return
        self._logger.log(level, msg, *args, **kwargs)

    def _ldebug(self, msg: object, *args, **kwargs):
        self._log_to_logger(logging.debug, msg, *args, **kwargs)

    def _linfo(self, msg: object, *args, **kwargs):
        self._log_to_logger(logging.INFO, msg, *args, **kwargs)
    
    def _lwarn(self, msg: object, *args, **kwargs):
        self._log_to_logger(logging.WARN, msg, *args, **kwargs)

    def _lerr(self, msg: object, *args, **kwargs):
        self._log_to_logger(logging.ERROR, msg, *args, **kwargs)
    # endregion Logger

    def camel_to_snake(self, input: str) -> str:
        """
        Converts Camel case to snake clase

        Args:
            name (str): Camel name

        Returns:
            str: snake case
        """
        _input = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', _input).lower()
    
    def get_clean_name(self, input: str) -> str:
        """
        Removes all char from a string except for ``a-zA-Z0-9_``

        Args:
            input (str): string to clean    

        Returns:
            str: input with any other chars removed
        """
        # https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
        return py_name_pattern.sub('', input)
    
    def line_gen(self, input) -> str:
        """
        Generates lines from str or list like

        Args:
            input (str, list, tuple, set): input str or iterable str

        Yields:
            [str]: line by line
        """
        if isinstance(input, str):
            yield input
            return
        for s in input:
            yield s

    def dict_keys_to_str(self, input: dict, sep: str = ', ') -> str:
        """
        Converts a dictionary's keys into a string seperated by ``sep``

        Args:
            input (dict): input dictionary
            sep (str, optional): seperator. Defaults to ``', '``

        Returns:
            str: keys a string.
        """
        keys = list(input.keys())
        if len(keys) == 0:
            return ''
        return sep.join(keys)

    def lst_to_str(self, input, sep:str = ', ') -> str:
        """
        Writes list items into a str seperated by ``sep``.
        If input is ``str`` then it is returned verbatium

        Args:
            input (str, Iterable[str]): input to parse
            sep (str, optional): Seperate usd when joining list. Defaults to ', '.

        Returns:
            str: value
        """
        if isinstance(input, str):
            return input
        if len(input) == 0:
            return ''
        return sep.join(input)
    
    def is_out_arg(self, input: str) -> bool:
        """Gets if input is ``out`"""
        if not input:
            return False
        return input == 'out'
    
    def get_last_part(self, input: str, sep='.') -> str:
        """
        Splits a string and returns the last part

        Args:
            input (str): string to get last part of.
            sep (str, optional): string used to split. Defaults to ``.``

        Returns:
            str: last part of input
        """
        if not input:
            return ''
        _parts = input.rsplit(sep=sep, maxsplit=1)
        return _parts.pop()

    def convert_lst_last(self, lst: List[str], sep='.') -> List[str]:
        """
        Converts a list of Long names such as ["com.sun.star.uno.XInterface"]
        into list of last part such as ["XInterface"]

        Args:
            lst (List[str]): Input list
            sep (str, optional): string used to split. Defaults to ``.``

        Returns:
            List[str]: result list
        """
        result =[]
        for itm in lst:
            result.append(self.get_last_part(input=itm, sep=sep))
        return result
    
    # region sorting
    def _sort_dict(self, d:dict, reverse: bool = False) -> dict:
        """
        Sorts a dictionary by its keys

        Args:
            d (dict): input dictionary
            reverse (bool, optional): If ``True`` result are reversed. Defaults to ``False``.

        Returns:
            dict: new sorted dict.
        """
        if not d:
            return {}
        keys = list(d.keys())
        keys.sort(reverse=reverse)
        result = {}
        for key in keys:
            result[key] = d[key]
        return result
        
        
    def _sort_dicts(self, lst: List[dict], sort_key: str) -> List[dict]:
        """
        Sort a list of Dictionaries

        Args:
            lst (List[dict]): List of dictionaries to sort
            sort_key (str): Key of dictionary used for sorting

        Returns:
            List[dict]: Sorted list of dictionaries.
        """
        if len(lst) == 0:
            return lst
        keys: List[str] = []
        _result: List[dict] = []
        for i, itm in enumerate(lst):
            keys.append((itm[sort_key], i))
        keys.sort()
        for k in keys:
            _result.append(lst[k[1]])
        return _result

    # endregion sorting
    
    def dynamic_imp(self, package: str, mod_name: str, class_name: str) -> Tuple[ModuleType, object]:
        try:
            module = importlib.import_module(f"{package}.{mod_name}")
            my_class = getattr(module, class_name)
            return module, my_class
        except Exception as e:
            # print(e)
            raise e

    def get_safe_word(self, in_str: object) -> object:
        if not isinstance(in_str, str):
            return in_str
        if in_str in RESERVER_WORDS:
            return in_str + '_'
        return in_str

    def get_q_type(self, in_type: object) -> object:
        """If in_type is in quote then it is quoted.  Otherwise in_type is returned"""
        if not isinstance(in_type, str):
            return in_type
        if in_type in self.quote:
            return f"'{in_type}'"
        return in_type

    def get_timestamp_utc(self) -> str:
        """
        Gets utc timestamp in format of ``2021-12-16 11:37:50+00:00``

        Returns:
            datetime: utc timestamp
        """
        current_GMT = time.gmtime()
        ts = calendar.timegm(current_GMT)
        return str(datetime.fromtimestamp(ts, tz=timezone.utc))

    # region Class inherits and From Imports

    def get_from_import(self, class_name: str, im_data: Iterable[str]) -> str:
        """
        Get a from string such as 'from ..sdbcx.table_descriptor import DataSettings`

        Args:
            class_name (str): Name if the class then is using the import or is extended by import
            im_data (List[str]): List of str expected to be a length of two.

        Returns:
            str: string formated for a from statement
        """
        im_len = len(im_data)
        if im_len < 2:
            raise Exception(f"{self.__class__.__name__}.get_from_import() Expected im_data param to have a min length of two!")
        im = im_data[0]  # .sdbcx.table_descriptor
        name = im_data[1]  # DataSettings
        if im_len == 3:
            s_as = im_data[2]
            return f"from {im} import {name} as {s_as}"
        if name == class_name:
            # can not extend a class with the same name.
            # Change the from import and elsewhere change the extends name to match
            im_parts = im.rsplit(sep='.', maxsplit=1)
            # because there is a standerd through all templates for snake case name and name,
            # such table_descriptor, TableDescriptor
            # it means we can rely on this standerd to adjust import
            im_last = im_parts.pop()
            im = '.'.join(im_parts)
            return f"from {im} import {im_last}"
        return f"from {im} import {name}"
            
    def get_class_inherits(self, class_name: str, imports: Union[str, List[str]]) -> str:
        """
        Gets class inherits taking into accout if an inherit is the same name as the class.

        Args:
            class_name (str): Name of the class inheriting
            imports (Union[str, List[str]]): string or list of strings of class inherits

        Returns:
            str: comma sep string of inherits.
        """
        def get_import(name: str) -> str:
            def is_mapped(name: str) -> bool:
                return name in self.extends_map
            def get_mapped(name: str) -> bool:
                return self.extends_map[name]
            if is_mapped(name):
                return get_mapped(name)
            _name = self.get_last_part(input=name)
            if class_name == _name:
                return f"{self.camel_to_snake(_name)}.{_name}"
            else:
                return _name
        if isinstance(imports, str):
            return get_import(imports)
        im_lst: List[str] = []
        for s in imports:
            im_lst.append(get_import(s))
        s = 'object'
        for i, im in enumerate(im_lst):
            if i == 0:
                s = ''
            if i > 0:
                s += ', '
            s += im
        return s
    # endregion Class inherits and From Imports
