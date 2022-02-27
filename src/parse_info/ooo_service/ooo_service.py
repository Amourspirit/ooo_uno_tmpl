# coding: utf-8
from ..shared.ooo_class import OooClass
from .parser_args import ParserArgs
from .writer_args import WriterArgs
from .data.ooo_data import Data


class OooService(OooClass):
    parser_args: ParserArgs
    writer_args: WriterArgs
    data: Data
