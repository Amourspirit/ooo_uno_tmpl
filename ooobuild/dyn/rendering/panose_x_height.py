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
    from com.sun.star.rendering import PanoseXHeight as PanoseXHeight
    if hasattr(PanoseXHeight, '_constants') and isinstance(PanoseXHeight._constants, dict):
        PanoseXHeight._constants['__ooo_ns__'] = 'com.sun.star.rendering'
        PanoseXHeight._constants['__ooo_full_ns__'] = 'com.sun.star.rendering.PanoseXHeight'
        PanoseXHeight._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global PanoseXHeightEnum
        ls = [f for f in dir(PanoseXHeight) if not callable(getattr(PanoseXHeight, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(PanoseXHeight, name)
        PanoseXHeightEnum = IntEnum('PanoseXHeightEnum', _dict)
    build_enum()
else:
    from ...lo.rendering.panose_x_height import PanoseXHeight as PanoseXHeight

    class PanoseXHeightEnum(IntEnum):
        """
        Enum of Const Class PanoseXHeight

        """
        ANYTHING = PanoseXHeight.ANYTHING
        NO_FIT = PanoseXHeight.NO_FIT
        CONSTANT_SMALL = PanoseXHeight.CONSTANT_SMALL
        CONSTANT_STANDARD = PanoseXHeight.CONSTANT_STANDARD
        CONSTANT_LARGE = PanoseXHeight.CONSTANT_LARGE
        DUCKING_SMALL = PanoseXHeight.DUCKING_SMALL
        DUCKING_STANDARD = PanoseXHeight.DUCKING_STANDARD
        DUCKING_LARGE = PanoseXHeight.DUCKING_LARGE

__all__ = ['PanoseXHeight', 'PanoseXHeightEnum']