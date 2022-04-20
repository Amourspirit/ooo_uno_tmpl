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
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.i18n import reservedWords as reservedWords
    if hasattr(reservedWords, '_constants') and isinstance(reservedWords._constants, dict):
        reservedWords._constants['__ooo_ns__'] = 'com.sun.star.i18n'
        reservedWords._constants['__ooo_full_ns__'] = 'com.sun.star.i18n.reservedWords'
        reservedWords._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global reservedWordsEnum
        ls = [f for f in dir(reservedWords) if not callable(getattr(reservedWords, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(reservedWords, name)
        reservedWordsEnum = IntEnum('reservedWordsEnum', _dict)
    build_enum()
else:
    from ...lo.i18n.reserved_words import reservedWords as reservedWords

    class reservedWordsEnum(IntEnum):
        """
        Enum of Const Class reservedWords

        Offsets into the sequence of strings returned by XLocaleData.getReservedWord().
        """
        TRUE_WORD = reservedWords.TRUE_WORD
        """
        \"true\"
        """
        FALSE_WORD = reservedWords.FALSE_WORD
        """
        \"false\"
        """
        QUARTER1_WORD = reservedWords.QUARTER1_WORD
        """
        \"1st quarter\"
        """
        QUARTER2_WORD = reservedWords.QUARTER2_WORD
        """
        \"2nd quarter\"
        """
        QUARTER3_WORD = reservedWords.QUARTER3_WORD
        """
        \"3rd quarter\"
        """
        QUARTER4_WORD = reservedWords.QUARTER4_WORD
        """
        \"4th quarter\"
        """
        ABOVE_WORD = reservedWords.ABOVE_WORD
        """
        \"above\"
        """
        BELOW_WORD = reservedWords.BELOW_WORD
        """
        \"below\"
        """
        QUARTER1_ABBREVIATION = reservedWords.QUARTER1_ABBREVIATION
        """
        \"Q1\"
        """
        QUARTER2_ABBREVIATION = reservedWords.QUARTER2_ABBREVIATION
        """
        \"Q2\"
        """
        QUARTER3_ABBREVIATION = reservedWords.QUARTER3_ABBREVIATION
        """
        \"Q3\"
        """
        QUARTER4_ABBREVIATION = reservedWords.QUARTER4_ABBREVIATION
        """
        \"Q4\"
        """
        COUNT = reservedWords.COUNT
        """
        Yes, this must be the count of known reserved words and one more than the maximum number used above! Count of known reserved words.
        """

__all__ = ['reservedWords', 'reservedWordsEnum']
