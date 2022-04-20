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
# Namespace: com.sun.star.util
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_mode_change_approve_listener import XModeChangeApproveListener as XModeChangeApproveListener_7807110c
    from .x_mode_change_listener import XModeChangeListener as XModeChangeListener_9c30e2f

class XModeChangeBroadcaster(XInterface_8f010a43):
    """
    broadcasts changes in an object's internal mode.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XModeChangeBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XModeChangeBroadcaster.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.util.XModeChangeBroadcaster']

    def addModeChangeApproveListener(self, rxListener: 'XModeChangeApproveListener_7807110c') -> None:
        """
        adds the given listener to the list of components to be notified when the mode is about to change.

        Raises:
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
    def addModeChangeListener(self, rxListener: 'XModeChangeListener_9c30e2f') -> None:
        """
        adds the given listener to the list of components to be notified when the mode changes.
        """
    def removeModeChangeApproveListener(self, rxListener: 'XModeChangeApproveListener_7807110c') -> None:
        """
        remove the given listener from the list of components to be notified when the mode is about to change.

        Raises:
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
    def removeModeChangeListener(self, rxListener: 'XModeChangeListener_9c30e2f') -> None:
        """
        removes the given listener from the list of components to be notified when the mode changes.
        """

