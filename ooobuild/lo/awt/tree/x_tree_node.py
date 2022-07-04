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
# Libre Office Version: 7.3
# Namespace: com.sun.star.awt.tree
from abc import abstractmethod, ABC

class XTreeNode(ABC):
    """
    An instance implementing this interface represents the model data for an entry in a XTreeDataModel.
    
    The TreeControl uses this interface to retrieve the model information needed to display a hierarchical outline
    
    Each XTreeNode in a XTreeDataModel must be unique.

    See Also:
        `API XTreeNode <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1tree_1_1XTreeNode.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.tree'
    __ooo_full_ns__: str = 'com.sun.star.awt.tree.XTreeNode'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.tree.XTreeNode'

    @abstractmethod
    def getChildAt(self, Index: int) -> 'XTreeNode':
        """
        Returns the child tree node at Index.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    @abstractmethod
    def getChildCount(self) -> int:
        """
        Returns the number of child nodes.
        """
        ...
    @abstractmethod
    def getCollapsedGraphicURL(self) -> str:
        """
        The URL for a graphic that is rendered to visualize collapsed non leaf nodes.
        
        If URL is empty, XTreeControl.DefaultCollapsedGraphicURL is used.
        """
        ...
    @abstractmethod
    def getDisplayValue(self) -> object:
        """
        If not empty, the textual representation of this any is used as the text part of this node.
        """
        ...
    @abstractmethod
    def getExpandedGraphicURL(self) -> str:
        """
        The URL for a graphic that is rendered to visualize expanded non leaf nodes.
        
        If URL is empty, XTreeControl.DefaultExpandedGraphicURL is used.
        """
        ...
    @abstractmethod
    def getIndex(self, Node: 'XTreeNode') -> int:
        """
        Returns the index of Node in this instances children.
        """
        ...
    @abstractmethod
    def getNodeGraphicURL(self) -> str:
        """
        The URL for a graphic that is rendered before the text part of this node.
        
        If this URL is empty, no graphic is rendered.
        """
        ...
    @abstractmethod
    def getParent(self) -> 'XTreeNode':
        """
        Returns the parent node of this node.
        """
        ...
    @abstractmethod
    def hasChildrenOnDemand(self) -> bool:
        """
        Returns TRUE if the children of this node are created on demand.
        
        A TreeControl will handle a node that returns TRUE always like a node that has child nodes, even if getChildCount() returns 0.
        """
        ...

__all__ = ['XTreeNode']

