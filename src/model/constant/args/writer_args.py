# coding: utf-8
from dataclasses import dataclass


@dataclass
class WriterArgs:
    hex: bool
    flags: bool
    include_desc: bool
