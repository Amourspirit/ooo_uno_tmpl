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
from data_manage import db_manager
from multiprocessing import Pool, TimeoutError
from typing import List, Optional, Set
from kwhelp import rules
from kwhelp.decorator import DecFuncEnum, RuleCheckAll
from kwhelp.exceptions import RuleError
from enum import IntEnum
from pathlib import Path
from logger.log_handle import get_logger
from parser import __version__, JSON_ID
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
        parse_enm('t', 'j', f=file)

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
        parse_const('t', 'j', f=file)

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
            self._processer = str(Path(self.json_parser_path, 'typedef_parser.py'))
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

    def _subprocess(self, file:str):
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
        parse_typedef('t', 'j', f=file)

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
            self._processer = str(Path(self.json_parser_path, 'struct_parser.py'))
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
        parse_struct('t', 'j', f=file)

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
            self._processer = str(Path(self.json_parser_path, 'interface_parser.py'))
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
        parse_interface('t', 'j', f=file)

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
        parse_singleton('t', 'j', f=file)

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
        parse_service('t', 'j', f=file)

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
        parse_ex('t', 'j', f=file)

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
    def __init__(self,config: AppConfig, **kwargs) -> None:
        super().__init__(config=config)
        self._check_exist: bool = bool(kwargs.get('check_exist', True))
        self._touch_struct: bool = bool(kwargs.get('touch_struct', False))
        self._touch_const: bool = bool(kwargs.get('touch_const', False))
        self._touch_enum: bool = bool(kwargs.get('touch_enum', False))
        self._touch_ex: bool = bool(kwargs.get('touch_ex', False))
        self._touch_typedef: bool = bool(kwargs.get('touch_typedef', False))
        self._touch_py_files: bool = bool(kwargs.get('touch_py_files', False))
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
        pattern = str(self._root_dir.joinpath('template'))  + '/[_]*.py'
        self._template_py_files=glob.glob(pattern)
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
                rel_str = '../' * (len(root_rel.parts) -1)
                rel = Path(rel_str + 'template')
                logger.debug("_create_sys_links() rel to template: %s", str(rel))
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

    def _compile_tmpl(self, w_info:WriteInfo):
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
                        file = file,
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
    ns = 'com.sun.star.form.component.DatabaseTextField'
    # ns = 'com.sun.star.form.DataAwareControlModel'
    # ns = 'com.sun.star.text.TextRange'
    sys.argv.extend(['-v', '--log-file', 'debug.log', 'data', 'qry',
                    '-f', ns])
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

    def get_compile_args(args:argparse.Namespace) -> CompileLinkArgs:
        path = getattr(args, 'path', None)
        cmd_line_process = getattr(args, 'cmd_line_process', True)
        c_args = CompileLinkArgs(
            config=config,
            path=path,
            use_sub_process=cmd_line_process
            )
        return c_args

    # region Script Start Action
    def log_start_action() -> None:
        if len(sys.argv) > 1:
            logger.info('Executing command: %s', sys.argv[1:])
        else:
            logger.info('Running with no args.')
    # endregion Script Start Action

    # region Script End Action
    def log_end_action() -> None:
        logger.info('Finished!')
    # endregion Script End Action
    
    # region create parsers
    parser = argparse.ArgumentParser(description='main')
    subparser = parser.add_subparsers(dest='command')
    ex_parser = subparser.add_parser(name='ex')
    enum_parser = subparser.add_parser(name='enum')
    const_parser = subparser.add_parser(name='const')
    struct_parser = subparser.add_parser(name='struct')
    interface_parser = subparser.add_parser(name='interface')
    singleton_parser = subparser.add_parser(name='singleton')
    service_parser = subparser.add_parser(name='service')
    typedef_parser = subparser.add_parser(name='typedef')
    touch = subparser.add_parser(name='touch')
    mod_links = subparser.add_parser(name='mod_links')

    data_subparser = subparser.add_parser(name='data')
    data = data_subparser.add_subparsers(dest='command_data')
    # data = data_subparser.add_parser(name='data')
    data_module = data.add_parser(name='module')
    data_init = data.add_parser(name='init')
    data_component = data.add_parser(name='component')
    data_qry = data.add_parser(name='qry')
    # endregion create parsers

    # region ex args
    ex_parser_file_group = ex_parser.add_mutually_exclusive_group()
    ex_parser_file_group.add_argument(
        '-a', '--all',
        help='Compile all exceptions recursivly',
        action='store_true',
        dest='ex_all',
        default=False
    )
    ex_parser_file_group.add_argument(
        '-p', '--path',
        help='Compile a specific path',
        action='store',
        dest='path',
        type=str
    )
    ex_parser.add_argument(
        '-u', '--run-as-cmdline',
        help='Run as command line suprocess. Default False',
        action='store_true',
        dest='cmd_line_process',
        default=False
    )
    # endregion ex args

    # region enum args
    enum_parser_file_group = enum_parser.add_mutually_exclusive_group()
    enum_parser_file_group.add_argument(
        '-a', '--all',
        help='Compile all enums recursivly',
        action='store_true',
        dest='enum_all',
        default=False
    )
    enum_parser_file_group.add_argument(
        '-p', '--path',
        help='Compile a specific path',
        action='store',
        dest='path',
        type=str
    )
    enum_parser.add_argument(
        '-u', '--run-as-cmdline',
        help='Run as command line suprocess. Default False',
        action='store_true',
        dest='cmd_line_process',
        default=False
    )
    # endregion enum args

    # region const args
    const_parser_file_group = const_parser.add_mutually_exclusive_group()
    const_parser_file_group.add_argument(
        '-a', '--all',
        help='Compile all constants recursivly',
        action='store_true',
        dest='const_all',
        default=False
    )
    const_parser_file_group.add_argument(
        '-p', '--path',
        help='Compile a specific path',
        action='store',
        dest='path',
        type=str
    )
    const_parser.add_argument(
        '-u', '--run-as-cmdline',
        help='Run as command line suprocess. Default False',
        action='store_true',
        dest='cmd_line_process',
        default=False
    )
    # endregion const args

    # region struct args
    struct_parser_file_group = struct_parser.add_mutually_exclusive_group()
    struct_parser_file_group.add_argument(
        '-a', '--all',
        help='Compile all struct recursivly',
        action='store_true',
        dest='struct_all',
        default=False
    )
    struct_parser_file_group.add_argument(
        '-p', '--path',
        help='Compile a specific path',
        action='store',
        dest='path',
        type=str
    )
    struct_parser.add_argument(
        '-u', '--run-as-cmdline',
        help='Run as command line suprocess. Default False',
        action='store_true',
        dest='cmd_line_process',
        default=False
    )
    # endregion struct args

    # region interface args
    interface_parser_file_group = interface_parser.add_mutually_exclusive_group()
    interface_parser_file_group.add_argument(
        '-a', '--all',
        help='Compile all interface recursivly',
        action='store_true',
        dest='interface_all',
        default=False
    )
    interface_parser_file_group.add_argument(
        '-p', '--path',
        help='Compile a specific path',
        action='store',
        dest='path',
        type=str
    )
    interface_parser.add_argument(
        '-u', '--run-as-cmdline',
        help='Run as command line suprocess. Default False',
        action='store_true',
        dest='cmd_line_process',
        default=False
    )

    # endregion interface args
    
    # region singleton args
    singleton_parser_file_group = singleton_parser.add_mutually_exclusive_group()
    singleton_parser_file_group.add_argument(
        '-a', '--all',
        help='Compile all singleton recursivly',
        action='store_true',
        dest='singleton_all',
        default=False
    )
    singleton_parser_file_group.add_argument(
        '-p', '--path',
        help='Compile a specific path',
        action='store',
        dest='path',
        type=str
    )
    singleton_parser.add_argument(
        '-u', '--run-as-cmdline',
        help='Run as command line suprocess. Default False',
        action='store_true',
        dest='cmd_line_process',
        default=False
    )

    # endregion service args

    # region service args
    service_parser_file_group = service_parser.add_mutually_exclusive_group()
    service_parser_file_group.add_argument(
        '-a', '--all',
        help='Compile all service recursivly',
        action='store_true',
        dest='service_all',
        default=False
    )
    service_parser_file_group.add_argument(
        '-p', '--path',
        help='Compile a specific path',
        action='store',
        dest='path',
        type=str
    )
    service_parser.add_argument(
        '-u', '--run-as-cmdline',
        help='Run as command line suprocess. Default False',
        action='store_true',
        dest='cmd_line_process',
        default=False
    )

    # endregion service args

    # region typedef args
    typedef_parser_file_group = typedef_parser.add_mutually_exclusive_group()
    typedef_parser_file_group.add_argument(
        '-a', '--all',
        help='Compile all struct recursivly',
        action='store_true',
        dest='typedef_all',
        default=False
    )
    typedef_parser_file_group.add_argument(
        '-p', '--path',
        help='Compile a specific path',
        action='store',
        dest='path',
        type=str
    )
    typedef_parser.add_argument(
        '-u', '--run-as-cmdline',
        help='Run as command line suprocess. Default False',
        action='store_true',
        dest='cmd_line_process',
        default=False
    )
    # endregion typedef args

    # region Touch
    touch.add_argument(
        '-s', '--struct',
        help='Touch all struct files',
        action='store_true',
        dest='struct_all',
        default=False
    )
    touch.add_argument(
        '-g', '--singleton',
        help='Touch all singleton files',
        action='store_true',
        dest='singleton_all',
        default=False
    )
    touch.add_argument(
        '-r', '--service',
        help='Touch all service files',
        action='store_true',
        dest='service_all',
        default=False
    )
    touch.add_argument(
        '-c', '--const',
        help='Touch all const files',
        action='store_true',
        dest='const_all',
        default=False
    )
    touch.add_argument(
        '-e', '--enum',
        help='Touch all enum files',
        action='store_true',
        dest='enum_all',
        default=False
    )
    touch.add_argument(
        '-x', '--exception',
        help='Touch all enum files',
        action='store_true',
        dest='ex_all',
        default=False
    )
    touch.add_argument(
        '-i', '--interface',
        help='Touch all interface files',
        action='store_true',
        dest='interface_all',
        default=False
    )
    touch.add_argument(
        '-t', '--typedef',
        help='Touch all interface files',
        action='store_true',
        dest='typedef_all',
        default=False
    )
    touch.add_argument(
        '-p', '--python',
        help='Touch python files instead of template files',
        action='store_true',
        dest='python_files',
        default=False
    )
    # endregion Touch

    # region Module Links
    mod_links.add_argument(
        '-a', '--all',
        help='Compile moddule_link json files',
        action='store_true',
        dest='mod_links_all',
        default=False
    )
    mod_links.add_argument(
        '-f', '--json-file',
        help='Optonal json file to parse such as resources/star.json',
        action='store',
        dest='json_file',
        default=None
    )
    mod_links.add_argument(
        '-r', '--no-recursive',
        help='Run as command line suprocess. Default False',
        action='store_true',
        dest='no_recursive',
        default=False
    )
    mod_links.add_argument(
        '-x', '--no-cache',
        help='No caching',
        action='store_false',
        dest='cache',
        default=True)


    # endregion Module Links

    # region make args
    make_parser = subparser.add_parser(name='make')
    make_parser.add_argument(
        '-f', '--force-compile',
        help='Force Compile of templates',
        action='store_true',
        dest='force_compile',
        default=False)
    make_parser.add_argument(
        '-c', '--clean-scratch',
        help='Wipes all files in scratch',
        action='store_true',
        dest='clean_scratch',
        default=False)
    make_parser.add_argument(
        '-p', '--processes',
        help='Number of Process to us for make.',
        action='store',
        dest='processes',
        type=int,
        default=4)
    # endregion make args

    # region data args
    # region    init
    data_init.add_argument(
        '-i', '--init-db',
        help='Initialize database',
        action='store_true',
        dest='init_db',
        default=False
    )
    # endregion init
    # region    module
    data_module_group = data_module.add_mutually_exclusive_group()
    data_module_group.add_argument(
        '-a', '--write-all',
        help=f"Write all {config.module_links_file} files to database",
        action='store_true',
        dest='write_all',
        default=False
    )
    data_module_group.add_argument(
        '-u', '--udate-all',
        help=f"Overwrite all {config.module_links_file} files to database",
        action='store_true',
        dest='update_all',
        default=False
    )
    data_module_group.add_argument(
        '-c', '--get-count',
        help='Get count of namesapce data',
        action='store_true',
        dest='count_all',
        default=False
    )
    
    # endregion module
    # region    component
    data_component_group = data_component.add_mutually_exclusive_group()
    data_component_group.add_argument(
        '-a', '--write-all',
        help='Write all component json files data to database',
        action='store_true',
        dest='write_all',
        default=False
    )
    data_component_group.add_argument(
        '-u', '--udate-all',
        help='Overwrite all component json files data in database',
        action='store_true',
        dest='update_all',
        default=False
    )
    # endregion component
    # region    qry
    data_qry_group = data_qry.add_mutually_exclusive_group()
    data_qry_group.add_argument(
        '-n', '--name-space',
        help='Genereate Namespace Data for a given namespace object',
        action='store',
        dest='ns_name',
        default=None
    )
    data_qry_group.add_argument(
        '-f', '--flat-name-space',
        help='Genereate flat unique namespace data for a given namespace object',
        action='store',
        dest='ns_flat',
        default=None
    )
    # endregion qry
    # endregion data args

    # region general args
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
    # endregion general args

    # region Read Args
    args = parser.parse_args()
    # endregion Read Args

    # region logger
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        if args.verbose:
            log_args['level'] = logging.DEBUG
        logger = get_logger(logger_name=Path(__file__).stem, **log_args)
    # endregion logger

    # region Make Command
    if args.command == 'make':
        log_start_action()
        try:
            _ = Make(config=config, force_compile=args.force_compile,
                        clean=args.clean_scratch, processes=args.processes)
        except Exception as e:
            logger.error(e)
        log_end_action()
    # endregion Make Command

    # region Compile Links Command
    if args.command == 'ex':
        log_start_action()
        c_args = get_compile_args(args=args)
        if args.ex_all:
            CompileExLinks(args=c_args)
        log_end_action()
    if args.command == 'enum':
        log_start_action()
        c_args = get_compile_args(args=args)
        if args.enum_all:
            CompileEnumLinks(args=c_args)
        log_end_action()
    if args.command == 'const':
        log_start_action()
        c_args = get_compile_args(args=args)
        if args.const_all:
            CompileConstLinks(args=c_args)
        log_end_action()
    if args.command == 'struct':
        log_start_action()
        c_args = get_compile_args(args=args)
        if args.struct_all:
            CompileStructLinks(args=c_args)
        log_end_action()
    if args.command == 'interface':
        log_start_action()
        c_args = get_compile_args(args=args)
        if args.interface_all:
            CompileInterfaceLinks(args=c_args)
        elif args.path:
            CompileInterfaceLinks(args=c_args)
        log_end_action()
    if args.command == 'singleton':
        log_start_action()
        c_args = get_compile_args(args=args)
        if args.singleton_all:
            CompileSingletonLinks(args=c_args)
        log_end_action()
    if args.command == 'service':
        log_start_action()
        c_args = get_compile_args(args=args)
        if args.service_all:
            c_args = get_compile_args(args=args)
            CompileServiceLinks(args=c_args)
        log_end_action()
    if args.command == 'typedef':
        log_start_action()
        c_args = get_compile_args(args=args)
        if args.typedef_all:
            CompileTypeDefLinks(args=c_args)
        log_end_action()
    # endregion Compile Links Command

    # region Touch Command
    if args.command == 'touch':
        log_start_action()
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
            touch_py_files=args.python_files
        )
        log_end_action()
    # endregion Touch Command

    # region Module Links Command
    if args.command == 'mod_links':
        log_start_action()
        if args.mod_links_all:
            if not query_yes_no(f"Are you sure you want to rebuild all {config.module_links_file} files?", 'no'):
                return
            linkproc.parse(
                json_file=args.json_file,
                recursive=not args.no_recursive,
                cache=args.cache,
                write_json=True,
                
            )
        log_end_action()
    # endregion Module Links Command

    # region data Command
    
    if args.command == 'data':
        # region Init
        if args.command_data == 'init':
            dbc = db_manager.DatabaseControler(
                config=config,
                init_db=args.init_db
            )
            if args.init_db:
                if not query_yes_no(f"Are you sure you want initialize the database '{config.db_mod_info}'?", 'no'):
                    return
            dbc.results()
        # endregion Init
        # region Module
        if args.command_data == 'module':
            mlc = db_manager.ModuleLinksControler(
                config=config,
                write_all=args.write_all,
                update_all=args.update_all,
                count_all=args.count_all
                )
            if args.write_all or args.update_all:
                if not query_yes_no(f"Are you sure you want to read all {config.module_links_file} files and write to database?", 'no'):
                    return
            mlc_result = mlc.results()
            if mlc_result:
                print(mlc_result)
        # endregion Module
        # region Component
        if args.command_data == 'component':
            mlc = db_manager.ComponentControler(
                config=config,
                write_all=args.write_all,
                update_all=args.update_all
            )
            if args.write_all or args.update_all:
                if not query_yes_no(f"Are you sure you want to read all component json files and write to database?", 'no'):
                    return
            mlc_result = mlc.results()
            if mlc_result:
                print(mlc_result)
        # endregion Component
        # region Namespace
        if args.command_data == 'qry':
            qc = db_manager.QueryControler(
                config=config,
                ns_name=args.ns_name,
                ns_flat=args.ns_flat
            )
            qc_result = qc.results()
            if qc_result:
                print(qc_result)
        # endregion Namespace
    # endregion data Command

    

if __name__ == '__main__':
    # _touch()
    _main()

# endregion Main
