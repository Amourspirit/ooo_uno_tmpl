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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.document
# Libre Office Version: 7.2
from typing_extensions import Literal
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class UndoManagerEvent(EventObject_a3d70b03):
    """
    Struct Class

    is an event sent by an XUndoManager implementation when the Undo/Redo stacks of the manager are modified.
    
    **since**
    
        OOo 3.4

    See Also:
        `API UndoManagerEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1document_1_1UndoManagerEvent.html>`_
    """
    typeName: Literal['com.sun.star.document.UndoManagerEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., UndoActionTitle: typing.Optional[str] = ..., UndoContextDepth: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            UndoActionTitle (str, optional): UndoActionTitle value.
            UndoContextDepth (int, optional): UndoContextDepth value.
        """


    @property
    def UndoActionTitle(self) -> str:
        """
        the title of the undo action which is described by the event
        """


    @property
    def UndoContextDepth(self) -> int:
        """
        denotes the number of Undo contexts which are open, and not yet closed, at the time the event is fired.
        """


