# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.text
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.text import ChapterFormat as ChapterFormat
    if hasattr(ChapterFormat, '_constants') and isinstance(ChapterFormat._constants, dict):
        ChapterFormat._constants['__ooo_ns__'] = 'com.sun.star.text'
        ChapterFormat._constants['__ooo_full_ns__'] = 'com.sun.star.text.ChapterFormat'
        ChapterFormat._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global ChapterFormatEnum
        ls = [f for f in dir(ChapterFormat) if not callable(getattr(ChapterFormat, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(ChapterFormat, name)
        ChapterFormatEnum = IntEnum('ChapterFormatEnum', _dict)
    build_enum()
else:
    from ...lo.text.chapter_format import ChapterFormat as ChapterFormat

    class ChapterFormatEnum(IntEnum):
        """
        Enum of Const Class ChapterFormat

        These constants define the display format of the chapter number in a chapter text field.
        """
        NAME = ChapterFormat.NAME
        """
        The title of the chapter is displayed.
        """
        NUMBER = ChapterFormat.NUMBER
        """
        The number including prefix and suffix of the chapter is displayed.
        """
        NAME_NUMBER = ChapterFormat.NAME_NUMBER
        """
        The title and number including prefix and suffix of the chapter are displayed.
        """
        NO_PREFIX_SUFFIX = ChapterFormat.NO_PREFIX_SUFFIX
        """
        The name and number of the chapter are displayed.
        """
        DIGIT = ChapterFormat.DIGIT
        """
        The number of the chapter is displayed.
        """

__all__ = ['ChapterFormat', 'ChapterFormatEnum']
