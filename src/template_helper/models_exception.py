# coding: utf-8
from typing import List,Union, overload
import json
from .class_arg import ClassArg
from .models_xsrc_base import ModelsXsrcBase
from ..model.ex.model_ex import ModelException
from ..model.shared.data.ooo_data import Data
from ..model.shared.args.parser_args import ParserArgs


class ModelsException(ModelsXsrcBase):
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
    def __init__(self, json_data: ModelException) -> None:
        """
        Constructor

        Args:
            json_data (ModelException): Exception Model.
        """

    def __init__(self, json_data: Union[str, dict, ModelException]) -> None:
        super().__init__()
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

        self._set_parents()

    # endregion Constructor

    def _set_parents(self) -> None:
        for ns in self._model.data.extends:
            # root uno exception inherits from python Exception
            if ns == 'Exception':
                break
            p = self._get_path_from_ns(ns)
            mod = ModelsException(json_data=str(p))
            self._parents.append(mod)

    def is_parents(self) -> bool:
        """Gets if instance as Parents"""
        return len(self._parents) > 0

    # region Abstract Implementions

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

    def get_name(self) -> str:
        return self._model.name

    def get_namespace(self) -> str:
        return self._model.namespace

    def get_long_names(self) -> bool:
        return self._model.parser_args.long_names

    @property
    def model_data(self) -> Data:
        return self._model.data

    @property
    def parser_args(self) -> ParserArgs:
        return self._model.parser_args
    # endregion Abstract Implementions

    @property
    def parents(self) -> 'List[ModelsException]':
        return self._parents

    @property
    def model(self) -> ModelException:
        return self._model
