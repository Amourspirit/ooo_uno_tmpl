# coding: utf-8
from typing import List
import os
import sys
import glob
from pathlib import Path

sys.path.append(os.path.realpath('.'))


def get_modules() -> List[str]:
    app_root = Path(__file__).parent.parent.parent
    dirname = app_root / 'build' / 'cssdyn'
    pattern = str(dirname) + f'/**/__init__.py'
    files = glob.glob(pattern, recursive=True)
    mods = []
    for file in files:
        pfile = Path(file)
        rel = pfile.relative_to(app_root)
        ns = str(rel.parent).replace(os.sep, '.') + '.' + rel.stem
        mods.append(ns)
    return mods
    

MODULES = get_modules()


def pytest_generate_tests(metafunc):
    if metafunc.function.__name__ == "test_imp_mod" and "module_data" in dir(metafunc.module):
        metafunc.parametrize(
            "module_data", metafunc.module.module_data.__wrapped__(
                MODULES))
