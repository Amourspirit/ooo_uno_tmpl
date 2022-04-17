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
from abc import ABC
if typing.TYPE_CHECKING:
    from .x_configuration_change_request import XConfigurationChangeRequest as XConfigurationChangeRequest_96e716cf

class XConfigurationControllerRequestQueue(ABC):
    """
    The request queue of the configuration controller handles requests for changes to the current configuration.
    
    This interface allows callers to add requests to the back of the queue and to determine whether the queue is empty. Using this interface should normally not be necessary for anyone else than the XConfigurationController. It may be removed in the future.

    See Also:
        `API XConfigurationControllerRequestQueue <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1XConfigurationControllerRequestQueue.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.drawing.framework.XConfigurationControllerRequestQueue']

    def hasPendingRequests(self) -> bool:
        """
        Return whether there are pending requests for configuration changes.
        """
    def postChangeRequest(self, xRequest: 'XConfigurationChangeRequest_96e716cf') -> None:
        """
        Add a request for a configuration change to the request queue.
        
        This method should not be called from outside the drawing framework. Other sub controllers of the drawing framework are typical callers. They can add change requests that can not be made with the requestResourceActivation() and requestResourceDeactivation() methods.
        """

