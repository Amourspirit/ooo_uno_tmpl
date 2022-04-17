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
    from com.sun.star.style import LineSpacingMode as LineSpacingMode
    if hasattr(LineSpacingMode, '_constants') and isinstance(LineSpacingMode._constants, dict):
        LineSpacingMode._constants['__ooo_ns__'] = 'com.sun.star.style'
        LineSpacingMode._constants['__ooo_full_ns__'] = 'com.sun.star.style.LineSpacingMode'
        LineSpacingMode._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global LineSpacingModeEnum
        ls = [f for f in dir(LineSpacingMode) if not callable(getattr(LineSpacingMode, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(LineSpacingMode, name)
        LineSpacingModeEnum = IntEnum('LineSpacingModeEnum', _dict)
    build_enum()
else:
    from ...lo.style.line_spacing_mode import LineSpacingMode as LineSpacingMode

    class LineSpacingModeEnum(IntEnum):
        """
        Enum of Const Class LineSpacingMode

        These constants specify the interpretation of LineHeight.
        """
        PROP = LineSpacingMode.PROP
        """
        This constant specifies the height value as a proportional value.
        """
        MINIMUM = LineSpacingMode.MINIMUM
        """
        This constant specifies the height as the minimum line height.
        """
        LEADING = LineSpacingMode.LEADING
        """
        This constant specifies the height value as the distance to the previous line.
        """
        FIX = LineSpacingMode.FIX
        """
        This constant specifies the height value as a fixed line height.
        """

__all__ = ['LineSpacingMode', 'LineSpacingModeEnum']
