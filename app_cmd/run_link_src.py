#!/usr/bin/env python
# coding: utf-8
"""
Creates system links for uno and uno_helper

see: docs/setup_env.rst
"""
import os
import sys
from pathlib import Path
import argparse


def set_cmd_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        '-a', '--add',
        help='create link from src ...site_packages/oootmp',
        action='store_true',
        dest='add_link',
        default=True)
    parser.add_argument(
        '-r', '--remove',
        help='Remove link from src to ...site_packages/oootmp',
        action='store_true',
        dest='remove_link',
        default=False)

def create():
    root = Path(__file__).parent.parent
    ver = f"{sys.version_info[0]}.{sys.version_info[1]}"
    p_src = Path(root, 'src')
    if p_src.exists():
        pkg_dir = Path(sys.base_exec_prefix,
                       f"lib/python{ver}/site-packages")
        dest = Path(pkg_dir, 'oootmpl')
        dest_rel = pkg_dir.relative_to(root)
        # print("dest_rel:", dest_rel)
        src_rel = dest.relative_to(root)
        src_rel = ''
        for _ in dest_rel.parts:
            src_rel += '..' + os.sep
        src_rel += 'src'
        # print('src_rel', src_rel)
        try:
            os.symlink(
                src=src_rel,
                dst=dest,
                target_is_directory=True
                )
            print(f"Created system link: {p_src} -> {dest}")
        except FileExistsError:
            print(f"File Exist: {dest}")

def remove():
    ver = f"{sys.version_info[0]}.{sys.version_info[1]}"
    pkg_dir = Path(sys.base_exec_prefix,
                   f"lib/python{ver}/site-packages/oootmpl")
    if not pkg_dir.exists():
        print("Does not exsit", pkg_dir)
        return
    try:
        # pkg_dir.rmdir()
        pkg_dir.unlink(missing_ok=False)
        print("removed", pkg_dir)
    except FileNotFoundError:
        print("Does not exist:", pkg_dir)
    except Exception as e:
        print(e)

def main():
    parser = argparse.ArgumentParser(description='star')
    set_cmd_args(parser)
    args = parser.parse_args()
    
    if args.remove_link:
        remove()
    else:
        create()

if __name__ == '__main__':
    main()
