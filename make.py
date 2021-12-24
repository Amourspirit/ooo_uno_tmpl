#!/usr/bin/env python
import logging
import os
import sys
import re
import shutil
import glob
import argparse
import subprocess
from typing import List, Set
from kwhelp import rules
from kwhelp.decorator import DecFuncEnum, RuleCheckAll
from kwhelp.exceptions import RuleError
from enum import IntEnum
from pathlib import Path
from logger.log_handle import get_logger
from parser import __version__, JSON_ID
from config import AppConfig, read_config
from parser.json_parser.interface_parser import parse as parse_interface
from parser.json_parser.struct_parser import parse as parse_struct
from parser.json_parser.enum_parser import parse as parse_enm
logger = None

os.environ['project_root'] = str(Path(__file__).parent)
# logger/log_handle.py

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

class BaseCompile:
    def __init__(self, config:AppConfig) -> None:
        self._root_dir = Path(__file__).parent
        self._json_parser_path = Path(self._root_dir, 'parser', 'json_parser')
        self._config = config
    
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
    
    @property
    def root_dir(self) -> Path:
        """Gets root_dir value"""
        return self._root_dir
    
    @property
    def json_parser_path(self) -> Path:
        """Gets json_parser_path value"""
        return self._json_parser_path


class CompileEnumLinks(BaseCompile):
    def __init__(self, config: AppConfig, use_subprocess: bool) -> None:
        super().__init__(config=config)
        self._do_sub = use_subprocess
        if self._do_sub:
            self._processer = str(Path(self.json_parser_path, 'enum_parser.py'))
        else:
            self._processer = ''
        self._process_files()

    def _subprocess(self, file:str):
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


class CompileStructLinks(BaseCompile):
    def __init__(self, config: AppConfig, use_subprocess: bool) -> None:
        super().__init__(config=config)
        self._do_sub = use_subprocess
        if self._do_sub:
            self._processer = str(Path(self.json_parser_path, 'struct_parser.py'))
        else:
            self._processer = ''
        self._process_files()

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
            "CompileInterfaceLinks: Processing interface in file: %s", file)
        parse_struct('t', 'j', f=file)

    def _process_files(self):
        link_files = self.get_module_link_files()
        for file in link_files:
            if self._do_sub:
                self._subprocess(file)
            else:
                self._process_direct(file)

class CompileInterfaceLinks(BaseCompile):

    def __init__(self, config: AppConfig, use_subprocess: bool) -> None:
        super().__init__(config=config)
        self._do_sub = use_subprocess
        if self._do_sub:
            self._processer = str(Path(self.json_parser_path, 'interface_parser.py'))
        else:
            self._processer = ''
        self._process_files()

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


