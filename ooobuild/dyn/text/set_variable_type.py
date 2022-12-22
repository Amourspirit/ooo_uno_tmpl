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

    class SetVariableType(metaclass=UnoConstMeta, type_name="com.sun.star.text.SetVariableType", name_space="com.sun.star.text"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.text.SetVariableType``"""
        pass

    class SetVariableTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.text.SetVariableType", name_space="com.sun.star.text"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.text.SetVariableType`` as Enum values"""
        pass

else:
    from ...lo.text.set_variable_type import SetVariableType as SetVariableType

    class SetVariableTypeEnum(IntEnum):
        """
        Enum of Const Class SetVariableType

        These constants define the type of a variable text field.
        """
        VAR = SetVariableType.VAR
        """
        specifies a simple variable.
        """
        SEQUENCE = SetVariableType.SEQUENCE
        """
        specifies a number sequence field.
        """
        FORMULA = SetVariableType.FORMULA
        """
        specifies a formula field.
        """
        STRING = SetVariableType.STRING
        """
        specifies a string field.
        """

__all__ = ['SetVariableType', 'SetVariableTypeEnum']
