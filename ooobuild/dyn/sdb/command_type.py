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
# Namespace: com.sun.star.sdb
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class CommandType(metaclass=UnoConstMeta, type_name="com.sun.star.sdb.CommandType", name_space="com.sun.star.sdb"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sdb.CommandType``"""
        pass

    class CommandTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.sdb.CommandType", name_space="com.sun.star.sdb"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sdb.CommandType`` as Enum values"""
        pass

else:
    from ...lo.sdb.command_type import CommandType as CommandType

    class CommandTypeEnum(IntEnum):
        """
        Enum of Const Class CommandType

        indicates the type of a command.
        """
        TABLE = CommandType.TABLE
        """
        indicates that a command contains a table name, which can be used to process a command like \"select * from tablename\".
        """
        QUERY = CommandType.QUERY
        """
        indicates that a command contains a name of a query component, which contains a certain statement.
        """
        COMMAND = CommandType.COMMAND
        """
        indicates that the command is an SQL-Statement.
        """

__all__ = ['CommandType', 'CommandTypeEnum']
