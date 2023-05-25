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
# Namespace: com.sun.star.xml.sax
from __future__ import annotations
import typing
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_fast_attribute_list import XFastAttributeList as XFastAttributeList_274d0f09

class XFastContextHandler(XInterface_8f010a43):
    """
    receives notification of sax document events from a XFastParser.

    See Also:
        `API XFastContextHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1sax_1_1XFastContextHandler.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.sax'
    __ooo_full_ns__: str = 'com.sun.star.xml.sax.XFastContextHandler'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.sax.XFastContextHandler'

    @abstractmethod
    def characters(self, aChars: str) -> None:
        """
        receives notification of character data.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    @abstractmethod
    def createFastChildContext(self, Element: int, Attribs: XFastAttributeList_274d0f09) -> XFastContextHandler:
        """
        receives notification of the beginning of a known child element.
        
        If the element has a namespace that was registered with the XFastParser, Element contains the integer token of the elements local name from the XFastTokenHandler and the integer token of the namespace combined with an arithmetic or operation.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    @abstractmethod
    def createUnknownChildContext(self, Namespace: str, Name: str, Attribs: XFastAttributeList_274d0f09) -> XFastContextHandler:
        """
        receives notification of the beginning of an unknown child element .

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    @abstractmethod
    def endFastElement(self, Element: int) -> None:
        """
        receives notification of the end of a known element.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    @abstractmethod
    def endUnknownElement(self, Namespace: str, Name: str) -> None:
        """
        receives notification of the end of a known element.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    @abstractmethod
    def startFastElement(self, Element: int, Attribs: XFastAttributeList_274d0f09) -> None:
        """
        receives notification of the beginning of an element .
        
        If the element has a namespace that was registered with the XFastParser, Element contains the integer token of the elements local name from the XFastTokenHandler and the integer token of the namespace combined with an arithmetic or operation.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    @abstractmethod
    def startUnknownElement(self, Namespace: str, Name: str, Attribs: XFastAttributeList_274d0f09) -> None:
        """
        receives notification of the beginning of an unknown element .

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...

__all__ = ['XFastContextHandler']


