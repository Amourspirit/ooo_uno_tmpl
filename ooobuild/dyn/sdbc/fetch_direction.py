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
# Namespace: com.sun.star.sdbc
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta,ConstEnumMeta
    class FetchDirection(metaclass=UnoConstMeta, type_name="com.sun.star.sdbc.FetchDirection", name_space="com.sun.star.sdbc"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sdbc.FetchDirection``"""
        pass

    class FetchDirectionEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.sdbc.FetchDirection", name_space="com.sun.star.sdbc"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sdbc.FetchDirection`` as Enum values"""
        pass

else:
    from ...lo.sdbc.fetch_direction import FetchDirection as FetchDirection

    class FetchDirectionEnum(IntEnum):
        """
        Enum of Const Class FetchDirection

        indicates in which direction a result set should fetch next, just for optimization.
        """
        FORWARD = FetchDirection.FORWARD
        """
        The rows in a result set will be processed in a forward direction; first-to-last.
        """
        REVERSE = FetchDirection.REVERSE
        """
        The rows in a result set will be processed in a reverse direction; last-to-first.
        """
        UNKNOWN = FetchDirection.UNKNOWN
        """
        The order in which rows in a result set will be processed is unknown:
        """

__all__ = ['FetchDirection', 'FetchDirectionEnum']
