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
# Namespace: com.sun.star.datatransfer
from __future__ import annotations
import uno
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XSystemTransferable(XInterface_8f010a43):
    """
    Interface to be implemented by objects used to provide system dependent data for a transfer operation.
    
    Those objects usually also implement XTransferable.

    See Also:
        `API XSystemTransferable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1XSystemTransferable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.datatransfer'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.XSystemTransferable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.datatransfer.XSystemTransferable'

    @abstractmethod
    def getData(self, aProcessId: uno.ByteSequence) -> object:
        """
        Called by a data consumer to obtain a system specific data object from the source.
        
        The data object is returned in an any. The contained type may differ on different platforms.
        
        Notes:Under Windows the returned any contains an unsigned long which represents a pointer to an IDataObject interface. The caller of getData has to release the data object (IDataObject.Release) if it is no longer needed. The caller must also make sure that the current thread has been initialized for OLE (use OleInitialize).
        """
        ...

__all__ = ['XSystemTransferable']


