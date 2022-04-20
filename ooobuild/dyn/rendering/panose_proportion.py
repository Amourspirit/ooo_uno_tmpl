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
# Namespace: com.sun.star.rendering
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.rendering import PanoseProportion as PanoseProportion
    if hasattr(PanoseProportion, '_constants') and isinstance(PanoseProportion._constants, dict):
        PanoseProportion._constants['__ooo_ns__'] = 'com.sun.star.rendering'
        PanoseProportion._constants['__ooo_full_ns__'] = 'com.sun.star.rendering.PanoseProportion'
        PanoseProportion._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global PanoseProportionEnum
        ls = [f for f in dir(PanoseProportion) if not callable(getattr(PanoseProportion, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(PanoseProportion, name)
        PanoseProportionEnum = IntEnum('PanoseProportionEnum', _dict)
    build_enum()
else:
    from ...lo.rendering.panose_proportion import PanoseProportion as PanoseProportion

    class PanoseProportionEnum(IntEnum):
        """
        Enum of Const Class PanoseProportion

        """
        ANYTHING = PanoseProportion.ANYTHING
        NO_FIT = PanoseProportion.NO_FIT
        OLD_SKOOL = PanoseProportion.OLD_SKOOL
        MODERN = PanoseProportion.MODERN
        EVEN_WIDTH = PanoseProportion.EVEN_WIDTH
        EXPANDED = PanoseProportion.EXPANDED
        CONDENSED = PanoseProportion.CONDENSED
        VERY_EXPANDED = PanoseProportion.VERY_EXPANDED
        VERY_CONDENSED = PanoseProportion.VERY_CONDENSED
        MONO_SPACED = PanoseProportion.MONO_SPACED

__all__ = ['PanoseProportion', 'PanoseProportionEnum']
