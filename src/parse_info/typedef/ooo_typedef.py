# coding: utf-8
from ..shared.ooo_class import OooClass
from .args.parser_args import ParserArgs
from .args.writer_args import WriterArgs
from .data import Data


class OooTypedef(OooClass):
    parser_args: ParserArgs
    writer_args: WriterArgs
    data: Data
