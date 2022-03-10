# coding: utf-8
from dataclasses import dataclass


@dataclass
class WriterArgs:
    sort: bool
    dynamic_struct: bool
    include_desc: bool
