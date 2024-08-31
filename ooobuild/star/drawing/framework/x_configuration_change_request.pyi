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
    from .x_configuration import XConfiguration as XConfiguration_8f0511a0


class XConfigurationChangeRequest(ABC):
    """
    A single explicit request for a configuration change.
    
    The requested change is committed to a configuration only when the execute() method is called. Configuration change requests are executed asynchronously. This is done to avoid reentrance problems with objects that are registered as XConfigurationChangeListener and at the same time make configuration change requests. When the requests were executed synchronously then the listeners would be notified of the changes while their request call has not yet returned.
    
    This interface is typically used internally by the XConfigurationController

    See Also:
        `API XConfigurationChangeRequest <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1XConfigurationChangeRequest.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.drawing.framework.XConfigurationChangeRequest'

    def execute(self, xConfiguration: XConfiguration_8f0511a0) -> None:
        """
        Commit the configuration change request represented by the called object to the given configuration.
        """
        ...


