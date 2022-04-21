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
# Namespace: com.sun.star.i18n
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.i18n import ScriptDirection as ScriptDirection
    if hasattr(ScriptDirection, '_constants') and isinstance(ScriptDirection._constants, dict):
        ScriptDirection._constants['__ooo_ns__'] = 'com.sun.star.i18n'
        ScriptDirection._constants['__ooo_full_ns__'] = 'com.sun.star.i18n.ScriptDirection'
        ScriptDirection._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global ScriptDirectionEnum
        ls = [f for f in dir(ScriptDirection) if not callable(getattr(ScriptDirection, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(ScriptDirection, name)
        ScriptDirectionEnum = IntEnum('ScriptDirectionEnum', _dict)
    build_enum()
else:
    from ...lo.i18n.script_direction import ScriptDirection as ScriptDirection

    class ScriptDirectionEnum(IntEnum):
        """
        Enum of Const Class ScriptDirection

        Script direction constants to use with XScriptTypeDetector methods.
        
        **since**
        
            OOo 1.1.2
        """
        NEUTRAL = ScriptDirection.NEUTRAL
        """
        Script direction is neutral.
        """
        LEFT_TO_RIGHT = ScriptDirection.LEFT_TO_RIGHT
        """
        Script direction is left to right.
        """
        RIGHT_TO_LEFT = ScriptDirection.RIGHT_TO_LEFT
        """
        Script direction is right to left.
        """

__all__ = ['ScriptDirection', 'ScriptDirectionEnum']
