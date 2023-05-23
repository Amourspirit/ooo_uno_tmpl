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
# Namespace: com.sun.star.xml.crypto.sax
import typing

from ....uno.x_interface import XInterface as XInterface_8f010a43


class XSAXEventKeeperStatusChangeListener(XInterface_8f010a43):
    """
    Interface of SAXEventKeeper Status Change Listener.
    
    This interface is used to receive the SAXEventKeeper status change notification.

    See Also:
        `API XSAXEventKeeperStatusChangeListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1sax_1_1XSAXEventKeeperStatusChangeListener.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.xml.crypto.sax.XSAXEventKeeperStatusChangeListener'

    def blockingStatusChanged(self, isBlocking: bool) -> None:
        """
        Notifies the SAXEventKeeper is entering/leaving blocking state.
        """
        ...
    def bufferStatusChanged(self, isBufferEmpty: bool) -> None:
        """
        Notifies the SAXEventKeeper's buffer is empty/not empty.
        """
        ...
    def collectionStatusChanged(self, isInsideCollectedElement: bool) -> None:
        """
        Notifies the SAXEventKeeper is entering/leaving collecting state.
        """
        ...

