# coding: utf-8
from rel import mod_rel as RelInfo
from abc import abstractmethod, abstractproperty
from typing import List, Set, Tuple
from .models_base import ModelsBase
from ..model.shared.data.ooo_data import Data
from ..model.shared.data.from_import import FromImport
from ..model.shared.args.parser_args import ParserArgs
from .class_arg import ClassArg
from ..model.shared.data.properties.prop import Prop


class ModelsXsrcBase(ModelsBase):
    # region Constructor   
    def __init__(self) -> None:
        super().__init__()
        
    # endregion Constructor

    @abstractmethod
    def _get_parents_class_args(self, uno_none: bool = True) -> List[ClassArg]: ...

    @abstractproperty
    def model_data(self) -> Data: ...
    
    @abstractproperty
    def parser_args(self) -> ParserArgs: ...
    
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
        if not self.model_data.items.types is None:
            for t in self.model_data.items.types:
                results.append(t.dict())
        if not self.model_data.items.properties is None:
            for p in self.model_data.items.properties:
                results.append(p.dict())
        self._cache[key] = results
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
            tipe = itm['returns']
            prop = Prop(**itm)
            results.append(ClassArg(
                name=name,
                type=tipe,
                default=self.get_attrib_default(
                    name=prop.name, returns=prop.returns, uno_none=uno_none),
                p_type=self.get_python_type(prop.origin)
            ))
        self._cache[key] = results
        return self._cache[key]

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
        sort = self.parser_args.sort
        i = 0
        if not self.model_data.items.types is None:
            for t in self.model_data.items.types:
                sorted.append((t.name, i))
                i += 1
        if not self.model_data.items.properties is None:
            for p in self.model_data.items.properties:
                sorted.append((p.name, i))
                i += 1
        if sort:
            sorted.sort()
        self._cache[key] = sorted
        return self._cache[key]

    def _get_model_full_imports(self) -> Set[str]:
        imp = set()
        imp.update(self.model_data.full_imports.general)
        imp.update(self.model_data.full_imports.typing)
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
                ns=self.model_data.namespace
            )
            return FromImport(
                frm=info.frm,
                imp=info.imp,
                az=info.as_
            )
        result = [*self.model_data.from_imports]
        pargs = self.get_parents_class_args(uno_none=False)
        if len(pargs) == 0:
            return result
        m_imports = self._get_model_full_imports()
        for arg in pargs:
            if not arg.p_type is None:
                imports = arg.p_type.get_all_imports(ns=self.model_data.namespace)
                for imp in imports:
                    if not imp in m_imports:
                        # this import is not currently part of any imports
                        result.append(get_rel(imp))
        return result

