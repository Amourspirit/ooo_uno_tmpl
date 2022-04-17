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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.embed
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class UnreachableStateException(Exception_85530a09):
    """
    Exception Class

    This exception can be thrown in case specified state can not be reached.

    See Also:
        `API UnreachableStateException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1embed_1_1UnreachableStateException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.UnreachableStateException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.embed.UnreachableStateException'
    __pyunostruct__: str = 'com.sun.star.embed.UnreachableStateException'

    typeName: str = 'com.sun.star.embed.UnreachableStateException'
    """Literal Constant ``com.sun.star.embed.UnreachableStateException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, CurrentState: typing.Optional[int] = 0, NextState: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            CurrentState (int, optional): CurrentState value.
            NextState (int, optional): NextState value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "CurrentState": CurrentState,
            "NextState": NextState,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._current_state = kwargs["CurrentState"]
        self._next_state = kwargs["NextState"]
        inst_keys = ('CurrentState', 'NextState')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def CurrentState(self) -> int:
        """
        The current state of the object.
        """
        return self._current_state
    
    @CurrentState.setter
    def CurrentState(self, value: int) -> None:
        self._current_state = value

    @property
    def NextState(self) -> int:
        """
        The state that could not be reached.
        """
        return self._next_state
    
    @NextState.setter
    def NextState(self, value: int) -> None:
        self._next_state = value


__all__ = ['UnreachableStateException']
