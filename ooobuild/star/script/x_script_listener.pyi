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
# Namespace: com.sun.star.script
from __future__ import annotations
import typing

from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .script_event import ScriptEvent as ScriptEvent_be710c14


class XScriptListener(XEventListener_c7230c4a):
    """
    makes it possible to receive ScriptEvents.

    See Also:
        `API XScriptListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XScriptListener.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.script.XScriptListener'

    def approveFiring(self, aEvent: ScriptEvent_be710c14) -> typing.Any:
        """
        gets called when a \"vetoable event\" occurs at the object.

        Raises:
            com.sun.star.reflection.InvocationTargetException: ``InvocationTargetException``
        """
        ...
    def firing(self, aEvent: ScriptEvent_be710c14) -> None:
        """
        gets called when an event takes place.
        
        For that a ScriptEventDescriptor is registered at and attached to an object by an XEventAttacherManager.
        """
        ...



