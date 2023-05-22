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

    class PanoseLetterForm(metaclass=UnoConstMeta, type_name="com.sun.star.rendering.PanoseLetterForm", name_space="com.sun.star.rendering"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.rendering.PanoseLetterForm``"""
        pass

    class PanoseLetterFormEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.rendering.PanoseLetterForm", name_space="com.sun.star.rendering"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.rendering.PanoseLetterForm`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.rendering import PanoseLetterForm as PanoseLetterForm
    else:
        # keep document generators happy
        from ...lo.rendering.panose_letter_form import PanoseLetterForm as PanoseLetterForm

    class PanoseLetterFormEnum(IntEnum):
        """
        Enum of Const Class PanoseLetterForm

        """
        ANYTHING = PanoseLetterForm.ANYTHING
        NO_FIT = PanoseLetterForm.NO_FIT
        NORMAL_CONTACT = PanoseLetterForm.NORMAL_CONTACT
        NORMAL_WEIGHTED = PanoseLetterForm.NORMAL_WEIGHTED
        NORMAL_BOXED = PanoseLetterForm.NORMAL_BOXED
        NORMAL_FLATTENED = PanoseLetterForm.NORMAL_FLATTENED
        NORMAL_ROUNDED = PanoseLetterForm.NORMAL_ROUNDED
        NORMAL_OFF_CENTER = PanoseLetterForm.NORMAL_OFF_CENTER
        NORMAL_SQUARE = PanoseLetterForm.NORMAL_SQUARE
        OBLIQUE_CONTACT = PanoseLetterForm.OBLIQUE_CONTACT
        OBLIQUE_WEIGHTED = PanoseLetterForm.OBLIQUE_WEIGHTED
        OBLIQUE_BOXED = PanoseLetterForm.OBLIQUE_BOXED
        OBLIQUE_FLATTENED = PanoseLetterForm.OBLIQUE_FLATTENED
        OBLIQUE_ROUNDED = PanoseLetterForm.OBLIQUE_ROUNDED
        OBLIQUE_OFF_CENTER = PanoseLetterForm.OBLIQUE_OFF_CENTER
        OBLIQUE_SQUARE = PanoseLetterForm.OBLIQUE_SQUARE

__all__ = ['PanoseLetterForm', 'PanoseLetterFormEnum']
