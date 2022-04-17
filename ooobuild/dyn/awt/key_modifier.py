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
# Namespace: com.sun.star.awt
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.awt import KeyModifier as KeyModifier
    if hasattr(KeyModifier, '_constants') and isinstance(KeyModifier._constants, dict):
        KeyModifier._constants['__ooo_ns__'] = 'com.sun.star.awt'
        KeyModifier._constants['__ooo_full_ns__'] = 'com.sun.star.awt.KeyModifier'
        KeyModifier._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global KeyModifierEnum
        ls = [f for f in dir(KeyModifier) if not callable(getattr(KeyModifier, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(KeyModifier, name)
        KeyModifierEnum = IntFlag('KeyModifierEnum', _dict)
    build_enum()
else:
    from ...lo.awt.key_modifier import KeyModifier as KeyModifier

    class KeyModifierEnum(IntFlag):
        """
        Enum of Const Class KeyModifier

        These values are used to specify which modifier keys are pressed.
        """
        SHIFT = KeyModifier.SHIFT
        """
        refers to both shift keys.
        """
        MOD1 = KeyModifier.MOD1
        """
        refers in the most cases to the \"Ctrl\" key (Cmd on macOS).
        """
        MOD2 = KeyModifier.MOD2
        """
        refers in the most cases to the \"Alt\" key.
        """
        MOD3 = KeyModifier.MOD3
        """
        refers in the most cases to the \"Ctrl\" key (macOS)
        """

__all__ = ['KeyModifier', 'KeyModifierEnum']
