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
# Namespace: com.sun.star.sheet
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta,ConstEnumMeta
    class StatusBarFunction(metaclass=UnoConstMeta, type_name="com.sun.star.sheet.StatusBarFunction", name_space="com.sun.star.sheet"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sheet.StatusBarFunction``"""
        pass

    class StatusBarFunctionEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.sheet.StatusBarFunction", name_space="com.sun.star.sheet"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sheet.StatusBarFunction`` as Enum values"""
        pass

else:
    from ...lo.sheet.status_bar_function import StatusBarFunction as StatusBarFunction

    class StatusBarFunctionEnum(IntEnum):
        """
        Enum of Const Class StatusBarFunction

        used to specify the function used to calculate a result in the spreadsheet's status bar.
        """
        NONE = StatusBarFunction.NONE
        """
        nothing is calculated.
        """
        AVERAGE = StatusBarFunction.AVERAGE
        """
        average of all numerical values is calculated.
        """
        COUNTNUMS = StatusBarFunction.COUNTNUMS
        """
        all values, including non-numerical values, are counted.
        """
        COUNT = StatusBarFunction.COUNT
        """
        numerical values are counted.
        """
        MAX = StatusBarFunction.MAX
        """
        maximum value of all numerical values is calculated.
        """
        MIN = StatusBarFunction.MIN
        """
        minimum value of all numerical values is calculated.
        """
        SUM = StatusBarFunction.SUM
        """
        sum of all numerical values is calculated.
        """

__all__ = ['StatusBarFunction', 'StatusBarFunctionEnum']
