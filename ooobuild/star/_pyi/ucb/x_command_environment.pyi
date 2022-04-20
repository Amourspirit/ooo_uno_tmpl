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
# Namespace: com.sun.star.ucb
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..task.x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51
    from .x_progress_handler import XProgressHandler as XProgressHandler_d4190cad

class XCommandEnvironment(XInterface_8f010a43):
    """
    defines the environment for a command.

    See Also:
        `API XCommandEnvironment <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XCommandEnvironment.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ucb.XCommandEnvironment']

    def getInteractionHandler(self) -> 'XInteractionHandler_bf80e51':
        """
        returns the command's interaction handler.
        
        If called multiple times, this method should consistently return the same value (to allow caching).
        """
    def getProgressHandler(self) -> 'XProgressHandler_d4190cad':
        """
        returns the command's progress handler.
        
        If called multiple times, this method should consistently return the same value (to allow caching).
        """

