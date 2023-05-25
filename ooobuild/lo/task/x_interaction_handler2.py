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
# Namespace: com.sun.star.task
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51
if typing.TYPE_CHECKING:
    from .x_interaction_request import XInteractionRequest as XInteractionRequest_cb20e7c

class XInteractionHandler2(XInteractionHandler_bf80e51):
    """
    An interaction request handler.
    
    This interface extends the interface XInteractionHandler the way that a caller can determine whether an interaction request was actually handled by the interaction handler.
    
    **since**
    
        OOo 3.2

    See Also:
        `API XInteractionHandler2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1task_1_1XInteractionHandler2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.XInteractionHandler2'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.task.XInteractionHandler2'

    @abstractmethod
    def handleInteractionRequest(self, Request: XInteractionRequest_cb20e7c) -> bool:
        """
        Handle an interaction request.
        """
        ...

__all__ = ['XInteractionHandler2']


