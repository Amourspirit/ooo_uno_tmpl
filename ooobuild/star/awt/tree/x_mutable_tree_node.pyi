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
# Namespace: com.sun.star.awt.tree
from __future__ import annotations
import typing

from .x_tree_node import XTreeNode as XTreeNode_baaf0ba0


class XMutableTreeNode(XTreeNode_baaf0ba0):
    """
    Represents a mutable tree node as used by the MutableTreeDataModel.

    See Also:
        `API XMutableTreeNode <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1tree_1_1XMutableTreeNode.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.awt.tree.XMutableTreeNode'

    def appendChild(self, ChildNode: XMutableTreeNode) -> None:
        """
        appends ChildNode to this instance.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def insertChildByIndex(self, Index: int, ChildNode: XMutableTreeNode) -> None:
        """
        inserts ChildNode to this instance at the given index.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def removeChildByIndex(self, Index: int) -> None:
        """
        removes the node from this instance at the specified index.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def setCollapsedGraphicURL(self, URL: str) -> None:
        """
        The URL for a graphic that is rendered to visualize collapsed non leaf nodes.
        
        If URL is empty, XTreeControl.DefaultCollapsedGraphicURL is used.
        """
        ...
    def setDisplayValue(self, Value: typing.Any) -> None:
        """
        sets the display value of this node
        """
        ...
    def setExpandedGraphicURL(self, URL: str) -> None:
        """
        The URL for a graphic that is rendered to visualize expanded non leaf nodes.
        
        If URL is empty, XTreeControl.DefaultExpandedGraphicURL is used.
        """
        ...
    def setHasChildrenOnDemand(self, ChildrenOnDemand: bool) -> None:
        """
        Changes if the children of this node are created on demand.
        """
        ...
    def setNodeGraphicURL(self, URL: str) -> None:
        """
        The URL for a graphic that is rendered before the text part of this node.
        
        If this URL is empty, no graphic is rendered.
        """
        ...

    @property
    def DataValue(self) -> object:
        """
        Stores an implementation dependent value.
        
        You can use this attribute to store data for this node that is independent of the display value
        """
        ...
    @DataValue.setter
    def DataValue(self, value: object) -> None:
        ...

