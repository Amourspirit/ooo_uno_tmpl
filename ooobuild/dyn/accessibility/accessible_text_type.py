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
# Namespace: com.sun.star.accessibility
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta,ConstEnumMeta
    class AccessibleTextType(metaclass=UnoConstMeta, type_name="com.sun.star.accessibility.AccessibleTextType", name_space="com.sun.star.accessibility"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.accessibility.AccessibleTextType``"""
        pass

    class AccessibleTextTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.accessibility.AccessibleTextType", name_space="com.sun.star.accessibility"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.accessibility.AccessibleTextType`` as Enum values"""
        pass

else:
    from ...lo.accessibility.accessible_text_type import AccessibleTextType as AccessibleTextType

    class AccessibleTextTypeEnum(IntEnum):
        """
        Enum of Const Class AccessibleTextType

        Collection of types of text portions.
        
        This collection describes the types of text portions that can be accessed with the help of the methods of the XAccessibleText interface.
        
        **since**
        
            OOo 1.1.2
        """
        CHARACTER = AccessibleTextType.CHARACTER
        """
        Single character.
        
        Indicates that single (multibyte) characters are used.
        """
        WORD = AccessibleTextType.WORD
        """
        Single word.
        
        Indicates that single words are used. The definition of what a word is, is implementation and language/locale dependent. While in English a word is ended by a space or a special character like a comma or a period, this is not necessarily true in other languages.
        """
        SENTENCE = AccessibleTextType.SENTENCE
        """
        Single sentence.
        
        Indicates that single sentences are used. The definition of what a sentence is, is implementation and language/locale dependent. While in English a sentence is ended by a period, this is not necessarily true in other languages.
        """
        PARAGRAPH = AccessibleTextType.PARAGRAPH
        """
        Single paragraph.
        
        Indicates that single paragraphs are used. The definition of what a paragraph is, is implementation and language/locale dependent.
        """
        LINE = AccessibleTextType.LINE
        """
        Single line.
        
        Indicates that single lines, as displayed on the screen, are used. In contrast to the constants CHARACTER, WORD, SENTENCE, and PARAGRAPH which are content oriented this constant is view oriented. It can be used to retrieve hyphenation information.
        """
        GLYPH = AccessibleTextType.GLYPH
        """
        Single glyph.
        
        Glyphs are runs of one or more (multibyte) characters which are displayed as one symbol.
        """
        ATTRIBUTE_RUN = AccessibleTextType.ATTRIBUTE_RUN
        """
        Attribute run.
        
        Each attribute run is a character run of maximal length where all characters have the same attributes set.
        """

__all__ = ['AccessibleTextType', 'AccessibleTextTypeEnum']
