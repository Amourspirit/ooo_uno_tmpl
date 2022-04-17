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
    from com.sun.star.rendering import PanoseLetterForm as PanoseLetterForm
    if hasattr(PanoseLetterForm, '_constants') and isinstance(PanoseLetterForm._constants, dict):
        PanoseLetterForm._constants['__ooo_ns__'] = 'com.sun.star.rendering'
        PanoseLetterForm._constants['__ooo_full_ns__'] = 'com.sun.star.rendering.PanoseLetterForm'
        PanoseLetterForm._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global PanoseLetterFormEnum
        ls = [f for f in dir(PanoseLetterForm) if not callable(getattr(PanoseLetterForm, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(PanoseLetterForm, name)
        PanoseLetterFormEnum = IntEnum('PanoseLetterFormEnum', _dict)
    build_enum()
else:
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
