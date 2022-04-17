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
from enum import IntFlag
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.i18n import KParseType as KParseType
    if hasattr(KParseType, '_constants') and isinstance(KParseType._constants, dict):
        KParseType._constants['__ooo_ns__'] = 'com.sun.star.i18n'
        KParseType._constants['__ooo_full_ns__'] = 'com.sun.star.i18n.KParseType'
        KParseType._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global KParseTypeEnum
        ls = [f for f in dir(KParseType) if not callable(getattr(KParseType, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(KParseType, name)
        KParseTypeEnum = IntFlag('KParseTypeEnum', _dict)
    build_enum()
else:
    from ...lo.i18n.k_parse_type import KParseType as KParseType

    class KParseTypeEnum(IntFlag):
        """
        Enum of Const Class KParseType

        Constants to specify the type of a parsed token.
        
        Set by XCharacterClassification.parseAnyToken() and XCharacterClassification.parsePredefinedToken() in ParseResult.TokenType.
        """
        ONE_SINGLE_CHAR = KParseType.ONE_SINGLE_CHAR
        """
        One single character like ! # ; : $ et al.
        """
        BOOLEAN = KParseType.BOOLEAN
        """
        A Boolean operator like <, >, <>, =, <=, >=.
        """
        IDENTNAME = KParseType.IDENTNAME
        """
        A name matching the conditions passed.
        """
        SINGLE_QUOTE_NAME = KParseType.SINGLE_QUOTE_NAME
        """
        \"A single-quoted name matching the conditions passed ( 'na\\'me' ).\" \"Dequoted name in ParseResult.DequotedNameOrString ( na'me ).\"
        """
        DOUBLE_QUOTE_STRING = KParseType.DOUBLE_QUOTE_STRING
        """
        A double-quoted string ( \"str\\\"i\"\"ng\" ).
        
        Dequoted string in ParseResult.DequotedNameOrString ( str\"i\"ng ).
        """
        ASC_NUMBER = KParseType.ASC_NUMBER
        """
        A number where all digits are ASCII characters.
        
        Numerical value in ParseResult.Value.
        """
        UNI_NUMBER = KParseType.UNI_NUMBER
        """
        A number where at least some digits are Unicode (and maybe ASCII) characters.
        
        Numerical value inKParseType ParseResult.Value.
        """
        MISSING_QUOTE = KParseType.MISSING_QUOTE
        """
        Set (ored) if SINGLE_QUOTE_NAME or DOUBLE_QUOTE_STRING has no closing quote.
        """
        ANY_NUMBER = KParseType.ANY_NUMBER
        """
        Any ASCII or Unicode number.
        """

__all__ = ['KParseType', 'KParseTypeEnum']