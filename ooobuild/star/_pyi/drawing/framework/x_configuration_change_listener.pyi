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
# Namespace: com.sun.star.drawing.framework
from typing_extensions import Literal
import typing
from ...lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .configuration_change_event import ConfigurationChangeEvent as ConfigurationChangeEvent_55151590

class XConfigurationChangeListener(XEventListener_c7230c4a):
    """
    A listener for configuration changes is called when it has been registered at the configuration controller and a configuration change occurs.

    See Also:
        `API XConfigurationChangeListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1XConfigurationChangeListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.drawing.framework.XConfigurationChangeListener']

    def notifyConfigurationChange(self, aEvent: 'ConfigurationChangeEvent_55151590') -> None:
        """
        The exact time of when a listener is called (before the change takes place, during the change, or when the change has been made) depends on the change event.
        
        The order in which listeners are called is the order in which they are registered (First registered, first called.)
        """
        ...


