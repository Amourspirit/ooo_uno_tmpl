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
# Namespace: com.sun.star.xml.input
from typing_extensions import Literal
import typing
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_attributes import XAttributes as XAttributes_e31a0d36

class XElement(XInterface_8f010a43):
    """
    Capsule around an XML element.

    See Also:
        `API XElement <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1input_1_1XElement.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.input.XElement']

    def characters(self, chars: str) -> None:
        """
        Called upon retrieval of characters.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    def endElement(self) -> None:
        """
        Receives notification of element closing.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    def getAttributes(self) -> 'XAttributes_e31a0d36':
        """
        Gets the attributes of this element.
        """
        ...
    def getLocalName(self) -> str:
        """
        Gets the local name of this element.
        """
        ...
    def getParent(self) -> 'XElement':
        """
        Gets the parent context.
        """
        ...
    def getUid(self) -> int:
        """
        Gets the namespace uid of this element.
        """
        ...
    def ignorableWhitespace(self, whitespace: str) -> None:
        """
        Receives notification of white space that can be ignored.

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
    def startChildElement(self, uid: int, localName: str, xAttributes: 'XAttributes_e31a0d36') -> 'XElement':
        """
        Called upon each occurring child element.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...


