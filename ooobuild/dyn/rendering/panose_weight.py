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
    from com.sun.star.rendering import PanoseWeight as PanoseWeight
    if hasattr(PanoseWeight, '_constants') and isinstance(PanoseWeight._constants, dict):
        PanoseWeight._constants['__ooo_ns__'] = 'com.sun.star.rendering'
        PanoseWeight._constants['__ooo_full_ns__'] = 'com.sun.star.rendering.PanoseWeight'
        PanoseWeight._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global PanoseWeightEnum
        ls = [f for f in dir(PanoseWeight) if not callable(getattr(PanoseWeight, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(PanoseWeight, name)
        PanoseWeightEnum = IntEnum('PanoseWeightEnum', _dict)
    build_enum()
else:
    from ...lo.rendering.panose_weight import PanoseWeight as PanoseWeight

    class PanoseWeightEnum(IntEnum):
        """
        Enum of Const Class PanoseWeight

        """
        ANYTHING = PanoseWeight.ANYTHING
        NO_FIT = PanoseWeight.NO_FIT
        VERY_LIGHT = PanoseWeight.VERY_LIGHT
        LIGHT = PanoseWeight.LIGHT
        THIN = PanoseWeight.THIN
        BOOK = PanoseWeight.BOOK
        MEDIUM = PanoseWeight.MEDIUM
        DEMI_BOLD = PanoseWeight.DEMI_BOLD
        BOLD = PanoseWeight.BOLD
        HEAVY = PanoseWeight.HEAVY
        BLACK = PanoseWeight.BLACK
        NORD = PanoseWeight.NORD

__all__ = ['PanoseWeight', 'PanoseWeightEnum']