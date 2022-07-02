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
# Namespace: com.sun.star.xml.dom
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .node_type import NodeType as NodeType_a3b00aef
    from .x_document import XDocument as XDocument_aebc0b5e
    from .x_named_node_map import XNamedNodeMap as XNamedNodeMap_de600ca8
    from .x_node_list import XNodeList as XNodeList_ae540b41

class XNode(XInterface_8f010a43):
    """
    The primary dom datatype.
    
    The Node interface is the primary datatype for the entire Document Object Model. It represents a single node in the document tree. While all objects implementing the Node interface expose methods for dealing with children, not all objects implementing the Node interface may have children. For example, Text nodes may not have children, and adding children to such nodes results in a DOMException being raised.
    
    The attributes nodeName, nodeValue and attributes are included as a mechanism to get at node information without casting down to the specific derived interface. In cases where there is no obvious mapping of these attributes for a specific nodeType (e.g., nodeValue for an Element or attributes for a Comment ), this returns null. Note that the specialized interfaces may contain additional and more convenient mechanisms to get and set the relevant information.
    
    The values of nodeName, nodeValue, and attributes vary according to the node type as follows:
    
    **since**
    
        OOo 2.0

    See Also:
        `API XNode <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1dom_1_1XNode.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.dom'
    __ooo_full_ns__: str = 'com.sun.star.xml.dom.XNode'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.dom.XNode'

    @abstractmethod
    def appendChild(self, newChild: 'XNode') -> 'XNode':
        """
        Adds the node newChild to the end of the list of children of this node.
        
        HIERARCHY_REQUEST_ERR: Raised if this node is of a type that does not allow children of the type of the newChild node, or if the node to append is one of this node's ancestors or this node itself.
        
        WRONG_DOCUMENT_ERR: Raised if newChild was created from a different document than the one that created this node.
        
        NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly or if the previous parent of the node being inserted is readonly.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def cloneNode(self, deep: bool) -> 'XNode':
        """
        Returns a duplicate of this node, i.e., serves as a generic copy constructor for nodes.
        """
        ...
    @abstractmethod
    def getAttributes(self) -> 'XNamedNodeMap_de600ca8':
        """
        A NamedNodeMap containing the attributes of this node (if it is an Element) or null otherwise.
        """
        ...
    @abstractmethod
    def getChildNodes(self) -> 'XNodeList_ae540b41':
        """
        A NodeList that contains all children of this node.
        """
        ...
    @abstractmethod
    def getFirstChild(self) -> 'XNode':
        """
        The first child of this node.
        """
        ...
    @abstractmethod
    def getLastChild(self) -> 'XNode':
        """
        The last child of this node.
        """
        ...
    @abstractmethod
    def getLocalName(self) -> str:
        """
        Returns the local part of the qualified name of this node.
        """
        ...
    @abstractmethod
    def getNamespaceURI(self) -> str:
        """
        The namespace URI of this node, or null if it is unspecified.
        """
        ...
    @abstractmethod
    def getNextSibling(self) -> 'XNode':
        """
        The node immediately following this node.
        """
        ...
    @abstractmethod
    def getNodeName(self) -> str:
        """
        The name of this node, depending on its type; see the table above.
        """
        ...
    @abstractmethod
    def getNodeType(self) -> 'NodeType_a3b00aef':
        """
        A code representing the type of the underlying object, as defined above.
        """
        ...
    @abstractmethod
    def getNodeValue(self) -> str:
        """
        The value of this node, depending on its type; see the table above.
        
        DOMSTRING_SIZE_ERR: Raised when it would return more characters than fit in a DOMString variable on the implementation platform.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def getOwnerDocument(self) -> 'XDocument_aebc0b5e':
        """
        The Document object associated with this node.
        """
        ...
    @abstractmethod
    def getParentNode(self) -> 'XNode':
        """
        The parent of this node.
        """
        ...
    @abstractmethod
    def getPrefix(self) -> str:
        """
        The namespace prefix of this node, or null if it is unspecified.
        """
        ...
    @abstractmethod
    def getPreviousSibling(self) -> 'XNode':
        """
        The node immediately preceding this node.
        """
        ...
    @abstractmethod
    def hasAttributes(self) -> bool:
        """
        Returns whether this node (if it is an element) has any attributes.
        """
        ...
    @abstractmethod
    def hasChildNodes(self) -> bool:
        """
        Returns whether this node has any children.
        """
        ...
    @abstractmethod
    def insertBefore(self, newChild: 'XNode', refChild: 'XNode') -> 'XNode':
        """
        Inserts the node newChild before the existing child node refChild.
        
        HIERARCHY_REQUEST_ERR: Raised if this node is of a type that does not allow children of the type of the newChild node, or if the node to insert is one of this node's ancestors or this node itself.
        
        WRONG_DOCUMENT_ERR: Raised if newChild was created from a different document than the one that created this node.
        
        NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly or if the parent of the node being inserted is readonly.
        
        NOT_FOUND_ERR: Raised if refChild is not a child of this node.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def isSupported(self, feature: str, ver: str) -> bool:
        """
        Tests whether the DOM implementation implements a specific feature and that feature is supported by this node.
        """
        ...
    @abstractmethod
    def normalize(self) -> None:
        """
        Puts all Text nodes in the full depth of the sub-tree underneath this Node, including attribute nodes, into a \"normal\" form where only structure (e.g., elements, comments, processing instructions, CDATA sections, and entity references) separates Text nodes, i.e., there are neither adjacent Text nodes nor empty Text nodes.
        """
        ...
    @abstractmethod
    def removeChild(self, oldChild: 'XNode') -> 'XNode':
        """
        Removes the child node indicated by oldChild from the list of children, and returns it.
        
        NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.
        
        NOT_FOUND_ERR: Raised if oldChild is not a child of this node.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def replaceChild(self, newChild: 'XNode', oldChild: 'XNode') -> 'XNode':
        """
        Replaces the child node oldChild with newChild in the list of children, and returns the oldChild node.
        
        HIERARCHY_REQUEST_ERR: Raised if this node is of a type that does not allow children of the type of the newChild node, or if the node to put in is one of this node's ancestors or this node itself.
        
        WRONG_DOCUMENT_ERR: Raised if newChild was created from a different document than the one that created this node.
        
        NO_MODIFICATION_ALLOWED_ERR: Raised if this node or the parent of the new node is readonly.
        
        NOT_FOUND_ERR: Raised if oldChild is not a child of this node.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def setNodeValue(self, nodeValue: str) -> None:
        """
        The value of this node, depending on its type; see the table above.
        
        NO_MODIFICATION_ALLOWED_ERR: Raised when the node is readonly.
        
        DOMSTRING_SIZE_ERR: Raised when it would return more characters than fit in a DOMString variable on the implementation platform.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def setPrefix(self, prefix: str) -> None:
        """
        The namespace prefix of this node, or null if it is unspecified.
        
        INVALID_CHARACTER_ERR: Raised if the specified prefix contains an illegal character, per the XML 1.0 specification .
        
        NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.
        
        NAMESPACE_ERR: Raised if the specified prefix is malformed per the Namespaces in XML specification, if the namespaceURI of this node is null, if the specified prefix is \"xml\" and the namespaceURI of this node is different from \"http://www.w3.org/XML/1998/namespace\", if this node is an attribute and the specified prefix is \"xmlns\" and the namespaceURI of this node is different from \" http://www.w3.org/2000/xmlns/\", or if this node is an attribute and the qualifiedName of this node is \"xmlns\" .

        Raises:
            DOMException: ``DOMException``
        """
        ...

__all__ = ['XNode']

