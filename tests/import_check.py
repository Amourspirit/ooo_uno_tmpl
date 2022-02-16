import importlib
import inspect
from types import ModuleType
from typing import Set, List


class ImportCheck:
    """
    Dynamically imports classes from scratch.
    Allows for testing of classes that are inherited so
    services do not inherit classes that are already inherited by a
    child class.
    """
    # https://tinyurl.com/y6veetog
    def __init__(self):
        """
        Constructor

        Args:
            ns (str): Namespace of the component being tested
                such as ``com.sun.star.uno``
        """
        self._imports = {}
        self._prefix = 'scratch.uno_obj'
        self._unique: Set[str] = set()
    #     self._ns_mod = Util.get_last_part(self._ns)

    # def _get_name_part(self, import_name: str) -> str:
    #     name = self._ns_mod + '.' + import_name
    #     return name

    def load_imports(self, imports: List[str]) -> bool:
        """
        Load a list of import names for later comparsion.
        Name can be in format of ``com.sun.star.accessibility.XAccessibleContext``
        or ``XAccessibleContext``

        Args:
            imports (List[str]): List of imports
    
        Returns:
            True if all imorts succeed import; Otherwise False
        """
        # imports will be in format of:
        # com.sun.star.accessibility.XAccessibleContext
        # or
        # XAccessibleContext
        
        for im in imports:
            result = self.load_import(im=im)
            if not result:
                return False
        return True

    def load_import(self, im: str) -> bool:
        """
        Load an import name for later comparsion.
        Name is expected in format of ``scratch.uno_obj.form.component.rich_text_control.RichTextControl``

        Args:
            imports (List[str]): List of imports

        Returns:
            True if imort succeeds; Otherwise False
        """
        try:
            parts = im.split(sep='.')
            cls_name = parts.pop()
            mod_name = parts.pop()
            pkg_name = '.'.join(parts)
            _, cl = self.dynamic_imp(pkg_name, mod_name, cls_name)
            names_lst = self.get_class_names(cl, False)
        except Exception:
            return False
        try:
            for n in names_lst:
                self._unique.add(n)
        except Exception:
            return False
        return True

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

    def get_class_name(self, obj) -> str:
        if (inspect.isclass(obj) == False):
            obj = obj.__class__
        class_name = obj.__name__
        return class_name

    # Works both for python 2 and 3
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

    def dynamic_imp(self, package: str, mod_name: str, class_name: str):
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
