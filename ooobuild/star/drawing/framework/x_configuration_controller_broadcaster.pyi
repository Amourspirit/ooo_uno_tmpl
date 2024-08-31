# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.drawing.framework
from __future__ import annotations
import typing

from abc import ABC
if typing.TYPE_CHECKING:
    from .configuration_change_event import ConfigurationChangeEvent as ConfigurationChangeEvent_55151590
    from .x_configuration_change_listener import XConfigurationChangeListener as XConfigurationChangeListener_adee172c


class XConfigurationControllerBroadcaster(ABC):
    """
    Manage the set of registered event listeners and the event notification for a configuration controller.
    
    The listeners are called in the order in which they are registered.

    See Also:
        `API XConfigurationControllerBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1XConfigurationControllerBroadcaster.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.drawing.framework.XConfigurationControllerBroadcaster'

    def addConfigurationChangeListener(self, xListener: XConfigurationChangeListener_adee172c, sEventType: str, aUserData: typing.Any) -> None:
        """
        Add a new listener for configuration changes.
        
        The listener is notified only for the specified type of configuration changes. When the listener is interested in more than one event type this method has to be called multiple times. Alternatively it can register as universal listener that will be called for all event types. However, this option is provided primarily to support debugging and monitoring.
        """
        ...
    def notifyEvent(self, aEvent: ConfigurationChangeEvent_55151590) -> None:
        """
        With this method other objects can send events to all the registered listeners.
        """
        ...
    def removeConfigurationChangeListener(self, xListener: XConfigurationChangeListener_adee172c) -> None:
        """
        Remove a listener for configuration changes.
        """
        ...


