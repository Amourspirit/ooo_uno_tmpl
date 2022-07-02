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
# Libre Office Version: 7.2
# Namespace: com.sun.star.xml.dom
import typing
from abc import abstractmethod
from .x_node import XNode as XNode_83fb09a5
if typing.TYPE_CHECKING:
    from .x_attr import XAttr as XAttr_840309ba
    from .xcdata_section import XCDATASection as XCDATASection_d9c00c51
    from .x_comment import XComment as XComment_a3690af2
    from .xdom_implementation import XDOMImplementation as XDOMImplementation_22320ec5
    from .x_document_fragment import XDocumentFragment as XDocumentFragment_17850e92
    from .x_document_type import XDocumentType as XDocumentType_e0340d00
    from .x_element import XElement as XElement_a33d0ae9
    from .x_entity_reference import XEntityReference as XEntityReference_9b70e2b
    from .x_node_list import XNodeList as XNodeList_ae540b41
    from .x_processing_instruction import XProcessingInstruction as XProcessingInstruction_691810de
    from .x_text import XText as XText_842c09c4

class XDocument(XNode_83fb09a5):
    """

    See Also:
        `API XDocument <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1dom_1_1XDocument.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.dom'
    __ooo_full_ns__: str = 'com.sun.star.xml.dom.XDocument'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.dom.XDocument'

    @abstractmethod
    def createAttribute(self, name: str) -> 'XAttr_840309ba':
        """
        Creates an Attr of the given name.
        
        Throws: DOMException - INVALID_CHARACTER_ERR: Raised if the specified name contains an illegal character.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def createAttributeNS(self, namespaceURI: str, qualifiedName: str) -> 'XAttr_840309ba':
        """
        Creates an attribute of the given qualified name and namespace URI.
        
        Throws: DOMException - INVALID_CHARACTER_ERR: Raised if the specified qualified name contains an illegal character, per the XML 1.0 specification . NAMESPACE_ERR: Raised if the qualifiedName is malformed per the Namespaces in XML specification, if the qualifiedName has a prefix and the namespaceURI is null, if the qualifiedName has a prefix that is \"xml\" and the namespaceURI is different from \" http://www.w3.org/XML/1998/namespace\", or if the qualifiedName, or its prefix, is \"xmlns\" and the namespaceURI is different from \" http://www.w3.org/2000/xmlns/\". NOT_SUPPORTED_ERR: Always thrown if the current document does not support the \"XML\" feature, since namespaces were defined by XML.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def createCDATASection(self, data: str) -> 'XCDATASection_d9c00c51':
        """
        Creates a CDATASection node whose value is the specified string.
        
        Throws: DOMException - NOT_SUPPORTED_ERR: Raised if this document is an HTML document.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def createComment(self, data: str) -> 'XComment_a3690af2':
        """
        Creates a Comment node given the specified string.
        """
        ...
    @abstractmethod
    def createDocumentFragment(self) -> 'XDocumentFragment_17850e92':
        """
        Creates an empty DocumentFragment object.
        """
        ...
    @abstractmethod
    def createElement(self, tagName: str) -> 'XElement_a33d0ae9':
        """
        Creates an element of the type specified.
        
        Throws: DOMException - INVALID_CHARACTER_ERR: Raised if the specified name contains an illegal character.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def createElementNS(self, namespaceURI: str, qualifiedName: str) -> 'XElement_a33d0ae9':
        """
        Creates an element of the given qualified name and namespace URI.
        
        Throws: DOMException - INVALID_CHARACTER_ERR: Raised if the specified qualified name contains an illegal character, per the XML 1.0 specification . NAMESPACE_ERR: Raised if the qualifiedName is malformed per the Namespaces in XML specification, if the qualifiedName has a prefix and the namespaceURI is null, or if the qualifiedName has a prefix that is \"xml\" and the namespaceURI is different from \" http://www.w3.org/XML/1998/namespace\" . NOT_SUPPORTED_ERR: Always thrown if the current document does not support the \"XML\" feature, since namespaces were defined by XML.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def createEntityReference(self, name: str) -> 'XEntityReference_9b70e2b':
        """
        Throws: DOMException - NOT_SUPPORTED_ERR: Raised if the type of node being imported is not supported.
        
        Creates an EntityReference object. Throws: DOMException - INVALID_CHARACTER_ERR: Raised if the specified name contains an illegal character. NOT_SUPPORTED_ERR: Raised if this document is an HTML document.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def createProcessingInstruction(self, target: str, data: str) -> 'XProcessingInstruction_691810de':
        """
        Creates a ProcessingInstruction node given the specified name and data strings.
        
        Throws: DOMException - INVALID_CHARACTER_ERR: Raised if the specified target contains an illegal character. NOT_SUPPORTED_ERR: Raised if this document is an HTML document.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    @abstractmethod
    def createTextNode(self, data: str) -> 'XText_842c09c4':
        """
        Creates a Text node given the specified string.
        """
        ...
    @abstractmethod
    def getDoctype(self) -> 'XDocumentType_e0340d00':
        """
        The Document Type Declaration (see DocumentType) associated with this document.
        """
        ...
    @abstractmethod
    def getDocumentElement(self) -> 'XElement_a33d0ae9':
        """
        This is a convenience attribute that allows direct access to the child node that is the root element of the document.
        """
        ...
    @abstractmethod
    def getElementById(self, elementId: str) -> 'XElement_a33d0ae9':
        """
        Returns the Element whose ID is given by elementId.
        """
        ...
    @abstractmethod
    def getElementsByTagName(self, tagname: str) -> 'XNodeList_ae540b41':
        """
        Returns a NodeList of all the Elements with a given tag name in the order in which they are encountered in a preorder traversal of the Document tree.
        """
        ...
    @abstractmethod
    def getElementsByTagNameNS(self, namespaceURI: str, localName: str) -> 'XNodeList_ae540b41':
        """
        Returns a NodeList of all the Elements with a given local name and namespace URI in the order in which they are encountered in a preorder traversal of the Document tree.
        """
        ...
    @abstractmethod
    def getImplementation(self) -> 'XDOMImplementation_22320ec5':
        """
        The DOMImplementation object that handles this document.
        """
        ...
    @abstractmethod
    def importNode(self, importedNode: 'XNode_83fb09a5', deep: bool) -> 'XNode_83fb09a5':
        """
        Imports a node from another document to this document.
        
        Throws: DOMException - NOT_SUPPORTED_ERR: Raised if the type of node being imported is not supported.

        Raises:
            DOMException: ``DOMException``
        """
        ...

__all__ = ['XDocument']

