# coding: utf-8
import logging
import inspect
import importlib
from kwhelp.decorator import AcceptedTypes, DecFuncEnum
from typing import Set, List, Tuple
from types import ModuleType
from ..common.util import Util
from ..common import log_load
# region Logger
logger: logging.Logger = log_load.get_logger()
# endregion Logger


class ImportCheck:
    """
    Dynamically imports classes from scratch.
    Allows for testing of classes that are inherited so
    services do not inherit classes that are already inherited by a
    child class.
    """
    # https://tinyurl.com/y6veetog
    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def __init__(self, ns: str):
        """
        Constructor

        Args:
            ns (str): Namespace of the component being tested
                such as ``com.sun.star.uno``
        """
        self._imports = {}
        self._prefix = 'scratch.uno_obj'
        self._unique: Set[str] = set()
        self._ns = ns
        self._ns_mod = Util.get_last_part(self._ns)

    def _get_name_part(self, import_name: str) -> str:
        name = import_name
        if name.startswith('com.sun'):
            name = name[13:]
            # accessibility.XAccessibleContext
        else:
            name = self._ns_mod + '.' + name
        return name

    @AcceptedTypes((list, tuple, set), ftype=DecFuncEnum.METHOD)
    def load_imports(self, imports: List[str]):
        """
        Load a list of import names for later comparsion.
        Name can be in format of ``com.sun.star.accessibility.XAccessibleContext``
        or ``XAccessibleContext``

        Args:
            imports (List[str]): List of imports

        Note:
            If an import is unable to load then it is simpley ignored
            and not tested.
        """
        # imports will be in format of:
        # com.sun.star.accessibility.XAccessibleContext
        # or
        # XAccessibleContext
        for im in imports:
            name = self._get_name_part(im)
            parts = name.rsplit(sep='.', maxsplit=1)
            pkg_name = f"{self._prefix}.{parts[0]}"
            cls_name = parts[1]
            mod_name = Util.camel_to_snake(cls_name)
            try:
                mod, cl = self.dynamic_imp(pkg_name, mod_name, cls_name)
            except Exception as e:
                logger.warn(
                    'ImportCheck.load_imports() Unable to load module for : Package:%s, Module: %s Class: %s', pkg_name, mod_name, cls_name)
                continue
            names_lst = self.get_class_names(cl, False)

            for n in names_lst:
                self._unique.add(n)

    @AcceptedTypes(str, ftype=DecFuncEnum.METHOD)
    def is_inherited(self, import_name: str) -> bool:
        """
        Test if the ``import_name`` is inherited by any of the current
        classes loaded through ``load_imports()``.

        Args:
            import_name (str): import to test

        Returns:
            bool: ``True`` if already inherited by another class; Otherwise, ``False``
        """
        name = self._get_name_part(import_name)
        return name in self._unique

    def get_class_name(self, obj):
        if (inspect.isclass(obj) == False):
            obj = obj.__class__
        class_name = obj.__name__
        return class_name

    # Works both for python 2 and 3
    @AcceptedTypes(object, bool, ftype=DecFuncEnum.METHOD)
    def get_class_names(self, obj: object, include_obj: bool = True):
        class_name = []
        if (inspect.isclass(obj) == False):
            obj = obj.__class__
        classes = inspect.getmro(obj)
        c_name = str(obj.__name__)
        for cl in classes:
            name = cl.__name__
            if include_obj is False:
                if name == c_name:
                    continue
            mod = cl.__module__
            if mod.startswith(self._prefix):
                # scratch.uno_obj.uno.x_interface
                _mod = mod.split(sep='.', maxsplit=2)[2]  # uno.x_interface
                _mod = _mod.rsplit(sep='.', maxsplit=1)[0]  # uno
                class_name.append(f"{_mod}.{name}")
        return class_name

    @AcceptedTypes(str, opt_all_args=True, ftype=DecFuncEnum.METHOD)
    def dynamic_imp(self, package: str, mod_name: str, class_name: str) -> Tuple[ModuleType, object]:
        try:
            key = f"{package}.{mod_name}"
            if key in self._imports:
                module = self._imports[key]
            else:
                module = importlib.import_module(key)
                self._imports[key] = module
            my_class = getattr(module, class_name)
            return module, my_class
        except Exception as e:
            # print(e)
            raise e
