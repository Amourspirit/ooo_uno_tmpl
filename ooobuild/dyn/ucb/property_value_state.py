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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import TYPE_CHECKING


if TYPE_CHECKING:

    class PropertyValueState(uno.Enum):
        """
        Enum Class


        See Also:
            `API PropertyValueState <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#a82ef3fdcd414866879e7aae1e52748d0>`_
        """
        __ooo_ns__: str = ...
        __ooo_full_ns__: str = ...
        __ooo_type_name__: str = ...

        @property
        def typeName(self) -> str:
            ...

        INVALID_NAME: PropertyValueState = ...
        """
        The given property name/handle is invalid.
        """
        INVALID_TYPE: PropertyValueState = ...
        """
        The given property type is invalid.
        """
        PROCESSED: PropertyValueState = ...
        """
        The value was obtained.
        """
        UNPROCESSED: PropertyValueState = ...
        """
        The property value was not obtained yet.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class PropertyValueState(metaclass=UnoEnumMeta, type_name="com.sun.star.ucb.PropertyValueState", name_space="com.sun.star.ucb"):
        """Dynamically created class that represents ``com.sun.star.ucb.PropertyValueState`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['PropertyValueState']

