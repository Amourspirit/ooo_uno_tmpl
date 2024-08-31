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
# Namespace: com.sun.star.xml.sax
from __future__ import annotations
from abc import abstractmethod
from ...uno.x_interface import XInterface as XInterface_8f010a43

class XFastNamespaceHandler(XInterface_8f010a43):
    """
    Stores and manages namespace declarations of a sax document parsed by XFastParser.
    
    **since**
    
        LibreOffice 5.3

    See Also:
        `API XFastNamespaceHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1sax_1_1XFastNamespaceHandler.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.sax'
    __ooo_full_ns__: str = 'com.sun.star.xml.sax.XFastNamespaceHandler'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.sax.XFastNamespaceHandler'

    @abstractmethod
    def getNamespaceURI(self, NamespacePrefix: str) -> str:
        """
        retrieves the namespace URI of a namespace prefix
        """
        ...
    @abstractmethod
    def registerNamespace(self, NamespacePrefix: str, NamespaceURI: str) -> None:
        """
        receives notification of namespace declarations from a XFastParser.
        """
        ...

__all__ = ['XFastNamespaceHandler']

