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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.accessibility
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_accessible import XAccessible as XAccessible_1cbc0eb6


class XAccessibleSelection(XInterface_8f010a43):
    """
    Implement this interface to represent a selection of accessible objects.
    
    This interface is the standard mechanism to obtain and modify the currently selected children. Every object that has children that can be selected should support this interface.
    
    The XAccessibleSelection interface has to be implemented in conjunction with the XAccessibleContext interface that provides the children on which the first operates.
    
    It depends on the class implementing this interface, whether it supports single or multi selection.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XAccessibleSelection <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleSelection.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.accessibility.XAccessibleSelection']

    def clearAccessibleSelection(self) -> None:
        """
        Clears the selection, so that no children of the object are selected.
        """
        ...
    def deselectAccessibleChild(self, nChildIndex: int) -> None:
        """
        Removes the specified child from the set of this object's selected children.
        
        Note that not all applications support deselection: calls to this method may be silently ignored.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def getSelectedAccessibleChild(self, nSelectedChildIndex: int) -> 'XAccessible_1cbc0eb6':
        """
        Returns the specified selected Accessible child.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def getSelectedAccessibleChildCount(self) -> int:
        """
        Returns the number of Accessible children that are currently selected.
        
        This number specifies the valid interval of indices that can be used as arguments for the method XAccessibleSelection.getSelectedAccessibleChild().
        """
        ...
    def isAccessibleChildSelected(self, nChildIndex: int) -> bool:
        """
        Determines if the specified child of this object is selected.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def selectAccessibleChild(self, nChildIndex: int) -> None:
        """
        Selects the specified Accessible child of the object.
        
        Depending on the implementing class the child is added to the current set a selected children (multi selection) or a previously selected child is deselected first (single selection).

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def selectAllAccessibleChildren(self) -> None:
        """
        Select all children.
        
        Causes every child of the object to be selected if the object supports multiple selections. If multiple selection is not supported then the first child, if it exists, is selected and all other children are deselected.
        """
        ...


