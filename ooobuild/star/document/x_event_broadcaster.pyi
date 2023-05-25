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

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_event_listener import XEventListener as XEventListener_ff7f0e07


class XEventBroadcaster(XInterface_8f010a43):
    """
    makes it possible to register listeners which are called whenever a document event (see EventObject) occurs
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XEventBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XEventBroadcaster.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.document.XEventBroadcaster'

    def addEventListener(self, Listener: XEventListener_ff7f0e07) -> None:
        """
        registers the given listener
        """
        ...
    def removeEventListener(self, Listener: XEventListener_ff7f0e07) -> None:
        """
        unregisters the given listener
        """
        ...



