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

    class UserFieldFormat(metaclass=UnoConstMeta, type_name="com.sun.star.text.UserFieldFormat", name_space="com.sun.star.text"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.text.UserFieldFormat``"""
        pass

    class UserFieldFormatEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.text.UserFieldFormat", name_space="com.sun.star.text"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.text.UserFieldFormat`` as Enum values"""
        pass

else:
    from ...lo.text.user_field_format import UserFieldFormat as UserFieldFormat

    class UserFieldFormatEnum(IntEnum):
        """
        Enum of Const Class UserFieldFormat

        These constants describe how the content of a user text field is formatted.
        """
        SYSTEM = UserFieldFormat.SYSTEM
        """
        The number format of the operating system is used.
        """
        TEXT = UserFieldFormat.TEXT
        """
        The content is formatted as text.
        """
        NUM = UserFieldFormat.NUM
        """
        The number format of the property \"NumberFormat\" is used.
        """

__all__ = ['UserFieldFormat', 'UserFieldFormatEnum']
