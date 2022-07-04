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
# Namespace: com.sun.star.xml.crypto.sax
import typing
from abc import abstractmethod
from ....uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ...sax.x_document_handler import XDocumentHandler as XDocumentHandler_9b90e28

class XElementStackKeeper(XInterface_8f010a43):
    """
    Manipulate the \"key SAX events\" in a SAX event stream.

    See Also:
        `API XElementStackKeeper <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1sax_1_1XElementStackKeeper.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml.crypto.sax'
    __ooo_full_ns__: str = 'com.sun.star.xml.crypto.sax.XElementStackKeeper'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.xml.crypto.sax.XElementStackKeeper'

    @abstractmethod
    def retrieve(self, handler: 'XDocumentHandler_9b90e28', includingTheLastEvent: bool) -> None:
        """
        Transfers the buffered key SAX events to a document handler.
        
        All transferred events are removed from the buffer.
        """
        ...
    @abstractmethod
    def start(self) -> None:
        """
        Starts to buffer key SAX events.
        """
        ...
    @abstractmethod
    def stop(self) -> None:
        """
        Stops buffering key SAX events.
        """
        ...

__all__ = ['XElementStackKeeper']

