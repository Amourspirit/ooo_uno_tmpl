# coding: utf-8
import uno
from pathlib import Path
from typing import List, Tuple, Union, Any, overload
import json

from rel import mod_rel as RelInfo

from .class_arg import ClassArg
from .models_base import ModelsBase
from ..model.shared.data.from_import import FromImport
from ..model.shared.data.properties.prop import Prop
from ..model.ex.model_ex import ModelException
from ..utilities import util
from ..data_manage.db_class.qry_component import QryComponent
from ..data_manage.db_class.db_connect import DbConnect


class ModelsException(ModelsBase):
    @overload
    def __init__(self, json_data: str) -> None:
        """
        Constructor

        Args:
            json_data (str): relative or absoulete path to json file.
        """

    @overload
    def __init__(self, json_data: dict) -> None:
        """
        Constructor

        Args:
            json_data (dict): Json data as dictionary.
        """

    @overload
    def __init__(self, json_data: ModelException) -> None:
        """
        Constructor

        Args:
            json_data (ModelException): Exception Model.
        """

    def __init__(self, json_data: Union[str, dict, ModelException]) -> None:
        super().__init__()
        self._config = util.get_app_cfg()
        if isinstance(json_data, str):
            self._init_str(json_data)
        elif isinstance(json_data, dict):
            self._init_dict(json_data)
        elif isinstance(json_data, ModelException):
            self._init(json_data)

    def _init_str(self, json_file: str) -> None:
        j_file = self._get_json_path(json_file=json_file)
        with open(j_file) as file:
            json_data: dict = json.load(file)
        self._init_dict(json_data)

    def _init_dict(self, dct: dict) -> None:
        model = ModelException(**dct)
        self._init(model)

    def _init(self, mod: ModelException) -> None:
        self._model = mod
        self._parents: List[ModelsException] = []
        self._cache = {}
        self._uno_instance: Any = False
        self._conn = DbConnect(self._config)
        self._set_parents()

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

    def _set_parents(self) -> None:
        for ns in self._model.data.extends:
            # root uno exception inherits from python Exception
            if ns == 'Exception':
                break
            p = self._get_path_from_ns(ns)
            mod = ModelsException(json_data=str(p))
            self._parents.append(mod)

    def get_properties_all(self) -> List[dict]:
        """
        Gets combined args for types, and properties as dict.

        Returns:
            List[dict]: dictionary of types and args
        
        Note:
            This method is internaly cached.
        """
        key = 'get_properties_all'
        if key in self._cache:
            return self._cache[key]
        results: List[dict] = []
        if not self._model.data.items.types is None:
            for t in self._model.data.items.types:
                results.append(t.dict())
        if not self._model.data.items.properties is None:
            for p in self._model.data.items.properties:
                results.append(p.dict())
        self._cache[key] = results
        return self._cache[key]

    def get_sorted_names(self) -> List[Tuple[str, int]]:
        """
        Gets a list of tuple. (<name>, <index>)

        if instance sort is true then sorting is applied.

        Returns:
            List[Tuple[str, int]]: List of tuple

        Note:
            This method is internaly cached.
        """
        key = "get_sorted_names"
        if key in self._cache:
            return self._cache[key]
        sorted = []
        sort = self._model.parser_args.sort
        i = 0
        if not self._model.data.items.types is None:
            for t in self._model.data.items.types:
                sorted.append((t.name, i))
                i += 1
        if not self._model.data.items.properties is None:
            for p in self._model.data.items.properties:
                sorted.append((p.name, i))
                i += 1
        if sort:
            sorted.sort()
        self._cache[key] = sorted
        return self._cache[key]

    def get_class_args(self, uno_none: bool = True) -> List[ClassArg]:
        """
        Get args for current instance's model.
        
        This is the current instance constructor args.

        Args:
            uno_none (bool, optional): Determines if ``UNO_NONE`` is used. Defaults to True.

        Returns:
            List[ClassArg]: List of args.

        Note:
            This method is internaly cached.
        """
        key = 'get_class_args_' + str(uno_none)
        if key in self._cache:
            return self._cache[key]
        sorted_names = self.get_sorted_names()
        d_lst = self.get_properties_all()
        results: List[ClassArg] = []
        qry = QryComponent(self._conn.connection_str)
        for _, index in sorted_names:
            itm: dict = d_lst[index]
            name = self.get_safe_word(itm['name'])
            tipe = itm['returns']
            prop = Prop(**itm)
            results.append(ClassArg(
                name=name,
                type=tipe,
                default=self.get_attrib_default(name=prop.name, returns=prop.returns, uno_none=uno_none),
                component=None if prop.origtype is None else qry.get_component(full_ns=prop.origtype)
            ))
        self._cache[key] = results
        return self._cache[key]

    def _get_parents_class_args(self, uno_none: bool = True) -> List[ClassArg]:
        results = []
        if self.is_parents is False:
            return results
        for parent in self._parents:
            results.extend(parent.get_class_args(uno_none=uno_none))
            # results.extend(parent.get_parents_class_args(uno_none=uno_none))
            results = parent._get_parents_class_args(
                uno_none=uno_none) + results
        return results

    def get_parents_class_args(self, uno_none: bool = True) -> List[ClassArg]:
        """
        Gets parent Class args.
        
        Gets the args of parent constructor excluding this instance's model args

        Args:
            uno_none (bool, optional): Determines if ``UNO_NONE`` is used. Defaults to True.

        Returns:
            List[ClassArg]: List or args

        Note:
            This method is internaly cached.
        """
        key = 'get_parents_class_args_' + str(uno_none)
        if key in self._cache:
            return self._cache[key]

        self._cache[key] = self._get_parents_class_args(uno_none=uno_none)
        return self._cache[key]

    def get_class_args_all(self, uno_none: bool = True) -> List[ClassArg]:
        pargs = self.get_parents_class_args()
        cargs = self.get_class_args()
        return pargs + cargs

    def is_parents(self) -> bool:
        """Gets if instance as Parents"""
        return len(self._parents) > 0
    
    def is_args(self) -> bool:
        """
        Gets if there is any args for current instance or its parent classes.

        Returns:
            bool: ``True`` if instance or parent classes have constructor args;
            Otherwise ``False``.
        """
        cargs = self.get_class_args()
        if len(cargs) > 0:
            return True
        pargs = self.get_parents_class_args()
        if len(pargs) > 0:
            return True
        return False

    def _get_model_full_imports(self):
        imp = set()
        imp.update(self._model.data.full_imports.general)
        imp.update(self._model.data.full_imports.typing)
        return imp
    
    def get_full_imports(self) -> List[FromImport]:
        """
        Get full import for current model plus all parent models.
        
        I a parent model constructor arg needs an import then this method detects
        it and adds it to the list if it is not already included.

        Returns:
            List[FromImport]: List of form imports
        """
        def get_rel(ns: str) -> FromImport:
            info = RelInfo.get_rel_import_long(
                in_str=ns,
                ns=self._model.namespace
            )
            return FromImport(
                frm=info.frm,
                imp=info.imp,
                az=info.as_
            )
        result = [*self._model.data.from_imports]
        pargs = self.get_parents_class_args(uno_none=False)
        if len(pargs) == 0:
            return result
        m_imports = self._get_model_full_imports()
        for arg in pargs:
            if not arg.component is None:
                # if there is an arg component then it may need an import
                if not arg.component.id_component in m_imports:
                    # this import is not currently part of any imports
                    result.append(get_rel(arg.component.id_component))
        return result

    def get_attrib_default(self, name: str, returns: str, uno_none: bool = False) -> str:
        """
        Get defatul attribute value from uno

        Args:
            name (str): Name of property to get attrib for.
            returns (str): property returns type
            uno_none (bool, optional): If ``True`` replaces ``None`` with ``UNO_NONE`` where needed; Otherwise uses ``None``. Defaults to False.

        Returns:
            str: attribute default value as string.

        Note:
            If current exception/struct is not in the installled uno version then
            all unknow value are either ``None`` or ``UNO_NONE``
            
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

    @property
    def uno_instance(self):
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

    @property
    def parents(self) -> 'List[ModelsException]':
        return self._parents

    @property
    def model(self) -> ModelException:
        return self._model
