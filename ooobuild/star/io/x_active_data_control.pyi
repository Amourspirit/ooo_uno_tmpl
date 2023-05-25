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
# Namespace: com.sun.star.io
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_stream_listener import XStreamListener as XStreamListener_baf80bea


class XActiveDataControl(XInterface_8f010a43):
    """
    makes it possible to control an active data source.
    
    This interface should be supported by objects which implement XActiveDataSource or XActiveDataSink.

    See Also:
        `API XActiveDataControl <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XActiveDataControl.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.io.XActiveDataControl'

    def addListener(self, aListener: XStreamListener_baf80bea) -> None:
        """
        registers an object to receive events from this data source.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.
        """
        ...
    def removeListener(self, aListener: XStreamListener_baf80bea) -> None:
        """
        unregisters an object to receive events from this data source.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.
        """
        ...
    def start(self) -> None:
        """
        starts I/O.
        
        Either XActiveDataControl.setInputStream() or XActiveDataControl.setOutputStream() must be called beforehand.
        
        This method does not block the thread, so reading is generally not finished when the method returns.
        """
        ...
    def terminate(self) -> None:
        """
        does a weak abort.
        
        It closes all connected resources and calls XInputStream.close() or XOutputStream.close() and fires the XStreamListener.terminated()-event.
        """
        ...



