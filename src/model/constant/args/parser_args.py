# coding: utf-8
from dataclasses import dataclass


@dataclass
class ParserArgs:
    sort: bool
    remove_parent_inherited: bool
