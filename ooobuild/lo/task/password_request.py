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
# Namespace: com.sun.star.task
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing
from .classified_interaction_request import ClassifiedInteractionRequest as ClassifiedInteractionRequest_9f72121b
from ..uno.x_interface import XInterface as XInterface_8f010a43
from .interaction_classification import InteractionClassification as InteractionClassification_6c4d10e7
from .password_request_mode import PasswordRequestMode as PasswordRequestMode_ec10e7c

class PasswordRequest(ClassifiedInteractionRequest_9f72121b):
    """
    Exception Class

    this request specifies the mode in which the password should be asked
    
    It is supported by InteractionHandler service, and can be used to interact for a password. Continuations for using with the mentioned service are Abort and Approve.

    See Also:
        `API PasswordRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1task_1_1PasswordRequest.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.PasswordRequest'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.task.PasswordRequest'
    __pyunostruct__: str = 'com.sun.star.task.PasswordRequest'

    typeName: str = 'com.sun.star.task.PasswordRequest'
    """Literal Constant ``com.sun.star.task.PasswordRequest``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, Classification: typing.Optional[InteractionClassification_6c4d10e7] = InteractionClassification_6c4d10e7.ERROR, Mode: typing.Optional[PasswordRequestMode_ec10e7c] = PasswordRequestMode_ec10e7c.PASSWORD_CREATE) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Classification (InteractionClassification, optional): Classification value.
            Mode (PasswordRequestMode, optional): Mode value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "Classification": Classification,
            "Mode": Mode,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._mode = kwargs["Mode"]
        inst_keys = ('Mode',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def Mode(self) -> PasswordRequestMode_ec10e7c:
        """
        the mode in which password should be asked
        """
        return self._mode
    
    @Mode.setter
    def Mode(self, value: PasswordRequestMode_ec10e7c) -> None:
        self._mode = value


__all__ = ['PasswordRequest']

