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
# Namespace: com.sun.star.xml
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .sax.x_fast_parser import XFastParser as XFastParser_c6ba0c26

class XImportFilter2(XInterface_8f010a43):
    """
    interface to implement for an XML-based import filter.
    
    Enhanced vs XImportFilter to take a XFastDocumentHandler.
    
    **since**
    
        LibreOffice 7.1

    See Also:
        `API XImportFilter2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1XImportFilter2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml'
    __ooo_full_ns__: str = 'com.sun.star.xml.XImportFilter2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.XImportFilter2'

    @abstractmethod
    def importer(self, aSourceData: 'typing.Tuple[PropertyValue_c9610c73, ...]', xFastParser: 'XFastParser_c6ba0c26', msUserData: 'typing.Tuple[str, ...]') -> bool:
        """
        performs the import.
        
        The source data (location indicated by aSourceData), and the XML representation of the document must be generated by calls to xocHandler (???) methods.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XImportFilter2']

