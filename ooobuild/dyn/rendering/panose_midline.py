# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.rendering
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class PanoseMidline(metaclass=UnoConstMeta, type_name="com.sun.star.rendering.PanoseMidline", name_space="com.sun.star.rendering"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.rendering.PanoseMidline``"""
        pass

    class PanoseMidlineEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.rendering.PanoseMidline", name_space="com.sun.star.rendering"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.rendering.PanoseMidline`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.rendering import PanoseMidline as PanoseMidline
    else:
        # keep document generators happy
        from ...lo.rendering.panose_midline import PanoseMidline as PanoseMidline

    class PanoseMidlineEnum(IntEnum):
        """
        Enum of Const Class PanoseMidline

        """
        ANYTHING = PanoseMidline.ANYTHING
        NO_FIT = PanoseMidline.NO_FIT
        STANDARD_TRIMMED = PanoseMidline.STANDARD_TRIMMED
        STANDARD_POINTED = PanoseMidline.STANDARD_POINTED
        STANDARD_SERIFED = PanoseMidline.STANDARD_SERIFED
        HIGH_TRIMMER = PanoseMidline.HIGH_TRIMMER
        HIGH_POINTED = PanoseMidline.HIGH_POINTED
        HIGH_SERIFED = PanoseMidline.HIGH_SERIFED
        CONSTANT_TRIMMED = PanoseMidline.CONSTANT_TRIMMED
        CONSTANT_POINTED = PanoseMidline.CONSTANT_POINTED
        CONSTANT_SERIFED = PanoseMidline.CONSTANT_SERIFED
        LOW_TRIMMED = PanoseMidline.LOW_TRIMMED
        LOW_POINTED = PanoseMidline.LOW_POINTED
        LOW_SERIFED = PanoseMidline.LOW_SERIFED

__all__ = ['PanoseMidline', 'PanoseMidlineEnum']
