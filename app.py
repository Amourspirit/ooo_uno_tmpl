#!/usr/bin/env python
# region Imports
from dataclasses import dataclass
import logging
import os
import sys
import re
import shutil
import glob
import argparse
import subprocess
import tempfile
from data_manage import db_manager, json_controler
from multiprocessing import Pool
from typing import List, Optional, Set, Type
from kwhelp import rules
from kwhelp.decorator import DecFuncEnum, RuleCheckAll
from kwhelp.exceptions import RuleError
from enum import IntEnum
from pathlib import Path
from logger.log_handle import get_logger
from parser import __version__, JSON_ID, const as url_parser_const, enm as url_parser_enum, ex as url_parser_ex, xsrc as url_parser_interface, service as url_parser_service, singleton as url_parser_singleton, struc as url_parser_struct, typedef as url_parser_typedef
from config import AppConfig, read_config
from parser.json_parser.interface_parser import parse as parse_interface, Parser as ParserInterface
from parser.json_parser.singleton_parser import parse as parse_singleton, Parser as ParserSingleton
from parser.json_parser.service_parser import parse as parse_service, Parser as ParserService
from parser.json_parser.struct_parser import parse as parse_struct, ParserStruct
from parser.json_parser.enum_parser import parse as parse_enm, ParserEnum
from parser.json_parser.exception_parser import parse as parse_ex, ParserException
from parser.json_parser.typedef_parser import parse as parse_typedef, ParserTypeDef
from parser.json_parser.const_parser import parse as parse_const, ParserConst
from parser.json_parser import linkproc

# endregion Imports

# region Data Class


@dataclass
class WriteInfo:
    file: str
    py_file: str
    scratch_path: Path


@dataclass(frozen=True, eq=True)
class CompileLinkArgs:
    config: AppConfig
    path: Optional[str] = None
    use_sub_process: bool = True
# endregion Data Class


# region Logger
logger = None

# logger/log_handle.py

# endregion Logger

# region Compare


class CompareEnum(IntEnum):
    Before = -1
    Equal = 0
    After = 1


class CompareFile:

    @staticmethod
    @RuleCheckAll(rules.RulePathExist, ftype=DecFuncEnum.METHOD_STATIC)
    def compare(file1, file2) -> CompareEnum:
        time1 = os.path.getmtime(file1)
        time2 = os.path.getmtime(file2)
        if time1 < time2:
            return CompareEnum.Before
        if time1 > time2:
            return CompareEnum.After
        return CompareEnum.Equal

# endregion Compare

# region FilesBase


class FilesBase:
    def __init__(self, config: AppConfig) -> None:
        self._config: AppConfig = config
        self._root_dir = Path(__file__).parent

    def _mkdirp(self, dest_dir):
        # Python ≥ 3.5
        if isinstance(dest_dir, Path):
            dest_dir.mkdir(parents=True, exist_ok=True)
        else:
            Path(dest_dir).mkdir(parents=True, exist_ok=True)

    def _get_template_files(self):
        dirname = str(self._root_dir / self._config.uno_obj_dir)
        # https://stackoverflow.com/questions/20638040/glob-exclude-pattern
        # exclude files that start with _
        pattern = dirname + '/**/[!_]*.tmpl'
        files = glob.glob(pattern, recursive=True)
        # print('files', files)
        return files

    def _get_template_tppi_files(self):
        dirname = str(self._root_dir / self._config.uno_obj_dir)
        pattern = dirname + '/**/*.tppi'
        files = glob.glob(pattern, recursive=True)
        # print('files', files)
        return files

    def _get_py_path(self, tmpl_file) -> Path:
        t_file = Path(tmpl_file)
        p_file = Path(t_file.parent, str(t_file.stem) + '.py')
        return p_file

    def get_module_link_files(self) -> Set[str]:
        dirname = str(self._root_dir / self._config.uno_base_dir)
        # https://stackoverflow.com/questions/20638040/glob-exclude-pattern
        # root module_links.json needs to be remove from listing.
        # it will not need any processing here.
        # using sets and deduct seem the simplist way.
        pattern = dirname + f'/**/{self._config.module_links_file}'
        root_json = Path(dirname, self._config.module_links_file)
        files = set(glob.glob(pattern, recursive=True))
        ex_files = set()
        ex_files.add(str(root_json))
        # deduct sets:
        return files - ex_files

    def camel_to_snake(self, name: str) -> str:
        _name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', _name).lower()

    # region Properties
    @property
    def root_dir(self) -> Path:
        """Gets root_dir value"""
        return self._root_dir
    # endregion Properties

# endregion FilesBase

# region Compile Links


class BaseCompile(FilesBase):
    def __init__(self, args: CompileLinkArgs) -> None:
        super().__init__(config=args.config)
        self._args = args
        self._json_parser_path = Path(self._root_dir, 'parser', 'json_parser')

    def _get_args_module_links(self) -> Path:
        """
        Gets module links file from args.
        If ``args.path`` is a dir then ``module_links.json`` is appended

        Raises:
            Exception: If args.path is not set
            FileNotFoundError: If File not found

        Returns:
            Path: file path object
        """
        if not self._args.path:
            msg = f"{self.__class__.__name__}._get_args_module_links(): Required arg args.path not set"
            logger.error(msg)
            raise Exception(msg)
        p = Path(self.args.path)

        if not p.is_absolute():
            try:
                # might raise FileNotFoundError
                # https://stackoverflow.com/a/44569249/1171746
                p = p.resolve(strict=True)
            except FileNotFoundError:
                msg = f"{self.__class__.__name__}._get_args_module_links(): File not found: {p}"
                logger.error(msg)
                raise FileNotFoundError(msg)

        if p.is_dir():
            p = p / self._config.module_links_file

        if not p.exists():
            msg = f"{self.__class__.__name__}._get_args_module_links(): File not found: {p}"
            logger.error(msg)
            raise FileNotFoundError(msg)
        return p

    @property
    def json_parser_path(self) -> Path:
        """Gets json_parser_path value"""
        return self._json_parser_path

    @property
    def args(self) -> CompileLinkArgs:
        """Gets Args"""
        return self._args


class CompileEnumLinks(BaseCompile):
    def __init__(self, args: CompileLinkArgs) -> None:
        super().__init__(args=args)
        self._do_sub = args.use_sub_process
        if self._do_sub:
            self._processer = str(
                Path(self.json_parser_path, 'enum_parser.py'))
        else:
            self._processer = ''
        if self.args.path:
            self._process_path()
        else:
            self._process_files()

    def _process_path(self) -> None:
        p = self._get_args_module_links()
        file = str(p)
        if self._do_sub:
            self._subprocess(file)
        else:
            self._process_direct(file)

    def _subprocess(self, file: str):
        cmd_str = f"{self._processer} -f {file}"
        cmd = [sys.executable] + cmd_str.split()
        logger.info("CompileEnumLinks: Processing enums in file: %s", file)
        res = subprocess.run(cmd)
        if res.stdout:
            logger.info(res.stdout)
        if res.stderr:
            logger.error(res.stderr)

    def _process_direct(self, file: str):
        logger.info(
            "CompileEnumLinks: Processing interface in file: %s", file)
        parse_enm(write_template=True, write_json=True, json_file=file)

    def _process_files(self):
        link_files = self.get_module_link_files()
        for file in link_files:
            if self._do_sub:
                self._subprocess(file)
            else:
                self._process_direct(file)


