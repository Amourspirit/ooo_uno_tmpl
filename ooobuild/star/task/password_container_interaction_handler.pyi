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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.task
from __future__ import annotations
from .x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51

class PasswordContainerInteractionHandler(XInteractionHandler_bf80e51):
    """
    Service Class

    An interaction request handler that uses the com.sun.star.task.PasswordContainer service to handle com.sun.star.ucb.AuthenticationRequest.
    
    If the password container contains credentials matching the authentication request, the service implementation selects the com.sun.star.ucb.XInteractionSupplyAuthentication continuation, that should be supplied with the interaction request.
    
    If the password container does not contain credentials matching the authentication request, the service implementation selects no continuation.
    
    **since**
    
        OOo 3.3

    See Also:
        `API PasswordContainerInteractionHandler <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1task_1_1PasswordContainerInteractionHandler.html>`_
    """
    ...

