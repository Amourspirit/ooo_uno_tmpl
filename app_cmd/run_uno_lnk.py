#!/usr/bin/env python
# coding: utf-8
"""
Creates system links for uno and uno_helper

see: docs/setup_env.rst
"""
import os
import sys
from pathlib import Path


def main():
    ver = f"{sys.version_info[0]}.{sys.version_info[1]}"
    p_uno = Path('/usr/lib/python3/dist-packages/uno.py')
    p_uno_helper = Path('/usr/lib/python3/dist-packages/unohelper.py')
    if p_uno.exists():
        dest = Path(sys.base_exec_prefix,
                    f"lib/python{ver}/site-packages/uno.py")
        try:
            os.symlink(
                src=p_uno,
                dst=dest)
            print(f"Created system link: {p_uno} -> {dest}")
        except FileExistsError:
            print(f"File Exist: {dest}")

    if p_uno_helper.exists():
        dest = Path(sys.base_exec_prefix,
                    f"lib/python{ver}/site-packages/unohelper.py")
        try:
            os.symlink(
                src=p_uno_helper,
                dst=dest)
            print(f"Created system link: {p_uno_helper} -> {dest}")
        except FileExistsError:
            print(f"File Exist: {dest}")

if __name__ == '__main__':
    main()