class CompileConstLinks(BaseCompile):
    def __init__(self, args: CompileLinkArgs) -> None:
        super().__init__(args=args)
        self._do_sub = args.use_sub_process
        if self._do_sub:
            self._processer = str(
                Path(self.json_parser_path, 'const_parser.py'))
        else:
            self._processer = ''
        if self.args.path:
            self._process_path()
        else:
            self._process_files()

    def _process_path(self) -> None:
        p = self._get_args_module_links()
        file = str(p)
        if self._do_sub:
            self._subprocess(file)
        else:
            self._process_direct(file)

    def _subprocess(self, file: str):
        cmd_str = f"{self._processer} -f {file}"
        cmd = [sys.executable] + cmd_str.split()
        logger.info("CompileConstLinks: Processing enums in file: %s", file)
        res = subprocess.run(cmd)
        if res.stdout:
            logger.info(res.stdout)
        if res.stderr:
            logger.error(res.stderr)

    def _process_direct(self, file: str):
        logger.info(
            "CompileConstLinks: Processing interface in file: %s", file)
        parse_const(write_template=True, write_json=True, json_file=file)

    def _process_files(self):
        link_files = self.get_module_link_files()
        for file in link_files:
            if self._do_sub:
                self._subprocess(file)
            else:
                self._process_direct(file)


class CompileTypeDefLinks(BaseCompile):
    def __init__(self, args: CompileLinkArgs) -> None:
        super().__init__(args=args)
        self._do_sub = args.use_sub_process
        if self._do_sub:
            self._processer = str(
                Path(self.json_parser_path, 'typedef_parser.py'))
        else:
            self._processer = ''
        if self.args.path:
            self._process_path()
        else:
            self._process_files()

    def _process_path(self) -> None:
        p = self._get_args_module_links()
        file = str(p)
        if self._do_sub:
            self._subprocess(file)
        else:
            self._process_direct(file)

    def _subprocess(self, file: str):
        cmd_str = f"{self._processer} -f {file}"
        cmd = [sys.executable] + cmd_str.split()
        logger.info("CompileTypeDefLinks: Processing enums in file: %s", file)
        res = subprocess.run(cmd)
        if res.stdout:
            logger.info(res.stdout)
        if res.stderr:
            logger.error(res.stderr)

    def _process_direct(self, file: str):
        logger.info(
            "CompileTypeDefLinks: Processing interface in file: %s", file)
        parse_typedef(write_template=True, write_json=True, json_file=file)

    def _process_files(self):
        link_files = self.get_module_link_files()
        for file in link_files:
            if self._do_sub:
                self._subprocess(file)
            else:
                self._process_direct(file)


class CompileStructLinks(BaseCompile):
    def __init__(self, args: CompileLinkArgs) -> None:
        super().__init__(args=args)
        self._do_sub = args.use_sub_process
        if self._do_sub:
            self._processer = str(
                Path(self.json_parser_path, 'struct_parser.py'))
        else:
            self._processer = ''
        if self.args.path:
            self._process_path()
        else:
            self._process_files()

    def _process_path(self) -> None:
        p = self._get_args_module_links()
        file = str(p)
        if self._do_sub:
            self._subprocess(file)
        else:
            self._process_direct(file)

    def _subprocess(self, file: str):
        cmd_str = f"{self._processer} -f {file}"
        cmd = [sys.executable] + cmd_str.split()
        logger.info("CompileStructLinks: Processing struct in file: %s", file)
        res = subprocess.run(cmd)
        if res.stdout:
            logger.info(res.stdout)
        if res.stderr:
            logger.error(res.stderr)

    def _process_direct(self, file: str):
        logger.info(
            "CompileStructLinks: Processing interface in file: %s", file)
        parse_struct(write_template=True, write_json=True, json_file=file)

    def _process_files(self):
        link_files = self.get_module_link_files()
        for file in link_files:
            if self._do_sub:
                self._subprocess(file)
            else:
                self._process_direct(file)


class CompileInterfaceLinks(BaseCompile):

    def __init__(self, args: CompileLinkArgs) -> None:
        super().__init__(args=args)
        self._do_sub = args.use_sub_process
        if self._do_sub:
            self._processer = str(
                Path(self.json_parser_path, 'interface_parser.py'))
        else:
            self._processer = ''

        if self.args.path:
            self._process_path()
        else:
            self._process_files()

    def _process_path(self) -> None:
        p = self._get_args_module_links()
        file = str(p)
        if self._do_sub:
            self._subprocess(file)
        else:
            self._process_direct(file)

    def _subprocess(self, file: str):
        cmd_str = f"{self._processer} -f {file}"
        cmd = [sys.executable] + cmd_str.split()
        logger.info(
            "CompileInterfaceLinks: Processing interface in file: %s", file)
        res = subprocess.run(cmd)
        if res.stdout:
            logger.info(res.stdout)
        if res.stderr:
            logger.error(res.stderr)

    def _process_direct(self, file: str):
        logger.info(
            "CompileInterfaceLinks: Processing interface in file: %s", file)
        parse_interface(write_template=True, write_json=True, json_file=file)

    def _process_files(self):
        link_files = self.get_module_link_files()
        for file in link_files:
            if self._do_sub:
                self._subprocess(file)
            else:
                self._process_direct(file)


class CompileSingletonLinks(BaseCompile):

    def __init__(self, args: CompileLinkArgs) -> None:
        super().__init__(args=args)
        self._do_sub = args.use_sub_process
        if self._do_sub:
            self._processer = str(
                Path(self.json_parser_path, 'singleton_parser.py'))
        else:
            self._processer = ''
        if self.args.path:
            self._process_path()
        else:
            self._process_files()

    def _process_path(self) -> None:
        p = self._get_args_module_links()
        file = str(p)
        if self._do_sub:
            self._subprocess(file)
        else:
            self._process_direct(file)

    def _subprocess(self, file: str):
        cmd_str = f"{self._processer} -f {file}"
        cmd = [sys.executable] + cmd_str.split()
        logger.info(
            "CompileSingletonLinks: Processing singleton in file: %s", file)
        res = subprocess.run(cmd)
        if res.stdout:
            logger.info(res.stdout)
        if res.stderr:
            logger.error(res.stderr)

    def _process_direct(self, file: str):
        logger.info(
            "CompileSingletonLinks: Processing singleton in file: %s", file)
        parse_singleton(write_template=True, write_json=True, json_file=file)

    def _process_files(self):
        link_files = self.get_module_link_files()
        for file in link_files:
            if self._do_sub:
                self._subprocess(file)
            else:
                self._process_direct(file)


