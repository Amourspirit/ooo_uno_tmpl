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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.frame
# Libre Office Version: 2024.2
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class DispatchResultEvent(EventObject_a3d70b03):
    """
    Struct Class

    contains the result of the dispatch action, if State is set to SUCCESS
    
    The type of the result is dispatch action dependent. The member State can be set to one of the values defined in DispatchResultState. If State is set to DispatchResultState.FAILURE, Result may specify the reason (or is empty). The type is also dispatch action dependent. If State is set to DispatchResultState.DONTKNOW, Result is empty.

    See Also:
        `API DispatchResultEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1DispatchResultEvent.html>`_
    """
    typeName: str = 'com.sun.star.frame.DispatchResultEvent'

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., State: typing.Optional[int] = ..., Result: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            State (int, optional): State value.
            Result (object, optional): Result value.
        """
        ...

    @property
    def State(self) -> int:
        """
        describes state of dispatch
        """
        ...
    @State.setter
    def State(self, value: int) -> None:
        ...
    @property
    def Result(self) -> object:
        """
        describes result for given State
        """
        ...
    @Result.setter
    def Result(self, value: object) -> None:
        ...

