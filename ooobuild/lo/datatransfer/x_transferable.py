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
# Namespace: com.sun.star.datatransfer
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .data_flavor import DataFlavor as DataFlavor_ffd30deb

class XTransferable(XInterface_8f010a43):
    """
    Interface to be implemented by objects used to provide data for a data transfer operation.

    See Also:
        `API XTransferable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1XTransferable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.datatransfer'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.XTransferable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.datatransfer.XTransferable'

    @abstractmethod
    def getTransferData(self, aFlavor: 'DataFlavor_ffd30deb') -> object:
        """
        Called by a data consumer to obtain data from the source in a specified format.

        Raises:
            UnsupportedFlavorException: ``UnsupportedFlavorException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    @abstractmethod
    def getTransferDataFlavors(self) -> 'typing.Tuple[DataFlavor_ffd30deb, ...]':
        """
        Returns a sequence of supported DataFlavor.
        """
        ...
    @abstractmethod
    def isDataFlavorSupported(self, aFlavor: 'DataFlavor_ffd30deb') -> bool:
        """
        Checks if the data object supports the specified data flavor.
        
        A value of FALSE if the DataFlavor is unsupported by the transfer source.
        
        Note: This method is only for analogy with the JAVA Clipboard interface. To avoid many calls, the caller should instead use com.sun.star.datatransfer.XTransferable.getTransferDataFlavors().
        """
        ...

__all__ = ['XTransferable']

