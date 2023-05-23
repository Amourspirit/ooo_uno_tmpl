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
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d

class XViewDataSupplier(XInterface_8f010a43):
    """
    gives access to some properties describing all open views to a document
    
    Each view is described by a sequence< .com.sun.star.beans.PropertyValue >. Through this interface the state of all open views can be retrieved and restored later. These states can also be made persistent so that a document loader can create all views of the correct types and restore their state to the state when the document was saved.

    See Also:
        `API XViewDataSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XViewDataSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.document'
    __ooo_full_ns__: str = 'com.sun.star.document.XViewDataSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.document.XViewDataSupplier'

    @abstractmethod
    def getViewData(self) -> XIndexAccess_f0910d6d:
        """
        retrieve information about currently opened view to restore it later
        """
        ...
    @abstractmethod
    def setViewData(self, Data: XIndexAccess_f0910d6d) -> None:
        """
        restore all views which will be represented by given data argument
        """
        ...

__all__ = ['XViewDataSupplier']

