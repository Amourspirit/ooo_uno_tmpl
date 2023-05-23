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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.frame
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from typing import Any, TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoEnumMeta
    class FrameAction(metaclass=UnoEnumMeta, type_name="com.sun.star.frame.FrameAction", name_space="com.sun.star.frame"):
        """Dynamically created class that represents ``com.sun.star.frame.FrameAction`` Enum. Class loosely mimics Enum"""
        pass
else:
    if TYPE_CHECKING:
        from com.sun.star.frame.FrameAction import COMPONENT_ATTACHED as FRAME_ACTION_COMPONENT_ATTACHED
        from com.sun.star.frame.FrameAction import COMPONENT_DETACHING as FRAME_ACTION_COMPONENT_DETACHING
        from com.sun.star.frame.FrameAction import COMPONENT_REATTACHED as FRAME_ACTION_COMPONENT_REATTACHED
        from com.sun.star.frame.FrameAction import CONTEXT_CHANGED as FRAME_ACTION_CONTEXT_CHANGED
        from com.sun.star.frame.FrameAction import FRAME_ACTIVATED as FRAME_ACTION_FRAME_ACTIVATED
        from com.sun.star.frame.FrameAction import FRAME_DEACTIVATING as FRAME_ACTION_FRAME_DEACTIVATING
        from com.sun.star.frame.FrameAction import FRAME_UI_ACTIVATED as FRAME_ACTION_FRAME_UI_ACTIVATED
        from com.sun.star.frame.FrameAction import FRAME_UI_DEACTIVATING as FRAME_ACTION_FRAME_UI_DEACTIVATING

        class FrameAction(uno.Enum):
            """
            Enum Class


            See Also:
                `API FrameAction <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1frame.html#a793fdb3e5cab69d63a9c89b5e4f83dfd>`_
            """

            def __init__(self, value: Any) -> None:
                super().__init__('com.sun.star.frame.FrameAction', value)

            __ooo_ns__: str = 'com.sun.star.frame'
            __ooo_full_ns__: str = 'com.sun.star.frame.FrameAction'
            __ooo_type_name__: str = 'enum'

            COMPONENT_ATTACHED = FRAME_ACTION_COMPONENT_ATTACHED
            """
            an event of this kind is broadcast whenever a component is attached to a frame

            This is almost the same as the instantiation of the component within that frame. The component is attached to the frame immediately before this event is broadcast.
            """
            COMPONENT_DETACHING = FRAME_ACTION_COMPONENT_DETACHING
            """
            an event of this kind is broadcast whenever a component is detaching from a frame

            This is quite the same as the destruction of the component which was in that frame. At the moment when the event is broadcast the component is still attached to the frame but in the next moment it won't.
            """
            COMPONENT_REATTACHED = FRAME_ACTION_COMPONENT_REATTACHED
            """
            an event of this kind is broadcast whenever a component is attached to a new model.

            In this case the component remains the same but operates on a new model component.
            """
            CONTEXT_CHANGED = FRAME_ACTION_CONTEXT_CHANGED
            """
            an event of this kind is broadcast whenever a component changes its internal context (i.e., the selection).

            If the activation status within a frame changes, this counts as a context change too.
            """
            FRAME_ACTIVATED = FRAME_ACTION_FRAME_ACTIVATED
            """
            an event of this kind is broadcast whenever a component gets activated

            Activations are broadcast from the top component which was not active before, down to the inner most component.
            """
            FRAME_DEACTIVATING = FRAME_ACTION_FRAME_DEACTIVATING
            """
            an event of this kind is broadcasted immediately before the component is deactivated

            Deactivations are broadcast from the innermost component which does not stay active up to the outer most component which does not stay active.
            """
            FRAME_UI_ACTIVATED = FRAME_ACTION_FRAME_UI_ACTIVATED
            """
            an event of this kind is broadcast by an active frame when it is getting UI control (tool control).
            """
            FRAME_UI_DEACTIVATING = FRAME_ACTION_FRAME_UI_DEACTIVATING
            """
            an event of this kind is broadcast by an active frame when it is losing UI control (tool control).
            """
    else:
        # keep document generators happy
        from ...lo.frame.frame_action import FrameAction as FrameAction


__all__ = ['FrameAction']
