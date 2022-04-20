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
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
import typing
from .password_request import PasswordRequest as PasswordRequest_d7280cf7
from ..uno.x_interface import XInterface as XInterface_8f010a43
from .interaction_classification import InteractionClassification as InteractionClassification_6c4d10e7
from .password_request_mode import PasswordRequestMode as PasswordRequestMode_ec10e7c

class DocumentMSPasswordRequest(PasswordRequest_d7280cf7):
    """
    Exception Class

    this request specifies the mode in which the password for Microsoft Office file format encryption should be asked
    
    It is supported by InteractionHandler service, and can be used to interact for a document password. Continuations for using with the mentioned service are Abort and Approve.
    
    **since**
    
        OOo 3.2

    See Also:
        `API DocumentMSPasswordRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1task_1_1DocumentMSPasswordRequest.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.DocumentMSPasswordRequest'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.task.DocumentMSPasswordRequest'
    __pyunostruct__: str = 'com.sun.star.task.DocumentMSPasswordRequest'

    typeName: str = 'com.sun.star.task.DocumentMSPasswordRequest'
    """Literal Constant ``com.sun.star.task.DocumentMSPasswordRequest``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, Classification: typing.Optional[InteractionClassification_6c4d10e7] = InteractionClassification_6c4d10e7.ERROR, Mode: typing.Optional[PasswordRequestMode_ec10e7c] = PasswordRequestMode_ec10e7c.PASSWORD_CREATE, Name: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Classification (InteractionClassification, optional): Classification value.
            Mode (PasswordRequestMode, optional): Mode value.
            Name (str, optional): Name value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "Classification": Classification,
            "Mode": Mode,
            "Name": Name,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._name = kwargs["Name"]
        inst_keys = ('Name',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def Name(self) -> str:
        """
        the name of the document (more properly, the URL of the document)
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value


__all__ = ['DocumentMSPasswordRequest']

