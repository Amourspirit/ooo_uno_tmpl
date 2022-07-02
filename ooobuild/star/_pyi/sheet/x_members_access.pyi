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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sheet
from typing_extensions import Literal
import typing
from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6

class XMembersAccess(XNameAccess_e2ab0cf6):
    """
    is used to access named members in a data pilot source level collection.

    See Also:
        `API XMembersAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XMembersAccess.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.XMembersAccess']

    def getLocaleIndependentElementNames(self) -> 'typing.Tuple[str, ...]':
        """
        returns names of data pilot members in a locale independent notation.
        
        Specifically date values are represented in an ISO 8601 YYYY-MM-DD notation and date+time as YYYY-MM-DD HH:MM:SS, whereas the strings returned by com.sun.star.container.XNameAccess.getElementNames() may represent these in a locale dependent or user formatted notation such as MM/DD/YY or DD.MM.YYYY or other.
        
        The names returned by this function can NOT be used in calls to com.sun.star.container.XNameAccess.getByName(). However, the order returned in two immediately consecutive calls to getElementNames() and getLocaleIndependentElementNames() maps to the same elements in order.
        """
        ...


