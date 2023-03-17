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
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..embed.x_storage import XStorage as XStorage_8e460a32

class XDocumentSubStorageSupplier(XInterface_8f010a43):
    """
    through this interface documents can provide access to their substorages
    
    A temporary interface to get access to documents substorages.

    See Also:
        `API XDocumentSubStorageSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XDocumentSubStorageSupplier.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.document.XDocumentSubStorageSupplier']

    def getDocumentSubStorage(self, StorageName: str, nMode: int) -> 'XStorage_8e460a32':
        """
        provides the access to a substorage with specified name
        """
        ...
    def getDocumentSubStoragesNames(self) -> 'typing.Tuple[str, ...]':
        """
        provides the list of substorages

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...


