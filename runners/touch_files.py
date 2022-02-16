# coding: utf-8
import re
import logging
import glob
import tempfile
from pathlib import Path
from config import AppConfig
from typing import List
from .file_base import FilesBase
from parser.json_parser.interface_parser import Parser as ParserInterface
from parser.json_parser.singleton_parser import Parser as ParserSingleton
from parser.json_parser.service_parser import Parser as ParserService
from parser.json_parser.struct_parser import ParserStruct
from parser.json_parser.enum_parser import ParserEnum
from parser.json_parser.exception_parser import ParserException
from parser.json_parser.typedef_parser import ParserTypeDef
from parser.json_parser.const_parser import ParserConst
# region Touch Files


class TouchFiles(FilesBase):
    _pattern_generic_name = re.compile(r"([a-zA-Z0-9_]+)(<[A-Z, ]+>)")
    def __init__(self, config: AppConfig, log: logging.Logger, **kwargs) -> None:
        super().__init__(config=config)
        self._log = log
        self._check_exist: bool = bool(kwargs.get('check_exist', True))
        self._touch_struct: bool = bool(kwargs.get('touch_struct', False))
        self._touch_const: bool = bool(kwargs.get('touch_const', False))
        self._touch_enum: bool = bool(kwargs.get('touch_enum', False))
        self._touch_ex: bool = bool(kwargs.get('touch_ex', False))
        self._touch_typedef: bool = bool(kwargs.get('touch_typedef', False))
        self._touch_py_files: bool = bool(kwargs.get('touch_py_files', False))
        self._touch_dyn_files: bool = bool(kwargs.get('touch_dyn_files', False))
        self._touch_dyn_py_files: bool = bool(
            kwargs.get('touch_dyn_py_files', False))
        self._touch_cache: bool = bool(kwargs.get('touch_cache_files', False))
        

        self._touch_interface: bool = bool(
            kwargs.get('touch_interface', False))
        self._touch_singleton: bool = bool(
            kwargs.get('touch_singleton', False))
        self._touch_service: bool = bool(
            kwargs.get('touch_service', False))
        self._touch_count = 0
        self._cache = {}
        if self._touch_struct:
            self._touch_struct_files()
        if self._touch_const:
            self._touch_const_files()
        if self._touch_enum:
            self._touch_enum_files()
        if self._touch_ex:
            self._touch_exception_files()
        if self._touch_interface:
            self._touch_interface_files()
        if self._touch_singleton:
            self._touch_singleton_files()
        if self._touch_service:
            self._touch_service_files()
        if self._touch_typedef:
            self._touch_typedef_files()
        if self._touch_cache:
            self._touch_cache_files()

        self._log.info('Touched a total of %d files.', self._touch_count)

    def _get_module_links(self) -> List[str]:
        key = '_get_module_links'
        if key in self._cache:
            return self._cache[key]
        self._cache[key] = self.get_module_link_files()
        return self._cache[key]

    def _touch_struct_files(self):
        link_files = self._get_module_links()
        touched = 0

        def process(f: str):
            nonlocal touched
            p: ParserStruct = ParserStruct(json_path=f)
            links = p.get_links()
            f_path = Path(f).parent
            for link in links:
                name = self._get_clean_filename(link.name)
                if self._touch_py_files:
                    name += '.py'
                elif self._touch_dyn_files:
                    name += self._config.template_dyn_ext
                elif self._touch_dyn_py_files:
                    name += self._config.template_dyn_py_ext
                else:
                    name += self._config.template_struct_ext
                t_path = Path(f_path, name)
                if self._check_exist:
                    if not t_path.exists():
                        continue
                t_path.touch(exist_ok=True)
                touched += 1
                self._log.debug('Touched Struct file: %s', t_path)

        for file in link_files:
            process(file)
        self._log.info('Touched %d Struct files', touched)
        self._touch_count += touched

    def _touch_const_files(self):
        link_files = self._get_module_links()
        touched = 0

        def process(f: str):
            nonlocal touched
            p: ParserConst = ParserConst(json_path=f)
            links = p.get_links()
            f_path = Path(f).parent
            for link in links:
                name = self._get_clean_filename(link.name)
                if self._touch_py_files:
                    name += '.py'
                elif self._touch_dyn_files:
                    name += self._config.template_dyn_ext
                elif self._touch_dyn_py_files:
                    name += self._config.template_dyn_py_ext
                else:
                    name += self._config.template_const_ext
                t_path = Path(f_path, name)
                if self._check_exist:
                    if not t_path.exists():
                        continue
                t_path.touch(exist_ok=True)
                touched += 1
                self._log.debug('Touched Const file: %s', t_path)

        for file in link_files:
            process(file)
        self._log.info('Touched %d Const files', touched)
        self._touch_count += touched

    def _touch_enum_files(self):
        link_files = self._get_module_links()
        touched = 0

        def process(f: str):
            nonlocal touched
            p: ParserEnum = ParserEnum(json_path=f)
            links = p.get_links()
            f_path = Path(f).parent
            for link in links:
                name = self._get_clean_filename(link.name)
                if self._touch_py_files:
                    name += '.py'
                elif self._touch_dyn_files:
                    name += self._config.template_dyn_ext
                elif self._touch_dyn_py_files:
                    name += self._config.template_dyn_py_ext
                else:
                    name += self._config.template_enum_ext
                t_path = Path(f_path, name)
                if self._check_exist:
                    if not t_path.exists():
                        continue
                t_path.touch(exist_ok=True)
                touched += 1
                self._log.debug('Touched Enum file: %s', t_path)

        for file in link_files:
            process(file)
        self._log.info('Touched %d Enum files', touched)
        self._touch_count += touched

    def _touch_exception_files(self):
        link_files = self._get_module_links()
        touched = 0

        def process(f: str):
            nonlocal touched
            p: ParserException = ParserException(json_path=f)
            links = p.get_links()
            f_path = Path(f).parent
            for link in links:
                name = self._get_clean_filename(link.name)
                if self._touch_py_files:
                    name += '.py'
                elif self._touch_dyn_files:
                    name += self._config.template_dyn_ext
                elif self._touch_dyn_py_files:
                    name += self._config.template_dyn_py_ext
                else:
                    name += self._config.template_exception_ext
                t_path = Path(f_path, name)
                if self._check_exist:
                    if not t_path.exists():
                        continue
                t_path.touch(exist_ok=True)
                touched += 1
                self._log.debug('Touched Exception file: %s', t_path)

        for file in link_files:
            process(file)
        self._log.info('Touched %d Exception files', touched)
        self._touch_count += touched

    def _touch_interface_files(self):
        link_files = self._get_module_links()
        touched = 0

        def process(f: str):
            nonlocal touched
            p: ParserInterface = ParserInterface(json_path=f)
            links = p.get_links()
            f_path = Path(f).parent
            for link in links:
                name = self._get_clean_filename(link.name)
                if self._touch_py_files:
                    name += '.py'
                elif self._touch_dyn_files:
                    name += self._config.template_dyn_ext
                elif self._touch_dyn_py_files:
                    name += self._config.template_dyn_py_ext
                else:
                    name += self._config.template_interface_ext
                t_path = Path(f_path, name)
                if self._check_exist:
                    if not t_path.exists():
                        continue
                t_path.touch(exist_ok=True)
                touched += 1
                self._log.debug('Touched Interface file: %s', t_path)

        for file in link_files:
            process(file)
        self._log.info('Touched %d Interface files', touched)
        self._touch_count += touched

    def _touch_singleton_files(self):
        link_files = self._get_module_links()
        touched = 0

        def process(f: str):
            nonlocal touched
            p: ParserSingleton = ParserSingleton(json_path=f)
            links = p.get_links()
            f_path = Path(f).parent
            for link in links:
                name = self._get_clean_filename(link.name)
                if self._touch_py_files:
                    name += '.py'
                elif self._touch_dyn_files:
                    name += self._config.template_dyn_ext
                elif self._touch_dyn_py_files:
                    name += self._config.template_dyn_py_ext
                else:
                    name += self._config.template_singleton_ext
                t_path = Path(f_path, name)
                if self._check_exist:
                    if not t_path.exists():
                        continue
                t_path.touch(exist_ok=True)
                touched += 1
                self._log.debug('Touched Singleton file: %s', t_path)

        for file in link_files:
            process(file)
        self._log.info('Touched %d Singleton files', touched)
        self._touch_count += touched

    def _touch_service_files(self):
        link_files = self._get_module_links()
        touched = 0

        def process(f: str):
            nonlocal touched
            p: ParserService = ParserService(json_path=f)
            links = p.get_links()
            f_path = Path(f).parent
            for link in links:
                name = self._get_clean_filename(link.name)
                if self._touch_py_files:
                    name += '.py'
                elif self._touch_dyn_files:
                    name += self._config.template_dyn_ext
                elif self._touch_dyn_py_files:
                    name += self._config.template_dyn_py_ext
                else:
                    name += self._config.template_service_ext
                t_path = Path(f_path, name)
                if self._check_exist:
                    if not t_path.exists():
                        continue
                t_path.touch(exist_ok=True)
                touched += 1
                self._log.debug('Touched Service file: %s', t_path)

        for file in link_files:
            process(file)
        self._log.info('Touched %d Service files', touched)
        self._touch_count += touched

    def _touch_typedef_files(self):
        link_files = self._get_module_links()
        touched = 0

        def process(f: str):
            nonlocal touched
            p: ParserTypeDef = ParserTypeDef(json_path=f)
            links = p.get_links()
            f_path = Path(f).parent
            for link in links:
                name = self._get_clean_filename(link.name)
                if self._touch_py_files:
                    name += '.py'
                elif self._touch_dyn_files:
                    name += self._config.template_dyn_ext
                elif self._touch_dyn_py_files:
                    name += self._config.template_dyn_py_ext
                else:
                    name += self._config.template_typedef_ext
                t_path = Path(f_path, name)
                if self._check_exist:
                    if not t_path.exists():
                        continue
                t_path.touch(exist_ok=True)
                touched += 1
                self._log.debug('Touched TypeDef file: %s', t_path)

        for file in link_files:
            process(file)
        self._log.info('Touched %d TypeDef files', touched)
        self._touch_count += touched

    def _touch_cache_files(self) -> None:
        touched = 0
        t_path = Path(tempfile.gettempdir())
        cache_path = t_path / self._config.cache_dir
        if not cache_path.exists():
            self._log.info('Touched %d Cache files', touched)
            return

        def process(f: str):
            nonlocal touched
            t_path = Path(f)
            t_path.touch(exist_ok=True)
            touched += 1
        pattern = str(cache_path) + '/*'
        files = glob.glob(pattern)
        for file in files:
            process(file)
        self._log.info('Touched %d Cache files', touched)
        self._touch_count += touched


    def _get_clean_filename(self, input: str) -> str:
        """
        Clean a file name and changes name suah as ``Pair< T, U >`` to ``Pair``

        Args:
            input (str): filename

        Returns:
            str: cleaned file name
        """
        # convert 'Pair< T, U >' to 'Pair'
        s = TouchFiles._pattern_generic_name.sub(r'\g<1>', input)
        s = s.replace(" ", "_")
        return s
# endregion Touch Files
