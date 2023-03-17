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
# Libre Office Version: 7.4
# Namespace: com.sun.star.document
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_document_properties import XDocumentProperties as XDocumentProperties_4c31102b

class XDocumentPropertiesSupplier(ABC):
    """
    provides access to the XDocumentProperties instance of a document.
    
    A DocumentProperties instance is available on loaded documents via this supplier interface.
    
    **since**
    
        OOo 3.0

    See Also:
        `API XDocumentPropertiesSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XDocumentPropertiesSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.XDocumentPropertiesSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.document.XDocumentPropertiesSupplier'

    @abstractmethod
    def getDocumentProperties(self) -> 'XDocumentProperties_4c31102b':
        """
        provides the document properties object.
        """
        ...

__all__ = ['XDocumentPropertiesSupplier']

