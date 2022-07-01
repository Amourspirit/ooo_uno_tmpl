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
# Namespace: com.sun.star.presentation
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.presentation import EffectPresetClass as EffectPresetClass
    if hasattr(EffectPresetClass, '_constants') and isinstance(EffectPresetClass._constants, dict):
        EffectPresetClass._constants['__ooo_ns__'] = 'com.sun.star.presentation'
        EffectPresetClass._constants['__ooo_full_ns__'] = 'com.sun.star.presentation.EffectPresetClass'
        EffectPresetClass._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global EffectPresetClassEnum
        ls = [f for f in dir(EffectPresetClass) if not callable(getattr(EffectPresetClass, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(EffectPresetClass, name)
        EffectPresetClassEnum = IntEnum('EffectPresetClassEnum', _dict)
    build_enum()
else:
    from ...lo.presentation.effect_preset_class import EffectPresetClass as EffectPresetClass

    class EffectPresetClassEnum(IntEnum):
        """
        Enum of Const Class EffectPresetClass

        This constants defines the class for a preset animation effect.
        
        This is stored with the name preset-class inside the com.sun.star.animations.XAnimationNode.UserData sequence. This does not manipulate the timing or synchronization. It can be used to quickly identify preset animations inside an animation hierarchy.
        """
        CUSTOM = EffectPresetClass.CUSTOM
        ENTRANCE = EffectPresetClass.ENTRANCE
        EXIT = EffectPresetClass.EXIT
        EMPHASIS = EffectPresetClass.EMPHASIS
        MOTIONPATH = EffectPresetClass.MOTIONPATH
        OLEACTION = EffectPresetClass.OLEACTION
        MEDIACALL = EffectPresetClass.MEDIACALL

__all__ = ['EffectPresetClass', 'EffectPresetClassEnum']
