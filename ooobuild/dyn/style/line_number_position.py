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
# Libre Office Version: 7.3
# Namespace: com.sun.star.style
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.style import LineNumberPosition as LineNumberPosition
    if hasattr(LineNumberPosition, '_constants') and isinstance(LineNumberPosition._constants, dict):
        LineNumberPosition._constants['__ooo_ns__'] = 'com.sun.star.style'
        LineNumberPosition._constants['__ooo_full_ns__'] = 'com.sun.star.style.LineNumberPosition'
        LineNumberPosition._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global LineNumberPositionEnum
        ls = [f for f in dir(LineNumberPosition) if not callable(getattr(LineNumberPosition, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(LineNumberPosition, name)
        LineNumberPositionEnum = IntEnum('LineNumberPositionEnum', _dict)
    build_enum()
else:
    from ...lo.style.line_number_position import LineNumberPosition as LineNumberPosition

    class LineNumberPositionEnum(IntEnum):
        """
        Enum of Const Class LineNumberPosition

        These constants are used to specify the position of the numbering of lines.
        """
        LEFT = LineNumberPosition.LEFT
        """
        the number occurs on the left side of the pages.
        """
        RIGHT = LineNumberPosition.RIGHT
        """
        the number occurs on the right side of the pages.
        """
        INSIDE = LineNumberPosition.INSIDE
        """
        the number occurs alternating on the inner side of the pages.
        """
        OUTSIDE = LineNumberPosition.OUTSIDE
        """
        the number occurs alternating on the outside side of the pages.
        """

__all__ = ['LineNumberPosition', 'LineNumberPositionEnum']