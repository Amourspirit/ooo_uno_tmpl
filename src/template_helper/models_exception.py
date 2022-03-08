# coding: utf-8
import uno
from pathlib import Path
from typing import List, Tuple, Union
import json
from ..model.shared.data.properties.prop import Prop
from ..model.ex.model_ex import ModelException
from ..utilities import util
from .class_arg import ClassArg
from .models_base import ModelsBase


class ModelExceptions(ModelsBase):
    def __init__(self, json_data_file: str) -> None:
        super().__init__()
        self._config = util.get_app_cfg()
        j_file = self._get_json_path(json_file=json_data_file)
        with open(j_file) as file:
            json_data: dict = json.load(file)
        self._model = ModelException(**json_data)
        self._parents: List[ModelExceptions] = []
        self._cache = {}
        self._uno_instance = None
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
            mod = ModelExceptions(json_data_file=str(p))
            self._parents.append(mod)

    def get_properties_all(self) -> List[dict]:
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
        """
        key = "get_sorted_names"
        if key in self._cache:
            return self._cache[key]
        sorted = []
        sort = self._model.parser_args.sort
        if not self._model.data.items.types is None:
            for i, t in enumerate(self._model.data.items.types):
                sorted.append((t.name, i))
        if not self._model.data.items.properties is None:
            for i, p in enumerate(self._model.data.items.properties):
                sorted.append((p.name, i))
        if sort:
            sorted.sort()
        self._cache[key] = sorted
        return self._cache[key]

    def get_class_args(self, uno_none: bool = True) -> List[ClassArg]:
        key = 'get_class_args'
        if key in self._cache:
            return self._cache[key]
        sorted_names = self.get_sorted_names()
        d_lst = self.get_properties_all()
        results: List[ClassArg] = []
        for _, index in sorted_names:
            itm: dict = d_lst[index]
            name = self.get_safe_word(itm['name'])
            tipe = itm['returns']
            prop = Prop(**itm)
            results.append(ClassArg(
                name=name,
                type=tipe,
                default=self.get_attrib_default(prop=prop, uno_none=uno_none)))
        self._cache[key] = results
        return self._cache[key]

    def get_parents_class_args(self, uno_none: bool = True) -> List[ClassArg]:
        results = []
        if self.is_parents is False:
            return results
        for parent in self._parents:
            results.extend(parent.get_class_args(uno_none=uno_none))
            results.extend(parent.get_parents_class_args(uno_none=uno_none))
        return results

    def is_parents(self) -> bool:
        """Gets if instance as Parents"""
        return len(self._parents) > 0
    
    def get_attrib_default(self, prop: Prop, uno_none: bool = False) -> str:
        name = prop.name
        returns = prop.returns
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
        if self._uno_instance is None:
            self._uno_instance = uno.createUnoStruct(self.model.data.full_name)
        return self._uno_instance

    @property
    def parents(self) -> 'List[ModelExceptions]':
        return self._parents
    
    @property
    def model(self) -> ModelException:
        return self._model
