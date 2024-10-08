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
# Namespace: com.sun.star.xml.input
from __future__ import annotations
import typing

from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_attributes import XAttributes as XAttributes_e31a0d36
    from .x_element import XElement as XElement_bc5b0bd9
    from .x_namespace_mapping import XNamespaceMapping as XNamespaceMapping_38700f68
    from ..sax.x_locator import XLocator as XLocator_a3fb0aff


class XRoot(XInterface_8f010a43):
    """
    Root interface being passed to SaxDocumentHandler service upon instantiation.

    See Also:
        `API XRoot <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1input_1_1XRoot.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.xml.input.XRoot'

    def endDocument(self) -> None:
        """
        Receives notification of the end of a document.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    def processingInstruction(self, target: str, data: str) -> None:
        """
        Receives notification of a processing instruction.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    def setDocumentLocator(self, locator: XLocator_a3fb0aff) -> None:
        """
        Receives an object for locating the origin of SAX document events.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    def startDocument(self, xMapping: XNamespaceMapping_38700f68) -> None:
        """
        Receives notification of the beginning of a document.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    def startRootElement(self, uid: int, localName: str, xAttributes: XAttributes_e31a0d36) -> XElement_bc5b0bd9:
        """
        Called upon root element.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...