class Make:
    def __init__(self, **kwargs) -> None:
        self._clean = bool(kwargs.get('clean', False))
        self._root_dir = Path(__file__).parent
        self._scratch = self._root_dir / 'scratch'
        self._force_compile = bool(kwargs.get('force_compile', False))
        self._processed_dirs: Set[str] = set()
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
    
    def _make_tmpl(self):
        files = self._get_template_files()
        for file in files:
            try:
                if not self._is_skip_compile(tmpl_file=file):
                    f_dir = Path(file).parent
                    if not f_dir in self._processed_dirs:
                        self._processed_dirs.add(f_dir)
                        # logger.debug("_make() current dir: %s", f_dir)
                        self._create_sys_links(f_dir)
                    logger.debug('Compiling file: %s', file)
                    self._compile(tmpl_file=file)
                    
                    py_file = self._get_py_path(tmpl_file=file)
                    self._write(py_file)
            except Exception as e:
                logger.error(e)
    
    def _make_tppi(self):
        files = self._get_template_tppi_files()
        for file in files:
            try:
                if not self._is_skip_compile(tmpl_file=file):
                    f_dir = Path(file).parent
                    if not f_dir in self._processed_dirs:
                        self._processed_dirs.add(f_dir)
                        # logger.debug("_make() current dir: %s", f_dir)
                        self._create_sys_links(f_dir)
                    logger.debug('Compiling file: %s', file)
                    self._compile_tppi(tmpl_file=file)
                    
                    py_file = self._get_py_path(tmpl_file=file)
                    self._write(py_file, '.pyi')
            except Exception as e:
                logger.error(e)

    def _mkdirp(self, dest_dir):
        # Python ≥ 3.5
        if isinstance(dest_dir, Path):
            dest_dir.mkdir(parents=True, exist_ok=True)
        else:
            Path(dest_dir).mkdir(parents=True, exist_ok=True)

    def _get_template_files(self):
        dirname = str(self._root_dir / 'uno_obj')
        # https://stackoverflow.com/questions/20638040/glob-exclude-pattern
        # exclude files that start with _
        pattern = dirname + '/**/[!_]*.tmpl'
        files = glob.glob(pattern, recursive=True)
        # print('files', files)
        return files
    
    def _get_template_tppi_files(self):
        dirname = str(self._root_dir / 'uno_obj')
        pattern = dirname + '/**/*.tppi'
        files = glob.glob(pattern, recursive=True)
        # print('files', files)
        return files

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

    def _compile(self, tmpl_file):
        cmd_str = f"cheetah compile --nobackup {tmpl_file}"
        logger.info('Running subprocess: %s', cmd_str)
        p = subprocess.run(cmd_str.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        exit_status = p.returncode
        std_out = p.stdout.decode()
        if std_out:
            logger.info("Cheetah output: %s", std_out)
        if exit_status != 0:
            logger.warning("Cheeta error Outuput: %s", p.stderr.decode())
    
    def _compile_tppi(self, tmpl_file):
        cmd_str = f"cheetah compile --nobackup --iext=.tppi {tmpl_file}"
        logger.info('Running subprocess: %s', cmd_str)
        res = subprocess.run(cmd_str.split())
        if res.stdout:
            logger.info(res.stdout)
        if res.stderr:
            logger.error(res.stderr)

    def _get_scratch_path(self, tmpl_file) -> Path:
        
        p_file = Path(tmpl_file)
        ext = p_file.suffix
        p_dir = p_file.parent
        p_rel = p_dir.relative_to(self._root_dir)
        p_scratch_dir = Path(self._scratch, p_rel)
        self._mkdirp(p_scratch_dir)
        p_scratch = Path(
            p_scratch_dir, self._camel_to_snake(str(p_file.stem)) + ext)
        return p_scratch

    def _get_py_path(self, tmpl_file) -> Path:
        t_file = Path(tmpl_file)
        p_file = Path(t_file.parent, str(t_file.stem) + '.py')
        return p_file

    def _camel_to_snake(self, name: str) -> str:
        _name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', _name).lower()

    def _ensure_init(self, path:Path):
        init_file = Path(path, '__init__.py')
        if not init_file.exists():
            init_file.touch()
            logger.info('Created File: %s', str(init_file))

    def _write(self, py_file, ext:str =''):
        _file = py_file
        if ext:
            _tmp = Path(_file)
            _file = _tmp.parent
            _file = _file.joinpath(_tmp.stem + ext)
            
        p_out = self._get_scratch_path(tmpl_file=_file)
        self._ensure_init(p_out.parent)
        with open(p_out, "w") as outfile:
            subprocess.run([sys.executable, py_file], stdout=outfile)
            logger.info('Wrote file: %s', str(p_out))


def _main():
    sys.argv.extend(['-v', '--log-file', 'make.log'])
    main()

def main():
    global logger
    config = read_config('./config.json')
    parser = argparse.ArgumentParser(description='make')
    subparser = parser.add_subparsers(dest='command')
    enum_parser = subparser.add_parser(name='enum')
    struct_parser = subparser.add_parser(name='struct')
    interface_parser = subparser.add_parser(name='interface')
    # region enum args
    enum_parser.add_argument(
        '-a', '--all',
        help='Compile all enums recursivly',
        action='store_true',
        dest='enum_all',
        default=False
    )
    # endregion enum args

    # region struct args
    struct_parser.add_argument(
        '-a', '--all',
        help='Compile all struct recursivly',
        action='store_true',
        dest='struct_all',
        default=False
    )
    # endregion struct args

    # region interface args
    interface_parser.add_argument(
        '-a', '--all',
        help='Compile all interface recursivly',
        action='store_true',
        dest='interface_all',
        default=False
    )

    # endregion interface args

    make_parser = subparser.add_parser(name='make')
    # region make args
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
    # region make args
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
    args = parser.parse_args()
    if logger is None:
        log_args = {}
        if args.log_file:
            log_args['log_file'] = args.log_file
        if args.verbose:
            log_args['level'] = logging.DEBUG
        logger = get_logger(logger_name=Path(__file__).stem, **log_args)
    if len(sys.argv) > 1:
        logger.info('Executing command: %s', sys.argv[1:])
    else:
        logger.info('Running with no args.')
    if args.command == 'make':
        try:
            make = Make(force_compile=args.force_compile, clean=args.clean_scratch)
        except Exception as e:
            logger.error(e)
    if args.command == 'enum':
        if args.enum_all:
            CompileEnumLinks(config=config, use_subprocess=False)
    if args.command == 'struct':
        if args.struct_all:
            CompileStructLinks(config=config, use_subprocess=False)
    if args.command == 'interface':
        if args.interface_all:
            CompileInterfaceLinks(config=config, use_subprocess=False)
    logger.info('Finished!')


if __name__ == '__main__':
    main()
