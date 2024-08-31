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
# Namespace: com.sun.star.system.windows
from __future__ import annotations
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .jump_list_item import JumpListItem as JumpListItem_3f370fad

class XJumpList(XInterface_8f010a43):
    """
    Specifies an interface for adding custom jump lists to the task bar (Windows only)
    
    To add a new jump list, call
    
    Use XJumpList.abortList to cancel a current list building session. Use XJumpList.getRemovedItems to see which items were removed by the user.
    
    **since**
    
        LibreOffice 7.4

    See Also:
        `API XJumpList <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1system_1_1windows_1_1XJumpList.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.system.windows'
    __ooo_full_ns__: str = 'com.sun.star.system.windows.XJumpList'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.system.windows.XJumpList'

    @abstractmethod
    def abortList(self) -> None:
        """
        Aborts a list building session started with beginList.

        Raises:
            com.sun.star.util.InvalidStateException: ``InvalidStateException``
        """
        ...
    @abstractmethod
    def addTasks(self, jumpListItems: typing.Tuple[JumpListItem_3f370fad, ...]) -> None:
        """
        Add items to the \"Tasks\" category.
        
        This category is system-defined and the category title cannot be changed. Also the user cannot remove or pin items from this category (as he can with items added via XJumpList.appendCategory ).

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.util.InvalidStateException: ``InvalidStateException``
        """
        ...
    @abstractmethod
    def appendCategory(self, category: str, jumpListItems: typing.Tuple[JumpListItem_3f370fad, ...]) -> None:
        """
        Add a jump list category.
        
        Users can pin or remove items added via this method. Use XJumpList.getRemovedItems to see which items were removed by the user.
        
        Make sure you don't add items which the user has removed before (check the result of getRemovedItems before updating a category). If you try to add items which the user removed before, they will be silently ignored and not added to the list.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.util.InvalidStateException: ``InvalidStateException``
        """
        ...
    @abstractmethod
    def beginList(self, application: str) -> None:
        """
        Start a new jump list.
        
        \"Startcenter\" will map to the generic \"LibreOffice\" icon.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.util.InvalidStateException: ``InvalidStateException``
        """
        ...
    @abstractmethod
    def commitList(self) -> None:
        """
        Commits the list.

        Raises:
            com.sun.star.util.InvalidStateException: ``InvalidStateException``
        """
        ...
    @abstractmethod
    def deleteList(self, application: str) -> None:
        """
        Deletes the Jump List for a certain application.
        
        \"Startcenter\" will map to the generic \"LibreOffice\" icon.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def getRemovedItems(self, application: str) -> typing.Tuple[JumpListItem_3f370fad, ...]:
        """
        Returns items that were removed from the jump list by the user.
        
        appendCategory will ignore items which were removed by the user before. Use this method to learn which items were removed by the user.
        
        \"Startcenter\" will map to the generic \"LibreOffice\" icon.
        """
        ...
    @abstractmethod
    def showFrequentFiles(self) -> None:
        """
        Display the frequently used files (populated by LibreOffice)

        Raises:
            com.sun.star.util.InvalidStateException: ``InvalidStateException``
        """
        ...
    @abstractmethod
    def showRecentFiles(self) -> None:
        """
        Display the recently used files (populated by LibreOffice)

        Raises:
            com.sun.star.util.InvalidStateException: ``InvalidStateException``
        """
        ...

__all__ = ['XJumpList']

