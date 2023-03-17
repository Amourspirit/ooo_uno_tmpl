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
# Namespace: com.sun.star.task
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_interaction_continuation import XInteractionContinuation as XInteractionContinuation_5af0108e

class XInteractionRequest(XInterface_8f010a43):
    """
    The description of an interaction request.

    See Also:
        `API XInteractionRequest <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1task_1_1XInteractionRequest.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.XInteractionRequest'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.task.XInteractionRequest'

    @abstractmethod
    def getContinuations(self) -> 'typing.Tuple[XInteractionContinuation_5af0108e, ...]':
        """
        Get the set of com.sun.star.task.XInteractionContinuations the client supports for this request.
        """
        ...
    @abstractmethod
    def getRequest(self) -> object:
        """
        Get information about the request itself.
        """
        ...

__all__ = ['XInteractionRequest']

