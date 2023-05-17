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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.form
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import TYPE_CHECKING


if TYPE_CHECKING:

    class ListSourceType(uno.Enum):
        """
        Enum Class


        See Also:
            `API ListSourceType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1form.html#a52e06ed91fb133bc98c089a401a724fb>`_
        """
        __ooo_ns__: str = ...
        __ooo_full_ns__: str = ...
        __ooo_type_name__: str = ...

        @property
        def typeName(self) -> str:
            ...

        QUERY: ListSourceType = ...
        """
        The control should be filled with the results of a database query.
        """
        SQL: ListSourceType = ...
        """
        The control should be filled with the results of a database statement.
        """
        SQLPASSTHROUGH: ListSourceType = ...
        """
        The control should be filled with the results of a database statement, which is not evaluated by the database engine.
        """
        TABLE: ListSourceType = ...
        """
        The control should be filled with the data of a table.
        """
        TABLEFIELDS: ListSourceType = ...
        """
        The control should be filled with the field names of a database table.
        """
        VALUELIST: ListSourceType = ...
        """
        The control should be filled with a list of string values.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class ListSourceType(metaclass=UnoEnumMeta, type_name="com.sun.star.form.ListSourceType", name_space="com.sun.star.form"):
        """Dynamically created class that represents ``com.sun.star.form.ListSourceType`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['ListSourceType']

