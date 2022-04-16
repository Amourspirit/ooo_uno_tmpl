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
# Namespace: com.sun.star.i18n
from typing_extensions import Literal


class CharType:
    """
    Const Class

    Constants to specify the character type that starts a character block.
    
    Character type is Unicode type defined in UnicodeType
    
    Used with XBreakIterator.beginOfCharBlock(), XBreakIterator.endOfCharBlock(), XBreakIterator.nextCharBlock(), XBreakIterator.previousCharBlock()

    See Also:
        `API CharType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1CharType.html>`_
    """
    ANY_CHAR: Literal[0]
    """
    all alpha characters allowed
    """
    UPPERCASE_LETTER: Literal[1]
    LOWERCASE_LETTER: Literal[2]
    TITLECASE_LETTER: Literal[3]
    MODIFIER_LETTER: Literal[4]
    OTHER_LETTER: Literal[5]
    NON_SPACING_MARK: Literal[6]
    ENCLOSING_MARK: Literal[7]
    COMBINING_SPACING_MARK: Literal[8]
    DECIMAL_DIGIT_NUMBER: Literal[9]
    LETTER_NUMBER: Literal[10]
    OTHER_NUMBER: Literal[11]
    SPACE_SEPARATOR: Literal[12]
    LINE_SEPARATOR: Literal[13]
    PARAGRAPH_SEPARATOR: Literal[14]
    CONTROL: Literal[15]
    FORMAT: Literal[16]
    PRIVATE_USE: Literal[17]
    SURROGATE: Literal[18]
    DASH_PUNCTUATION: Literal[19]
    START_PUNCTUATION: Literal[20]
    END_PUNCTUATION: Literal[21]
    CONNECTOR_PUNCTUATION: Literal[22]
    OTHER_PUNCTUATION: Literal[23]
    MATH_SYMBOL: Literal[24]
    CURRENCY_SYMBOL: Literal[25]
    MODIFIER_SYMBOL: Literal[26]
    OTHER_SYMBOL: Literal[27]
    INITIAL_PUNCTUATION: Literal[28]
    FINAL_PUNCTUATION: Literal[29]
    GENERAL_TYPES_COUNT: Literal[30]

