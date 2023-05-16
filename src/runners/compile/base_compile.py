# coding: utf-8
from ..file_base import FilesBase
from ..data_class import CompileLinkArgs
from pathlib import Path


class BaseCompile(FilesBase):
    def __init__(self, args: CompileLinkArgs) -> None:
        super().__init__(config=args.config)
        self._args = args
        self._ensure_build_init()

    def _ensure_build_init(self) -> None:
        # ensure build/uno_obj/__init__.py exist
        p = Path(self._config.build_dir, self._config.uno_obj_dir)
        if not p.is_absolute():
            p = self.root_dir.joinpath(p)
        self._mkdirp(p)
        init_file = Path(p, '__init__.py')
        try:
            init_file.touch(exist_ok=False)
        except FileExistsError:
            # file already exist so just ignore
            pass
    
    def _get_absolute_path(self, rel_path: Path) -> Path:
        # might raise FileNotFoundError
        # https://stackoverflow.com/a/44569249/1171746
        if rel_path.is_absolute():
            return rel_path
        p = self.root_dir.joinpath(rel_path)
        if not p.is_absolute():
            p = p.resolve(strict=True)
        return p

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
            self._args.log.error(msg)
            raise Exception(msg)
        p = Path(self.args.path)

        if not p.is_absolute():
            try:
                p = self._get_absolute_path(rel_path=p)
            except FileNotFoundError:
                msg = f"{self.__class__.__name__}._get_args_module_links(): File not found: {p}"
                self._args.log.error(msg)
                raise FileNotFoundError(msg)

        if p.is_dir():
            p = p / self._config.module_links_file

        if not p.exists():
            msg = f"{self.__class__.__name__}._get_args_module_links(): File not found: {p}"
            self._args.log.error(msg)
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
