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
# Namespace: com.sun.star.i18n


class UnicodeType(object):
    """
    Const Class

    Constants to classify Unicode characters, returned by XCharacterClassification.getType()

    See Also:
        `API UnicodeType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1UnicodeType.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.UnicodeType'
    __ooo_type_name__: str = 'const'

    UNASSIGNED = 0
    UPPERCASE_LETTER = 1
    LOWERCASE_LETTER = 2
    TITLECASE_LETTER = 3
    MODIFIER_LETTER = 4
    OTHER_LETTER = 5
    NON_SPACING_MARK = 6
    ENCLOSING_MARK = 7
    COMBINING_SPACING_MARK = 8
    DECIMAL_DIGIT_NUMBER = 9
    LETTER_NUMBER = 10
    OTHER_NUMBER = 11
    SPACE_SEPARATOR = 12
    LINE_SEPARATOR = 13
    PARAGRAPH_SEPARATOR = 14
    CONTROL = 15
    FORMAT = 16
    PRIVATE_USE = 17
    SURROGATE = 18
    DASH_PUNCTUATION = 19
    INITIAL_PUNCTUATION = 20
    FINAL_PUNCTUATION = 21
    CONNECTOR_PUNCTUATION = 22
    OTHER_PUNCTUATION = 23
    MATH_SYMBOL = 24
    CURRENCY_SYMBOL = 25
    MODIFIER_SYMBOL = 26
    OTHER_SYMBOL = 27
    START_PUNCTUATION = 28
    END_PUNCTUATION = 29
    GENERAL_TYPES_COUNT = 30

__all__ = ['UnicodeType']
