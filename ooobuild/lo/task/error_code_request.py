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
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class ErrorCodeRequest(Exception_85530a09):
    """
    Exception Class

    represents a general error exception.
    
    It can be used to transport the error code information. E.g. that can be useful for interactions.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API ErrorCodeRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1task_1_1ErrorCodeRequest.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.ErrorCodeRequest'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.task.ErrorCodeRequest'
    __pyunostruct__: str = 'com.sun.star.task.ErrorCodeRequest'

    typeName: str = 'com.sun.star.task.ErrorCodeRequest'
    """Literal Constant ``com.sun.star.task.ErrorCodeRequest``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, ErrCode: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            ErrCode (int, optional): ErrCode value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "ErrCode": ErrCode,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._err_code = kwargs["ErrCode"]
        inst_keys = ('ErrCode',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def ErrCode(self) -> int:
        """
        specifies the error code.
        """
        return self._err_code
    
    @ErrCode.setter
    def ErrCode(self, value: int) -> None:
        self._err_code = value


__all__ = ['ErrorCodeRequest']

