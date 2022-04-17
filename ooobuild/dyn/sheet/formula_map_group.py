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
# Namespace: com.sun.star.sheet
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME
_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from com.sun.star.sheet import FormulaMapGroup as FormulaMapGroup
    if hasattr(FormulaMapGroup, '_constants') and isinstance(FormulaMapGroup._constants, dict):
        FormulaMapGroup._constants['__ooo_ns__'] = 'com.sun.star.sheet'
        FormulaMapGroup._constants['__ooo_full_ns__'] = 'com.sun.star.sheet.FormulaMapGroup'
        FormulaMapGroup._constants['__ooo_type_name__'] = 'const'
    def build_enum():
        global FormulaMapGroupEnum
        ls = [f for f in dir(FormulaMapGroup) if not callable(getattr(FormulaMapGroup, f)) and not f.startswith('__')]
        _dict = {}
        for name in ls:
            _dict[name] = getattr(FormulaMapGroup, name)
        FormulaMapGroupEnum = IntEnum('FormulaMapGroupEnum', _dict)
    build_enum()
else:
    from ...lo.sheet.formula_map_group import FormulaMapGroup as FormulaMapGroup

    class FormulaMapGroupEnum(IntEnum):
        """
        Enum of Const Class FormulaMapGroup

        Constants of bit masks used with XFormulaOpCodeMapper.getAvailableMappings() to specify for which group of symbols the mappings are to be obtained.
        
        If no bit is set, a sequence of special mappings is returned in the order that is defined by FormulaMapGroupSpecialOffset. Note that the special group and other groups are mutual exclusive.
        """
        SPECIAL = FormulaMapGroup.SPECIAL
        """
        Group of op-codes without a string symbol.
        """
        SEPARATORS = FormulaMapGroup.SEPARATORS
        """
        Separators and parentheses.
        """
        ARRAY_SEPARATORS = FormulaMapGroup.ARRAY_SEPARATORS
        """
        Separators and parentheses for constant arrays.
        """
        UNARY_OPERATORS = FormulaMapGroup.UNARY_OPERATORS
        """
        Unary operators.
        """
        BINARY_OPERATORS = FormulaMapGroup.BINARY_OPERATORS
        """
        Binary operators.
        """
        FUNCTIONS = FormulaMapGroup.FUNCTIONS
        """
        Functions.
        """
        ALL_EXCEPT_SPECIAL = FormulaMapGroup.ALL_EXCEPT_SPECIAL
        """
        All groups except SPECIAL.
        """

__all__ = ['FormulaMapGroup', 'FormulaMapGroupEnum']
