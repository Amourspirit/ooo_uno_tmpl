# coding: utf-8
# region Imports
import os
import __main__
import re
import glob
from typing import Optional, Set
from pathlib import Path
from config import AppConfig
# endregion Imports

# region FilesBase


class FilesBase:
    def __init__(self, config: AppConfig) -> None:
        self._config: AppConfig = config
        root_dir = os.environ.get('project_root', None)
        if root_dir:
            self._root_dir = Path(root_dir)
        else:
            self._root_dir = Path(__main__.__file__).parent

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
    
    def _get_template_dyn_files(self):
        dirname = str(self._root_dir / self._config.uno_obj_dir)
        pattern = dirname + '/**/*.dyn'
        files = glob.glob(pattern, recursive=True)
        # print('files', files)
        return files

    def _get_py_path(self, tmpl_file) -> Path:
        t_file = Path(tmpl_file)
        p_file = Path(t_file.parent, str(t_file.stem) + '.py')
        return p_file
    
    def _get_py_dyn_path(self, tmpl_file) -> Path:
        t_file = Path(tmpl_file)
        p_file = Path(t_file.parent, str(t_file.stem) + '.dynpy')
        return p_file

    def get_module_link_files(self, dir_name: Optional[str] = None) -> Set[str]:
        if dir_name:
            dirname = str(self._root_dir / dir_name)
        else:
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

    @property
    def config(self) -> AppConfig:
        """Gets config value"""
        return self._config
    # endregion Properties

# endregion FilesBase
