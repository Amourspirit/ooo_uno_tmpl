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
# Namespace: com.sun.star.task
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_interaction_request import XInteractionRequest as XInteractionRequest_cb20e7c

class XInteractionRequestStringResolver(XInterface_8f010a43):
    """
    Obtains human readable strings from an XInteractionRequest.

    See Also:
        `API XInteractionRequestStringResolver <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1task_1_1XInteractionRequestStringResolver.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.task.XInteractionRequestStringResolver']

    def getStringFromInformationalRequest(self, Request: 'XInteractionRequest_cb20e7c') -> object:
        """
        Obtains a string containing a human readable message from an informational interaction request.
        
        An informational interaction request contains not more than one interaction continuation (user has no choice; request is just informational). The supplies continuation must either be a XInteractionAbort or XInteractionApprove
        """

