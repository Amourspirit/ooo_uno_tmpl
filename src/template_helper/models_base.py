# coding: utf-8
import uno
from pathlib import Path
from typing import Any, Dict, Union
from abc import ABC, abstractmethod
from ..utilities import util
from ..cfg.config import AppConfig
from ..utilities import util
from ..parser import mod_type

class ModelsBase(ABC):

    # region Constructor
    def __init__(self) -> None:
        super().__init__()
        self._config = util.get_app_cfg()
        self._uno_instance: Any = False
        self._cache: Dict[str, object] = {}
    # endregion Constructor

    def get_safe_word(self, in_str: object) -> object:
        """
        Get safe word. If a word is a reserved python word then _ is appended.

        Args:
            in_str (object): input

        Returns:
            object: if ``in_str`` is not str then it is returned verbatim. Otherwise returns str.
        """
        if not isinstance(in_str, str):
            return in_str
        if in_str in util.RESERVER_WORDS:
            return in_str + '_'
        return in_str

    def get_attrib_default(self, name: str, returns: str, uno_none: bool = False) -> str:
        """
        Get default attribute value from uno

        Args:
            name (str): Name of property to get attrib for.
            returns (str): property returns type
            uno_none (bool, optional): If ``True`` replaces ``None`` with ``UNO_NONE`` where needed; Otherwise uses ``None``. Defaults to False.

        Returns:
            str: attribute default value as string.

        Note:
            If current exception/struct is not in the installed uno version then
            all unknown value are either ``None`` or ``UNO_NONE``
            
            For instance ReadOnlyOpenRequest: https://tinyurl.com/ycu8u8wu
            is a 7.2 version
        """
        if self.uno_instance is None:
            if uno_none is True:
                return 'UNO_NONE'
            return 'None'
        result = getattr(self.uno_instance, name, None)
        if isinstance(result, str):
            return result
        elif isinstance(result, uno.Enum):
            return f"{returns}.{result.value}"
        elif isinstance(result, uno.Char):
            char = ''.join(r'\u{:04X}'.format(ord(chr))
                           for chr in result.value)
            return char
        elif isinstance(result, uno.ByteSequence):
            if uno_none is True:
                return 'UNO_NONE'
            return 'None'
        elif hasattr(result, '__pyunostruct__'):
            if uno_none is True:
                return 'UNO_NONE'
            if returns == 'object':
                return 'None'
            return f"{returns}()"
        return str(result)

    def _get_json_path(self, json_file) -> Path:
        p = Path(json_file)
        if p.is_absolute():
            return p
        return Path(util.get_root(), p)

    def _get_path_from_ns(self, ns: str) -> Path:
        parts = ns.removeprefix('com.sun.star.').split('.')
        file_name = parts.pop() + ".json"
        p = Path(util.get_root(), self._config.uno_base_dir, *parts, file_name)
        return p

    def get_python_type(self, origin: Union[str, None]) -> Union[mod_type.PythonType, None]:
        """
        Get python type form origin data.

        Args:
            origin (Union[str, None]): origin data get ``PythonType`` from.

        Returns:
            Union[mod_type.PythonType, None]: Python type if ``origin`` is str; Otherwise, ``None``.
        """
        def get_engine() -> mod_type.TypeRules:
            key = "mod_type_type_rules"
            if key in self._cache:
                return self._cache[key]
            self._cache[key] = mod_type.TypeRules(
                ns=self.get_namespace(), long_names=self.get_long_names())
            return self._cache[key]
        if origin is None:
            return None
        eng = get_engine()
        return eng.get_python_type(origin)

    # region Abstract Methods
    @abstractmethod
    def get_name(self) -> str: ...
    @abstractmethod
    def get_namespace(self) -> str: ...
    @abstractmethod
    def get_long_names(self) -> bool: ...
    # endregion Abstract Methods

    @property
    def app_config(self) -> AppConfig:
        """Global Instance of AppConfig"""
        return self._config

    @property
    def uno_instance(self) -> Any:
        """
        Get a uno instance of current uno exception being processed

        Returns:
            Any: return uno instance if it can be created; Otherwise, ``None``

        Note:
            not all exceptions/struct are available in all version.
            ReadOnlyOpenRequest: https://tinyurl.com/ycu8u8wu
            is a 7.2 version
        """
        if self._uno_instance is False:
            try:
                self._uno_instance = uno.createUnoStruct(
                    self.model.data.full_name)
            except Exception as e:
                self._uno_instance = None
        return self._uno_instance
