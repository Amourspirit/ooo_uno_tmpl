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
# Namespace: com.sun.star.text
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.text import PositionLayoutDir as PositionLayoutDir
    if hasattr(PositionLayoutDir, '_constants') and isinstance(PositionLayoutDir._constants, dict):
        PositionLayoutDir._constants['__ooo_ns__'] = 'com.sun.star.text'
        PositionLayoutDir._constants['__ooo_full_ns__'] = 'com.sun.star.text.PositionLayoutDir'
        PositionLayoutDir._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global PositionLayoutDirEnum
        ls = [f for f in dir(PositionLayoutDir) if not callable(getattr(PositionLayoutDir, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(PositionLayoutDir, name)
        PositionLayoutDirEnum = IntFlag('PositionLayoutDirEnum', _dict)
    build_enum()
else:
    from ...lo.text.position_layout_dir import PositionLayoutDir as PositionLayoutDir

    class PositionLayoutDirEnum(IntFlag):
        """
        Enum of Const Class PositionLayoutDir

        These values specify the layout direction, in which the position attributes of a shape are given.
        
        **since**
        
            OOo 2.0
        """
        PositionInHoriL2R = PositionLayoutDir.PositionInHoriL2R
        """
        position attributes are given in horizontal left-to-right direction
        """
        PositionInLayoutDirOfAnchor = PositionLayoutDir.PositionInLayoutDirOfAnchor
        """
        position attributes are given in layout direction of the drawing objects anchor
        """

__all__ = ['PositionLayoutDir', 'PositionLayoutDirEnum']