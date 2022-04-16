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
# Namespace: com.sun.star.rendering
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.rendering import PathCapType as PathCapType
    if hasattr(PathCapType, '_constants') and isinstance(PathCapType._constants, dict):
        PathCapType._constants['__ooo_ns__'] = 'com.sun.star.rendering'
        PathCapType._constants['__ooo_full_ns__'] = 'com.sun.star.rendering.PathCapType'
        PathCapType._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global PathCapTypeEnum
        ls = [f for f in dir(PathCapType) if not callable(getattr(PathCapType, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(PathCapType, name)
        PathCapTypeEnum = IntEnum('PathCapTypeEnum', _dict)
    build_enum()
else:
    from ...lo.rendering.path_cap_type import PathCapType as PathCapType

    class PathCapTypeEnum(IntEnum):
        """
        Enum of Const Class PathCapType

        These constants determine which shape to use for start or end of a stroked path.
        
        The start and end of stroked paths can have one out of several different shapes (which are, of course, only visible for strokes wider than one device pixel).
        
        **since**
        
            OOo 2.0
        """
        BUTT = PathCapType.BUTT
        """
        End the path at its start or end point, without any cap.
        """
        ROUND = PathCapType.ROUND
        """
        Extend the path with a half circle cap, diameter is the line width.
        """
        SQUARE = PathCapType.SQUARE
        """
        Extend the path with a rectangular cap, half the line width long.
        """

__all__ = ['PathCapType', 'PathCapTypeEnum']
