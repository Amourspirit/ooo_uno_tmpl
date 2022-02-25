# coding: utf-8
import sys
import subprocess
from pathlib import Path
from .base_compile import BaseCompile
from ..data_class import CompileLinkArgs
from ...parser.json_parser import enum_parser


class CompileEnumLinks(BaseCompile):
    def __init__(self, args: CompileLinkArgs) -> None:
        super().__init__(args=args)
        self._do_sub = args.use_sub_process
        if self._do_sub:
            self._processer = str(Path(enum_parser.__file__))
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
        if self.args.out_dir:
            cmd_str += f" --out {self.args.out_dir}"
        cmd = [sys.executable] + cmd_str.split()
        self.args.log.info(
            "CompileEnumLinks: Processing enums in file: %s", file)
        res = subprocess.run(cmd)
        if res.stdout:
            self.args.log.info(res.stdout)
        if res.stderr:
            self.args.log.error(res.stderr)

    def _process_direct(self, file: str):
        self.args.log.info(
            "CompileEnumLinks: Processing interface in file: %s", file)
        if self.args.out_dir:
            write_path = self.config.data_dir
        else:
            write_path = None
        enum_parser.parse(
            write_template=self.args.write_template,
            write_json=self.args.write_json,
            json_file=file,
            write_path=write_path,
            log_file='enum.log'
        )

    def _process_files(self):
        link_files = self.get_module_link_files(dir_name=self.args.out_dir)
        for file in link_files:
            if self._do_sub:
                self._subprocess(file)
            else:
                self._process_direct(file)
