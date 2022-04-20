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
# Namespace: com.sun.star.xml.sax
from typing_extensions import Literal
from .x_document_handler import XDocumentHandler as XDocumentHandler_9b90e28

class XExtendedDocumentHandler(XDocumentHandler_9b90e28):
    """
    this interface does not conform to the SAX-standard.
    
    Note: Whether or not every callback is supported is dependent on the parser implementation.

    See Also:
        `API XExtendedDocumentHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1sax_1_1XExtendedDocumentHandler.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.sax.XExtendedDocumentHandler']

    def allowLineBreak(self) -> None:
        """
        informs a writer that it is allowable to insert a line break and indentation before the next XDocumentHandler-call.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    def comment(self, sComment: str) -> None:
        """
        receives notification about a comment in the XML-source.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    def endCDATA(self) -> None:
        """
        informs about the end of a CDATA-Section.
        
        Note that startCDATA/endCDATA MUST NOT enclose any startElement/endElement-call!

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    def startCDATA(self) -> None:
        """
        receives notification about the start of a CDATA section in the XML-source.
        
        Any string coming in via character handler may include chars, that would otherwise be interpreted as markup.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    def unknown(self, sString: str) -> None:
        """
        notifies that any characters that cannot be handled by other callback methods are announced through this method.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """

