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
# Namespace: com.sun.star.sheet
import typing
from abc import abstractmethod
from ..container.x_enumeration_access import XEnumerationAccess as XEnumerationAccess_4bac0ffc
from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
if typing.TYPE_CHECKING:
    from .x_external_doc_link import XExternalDocLink as XExternalDocLink_ef5c0d60

class XExternalDocLinks(XEnumerationAccess_4bac0ffc, XIndexAccess_f0910d6d, XNameAccess_e2ab0cf6):
    """
    Primary interface for the com.sun.star.sheet.ExternalDocLinks service.
    
    **since**
    
        OOo 3.1

    See Also:
        `API XExternalDocLinks <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XExternalDocLinks.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XExternalDocLinks'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XExternalDocLinks'

    @abstractmethod
    def addDocLink(self, aDocName: str) -> 'XExternalDocLink_ef5c0d60':
        """
        This method adds a new external document link by its URL, and returns its instance.
        
        If a document instance already exists for the specified URL, then that instance gets returned instead of creating a new one.
        """

__all__ = ['XExternalDocLinks']

