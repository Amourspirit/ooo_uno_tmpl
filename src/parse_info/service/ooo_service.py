# coding: utf-8
from ..shared.ooo_class import OooClass
from ..shared.args.parser_args import ParserArgs
from ..shared.args.writer_args import WriterArgs
from ..shared.data.ooo_data import Data


class OooService(OooClass):
    parser_args: ParserArgs
    writer_args: WriterArgs
    data: Data
