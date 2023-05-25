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
# Namespace: com.sun.star.xml.dom
from __future__ import annotations
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_node import XNode as XNode_83fb09a5

class XNamedNodeMap(XInterface_8f010a43):
    """

    See Also:
        `API XNamedNodeMap <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1dom_1_1XNamedNodeMap.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.dom'
    __ooo_full_ns__: str = 'com.sun.star.xml.dom.XNamedNodeMap'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.dom.XNamedNodeMap'

    @abstractmethod
    def getLength(self) -> int:
        """
        The number of nodes in this map.
        """
        ...
    @abstractmethod
    def getNamedItem(self, name: str) -> XNode_83fb09a5:
        """
        Retrieves a node specified by local name.
        """
        ...
    @abstractmethod
    def getNamedItemNS(self, namespaceURI: str, localName: str) -> XNode_83fb09a5:
        """
        Retrieves a node specified by local name and namespace URI.
        """
        ...
    @abstractmethod
    def item(self, index: int) -> XNode_83fb09a5:
        """
        Returns a node specified by index.
        """
        ...
    @abstractmethod
    def removeNamedItem(self, name: str) -> XNode_83fb09a5:
        """
        Removes a node specified by name.
        
        Throws: DOMException - NOT_FOUND_ERR: Raised if there is no node named name in this map. NO_MODIFICATION_ALLOWED_ERR: Raised if this map is readonly.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def removeNamedItemNS(self, namespaceURI: str, localName: str) -> XNode_83fb09a5:
        """
        Removes a node specified by local name and namespace URI.
        
        Throws: DOMException - NOT_FOUND_ERR: Raised if there is no node with the specified namespaceURI and localName in this map. NO_MODIFICATION_ALLOWED_ERR: Raised if this map is readonly.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def setNamedItem(self, arg: XNode_83fb09a5) -> XNode_83fb09a5:
        """
        Adds a node using its nodeName attribute.
        
        Throws: DOMException - WRONG_DOCUMENT_ERR: Raised if arg was created from a different document than the one that created this map. NO_MODIFICATION_ALLOWED_ERR: Raised if this map is readonly. INUSE_ATTRIBUTE_ERR: Raised if arg is an Attr that is already an attribute of another Element object. The DOM user must explicitly clone Attr nodes to re-use them in other elements. HIERARCHY_REQUEST_ERR: Raised if an attempt is made to add a node doesn't belong in this NamedNodeMap. Examples would include trying to insert something other than an Attr node into an Element's map of attributes, or a non-Entity node into the DocumentType's map of Entities.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def setNamedItemNS(self, arg: XNode_83fb09a5) -> XNode_83fb09a5:
        """
        Adds a node using its namespaceURI and localName.
        
        Throws: DOMException - WRONG_DOCUMENT_ERR: Raised if arg was created from a different document than the one that created this map. NO_MODIFICATION_ALLOWED_ERR: Raised if this map is readonly. INUSE_ATTRIBUTE_ERR: Raised if arg is an Attr that is already an attribute of another Element object. The DOM user must explicitly clone Attr nodes to re-use them in other elements. HIERARCHY_REQUEST_ERR: Raised if an attempt is made to add a node doesn't belong in this NamedNodeMap. Examples would include trying to insert something other than an Attr node into an Element's map of attributes, or a non-Entity node into the DocumentType's map of Entities. NOT_SUPPORTED_ERR: Always thrown if the current document does not support the \"XML\" feature, since namespaces were defined by XML.

        Raises:
            DOMException: ``DOMException``
        """
        ...

__all__ = ['XNamedNodeMap']


