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
# Namespace: com.sun.star.awt.tree
import typing
from abc import abstractmethod
from .x_tree_data_model import XTreeDataModel as XTreeDataModel_f9fc0d85
if typing.TYPE_CHECKING:
    from .x_mutable_tree_node import XMutableTreeNode as XMutableTreeNode_17d80e6a

class XMutableTreeDataModel(XTreeDataModel_f9fc0d85):
    """
    This is the editable version of the XTreeDataModel.
    
    Note that only XTreeNode created from the same instance with createNode() are valid nodes for this instance.

    See Also:
        `API XMutableTreeDataModel <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1tree_1_1XMutableTreeDataModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.tree'
    __ooo_full_ns__: str = 'com.sun.star.awt.tree.XMutableTreeDataModel'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.tree.XMutableTreeDataModel'

    @abstractmethod
    def createNode(self, DisplayValue: object, ChildrenOnDemand: bool) -> 'XMutableTreeNode_17d80e6a':
        """
        creates a new tree node with the given value and given settings.
        """
        ...
    @abstractmethod
    def setRoot(self, RootNode: 'XMutableTreeNode_17d80e6a') -> None:
        """
        changes the root node of this model to RootNode.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XMutableTreeDataModel']

