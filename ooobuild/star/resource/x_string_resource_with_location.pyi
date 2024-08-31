# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.resource
from __future__ import annotations
import typing

from .x_string_resource_persistence import XStringResourcePersistence as XStringResourcePersistence_cabc130c


class XStringResourceWithLocation(XStringResourcePersistence_cabc130c):
    """
    Extends XStringResourcePersistence by methods to handle an associated location.

    See Also:
        `API XStringResourceWithLocation <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1resource_1_1XStringResourceWithLocation.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.resource.XStringResourceWithLocation'

    def setURL(self, URL: str) -> None:
        """
        Associates a location to the StringResourceWithStorage instance which is used on subsequent calls of store().
        
        This call has to be used carefully as it removes the location previously connected to the StringResourceWithStorage. It may force the implementation to reload data from the previous location before releasing it. The StringResourceManager will be modified after calling this method as the data isn't stored to the new location yet. storeAsURL() should be preferred as it directly stores the data to the new location and afterwards this location is in sync with the resource data.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
        ...
    def storeAsURL(self, URL: str) -> None:
        """
        Stores all string table data to a location and associates this location to this instance as if setLocation() was called with this location.
        
        The modified state will be unmodified after the call.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...


