# coding: utf-8
import uno
from typing import List, Set, Tuple, Union, Any, overload
from dataclasses import asdict
import json

from rel import mod_rel as RelInfo

from .class_arg import ClassArg
from .models_base import ModelsBase
from ..model.shared.data.from_import import FromImport
from ..model.shared.data.properties.prop import Prop
from ..model.struct.model_struct import ModelStruct
from ..utilities import util
from ..parser import mod_type


class ModelsStruct(ModelsBase):
    # region Constructor
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
    def __init__(self, json_data: ModelStruct) -> None:
        """
        Constructor

        Args:
            json_data (ModelException): Exception Model.
        """

    def __init__(self, json_data: Union[str, dict, ModelStruct]) -> None:
        super().__init__()
        if isinstance(json_data, str):
            self._init_str(json_data)
        elif isinstance(json_data, dict):
            self._init_dict(json_data)
        elif isinstance(json_data, ModelStruct):
            self._init(json_data)

    def _init_str(self, json_file: str) -> None:
        j_file = self._get_json_path(json_file=json_file)
        with open(j_file) as file:
            json_data: dict = json.load(file)
        self._init_dict(json_data)

    def _init_dict(self, dct: dict) -> None:
        model = ModelStruct(**dct)
        self._init(model)

    def _init(self, mod: ModelStruct) -> None:
        self._model = mod
        self._parents: List[ModelsStruct] = []
        self._set_parents()
    # endregion Constructor

    def _set_parents(self) -> None:
        for ns in self._model.data.extends:
            p = self._get_path_from_ns(ns)
            mod = ModelsStruct(json_data=str(p))
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

        for itm in self._model.data.items:
            results.append(asdict(itm))

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
        for i, itm in enumerate(self._model.data.items):
            sorted.append((itm.name, i))
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
        for _, index in sorted_names:
            itm: dict = d_lst[index]
            name = self.get_safe_word(itm['name'])
            tipe = itm['type']
            prop = Prop(
                name=itm['name'],
                returns=itm['type'],
                origin=itm['origin'],
                origtype=itm['origtype'],
                desc=itm['desc']
            )
            results.append(ClassArg(
                name=name,
                type=tipe,
                default=self.get_attrib_default(
                    name=prop.name, returns=prop.returns, uno_none=uno_none),
                p_type=self.get_python_type(prop.origin)
            ))
        self._cache[key] = results
        return self._cache[key]

    def _get_parents_class_args(self, uno_none: bool = True) -> List[ClassArg]:
        results = []
        if self.is_parents() is False:
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
        pargs = self.get_parents_class_args(uno_none=uno_none)
        cargs = self.get_class_args(uno_none=uno_none)
        return pargs + cargs

    def _get_model_full_imports(self) -> Set[str]:
        imp = set()
        imp.update(self._model.data.full_imports.general)
        imp.update(self._model.data.full_imports.typing)
        return imp

    def get_from_full_imports(self) -> List[FromImport]:
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
            if not arg.p_type is None:
                imports = arg.p_type.get_all_from_imports(
                    ns=self._model.namespace)
                for imp in imports:
                    if not imp in m_imports:
                        # this import is not currently part of any imports
                        result.append(get_rel(imp))
        return result

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

        # region Abstract Implementions

    def get_name(self) -> str:
        return self._model.name

    def get_namespace(self) -> str:
        return self._model.namespace

    def get_long_names(self) -> bool:
        return self._model.parser_args.long_names
    # endregion Abstract Implementions

    @property
    def parents(self) -> 'List[ModelsStruct]':
        return self._parents

    @property
    def model(self) -> ModelStruct:
        return self._model
