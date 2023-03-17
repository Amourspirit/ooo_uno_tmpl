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
# Namespace: com.sun.star.media
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_player_listener import XPlayerListener as XPlayerListener_e0ac0d13

class XPlayerNotifier(XInterface_8f010a43):
    """
    Interface to be implemented in order to support listener management.
    
    **since**
    
        LibreOffice 7.4

    See Also:
        `API XPlayerNotifier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1media_1_1XPlayerNotifier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.media'
    __ooo_full_ns__: str = 'com.sun.star.media.XPlayerNotifier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.media.XPlayerNotifier'

    @abstractmethod
    def addPlayerListener(self, xListener: 'XPlayerListener_e0ac0d13') -> None:
        """
        Interface for clients to register as XPlayerListener.
        
        Invalid interfaces or NULL values will be ignored.
        """
        ...
    @abstractmethod
    def removePlayerListener(self, xListener: 'XPlayerListener_e0ac0d13') -> None:
        """
        Interface for clients to unregister as XPlayerListener.
        
        Invalid interfaces or NULL values will be ignored.
        """
        ...

__all__ = ['XPlayerNotifier']

