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
# Namespace: com.sun.star.form.binding
from __future__ import annotations
import typing

from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_list_entry_listener import XListEntryListener as XListEntryListener_78de1111


class XListEntrySource(XInterface_8f010a43):
    """
    specifies a source of string list entries
    
    The interface supports foreign components which actively retrieve list entries, as well as components which want to passively being notified of changes in the list.

    See Also:
        `API XListEntrySource <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1binding_1_1XListEntrySource.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.form.binding.XListEntrySource'

    def addListEntryListener(self, Listener: XListEntryListener_78de1111) -> None:
        """
        adds a listener which will be notified about changes in the list reflected by the component.

        Raises:
            com.sun.star.lang.NullPointerException: ``NullPointerException``
        """
        ...
    def getAllListEntries(self) -> typing.Tuple[str, ...]:
        """
        provides access to the entirety of all list entries
        """
        ...
    def getListEntry(self, Position: int) -> str:
        """
        provides access to a single list entry

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def getListEntryCount(self) -> int:
        """
        retrieves the number of entries in the list
        """
        ...
    def removeListEntryListener(self, Listener: XListEntryListener_78de1111) -> None:
        """
        revokes the given listener from the list of components which will be notified about changes in the entry list.

        Raises:
            com.sun.star.lang.NullPointerException: ``NullPointerException``
        """
        ...


