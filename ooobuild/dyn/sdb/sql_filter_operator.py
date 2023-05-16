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
# Namespace: com.sun.star.sdb
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class SQLFilterOperator(metaclass=UnoConstMeta, type_name="com.sun.star.sdb.SQLFilterOperator", name_space="com.sun.star.sdb"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sdb.SQLFilterOperator``"""
        pass

    class SQLFilterOperatorEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.sdb.SQLFilterOperator", name_space="com.sun.star.sdb"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sdb.SQLFilterOperator`` as Enum values"""
        pass

else:
    from com.sun.star.sdb import SQLFilterOperator as SQLFilterOperator

    class SQLFilterOperatorEnum(IntEnum):
        """
        Enum of Const Class SQLFilterOperator

        These constants are used to specify the filter operator which should be applied when creating a filter with the method XSingleSelectQueryComposer.setStructuredFilter().
        """
        EQUAL = SQLFilterOperator.EQUAL
        """
        equal to
        """
        NOT_EQUAL = SQLFilterOperator.NOT_EQUAL
        """
        not equal to
        """
        LESS = SQLFilterOperator.LESS
        """
        less than
        """
        GREATER = SQLFilterOperator.GREATER
        """
        greater than
        """
        LESS_EQUAL = SQLFilterOperator.LESS_EQUAL
        """
        less or equal than
        """
        GREATER_EQUAL = SQLFilterOperator.GREATER_EQUAL
        """
        greater or equal than
        """
        LIKE = SQLFilterOperator.LIKE
        """
        like
        """
        NOT_LIKE = SQLFilterOperator.NOT_LIKE
        """
        not like
        """
        SQLNULL = SQLFilterOperator.SQLNULL
        """
        is null
        """
        NOT_SQLNULL = SQLFilterOperator.NOT_SQLNULL
        """
        is not null
        """

__all__ = ['SQLFilterOperator', 'SQLFilterOperatorEnum']