class CompileServiceLinks(BaseCompile):

    def __init__(self, args: CompileLinkArgs) -> None:
        super().__init__(args=args)
        self._do_sub = args.use_sub_process
        if self._do_sub:
            self._processer = str(
                Path(self.json_parser_path, 'service_parser.py'))
        else:
            self._processer = ''
        if self.args.path:
            self._process_path()
        else:
            self._process_files()

    def _process_path(self) -> None:
        p = self._get_args_module_links()
        file = str(p)
        if self._do_sub:
            self._subprocess(file)
        else:
            self._process_direct(file)

    def _subprocess(self, file: str):
        cmd_str = f"{self._processer} -f {file}"
        cmd = [sys.executable] + cmd_str.split()
        logger.info(
            "CompileServiceLinks: Processing service in file: %s", file)
        res = subprocess.run(cmd)
        if res.stdout:
            logger.info(res.stdout)
        if res.stderr:
            logger.error(res.stderr)

    def _process_direct(self, file: str):
        logger.info(
            "CompileServiceLinks: Processing service in file: %s", file)
        parse_service(write_template=True, write_json=True, json_file=file)

    def _process_files(self):
        link_files = self.get_module_link_files()
        for file in link_files:
            if self._do_sub:
                self._subprocess(file)
            else:
                self._process_direct(file)


class CompileExLinks(BaseCompile):
    def __init__(self, args: CompileLinkArgs) -> None:
        super().__init__(args=args)
        self._do_sub = args.use_sub_process
        if self._do_sub:
            self._processer = str(
                Path(self.json_parser_path, 'exception_parser.py'))
        else:
            self._processer = ''
        if self.args.path:
            self._process_path()
        else:
            self._process_files()

    def _process_path(self) -> None:
        p = self._get_args_module_links()
        file = str(p)
        if self._do_sub:
            self._subprocess(file)
        else:
            self._process_direct(file)

    def _subprocess(self, file: str):
        cmd_str = f"{self._processer} -f {file}"
        cmd = [sys.executable] + cmd_str.split()
        logger.info(
            "CompileExLinks: Processing interface in file: %s", file)
        res = subprocess.run(cmd)
        if res.stdout:
            logger.info(res.stdout)
        if res.stderr:
            logger.error(res.stderr)

    def _process_direct(self, file: str):
        logger.info(
            "CompileExLinks: Processing interface in file: %s", file)
        parse_ex(write_template=True, write_json=True, json_file=file)

    def _process_files(self):
        link_files = self.get_module_link_files()
        for file in link_files:
            if self._do_sub:
                self._subprocess(file)
            else:
                self._process_direct(file)

# endregion Compile Links

# region Touch Files


class TouchFiles(FilesBase):
    def __init__(self, config: AppConfig, **kwargs) -> None:
        super().__init__(config=config)
        self._check_exist: bool = bool(kwargs.get('check_exist', True))
        self._touch_struct: bool = bool(kwargs.get('touch_struct', False))
        self._touch_const: bool = bool(kwargs.get('touch_const', False))
        self._touch_enum: bool = bool(kwargs.get('touch_enum', False))
        self._touch_ex: bool = bool(kwargs.get('touch_ex', False))
        self._touch_typedef: bool = bool(kwargs.get('touch_typedef', False))
        self._touch_py_files: bool = bool(kwargs.get('touch_py_files', False))
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

        logger.info('Touched a total of %d files.', self._touch_count)

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
                name = link.name
                if self._touch_py_files:
                    name += '.py'
                else:
                    name += self._config.template_struct_ext
                t_path = Path(f_path, name)
                if self._check_exist:
                    if not t_path.exists():
                        continue
                t_path.touch(exist_ok=True)
                touched += 1
                logger.debug('Touched Struct file: %s', t_path)

        for file in link_files:
            process(file)
        logger.info('Touched %d Struct files', touched)
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
                name = link.name
                if self._touch_py_files:
                    name += '.py'
                else:
                    name += self._config.template_const_ext
                t_path = Path(f_path, name)
                if self._check_exist:
                    if not t_path.exists():
                        continue
                t_path.touch(exist_ok=True)
                touched += 1
                logger.debug('Touched Const file: %s', t_path)

        for file in link_files:
            process(file)
        logger.info('Touched %d Const files', touched)
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
                name = link.name
                if self._touch_py_files:
                    name += '.py'
                else:
                    name += self._config.template_enum_ext
                t_path = Path(f_path, name)
                if self._check_exist:
                    if not t_path.exists():
                        continue
                t_path.touch(exist_ok=True)
                touched += 1
                logger.debug('Touched Enum file: %s', t_path)

        for file in link_files:
            process(file)
        logger.info('Touched %d Enum files', touched)
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
                name = link.name
                if self._touch_py_files:
                    name += '.py'
                else:
                    name += self._config.template_exception_ext
                t_path = Path(f_path, name)
                if self._check_exist:
                    if not t_path.exists():
                        continue
                t_path.touch(exist_ok=True)
                touched += 1
                logger.debug('Touched Exception file: %s', t_path)

        for file in link_files:
            process(file)
        logger.info('Touched %d Exception files', touched)
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
                name = link.name
                if self._touch_py_files:
                    name += '.py'
                else:
                    name += self._config.template_interface_ext
                t_path = Path(f_path, name)
                if self._check_exist:
                    if not t_path.exists():
                        continue
                t_path.touch(exist_ok=True)
                touched += 1
                logger.debug('Touched Interface file: %s', t_path)

        for file in link_files:
            process(file)
        logger.info('Touched %d Interface files', touched)
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
                name = link.name
                if self._touch_py_files:
                    name += '.py'
                else:
                    name += self._config.template_singleton_ext
                t_path = Path(f_path, name)
                if self._check_exist:
                    if not t_path.exists():
                        continue
                t_path.touch(exist_ok=True)
                touched += 1
                logger.debug('Touched Singleton file: %s', t_path)

        for file in link_files:
            process(file)
        logger.info('Touched %d Singleton files', touched)
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
                name = link.name
                if self._touch_py_files:
                    name += '.py'
                else:
                    name += self._config.template_service_ext
                t_path = Path(f_path, name)
                if self._check_exist:
                    if not t_path.exists():
                        continue
                t_path.touch(exist_ok=True)
                touched += 1
                logger.debug('Touched Service file: %s', t_path)

        for file in link_files:
            process(file)
        logger.info('Touched %d Service files', touched)
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
                name = link.name
                if self._touch_py_files:
                    name += '.py'
                else:
                    name += self._config.template_typedef_ext
                t_path = Path(f_path, name)
                if self._check_exist:
                    if not t_path.exists():
                        continue
                t_path.touch(exist_ok=True)
                touched += 1
                logger.debug('Touched TypeDef file: %s', t_path)

        for file in link_files:
            process(file)
        logger.info('Touched %d TypeDef files', touched)
        self._touch_count += touched

    def _touch_cache_files(self) -> None:
        touched = 0
        t_path = Path(tempfile.gettempdir())
        cache_path = t_path / self._config.cache_dir
        if not cache_path.exists():
            logger.info('Touched %d Cache files', touched)
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
        logger.info('Touched %d Cache files', touched)
        self._touch_count += touched


