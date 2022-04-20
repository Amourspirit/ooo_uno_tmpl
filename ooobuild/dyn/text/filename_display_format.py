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
    from com.sun.star.text import FilenameDisplayFormat as FilenameDisplayFormat
    if hasattr(FilenameDisplayFormat, '_constants') and isinstance(FilenameDisplayFormat._constants, dict):
        FilenameDisplayFormat._constants['__ooo_ns__'] = 'com.sun.star.text'
        FilenameDisplayFormat._constants['__ooo_full_ns__'] = 'com.sun.star.text.FilenameDisplayFormat'
        FilenameDisplayFormat._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global FilenameDisplayFormatEnum
        ls = [f for f in dir(FilenameDisplayFormat) if not callable(getattr(FilenameDisplayFormat, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(FilenameDisplayFormat, name)
        FilenameDisplayFormatEnum = IntEnum('FilenameDisplayFormatEnum', _dict)
    build_enum()
else:
    from ...lo.text.filename_display_format import FilenameDisplayFormat as FilenameDisplayFormat

    class FilenameDisplayFormatEnum(IntEnum):
        """
        Enum of Const Class FilenameDisplayFormat

        These constants are used to specify which parts of a URL are displayed in a field.
        """
        FULL = FilenameDisplayFormat.FULL
        """
        The content of the URL is completely displayed.
        """
        PATH = FilenameDisplayFormat.PATH
        """
        Only the path of the file is displayed.
        """
        NAME = FilenameDisplayFormat.NAME
        """
        Only the name of the file without the file extension is displayed.
        """
        NAME_AND_EXT = FilenameDisplayFormat.NAME_AND_EXT
        """
        The file name including the file extension is displayed.
        """

__all__ = ['FilenameDisplayFormat', 'FilenameDisplayFormatEnum']
