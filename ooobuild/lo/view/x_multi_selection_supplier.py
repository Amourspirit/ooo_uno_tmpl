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
# Namespace: com.sun.star.view
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_selection_supplier import XSelectionSupplier as XSelectionSupplier_fed20e15
if typing.TYPE_CHECKING:
    from ..container.x_enumeration import XEnumeration as XEnumeration_f2180daa

class XMultiSelectionSupplier(XSelectionSupplier_fed20e15):
    """
    makes it possible to append and remove objects from a selection.
    
    The method XSelectionSupplier.setSelection() for an instance that also supports XMultiSelectionSupplier should be implemented that it also takes either a selectable object or a sequence of selectable objects.
    
    Adding an object more than once to a selection should not toggle the selection for that object but only select it once

    See Also:
        `API XMultiSelectionSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1view_1_1XMultiSelectionSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.view'
    __ooo_full_ns__: str = 'com.sun.star.view.XMultiSelectionSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.view.XMultiSelectionSupplier'

    @abstractmethod
    def addSelection(self, Selection: object) -> bool:
        """
        adds the object or the objects represented by Selection to the selection of this XMultiSelectionSupplier.
        
        Adding an object to the selection that is already part of the selection should not raise this exception

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def clearSelection(self) -> None:
        """
        clears the selection of this XMultiSelectionSupplier.
        """
        ...
    @abstractmethod
    def createReverseSelectionEnumeration(self) -> XEnumeration_f2180daa:
        """
        """
        ...
    @abstractmethod
    def createSelectionEnumeration(self) -> XEnumeration_f2180daa:
        """
        """
        ...
    @abstractmethod
    def getSelectionCount(self) -> int:
        """
        returns the number of selected objects of this XMultiSelectionSupplier.
        """
        ...
    @abstractmethod
    def removeSelection(self, Selection: object) -> None:
        """
        remove the object or objects represented by Selection from the selection of this XMultiSelectionSupplier.
        
        Removing an object from the selection that is not part of the selection should not raise this exception

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XMultiSelectionSupplier']

