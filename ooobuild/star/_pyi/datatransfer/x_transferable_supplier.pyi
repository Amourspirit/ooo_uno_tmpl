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
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from .x_transferable import XTransferable as XTransferable_2d800f38

class XTransferableSupplier(ABC):
    """

    See Also:
        `API XTransferableSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1XTransferableSupplier.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.datatransfer.XTransferableSupplier']

    def getTransferable(self) -> 'XTransferable_2d800f38':
        """
        To get access to a transferable representation of a selected part of an object.
        """
    def insertTransferable(self, xTrans: 'XTransferable_2d800f38') -> None:
        """
        Hands over a transferable object that shall be inserted.
        
        A NULL value is not allowed.

        Raises:
            UnsupportedFlavorException: ``UnsupportedFlavorException``
        """

