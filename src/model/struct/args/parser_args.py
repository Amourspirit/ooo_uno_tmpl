# coding: utf-8
from dataclasses import dataclass


@dataclass
class ParserArgs:
    sort: bool
    long_names: bool
    remove_parent_inherited: bool