# endregion Touch Files

# region Make
class Make(FilesBase):
    def __init__(self, config: AppConfig, **kwargs) -> None:
        super().__init__(config=config)
        self._clean = bool(kwargs.get('clean', False))
        self._root_dir = Path(__file__).parent
        self._scratch = self._root_dir / self._config.builld_dir
        self._force_compile = bool(kwargs.get('force_compile', False))
        self._processed_dirs: Set[str] = set()
        self._processes = int(kwargs.get('processes', 4))
        # exclude files that start with _
        pattern = str(self._root_dir.joinpath('template')) + '/[_]*.py'
        self._template_py_files = glob.glob(pattern)
        if os.path.exists(str(self._scratch)):
            if self._clean:
                logger.info('Deleting %s', str(self._scratch))
                shutil.rmtree(str(self._scratch))
        self._mkdirp(self._scratch)
        self._make()

    def _create_sys_links(self, dest: Path):
        # rel = Path('../../template')
        for file in self._template_py_files:
            try:

                p_file = Path(file)
                dst_file = dest / p_file.name

                root_rel = dst_file.relative_to(self._root_dir)
                rel_str = '../' * (len(root_rel.parts) - 1)
                rel = Path(rel_str + 'template')
                logger.debug(
                    "_create_sys_links() rel to template: %s", str(rel))
                rel_file = rel.joinpath(p_file.name)
                # logger.debug("_create_sys_links() file rel to root: %s", str(root_rel))
                # logger.debug("create_sys_links() file rel parts: %s", str(root_rel.parts))
                os.symlink(
                    src=rel_file,
                    dst=dst_file
                )
                msg = f"Created system link: {dst_file} -> {rel_file}"
                logger.info(msg)
            except FileExistsError:
                continue
            except Exception as e:
                logger.error(e)

    def _make(self):
        self._make_tmpl()
        self._make_tppi()

    def _compile_tmpl(self, w_info: WriteInfo):
        logger.debug('Compiling file: %s', w_info.file)
        cmd_str = f"cheetah compile --nobackup {w_info.file}"
        logger.info('Running subprocess: %s', cmd_str)
        p = subprocess.run(
            cmd_str.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        exit_status = p.returncode
        std_out = p.stdout.decode()
        if std_out:
            logger.info("Cheetah output: %s", std_out)
        if exit_status != 0:
            logger.warning("Cheeta error Outuput: %s", p.stderr.decode())

    def _make_tmpl(self):
        files = self._get_template_files()
        c_lst: List[WriteInfo] = []
        for file in files:
            try:
                if not self._is_skip_compile(tmpl_file=file):
                    f_dir = Path(file).parent
                    if not f_dir in self._processed_dirs:
                        self._processed_dirs.add(f_dir)
                        # logger.debug("_make() current dir: %s", f_dir)
                        self._create_sys_links(f_dir)

                    py_file = self._get_py_path(tmpl_file=file)

                    w_info = WriteInfo(
                        file=file,
                        py_file=py_file,
                        scratch_path=self._get_scratch_path(tmpl_file=py_file)
                    )
                    c_lst.append(w_info)
            except Exception as e:
                logger.error(e)
        # run two pools. First to compile. Second to write
        with Pool(processes=self._processes) as pool:
            pool.map(self._compile_tmpl, c_lst)
        with Pool(processes=self._processes) as pool:
            pool.map(self._write_multi, c_lst)

    def _compile_tppi(self, w_info: WriteInfo):
        logger.debug('Compiling file: %s', w_info.file)
        cmd_str = f"cheetah compile --nobackup --iext=.tppi {w_info.file}"
        logger.info('Running subprocess: %s', cmd_str)
        p = subprocess.run(
            cmd_str.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        exit_status = p.returncode
        std_out = p.stdout.decode()
        if std_out:
            logger.info("Cheetah output: %s", std_out)
        if exit_status != 0:
            logger.warning("Cheeta error Outuput: %s", p.stderr.decode())

    def _make_tppi(self):
        files = self._get_template_tppi_files()
        c_lst: List[WriteInfo] = []
        for file in files:
            try:
                if not self._is_skip_compile(tmpl_file=file):
                    f_dir = Path(file).parent
                    if not f_dir in self._processed_dirs:
                        self._processed_dirs.add(f_dir)
                        self._create_sys_links(f_dir)
                    py_file = self._get_py_path(tmpl_file=file)
                    _tmp = Path(file)
                    _file = _tmp.parent
                    _file = _file.joinpath(_tmp.stem + '.pyi')
                    w_info = WriteInfo(
                        file=file,
                        py_file=py_file,
                        scratch_path=self._get_scratch_path(tmpl_file=_file)
                    )
                    c_lst.append(w_info)
            except Exception as e:
                logger.error(e)
        # run two pools. First to compile. Second to write
        with Pool(processes=self._processes) as pool:
            pool.map(self._compile_tppi, c_lst)
        with Pool(processes=self._processes) as pool:
            pool.map(self._write_multi, c_lst)

    def _is_skip_compile(self, tmpl_file) -> bool:
        if self._force_compile:
            return False
        t_file = Path(tmpl_file)
        p_file = Path(t_file.parent, str(t_file.stem) + '.py')
        try:
            fc = CompareFile.compare(file1=t_file, file2=p_file)
            if fc > CompareEnum.Equal:
                logger.debug('Including file: %s', str(t_file))
                return False
            logger.debug('Excluding file: %s', str(t_file))
            return True
        except RuleError:
            logger.debug("Including File due to no py file: %s", str(p_file))
            return False

    def _get_scratch_path(self, tmpl_file) -> Path:

        p_file = Path(tmpl_file)
        ext = p_file.suffix
        p_dir = p_file.parent
        p_rel = p_dir.relative_to(self._root_dir)
        p_scratch_dir = Path(self._scratch, p_rel)
        self._mkdirp(p_scratch_dir)
        p_scratch = Path(
            p_scratch_dir, self.camel_to_snake(str(p_file.stem)) + ext)
        return p_scratch

    def _write_multi(self, w_info: WriteInfo):
        def ensure_init(path: Path):
            init_file = Path(path, '__init__.py')
            if not init_file.exists():
                init_file.touch()
                logger.info('Created File: %s', str(init_file))
        ensure_init(w_info.scratch_path.parent)
        with open(w_info.scratch_path, "w") as outfile:
            subprocess.run([sys.executable, w_info.py_file], stdout=outfile)
            logger.info('Wrote file: %s', str(w_info.scratch_path))


# endregion Make

# region Main
# region    Question Yes No
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    # https://tinyurl.com/yyg38fp2
    # https://tinyurl.com/y2pv2cdh
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write(
                "Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")
# endregion Question Yes No

# region    Main Testing


def _main():
    # ns = 'com.sun.star.form.component.DatabaseTextField'
    # ns = 'com.sun.star.form.component.RichTextControl'
    # ns = 'com.sun.star.form.FormController'
    # ns = 'com.sun.star.form.DataAwareControlModel'
    # ns = 'com.sun.star.text.TextRange'
    url = 'https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XDevice.html'
    sys.argv.extend(['-v', 'url-parse', 'interface', '-j', '-k', '-o', 'scratch/uno_obj', '-u', url])
    main()


def _touch():
    global logger

    if logger is None:
        log_args = {
            "log_file": "debug.log",
            "level": logging.DEBUG
        }
        logger = get_logger(logger_name=Path(__file__).stem, **log_args)
    config = read_config('./config.json')
    t = TouchFiles(config=config)
    t._touch_struct()
# endregion Main Testing

# region Logging


def _log_start_action() -> None:
    if len(sys.argv) > 1:
        logger.info('Executing command: %s', sys.argv[1:])
    else:
        logger.info('Running with no args.')


def _log_end_action() -> None:
    logger.info('Finished!')
# endregion Logging

# region parser
# region    SET ARGS
# region        Create Parsers


def _create_parser(name: str) -> argparse.ArgumentParser:
    return argparse.ArgumentParser(description=name)

# endregion     Create Parsers
# region        Url Parsers


def _args_url_const(parser: argparse.ArgumentParser) -> None:
    url_parser_const.set_cmd_args(parser)

def _args_url_enum(parser: argparse.ArgumentParser) -> None:
    url_parser_enum.set_cmd_args(parser)

def _args_url_exception(parser: argparse.ArgumentParser) -> None:
    url_parser_ex.set_cmd_args(parser)

def _args_url_interface(parser: argparse.ArgumentParser) -> None:
    url_parser_interface.set_cmd_args(parser)

def _args_url_service(parser: argparse.ArgumentParser) -> None:
    url_parser_service.set_cmd_args(parser)

def _args_url_singleton(parser: argparse.ArgumentParser) -> None:
    url_parser_singleton.set_cmd_args(parser)

def _args_url_struct(parser: argparse.ArgumentParser) -> None:
    url_parser_struct.set_cmd_args(parser)

def _args_url_typedef(parser: argparse.ArgumentParser) -> None:
    url_parser_typedef.set_cmd_args(parser)




# endregion     Url Parsers
# region        Compile Links


def _args_links_general(parser: argparse.ArgumentParser, name: str) -> None:
    parser_group = parser.add_mutually_exclusive_group()
    parser_group.add_argument(
        '-a', '--all',
        help=f"Compile all {name} recursivly",
        action='store_true',
        dest='cmd_all',
        default=False
    )
    parser_group.add_argument(
        '-p', '--path',
        help='Compile a specific path',
        action='store',
        dest='path',
        type=str
    )
    parser.add_argument(
        '-u', '--run-as-cmdline',
        help='Run as command line suprocess. Default False',
        action='store_true',
        dest='cmd_line_process',
        default=False
    )


def _args_links_ex(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name='exceptions')


def _args_links_enum(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name='enums')


def _args_links_const(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name='constants')


def _args_links_struct(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name='struct')


def _args_links_interface(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name='interface')


def _args_links_singleton(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name='singleton')


def _args_links_service(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name='service')


def _args_links_typedef(parser: argparse.ArgumentParser) -> None:
    _args_links_general(parser=parser, name='typedef')
# endregion     Compile Links
# region        Touch Parser


def _args_touch(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-s', '--struct',
        help='Touch all struct files',
        action='store_true',
        dest='struct_all',
        default=False
    )
    parser.add_argument(
        '-g', '--singleton',
        help='Touch all singleton files',
        action='store_true',
        dest='singleton_all',
        default=False
    )
    parser.add_argument(
        '-r', '--service',
        help='Touch all service files',
        action='store_true',
        dest='service_all',
        default=False
    )
    parser.add_argument(
        '-c', '--const',
        help='Touch all const files',
        action='store_true',
        dest='const_all',
        default=False
    )
    parser.add_argument(
        '-e', '--enum',
        help='Touch all enum files',
        action='store_true',
        dest='enum_all',
        default=False
    )
    parser.add_argument(
        '-x', '--exception',
        help='Touch all enum files',
        action='store_true',
        dest='ex_all',
        default=False
    )
    parser.add_argument(
        '-i', '--interface',
        help='Touch all interface files',
        action='store_true',
        dest='interface_all',
        default=False
    )
    parser.add_argument(
        '-t', '--typedef',
        help='Touch all interface files',
        action='store_true',
        dest='typedef_all',
        default=False
    )
    parser.add_argument(
        '-p', '--python',
        help='Touch python files instead of template files',
        action='store_true',
        dest='python_files',
        default=False
    )
    parser.add_argument(
        '--cache-files',
        help='Touch cached files. Resets cache file expire times',
        action='store_true',
        dest='cache_files',
        default=False
    )
# endregion     Touch Parser
# region        Module Links Parser


def _args_module_links(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-a', '--all',
        help='Compile moddule_link json files',
        action='store_true',
        dest='mod_links_all',
        default=False
    )
    parser.add_argument(
        '-f', '--json-file',
        help='Optonal json file to parse such as resources/star.json',
        action='store',
        dest='json_file',
        default=None
    )
    parser.add_argument(
        '-r', '--no-recursive',
        help='Run as command line suprocess. Default False',
        action='store_true',
        dest='no_recursive',
        default=False
    )
    parser.add_argument(
        '-x', '--no-cache',
        help='No caching',
        action='store_false',
        dest='cache',
        default=True)
# endregion     Module Links Parser
# region        Make Parser


def _args_make(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-f', '--force-compile',
        help='Force Compile of templates',
        action='store_true',
        dest='force_compile',
        default=False)
    parser.add_argument(
        '-c', '--clean-scratch',
        help='Wipes all files in scratch',
        action='store_true',
        dest='clean_scratch',
        default=False)
    parser.add_argument(
        '-p', '--processes',
        help='Number of Process to us for make.',
        action='store',
        dest='processes',
        type=int,
        default=4)
# endregion     Make Parser
# region        data args


def _args_data_init(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-i', '--init-db',
        help='Initialize database',
        action='store_true',
        dest='init_db',
        default=False
    )


def _args_data_qry(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-u', '--url',
        help='Get url for a full namespace.',
        action='store',
        dest='ns_url',
        default=None
    )


def _args_data_update(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-a', '--write-all',
        help='Write data from json files in database. Update/insert',
        action='store_true',
        dest='write_all',
        default=False
    )


def _args_data_json(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-n', '--name-space',
        help='Genereate Json for a given namespace',
        action='store',
        dest='namespace',
        default=None
    )

# region            Imports


def _args_data_imports(parser: argparse.ArgumentParser) -> None:
    data_group = parser.add_argument_group()
    # data_imports_group_rel = data_imports_group.add_argument_group()
    data_group.add_argument(
        '-n', '--name-space',
        help='Genereate Namespace Data for a given namespace object',
        action='store',
        dest='ns_import_name',
        default=None
    )
    data_group.add_argument(
        '-j', '--json',
        help='Output in json format',
        action='store_true',
        dest='as_json',
        default=False
    )
    data_group.add_argument(
        '-c', '--child',
        help='Process only direct children if namespace',
        action='store_true',
        dest='ns_import_child',
        default=False
    )
    data_group.add_argument(
        '-r', '--as-rel-from',
        help='Get as realitive from import strings',
        action='store_true',
        dest='ns_import_from',
        default=False
    )
    data_group.add_argument(
        '-l', '--as-long',
        help='Get as realitive im',
        action='store_true',
        dest='ns_import_from_long',
        default=False
    )
    exclusive_group = data_group.add_mutually_exclusive_group()
    exclusive_group.add_argument(
        '-t', '--typing',
        help='Only imports that require typing',
        action='store_true',
        dest='import_typing',
        default=False
    )
    exclusive_group.add_argument(
        '-f', '--no-typing',
        help='Only imports that do NOT require typing',
        action='store_true',
        dest='import_no_typing',
        default=False
    )


def _args_data_imports_child(parser: argparse.ArgumentParser) -> None:
    data_group = parser.add_argument_group()
    # data_imports_group_rel = data_imports_group.add_argument_group()
    data_group.add_argument(
        '-n', '--name-space',
        help='Genereate Namespace Data for a given namespace object',
        action='store',
        dest='namespace',
        default=None
    )
    data_group.add_argument(
        '-r', '--as-rel-from',
        help='Get as realitive from import strings',
        action='store_true',
        dest='ns_import_from',
        default=False
    )
    data_group.add_argument(
        '-l', '--as-long',
        help='Get as realitive im',
        action='store_true',
        dest='ns_import_from_long',
        default=False
    )
    data_group.add_argument(
        '-j', '--json',
        help='Output in json format',
        action='store_true',
        dest='as_json',
        default=False
    )


def _args_data_imports_extends_tree(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-n', '--name-space',
        help='Genereate Namespace Data for a given namespace object',
        action='store',
        dest='namespace',
        default=None
    )


def _args_data_imports_extends_flat(parser: argparse.ArgumentParser) -> None:
    data_group = parser.add_mutually_exclusive_group()
    parser.add_argument(
        '-n', '--namespace',
        help='Genereate flat unique namespace data for a given namespace object',
        action='store',
        dest='namespace',
        default=None
    )
    data_group.add_argument(
        '-i', '--flat-imports',
        help='Genereate imports if format of from ... import ... as ...',
        action='store_true',
        dest='ns_from_imports',
        default=False
    )
    data_group.add_argument(
        '-e', '--extends-short',
        help='Generates line of short extends such as: XTextRange, XInterface',
        action='store_true',
        dest='ns_extends_short',
        default=False
    )
    data_group.add_argument(
        '-x', '--extends-long',
        help='Generates line of short extends such as: text_x_text_range_i, uno_x_interface_i',
        action='store_true',
        dest='ns_extends_long',
        default=False
    )
    parser.add_argument(
        '-c', '--child',
        help='Process only direct children if namespace',
        action='store_true',
        dest='ns_child',
        default=False
    )
    parser.add_argument(
        '-j', '--json',
        help='Output in json format',
        action='store_true',
        dest='as_json',
        default=False
    )
# endregion         Imports
# endregion     data args
# region        General Args


def _args_general(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-v', '--verbose',
        help='verbose logging',
        action='store_true',
        dest='verbose',
        default=False)
    parser.add_argument(
        '-L', '--log-file',
        help='Log file to use',
        action='store',
        dest='log_file',
        type=str,
        default=None)
# endregion     General Args
# endregion SET ARGS

# region ARGS COMMANDS

# region    Args Helpers


def _get_compile_args(args: argparse.Namespace, config: AppConfig) -> CompileLinkArgs:
    path = getattr(args, 'path', None)
    cmd_line_process = getattr(args, 'cmd_line_process', True)
    c_args = CompileLinkArgs(
        config=config,
        path=path,
        use_sub_process=cmd_line_process
    )
    return c_args
# endregion     Args Helpers
# region    Make


def _args_action_make(args: argparse.Namespace, config: AppConfig) -> None:
    _log_start_action()
    try:
        _ = Make(config=config, force_compile=args.force_compile,
                 clean=args.clean_scratch, processes=args.processes)
    except Exception as e:
        logger.error(e)
    _log_end_action()
# endregion Make
# region    Compile Links Command


def _args_action_compile_links(args: argparse.Namespace, compiler: Type[BaseCompile], config: AppConfig) -> None:
    _log_start_action()
    c_args = _get_compile_args(args=args, config=config)
    if args.cmd_all or args.args.path:
        compiler(args=c_args)
    _log_end_action()


def _args_action_links_ex(args: argparse.Namespace, config: AppConfig) -> None:
    _args_action_compile_links(args, CompileExLinks, config)


def _args_action_links_enum(args: argparse.Namespace, config: AppConfig) -> None:
    _args_action_compile_links(args, CompileEnumLinks, config)


def _args_action_links_const(args: argparse.Namespace, config: AppConfig) -> None:
    _args_action_compile_links(args, CompileConstLinks, config)


def _args_action_links_struct(args: argparse.Namespace, config: AppConfig) -> None:
    _args_action_compile_links(args, CompileStructLinks, config)


def _args_action_links_interface(args: argparse.Namespace, config: AppConfig) -> None:
    _args_action_compile_links(args, CompileInterfaceLinks, config)


def _args_action_links_singleton(args: argparse.Namespace, config: AppConfig) -> None:
    _args_action_compile_links(args, CompileSingletonLinks, config)


def _args_action_links_service(args: argparse.Namespace, config: AppConfig) -> None:
    _args_action_compile_links(args, CompileServiceLinks, config)


def _args_action_links_typedef(args: argparse.Namespace, config: AppConfig) -> None:
    _args_action_compile_links(args, CompileTypeDefLinks, config)
    _log_start_action()


def _args_process_compile_cmd_data(args: argparse.Namespace, config: AppConfig) -> None:
    if args.command_data == 'ex':
        _args_action_links_ex(args=args, config=config)
    elif args.command_data == 'enum':
        _args_action_links_enum(args=args, config=config)
    elif args.command_data == 'const':
        _args_action_links_const(args=args, config=config)
    elif args.command_data == 'struct':
        _args_action_links_struct(args=args, config=config)
    elif args.command_data == 'interface':
        _args_action_links_interface(args=args, config=config)
    elif args.command_data == 'singleton':
        _args_action_links_singleton(args=args, config=config)
    elif args.command_data == 'service':
        _args_action_links_service(args=args, config=config)
    elif args.command_data == 'typedef':
        _args_action_links_typedef(args=args, config=config)
# endregion Compile Links Command
# region    Touch


def _args_action_touch(args: argparse.Namespace, config: AppConfig) -> None:
    _log_start_action()
    TouchFiles(
        config=config,
        touch_struct=args.struct_all,
        touch_const=args.const_all,
        touch_enum=args.enum_all,
        touch_ex=args.ex_all,
        touch_interface=args.interface_all,
        touch_typedef=args.typedef_all,
        touch_singleton=args.singleton_all,
        touch_service=args.service_all,
        touch_py_files=args.python_files,
        touch_cache_files=args.cache_files
    )
    _log_end_action()
# endregion Touch
# region    Module Links


def _args_action_module_links(args: argparse.Namespace, config: AppConfig) -> None:
    _log_start_action()
    if args.mod_links_all:
        if not query_yes_no(f"Are you sure you want to rebuild all {config.module_links_file} files?", 'no'):
            return
        linkproc.parse(
            json_file=args.json_file,
            recursive=not args.no_recursive,
            cache=args.cache,
            write_json=True,

        )
    _log_end_action()
# endregion Module Links
# region    data Command
# region        Init


def _args_action_db_init(args: argparse.Namespace, config: AppConfig) -> None:
    dbc = db_manager.DatabaseControler(
        config=config,
        init_db=args.init_db
    )
    if args.init_db:
        if not query_yes_no(f"Are you sure you want initialize the database '{config.db_mod_info}'?", 'no'):
            return
    dbc.results()
# endregion     Init
# region        Update


def _args_action_db_update(args: argparse.Namespace, config: AppConfig) -> None:
    mlc = db_manager.ModuleLinksControler(
        config=config,
        write_all=args.write_all
    )
    mcc = db_manager.ComponentControler(
        config=config,
        write_all=args.write_all
    )
    if args.write_all or args.update_all:
        if not query_yes_no(f"Are you sure you want to read all json files and write data in database?", 'no'):
            return
    _ = mlc.results()
    _ = mcc.results()
# endregion     Update
# region        Namespace


def _args_action_db_extends_tree(args: argparse.Namespace, config: AppConfig) -> None:
    qc = db_manager.NamespaceControler(
        config=config,
        ns_name=args.namespace
    )
    qc_result = qc.results()
    if qc_result:
        print(qc_result)


def _args_action_db_extends_flat(args: argparse.Namespace, config: AppConfig) -> None:
    if args.namespace:
        if args.ns_from_imports:
            qc = db_manager.NamespaceControler(
                config=config,
                ns_flat_frm=args.namespace,
                b_child=args.ns_child,
                b_json=args.as_json
            )
        elif args.ns_extends_short:
            qc = db_manager.NamespaceControler(
                config=config,
                extends_short=args.namespace,
                b_child=args.ns_child,
                b_json=args.as_json
            )
        elif args.ns_extends_long:
            qc = db_manager.NamespaceControler(
                config=config,
                extends_long=args.namespace,
                b_child=args.ns_child,
                b_json=args.as_json
            )
        else:
            qc = db_manager.NamespaceControler(
                config=config,
                ns_flat=args.namespace,
                b_child=args.ns_child,
                b_json=args.as_json
            )
        qc_result = qc.results()
        if qc_result:
            print(qc_result)


def _args_action_db_qry(args: argparse.Namespace, config: AppConfig) -> None:
    qc = db_manager.NamespaceControler(
        config=config,
        ns_link=args.ns_url
    )
    qc_result = qc.results()
    if qc_result:
        print(qc_result)


def _args_action_db_imports(args: argparse.Namespace, config: AppConfig) -> None:
    require_typing = None
    if args.import_typing:
        require_typing = True
    elif args.import_no_typing:
        require_typing = False
    qc = db_manager.NamespaceControler(
        config=config,
        ns_import=args.ns_import_name,
        b_child=args.ns_import_child,
        b_typing=require_typing,
        b_from=args.ns_import_from,
        b_from_long=args.ns_import_from_long,
        b_json=args.as_json
    )
    qc_result = qc.results()
    if qc_result:
        print(qc_result)


def _args_action_db_imports_typing_child(args: argparse.Namespace, config: AppConfig) -> None:
    qc = db_manager.NamespaceControler(
        config=config,
        ns_import_typing_child=args.namespace,
        b_from=args.ns_import_from,
        b_from_long=args.ns_import_from_long,
        b_json=args.as_json
    )
    qc_result = qc.results()
    if qc_result:
        print(qc_result)
# endregion     Namespace
# region        Json


def _args_action_db_json(args: argparse.Namespace, config: AppConfig) -> None:
    qc = json_controler.JsonController(
        config=config,
        namespace=args.namespace
    )
    qc_result = qc.results()
    if qc_result:
        print(qc_result)
# endregion     Json


def _args_process_data_cmd_data(args: argparse.Namespace, config: AppConfig) -> None:
    if args.command_data == 'db-init':
        _args_action_db_init(args=args, config=config)
    elif args.command_data == 'db-update':
        _args_action_db_update(args=args, config=config)
    elif args.command_data == 'db-extends-tree':
        _args_action_db_extends_tree(args=args, config=config)
    elif args.command_data == 'db-extends-flat':
        _args_action_db_extends_flat(args=args, config=config)
    elif args.command_data == 'db-qry':
        _args_action_db_qry(args=args, config=config)
    elif args.command_data == 'db-imports':
        _args_action_db_imports(args=args, config=config)
    elif args.command_data == 'db-imports-typing-child':
        _args_action_db_imports_typing_child(args=args, config=config)
    elif args.command_data == 'db-json':
        _args_action_db_json(args=args, config=config)

# endregion data Command
# region    Url Parsers

def _args_action_url_const(args: argparse.Namespace) -> None:
    d_args = url_parser_const.get_kwargs_from_args(args)
    url_parser_const.parse(**d_args)

def _args_action_url_enum(args: argparse.Namespace) -> None:
    d_args = url_parser_enum.get_kwargs_from_args(args)
    url_parser_enum.parse(**d_args)

def _args_action_url_exception(args: argparse.Namespace) -> None:
    d_args = url_parser_ex.get_kwargs_from_args(args)
    url_parser_ex.parse(**d_args)

def _args_action_url_interface(args: argparse.Namespace) -> None:
    d_args = url_parser_interface.get_kwargs_from_args(args)
    url_parser_interface.parse(**d_args)


def _args_action_url_service(args: argparse.Namespace) -> None:
    d_args = url_parser_service.get_kwargs_from_args(args)
    url_parser_service.parse(**d_args)


def _args_action_url_singleton(args: argparse.Namespace) -> None:
    d_args = url_parser_singleton.get_kwargs_from_args(args)
    url_parser_singleton.parse(**d_args)

def _args_action_url_struct(args: argparse.Namespace) -> None:
    d_args = url_parser_struct.get_kwargs_from_args(args)
    url_parser_struct.parse(**d_args)

def _args_action_url_typedef(args: argparse.Namespace) -> None:
    d_args = url_parser_typedef.get_kwargs_from_args(args)
    url_parser_typedef.parse(**d_args)

def _args_process_url_parser_cmd_data(args: argparse.Namespace) -> None:
    if args.command_data == 'const':
        _args_action_url_const(args=args)
    elif args.command_data == 'enum':
        _args_action_url_enum(args=args)
    elif args.command_data == 'exception':
        _args_action_url_exception(args=args)
    elif args.command_data == 'interface':
        _args_action_url_interface(args=args)
    elif args.command_data == 'service':
        _args_action_url_service(args=args)
    elif args.command_data == 'singleton':
        _args_action_url_singleton(args=args)
    elif args.command_data == 'struct':
        _args_action_url_struct(args=args)
    elif args.command_data == 'typedef':
        _args_action_url_typedef(args=args)
# endregion Url Parsers


def _args_process_cmd(args: argparse.Namespace, config: AppConfig) -> None:
    if args.command == 'make':
        _args_action_make(args=args, config=config)
    elif args.command == 'exception':
        _args_action_links_ex(args=args)
    elif args.command == 'enum':
        _args_action_links_enum(args=args)
    elif args.command == 'const':
        _args_action_links_const(args=args)
    elif args.command == 'struct':
        _args_action_links_struct(args=args)
    elif args.command == 'interface':
        _args_action_links_interface(args=args)
    elif args.command == 'singleton':
        _args_action_links_singleton(args=args)
    elif args.command == 'service':
        _args_action_links_service(args=args)
    elif args.command == 'typedef':
        _args_action_links_typedef(args=args)
    elif args.command == 'touch':
        _args_action_touch(args=args, config=config)
    elif args.command == 'mod-links':
        _args_action_module_links(args=args, config=config)
    elif args.command == 'data':
        _args_process_data_cmd_data(args=args, config=config)
    elif args.command == 'compile':
        _args_process_compile_cmd_data(args=args, config=config)
    elif args.command == 'url-parse':
        _args_process_url_parser_cmd_data(args=args)
# endregion ARGS COMMANDS
# endregion parser


def main():
    global logger
    # region Config
    config = read_config('./config.json')
    os.environ['config_cache_dir'] = config.cache_dir
    os.environ['config_cache_duration'] = str(config.cache_duration)
    os.environ['project_root'] = str(Path(__file__).parent)
    os.environ['config_resource_dir'] = config.resource_dir
    os.environ['config_db_mod_info'] = config.db_mod_info
    # endregion Config

    # region create parsers
    parser = _create_parser('main')
    subparser = parser.add_subparsers(dest='command')
    make_parser = subparser.add_parser(name='make')

    compile_subparser = subparser.add_parser(name='compile')
    compile = compile_subparser.add_subparsers(dest='command_data')
    links_const_parser = compile.add_parser(name='const')
    links_enum_parser = compile.add_parser(name='enum')
    links_ex_parser = compile.add_parser(name='exception')
    links_interface_parser = compile.add_parser(name='interface')
    links_service_parser = compile.add_parser(name='service')
    links_singleton_parser = compile.add_parser(name='singleton')
    links_struct_parser = compile.add_parser(name='struct')
    links_typedef_parser = compile.add_parser(name='typedef')

    url_parser_subparser = subparser.add_parser(name='url-parse')
    url_parser = url_parser_subparser.add_subparsers(dest='command_data')
    url_const = url_parser.add_parser(name='const')
    url_enum = url_parser.add_parser(name='enum')
    url_exception = url_parser.add_parser(name='exception')
    url_interface = url_parser.add_parser(name='interface')
    url_service = url_parser.add_parser(name='service')
    url_singleton = url_parser.add_parser(name='singleton')
    url_struct = url_parser.add_parser(name='struct')
    url_typedef = url_parser.add_parser(name='typedef')

    touch = subparser.add_parser(name='touch')
    mod_links = subparser.add_parser(name='mod-links')

    data_subparser = subparser.add_parser(name='data')
    data = data_subparser.add_subparsers(dest='command_data')
    data_update = data.add_parser(name='db-update')
    data_init = data.add_parser(name='db-init')
    data_extends_flat = data.add_parser(name='db-extends-flat')
    data_extends_tree = data.add_parser(name='db-extends-tree')
    data_imports = data.add_parser(name='db-imports')
    data_imports_typing_child = data.add_parser(name='db-imports-typing-child')
    data_qry = data.add_parser(name='db-qry')
    data_json = data.add_parser(name='db-json')
    # endregion create parsers

    # region Set Args

    # region compile links args
    _args_links_const(parser=links_const_parser)
    _args_links_enum(parser=links_enum_parser)
    _args_links_ex(parser=links_ex_parser)
    _args_links_interface(parser=links_interface_parser)
    _args_links_service(parser=links_service_parser)
    _args_links_singleton(parser=links_singleton_parser)
    _args_links_struct(parser=links_struct_parser)
    _args_links_typedef(parser=links_typedef_parser)
    # endregion compile links args

    # region url parser
    _args_url_const(parser=url_const)
    _args_url_enum(parser=url_enum)
    _args_url_exception(parser=url_exception)
    _args_url_interface(parser=url_interface)
    _args_url_service(parser=url_service)
    _args_url_singleton(parser=url_singleton)
    _args_url_struct(parser=url_struct)
    _args_url_typedef(parser=url_typedef)
    # endregion url parser

    # region Other Args
    _args_general(parser=parser)
    _args_touch(parser=touch)
    _args_module_links(parser=mod_links)
    _args_make(parser=make_parser)
    # endregion Other Args

    # region data args
    _args_data_init(parser=data_init)
    _args_data_qry(parser=data_qry)
    _args_data_update(parser=data_update)
    _args_data_json(parser=data_json)
    _args_data_imports(parser=data_imports)
    _args_data_imports_child(parser=data_imports_typing_child)
    _args_data_imports_extends_tree(parser=data_extends_tree)
    _args_data_imports_extends_flat(parser=data_extends_flat)
    # endregion data args
    # endregion Set Args

    # region Read Args
    args = parser.parse_args()
    # endregion Read Args

    # region logger
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        else:
            log_args['log_file'] = 'app.log'
        if args.verbose:
            log_args['level'] = logging.DEBUG
        logger = get_logger(logger_name=Path(__file__).stem, **log_args)
    # endregion logger

    _args_process_cmd(args=args, config=config)


if __name__ == '__main__':
    # _touch()
    main()

# endregion Main
