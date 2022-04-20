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
# Namespace: com.sun.star.datatransfer
from typing_extensions import Literal
import typing
from .x_transferable import XTransferable as XTransferable_2d800f38
if typing.TYPE_CHECKING:
    from .data_flavor import DataFlavor as DataFlavor_ffd30deb

class XTransferable2(XTransferable_2d800f38):
    """
    
    **since**
    
        LibreOffice 6.4

    See Also:
        `API XTransferable2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1XTransferable2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.datatransfer.XTransferable2']

    def getTransferData2(self, aFlavor: 'DataFlavor_ffd30deb', aDestShellID: str) -> object:
        """
        This is equivalent of getTransferData of XTransferable, but takes an additional parameter that specifies the destination document type.

        Raises:
            UnsupportedFlavorException: ``UnsupportedFlavorException``
            com.sun.star.io.IOException: ``IOException``
        """
    def isComplex(self) -> bool:
        """
        Returns true if the selection contains embedded objects or is a large text blob.
        
        **since**
        
            LibreOffice 6.4
        """

