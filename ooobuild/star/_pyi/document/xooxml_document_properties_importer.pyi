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
# Namespace: com.sun.star.document
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_document_properties import XDocumentProperties as XDocumentProperties_4c31102b
    from ..embed.x_storage import XStorage as XStorage_8e460a32
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4


class XOOXMLDocumentPropertiesImporter(XInterface_8f010a43):
    """
    allows to import the document properties from OOXML format
    
    **since**
    
        LibreOffice 7.3

    See Also:
        `API XOOXMLDocumentPropertiesImporter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XOOXMLDocumentPropertiesImporter.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.document.XOOXMLDocumentPropertiesImporter']

    def getCorePropertiesStream(self, xSource: 'XStorage_8e460a32') -> 'XInputStream_98d40ab4':
        """
        find and get core properties stream
        
        (usually it is docProps\\core.xml)
        
        **since**
        
            LibreOffice 7.3
        """
        ...
    def getCustomPropertiesStreams(self, xSource: 'XStorage_8e460a32') -> 'typing.Tuple[XInputStream_98d40ab4, ...]':
        """
        find and get custom properties streams
        
        (usually it is customXml*.xml)
        
        **since**
        
            LibreOffice 7.3
        """
        ...
    def getExtendedPropertiesStream(self, xSource: 'XStorage_8e460a32') -> 'XInputStream_98d40ab4':
        """
        find and get extended properties stream
        
        (usually it is docProps/app.xml)
        
        **since**
        
            LibreOffice 7.3
        """
        ...
    def importProperties(self, xSource: 'XStorage_8e460a32', xDocumentProperties: 'XDocumentProperties_4c31102b') -> None:
        """
        allows to import the document properties from OOXML format
        
        The implementation should parse the document properties from OOXML format storage and set them to the target XDocumentProperties implementation.
        
        The storage must represent OOXML format and support com.sun.star.embed.XRelationshipAccess interface. Please see com.sun.star.embed.StorageFactory for details regarding creation of such a storage.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.xml.sax.SAXException: ``SAXException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...


