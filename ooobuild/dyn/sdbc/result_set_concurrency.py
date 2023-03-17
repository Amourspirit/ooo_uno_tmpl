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
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdbc
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class ResultSetConcurrency(metaclass=UnoConstMeta, type_name="com.sun.star.sdbc.ResultSetConcurrency", name_space="com.sun.star.sdbc"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sdbc.ResultSetConcurrency``"""
        pass

    class ResultSetConcurrencyEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.sdbc.ResultSetConcurrency", name_space="com.sun.star.sdbc"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sdbc.ResultSetConcurrency`` as Enum values"""
        pass

else:
    from ...lo.sdbc.result_set_concurrency import ResultSetConcurrency as ResultSetConcurrency

    class ResultSetConcurrencyEnum(IntEnum):
        """
        Enum of Const Class ResultSetConcurrency

        describes the different scroll capabilities of a result set.
        """
        READ_ONLY = ResultSetConcurrency.READ_ONLY
        """
        is the concurrency mode for a com.sun.star.sdb.ResultSet object that may NOT be updated.
        """
        UPDATABLE = ResultSetConcurrency.UPDATABLE
        """
        is the concurrency mode for a com.sun.star.sdb.ResultSet object that may be updated.
        """

__all__ = ['ResultSetConcurrency', 'ResultSetConcurrencyEnum']
