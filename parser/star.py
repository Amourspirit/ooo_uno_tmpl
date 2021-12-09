#!/usr/bin/env python
import os
import sys
import argparse
from typing import Dict, List
from bs4.element import ResultSet, Tag
from kwhelp.decorator import DecFuncEnum, RuleCheckAllKw, RequireArgs, TypeCheckKw
from kwhelp import rules
from collections import namedtuple
from base import TagsStrObj, Util, WriteBase, ParserBase, SoupObj, UrlObj, BlockObj
from pathlib import Path
import textwrap
import xerox  # requires xclip - sudo apt-get install xclip
from logger.log_handle import get_logger
from parser import __version__, JSON_ID

logger = get_logger(Path(__file__).stem)

# body > div.contents > table > tbody > tr.memitem\:namespacecom_1_1sun_1_1star_1_1accessibility > td.memItemRight > a

# modules can contain other modules such as with chart2: https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart2.html

