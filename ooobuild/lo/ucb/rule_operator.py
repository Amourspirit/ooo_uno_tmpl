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
# Namespace: com.sun.star.ucb


class RuleOperator(object):
    """
    Const Class

    These are the possible values for RuleTerm.RuleOperator.

    See Also:
        `API RuleOperator <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb_1_1RuleOperator.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.RuleOperator'
    __ooo_type_name__: str = 'const'

    CONTAINS = 1
    """
    \"Contains\" - Object contains RuleTerm.Operand.
    """
    CONTAINSNOT = 2
    """
    \"ContainsNot\" - Object does not contain RuleTerm.Operand.
    """
    GREATEREQUAL = 3
    """
    \"GreaterEqual\" - Object is greater than or equal to RuleTerm.Operand.
    """
    LESSEQUAL = 4
    """
    \"LessEqual\" - Object is less than or equal to RuleTerm.Operand.
    """
    EQUAL = 5
    """
    \"Equal\" - Object is equal to RuleTerm.Operand.
    """
    NOTEQUAL = 6
    """
    \"NotEqual\" - Object is not equal to RuleTerm.Operand.
    """
    VALUE_TRUE = 7
    """
    \"True\" - Object has the value TRUE.
    """
    VALUE_FALSE = 8
    """
    \"False\" - Object has the value FALSE.
    """

__all__ = ['RuleOperator']