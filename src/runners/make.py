# coding: utf-8
# region Imports
import os
import sys
import shutil
import glob
import logging
import subprocess
from multiprocessing import Pool
from typing import List, Set
from kwhelp.exceptions import RuleError
from pathlib import Path
from . import compare as comp
from . import data_class as d_cls
from .file_base import FilesBase
from ..cfg.config import AppConfig
from ..utilities import util
# endregion Imports

# region Make


class Make(FilesBase):
    def __init__(self, config: AppConfig, log: logging.Logger, ** kwargs) -> None:
        super().__init__(config=config)
        self._log = log
        self._clean = bool(kwargs.get('clean', False))
        self._root_dir = Path(util.get_root())
        self._build = self._root_dir / self._config.builld_dir
        self._force_compile = bool(kwargs.get('force_compile', False))
        self._processed_dirs: Set[str] = set()
        self._processes = int(kwargs.get('processes', 4))
        # exclude files that start with _
        pattern = str(self._root_dir.joinpath('template')) + '/[_]*.py'
        self._template_py_files = glob.glob(pattern)
        if os.path.exists(str(self._build)):
            if self._clean:
                self._log.info('Deleting %s', str(self._build))
                shutil.rmtree(str(self._build))
        self._mkdirp(self._build)
        self._ensure_init(self._build)
        self._make()
        

    def _ensure_init(self, path: Path):
        init_file = Path(path, '__init__.py')
        if not init_file.exists():
            init_file.touch()
            self._log.info('Created File: %s', str(init_file))

    def _create_sys_links(self, dest: Path):
        # rel = Path('../../template')
        for file in self._template_py_files:
            try:

                p_file = Path(file)
                dst_file = dest / p_file.name

                root_rel = dst_file.relative_to(self._root_dir)
                rel_str = '../' * (len(root_rel.parts) - 1)
                rel = Path(rel_str + 'template')
                self._log.debug(
                    "_create_sys_links() rel to template: %s", str(rel))
                rel_file = rel.joinpath(p_file.name)
                # self._log.debug("_create_sys_links() file rel to root: %s", str(root_rel))
                # self._log.debug("create_sys_links() file rel parts: %s", str(root_rel.parts))
                os.symlink(
                    src=rel_file,
                    dst=dst_file
                )
                msg = f"Created system link: {dst_file} -> {rel_file}"
                self._log.info(msg)
            except FileExistsError:
                continue
            except Exception as e:
                self._log.error(e)

    def _make(self):
        self._make_tmpl()
        self._make_dyn()
        self._make_tppi()

    # region TMPL
    def _compile_tmpl(self, w_info: d_cls.WriteInfo):
        self._log.debug('Compiling file: %s', w_info.file)
        cmd_str = f"cheetah compile --nobackup {w_info.file}"
        self._log.info('Running subprocess: %s', cmd_str)
        p = subprocess.run(
            cmd_str.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        exit_status = p.returncode
        std_out = p.stdout.decode()
        if std_out:
            self._log.info("Cheetah output: %s", std_out)
        if exit_status != 0:
            self._log.warning("Cheeta error Outuput: %s", p.stderr.decode())

    def _make_tmpl(self):
        files = self._get_template_files()
        c_lst: List[d_cls.WriteInfo] = []
        for file in files:
            try:
                if not self._is_skip_compile(tmpl_file=file):
                    f_dir = Path(file).parent
                    if not f_dir in self._processed_dirs:
                        self._processed_dirs.add(f_dir)
                        # self._log.debug("_make() current dir: %s", f_dir)
                        self._create_sys_links(f_dir)

                    py_file = self._get_py_path(tmpl_file=file)

                    w_info = d_cls.WriteInfo(
                        file=file,
                        py_file=py_file,
                        scratch_path=self._get_scratch_path(tmpl_file=py_file)
                    )
                    c_lst.append(w_info)
            except Exception as e:
                self._log.error(e)
        if len(c_lst) == 0:
            return
        lo_dir = self._build / self._config.uno_obj_dir
        self._ensure_init(lo_dir)
        # run two pools. First to compile. Second to write
        with Pool(processes=self._processes) as pool:
            pool.map(self._compile_tmpl, c_lst)
        with Pool(processes=self._processes) as pool:
            pool.map(self._write_multi, c_lst)
    # endregion TMPL

    # region DYN

    def _compile_dyn(self, w_info: d_cls.WriteInfo):
        self._log.debug('Compiling file: %s', w_info.file)
        cmd_str = f"cheetah compile --nobackup --iext={self.config.template_dyn_ext} --oext={self.config.template_dyn_py_ext} {w_info.file}"
        self._log.info('Running subprocess: %s', cmd_str)
        p = subprocess.run(
            cmd_str.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        exit_status = p.returncode
        std_out = p.stdout.decode()
        if std_out:
            self._log.info("Cheetah output: %s", std_out)
        if exit_status != 0:
            self._log.warning("Cheeta error Outuput: %s", p.stderr.decode())

    def _make_dyn(self):
        files = self._get_template_dyn_files()
        c_lst: List[d_cls.WriteInfo] = []
        for file in files:
            try:
                if not self._is_skip_compile(tmpl_file=file, ext=self.config.template_dyn_py_ext):
                    f_dir = Path(file).parent
                    if not f_dir in self._processed_dirs:
                        self._processed_dirs.add(f_dir)
                        # self._log.debug("_make() current dir: %s", f_dir)
                        self._create_sys_links(f_dir)

                    py_file = self._get_py_dyn_path(tmpl_file=file)

                    w_info = d_cls.WriteInfo(
                        file=file,
                        py_file=py_file,
                        scratch_path=self._get_dyn_write_path(
                            tmpl_file=py_file)
                    )
                    c_lst.append(w_info)
            except Exception as e:
                self._log.error(e)
        if len(c_lst) == 0:
            return
        dyn_dir = self._build / self._config.dyn_dir
        self._ensure_init(dyn_dir)
        # run two pools. First to compile. Second to write
        with Pool(processes=self._processes) as pool:
            pool.map(self._compile_dyn, c_lst)
        with Pool(processes=self._processes) as pool:
            pool.map(self._write_multi, c_lst)
    # endregion DYN

    # region TPPI

    def _compile_tppi(self, w_info: d_cls.WriteInfo):
        self._log.debug('Compiling file: %s', w_info.file)
        cmd_str = f"cheetah compile --nobackup --iext=.tppi {w_info.file}"
        self._log.info('Running subprocess: %s', cmd_str)
        p = subprocess.run(
            cmd_str.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        exit_status = p.returncode
        std_out = p.stdout.decode()
        if std_out:
            self._log.info("Cheetah output: %s", std_out)
        if exit_status != 0:
            self._log.warning("Cheeta error Outuput: %s", p.stderr.decode())

    def _make_tppi(self):
        files = self._get_template_tppi_files()
        c_lst: List[d_cls.WriteInfo] = []
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
                    w_info = d_cls.WriteInfo(
                        file=file,
                        py_file=py_file,
                        scratch_path=self._get_scratch_path(tmpl_file=_file)
                    )
                    c_lst.append(w_info)
            except Exception as e:
                self._log.error(e)
        if len(c_lst) == 0:
            return
        # run two pools. First to compile. Second to write
        with Pool(processes=self._processes) as pool:
            pool.map(self._compile_tppi, c_lst)
        with Pool(processes=self._processes) as pool:
            pool.map(self._write_multi, c_lst)

    # endregion TPPI

    def _is_skip_compile(self, tmpl_file, ext: str = '.py') -> bool:
        if self._force_compile:
            return False
        t_file = Path(tmpl_file)
        p_file = Path(t_file.parent, str(t_file.stem) + ext)
        try:
            fc = comp.CompareFile.compare(file1=t_file, file2=p_file)
            if fc > comp.CompareEnum.Equal:
                self._log.debug('Including file: %s', str(t_file))
                return False
            self._log.debug('Excluding file: %s', str(t_file))
            return True
        except RuleError:
            self._log.debug(
                "Including File due to no py file: %s", str(p_file))
            return False

    def _get_scratch_path(self, tmpl_file) -> Path:
        # reading uno/...['.py' or '.pyi'] file
        # setting write path to build/uno/...
        p_file = Path(tmpl_file)
        ext = p_file.suffix
        p_dir = p_file.parent
        p_rel = p_dir.relative_to(self._root_dir)
        p_scratch_dir = Path(self._build, p_rel)
        self._mkdirp(p_scratch_dir)
        p_scratch = Path(
            p_scratch_dir, self.camel_to_snake(str(p_file.stem)) + ext)
        return p_scratch

    def _get_dyn_write_path(self, tmpl_file) -> Path:
        # reading uno/...['.py' or '.pyi'] file
        # setting write path to build/dyn/...

        p_file = Path(tmpl_file)
        ext = '.py'
        p_dir = p_file.parent
        p_rel = p_dir.relative_to(self._root_dir)
        # need to drop uno_dir form start of rel
        # expecing parts to be tuple starting with uno
        # when there is a root it is at the start of the tuple
        # https://tinyurl.com/lfl7fwd
        parts = list(p_rel.parts)
        parts[0] = self._config.dyn_dir  # replace uno with dyn
        # build up to build/dyn/somepath/somefile.py
        p_scratch_dir = Path(self._build, *parts)
        self._mkdirp(p_scratch_dir)
        p_scratch = Path(
            p_scratch_dir, self.camel_to_snake(str(p_file.stem)) + ext)
        return p_scratch

    def _write_multi(self, w_info: d_cls.WriteInfo):
        def ensure_init(path: Path):
            init_file = Path(path, '__init__.py')
            if not init_file.exists():
                init_file.touch()
                self._log.info('Created File: %s', str(init_file))
        ensure_init(w_info.scratch_path.parent)
        with open(w_info.scratch_path, "w") as outfile:
            subprocess.run([sys.executable, w_info.py_file], stdout=outfile)
            self._log.info('Wrote file: %s', str(w_info.scratch_path))


# endregion Make
