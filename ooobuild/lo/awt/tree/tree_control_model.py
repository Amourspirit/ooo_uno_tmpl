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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.awt.tree
from __future__ import annotations
import typing
from abc import abstractproperty
from ..uno_control_model import UnoControlModel as UnoControlModel_c8ce0c58
if typing.TYPE_CHECKING:
    from .x_tree_data_model import XTreeDataModel as XTreeDataModel_f9fc0d85
    from com.sun.star.view.SelectionType import SelectionTypeProto  # type: ignore

class TreeControlModel(UnoControlModel_c8ce0c58):
    """
    Service Class

    specifies the standard model of a TreeControl.

    See Also:
        `API TreeControlModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1tree_1_1TreeControlModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.tree'
    __ooo_full_ns__: str = 'com.sun.star.awt.tree.TreeControlModel'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def DataModel(self) -> XTreeDataModel_f9fc0d85:
        """
        Specifies the XTreeDataModel that is providing the hierarchical data.
        
        You can implement your own instance of XTreeDataModel or use the MutableTreeDataModel.
        """
        ...

    @abstractproperty
    def Editable(self) -> bool:
        """
        Specifies whether the nodes of the tree are editable.
        
        The default value is FALSE
        """
        ...

    @abstractproperty
    def InvokesStopNodeEditing(self) -> bool:
        """
        Specifies what happens when editing is interrupted by selecting another node in the tree, a change in the tree's data, or by some other means.
        
        Setting this property to TRUE causes the changes to be automatically saved when editing is interrupted. FALSE means that editing is canceled and changes are lost
        
        The default value is FALSE
        """
        ...

    @abstractproperty
    def RootDisplayed(self) -> bool:
        """
        Specifies if the root node of the tree is displayed.
        
        If RootDisplayed is set to FALSE, the root node of a model is no longer a valid node for the XTreeControl and can't be used with any method of XTreeControl.
        
        The default value is TRUE
        """
        ...

    @abstractproperty
    def RowHeight(self) -> int:
        """
        Specifies the height of each row, in pixels.
        
        If the specified value is less than or equal to zero, the row height is the maximum height of all rows.
        
        The default value is 0
        """
        ...

    @abstractproperty
    def SelectionType(self) -> SelectionTypeProto:
        """
        Specifies the selection mode that is enabled for this tree.
        
        The default value is com.sun.star.view.SelectionType.NONE
        """
        ...

    @abstractproperty
    def ShowsHandles(self) -> bool:
        """
        Specifies whether the node handles should be displayed.
        
        The handles are doted lines that visualize the tree like hierarchy
        
        The default value is TRUE
        """
        ...

    @abstractproperty
    def ShowsRootHandles(self) -> bool:
        """
        Specifies whether the node handles should also be displayed at root level.
        
        The default value is TRUE
        """
        ...


__all__ = ['TreeControlModel']