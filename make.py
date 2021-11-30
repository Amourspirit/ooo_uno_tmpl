#!/usr/bin/env python
import os
import sys
from kwhelp import rules
from kwhelp.decorator import DecFuncEnum, RuleCheckAll
from kwhelp.exceptions import RuleError
from enum import IntEnum
from pathlib import Path
import shutil
import glob
import subprocess
import argparse
import re
camel_to_snake_pattern = re.compile(r'(?<!^)(?=[A-Z])')

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


class Make:
    def __init__(self, **kwargs) -> None:
        self._clean = bool(kwargs.get('clean', False))
        self._root_dir = Path(os.path.dirname(__file__))
        self._scratch = self._root_dir / 'scratch'
        self._force_compile = bool(kwargs.get('force_compile', False))
        if os.path.exists(str(self._scratch)):
            if self._clean:
                shutil.rmtree(str(self._scratch))
        self._mkdirp(self._scratch)
        self._make()

    def _make(self):
        files = self._get_template_files()
        for file in files:
            try:
                if not self._is_skip_compile(tmpl_file=file):
                    self._compile(tmpl_file=file)
                py_file = self._get_py_path(tmpl_file=file)
                self._write(py_file)
            except Exception:
                print(Exception)

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

    def _is_skip_compile(self, tmpl_file) -> bool:
        if self._force_compile:
            return False
        t_file = Path(tmpl_file)
        p_file = Path(t_file.parent, str(t_file.stem) + '.py')
        try:
            fc = CompareFile.compare(file1=t_file, file2=p_file)
            if fc > CompareEnum.Equal:
                return False
            return True
        except RuleError:
            return False

    def _compile(self, tmpl_file):
        cmd_str = f"cheetah compile --nobackup {tmpl_file}"
        res = subprocess.run(cmd_str.split())
        if res.stdout:
            print(res.stdout)
        if res.stderr:
            print(res.stderr)

    def _get_scratch_path(self, tmpl_file) -> Path:
        p_file = Path(tmpl_file)
        p_dir = p_file.parent
        p_rel = p_dir.relative_to(self._root_dir)
        p_scratch_dir = Path(self._scratch, p_rel)
        self._mkdirp(p_scratch_dir)
        p_scratch = Path(
            p_scratch_dir, self._camel_to_snake(str(p_file.stem)) + '.py')
        return p_scratch

    def _get_py_path(self, tmpl_file) -> Path:
        t_file = Path(tmpl_file)
        p_file = Path(t_file.parent, str(t_file.stem) + '.py')
        return p_file

    def _camel_to_snake(self, name: str)-> str:
        _name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', _name).lower()

    def _write(self, py_file):
        f = Path(py_file)
        p_out = self._get_scratch_path(tmpl_file=py_file)
        cmd_str = f"python {py_file}"
        with open(p_out, "w") as outfile:
            subprocess.run([sys.executable, py_file], stdout=outfile)


def main():
    parser = argparse.ArgumentParser(description='make')
    parser.add_argument('-f', '--force-compile',
                        help='Force Compile of templates', type=bool, default=False)
    parser.add_argument(
        '-c', '--clean-scratch', help='Wipes all files in scratch', type=bool, default=False)
    args = parser.parse_args()
    # print("clean", args.clean_scratch)
    # /home/paul/Documents/Projects/Python/Cheeta3/ooo_uno/uno_obj/style/ParagraphAdjust.tmpl
    make = Make(force_compile=args.force_compile, clean=args.clean_scratch)
    print('Finished!')
    # f = '/home/paul/Documents/Projects/Python/Cheeta3/ooo_uno/uno_obj/style/ParagraphAdjust.py'
    # make._write(tmpl_file=f)


if __name__ == '__main__':
    main()
