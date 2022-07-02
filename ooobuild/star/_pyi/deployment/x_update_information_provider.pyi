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
# Namespace: com.sun.star.deployment
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ..container.x_enumeration import XEnumeration as XEnumeration_f2180daa
    from ..task.x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51
    from ..xml.dom.x_element import XElement as XElement_a33d0ae9

class XUpdateInformationProvider(ABC):
    """
    Objects implementing this interface provide access to the xml root of one or more update information files for a given set of URLs.
    
    **since**
    
        OOo 2.2

    See Also:
        `API XUpdateInformationProvider <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1deployment_1_1XUpdateInformationProvider.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.deployment.XUpdateInformationProvider']

    def cancel(self) -> None:
        """
        interrupts a getUpdateInformation call and let's it return immediately.
        """
        ...
    def getUpdateInformation(self, repositories: 'typing.Tuple[str, ...]', extensionId: str) -> 'typing.Tuple[XElement_a33d0ae9, ...]':
        """
        get update information for a specific extension or all available information from a repository.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    def getUpdateInformationEnumeration(self, repositories: 'typing.Tuple[str, ...]', extensionId: str) -> 'XEnumeration_f2180daa':
        """
        get update information for a specific extension or all available information from a repository.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    def setInteractionHandler(self, handler: 'XInteractionHandler_bf80e51') -> None:
        """
        Sets an interaction handler to be used for further operations.
        
        A default interaction handler is available as service com.sun.star.task.InteractionHandler. The documentation of this service also contains further information about the interaction handler concept.
        """
        ...


