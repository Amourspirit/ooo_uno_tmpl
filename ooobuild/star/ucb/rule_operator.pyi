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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.ucb
import typing


class RuleOperator:
    """
    Const

    These are the possible values for RuleTerm.RuleOperator.

    See Also:
        `API RuleOperator <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb_1_1RuleOperator.html>`_
    """
    CONTAINS: int = ...
    """
    \"Contains\" - Object contains RuleTerm.Operand.
    """
    CONTAINSNOT: int = ...
    """
    \"ContainsNot\" - Object does not contain RuleTerm.Operand.
    """
    GREATEREQUAL: int = ...
    """
    \"GreaterEqual\" - Object is greater than or equal to RuleTerm.Operand.
    """
    LESSEQUAL: int = ...
    """
    \"LessEqual\" - Object is less than or equal to RuleTerm.Operand.
    """
    EQUAL: int = ...
    """
    \"Equal\" - Object is equal to RuleTerm.Operand.
    """
    NOTEQUAL: int = ...
    """
    \"NotEqual\" - Object is not equal to RuleTerm.Operand.
    """
    VALUE_TRUE: int = ...
    """
    \"True\" - Object has the value TRUE.
    """
    VALUE_FALSE: int = ...
    """
    \"False\" - Object has the value FALSE.
    """

