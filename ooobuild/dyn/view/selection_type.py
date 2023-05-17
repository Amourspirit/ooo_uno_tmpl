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
# Namespace: com.sun.star.view
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.view.SelectionType import MULTI as SELECTION_TYPE_MULTI
    from com.sun.star.view.SelectionType import NONE as SELECTION_TYPE_NONE
    from com.sun.star.view.SelectionType import RANGE as SELECTION_TYPE_RANGE
    from com.sun.star.view.SelectionType import SINGLE as SELECTION_TYPE_SINGLE

    class SelectionType(uno.Enum):
        """
        Enum Class


        See Also:
            `API SelectionType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1view.html#acffca3b33fddce63d3220bc7487e879d>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.view.SelectionType', value)

        __ooo_ns__: str = 'com.sun.star.view'
        __ooo_full_ns__: str = 'com.sun.star.view.SelectionType'
        __ooo_type_name__: str = 'enum'

        MULTI = cast("SelectionType", SELECTION_TYPE_MULTI)
        """
        The selection can contain zero or more objects.
        """
        NONE = cast("SelectionType", SELECTION_TYPE_NONE)
        """
        No selection is possible.
        
        The selection is always empty.
        """
        RANGE = cast("SelectionType", SELECTION_TYPE_RANGE)
        """
        The selection can contain zero or more objects.
        
        all selected objects must be part of a continues range
        """
        SINGLE = cast("SelectionType", SELECTION_TYPE_SINGLE)
        """
        The selection can only contain one or zero objects.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class SelectionType(metaclass=UnoEnumMeta, type_name="com.sun.star.view.SelectionType", name_space="com.sun.star.view"):
        """Dynamically created class that represents ``com.sun.star.view.SelectionType`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['SelectionType']
