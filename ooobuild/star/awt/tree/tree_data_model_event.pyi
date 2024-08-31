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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.awt.tree
# Libre Office Version: 2024.2
from ...lang.event_object import EventObject as EventObject_a3d70b03
from ...uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .x_tree_node import XTreeNode as XTreeNode_baaf0ba0


class TreeDataModelEvent(EventObject_a3d70b03):
    """
    Struct Class

    An event used by a XTreeDataModel to notify changes in the data model to the XTreeControl.
    
    You usually need to fill this event only if you implement the XTreeDataModel yourself.

    See Also:
        `API TreeDataModelEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1tree_1_1TreeDataModelEvent.html>`_
    """
    typeName: str = 'com.sun.star.awt.tree.TreeDataModelEvent'

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., Nodes: typing.Optional[typing.Tuple[XTreeNode_baaf0ba0, ...]] = ..., ParentNode: typing.Optional[XTreeNode_baaf0ba0] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Nodes (typing.Tuple[XTreeNode, ...], optional): Nodes value.
            ParentNode (XTreeNode, optional): ParentNode value.
        """
        ...

    @property
    def Nodes(self) -> typing.Tuple[XTreeNode_baaf0ba0, ...]:
        """
        contains the changed, added or removed nodes.
        
        All nodes must have ParentNode as parent.
        """
        ...
    @Nodes.setter
    def Nodes(self, value: typing.Tuple[XTreeNode_baaf0ba0, ...]) -> None:
        ...
    @property
    def ParentNode(self) -> XTreeNode_baaf0ba0:
        """
        holds the parent node for changed, added or removed nodes.
        
        If this is null, Nodes must contain only the root node
        """
        ...
    @ParentNode.setter
    def ParentNode(self, value: XTreeNode_baaf0ba0) -> None:
        ...

