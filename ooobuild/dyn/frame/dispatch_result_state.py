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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.frame
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class DispatchResultState(metaclass=UnoConstMeta, type_name="com.sun.star.frame.DispatchResultState", name_space="com.sun.star.frame"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.frame.DispatchResultState``"""
        pass

    class DispatchResultStateEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.frame.DispatchResultState", name_space="com.sun.star.frame"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.frame.DispatchResultState`` as Enum values"""
        pass

else:
    from com.sun.star.frame import DispatchResultState as DispatchResultState

    class DispatchResultStateEnum(IntEnum):
        """
        Enum of Const Class DispatchResultState

        possible values for DispatchResultEvent
        """
        FAILURE = DispatchResultState.FAILURE
        """
        indicates: dispatch failed
        """
        SUCCESS = DispatchResultState.SUCCESS
        """
        indicates: dispatch was successful
        """
        DONTKNOW = DispatchResultState.DONTKNOW
        """
        indicates: result isn't defined
        """

__all__ = ['DispatchResultState', 'DispatchResultStateEnum']
