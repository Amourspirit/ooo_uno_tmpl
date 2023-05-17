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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.sheet.FilterConnection import AND as FILTER_CONNECTION_AND
    from com.sun.star.sheet.FilterConnection import OR as FILTER_CONNECTION_OR

    class FilterConnection(uno.Enum):
        """
        Enum Class


        See Also:
            `API FilterConnection <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#a946b76fb59cd525a1296ff815333d110>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.sheet.FilterConnection', value)

        __ooo_ns__: str = 'com.sun.star.sheet'
        __ooo_full_ns__: str = 'com.sun.star.sheet.FilterConnection'
        __ooo_type_name__: str = 'enum'

        AND: FilterConnection = FILTER_CONNECTION_AND
        """
        both conditions have to be fulfilled.
        """
        OR: FilterConnection = FILTER_CONNECTION_OR
        """
        at least one of the conditions has to be fulfilled.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class FilterConnection(metaclass=UnoEnumMeta, type_name="com.sun.star.sheet.FilterConnection", name_space="com.sun.star.sheet"):
        """Dynamically created class that represents ``com.sun.star.sheet.FilterConnection`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['FilterConnection']
