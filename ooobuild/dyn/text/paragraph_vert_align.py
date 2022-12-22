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
# Namespace: com.sun.star.text
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class ParagraphVertAlign(metaclass=UnoConstMeta, type_name="com.sun.star.text.ParagraphVertAlign", name_space="com.sun.star.text"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.text.ParagraphVertAlign``"""
        pass

    class ParagraphVertAlignEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.text.ParagraphVertAlign", name_space="com.sun.star.text"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.text.ParagraphVertAlign`` as Enum values"""
        pass

else:
    from ...lo.text.paragraph_vert_align import ParagraphVertAlign as ParagraphVertAlign

    class ParagraphVertAlignEnum(IntEnum):
        """
        Enum of Const Class ParagraphVertAlign

        These enumeration values are used to specify the vertical alignment of paragraphs.
        """
        AUTOMATIC = ParagraphVertAlign.AUTOMATIC
        """
        In automatic mode, horizontal text is aligned to the baseline.
        
        The same applies to text that is rotated 90°. Text that is rotated 270 ° is aligned to the center.
        """
        BASELINE = ParagraphVertAlign.BASELINE
        """
        The text is aligned to the baseline.
        """
        TOP = ParagraphVertAlign.TOP
        """
        The text is aligned to the top.
        """
        CENTER = ParagraphVertAlign.CENTER
        """
        The text is aligned to the center.
        """
        BOTTOM = ParagraphVertAlign.BOTTOM
        """
        The text is aligned to bottom.
        """

__all__ = ['ParagraphVertAlign', 'ParagraphVertAlignEnum']
