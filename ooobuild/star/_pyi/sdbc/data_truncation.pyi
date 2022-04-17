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
# Namespace: com.sun.star.sdbc
# Libre Office Version: 7.3
from typing_extensions import Literal
from ooo.oenv.env_const import UNO_NONE
import typing
from .sql_warning import SQLWarning as SQLWarning_96f10a6a
from ..uno.x_interface import XInterface as XInterface_8f010a43

class DataTruncation(SQLWarning_96f10a6a):
    """
    Exception Class

    reports a DataTruncation warning, on reads, or is thrown as a DataTruncation exception, on writes, when a data value is unexpectedly truncated.
    
    The SQL state for a DataTruncation is 01004.

    See Also:
        `API DataTruncation <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1sdbc_1_1DataTruncation.html>`_
    """

    typeName: Literal['com.sun.star.sdbc.DataTruncation']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., SQLState: typing.Optional[str] = ..., ErrorCode: typing.Optional[int] = ..., NextException: typing.Optional[object] = ..., Index: typing.Optional[int] = ..., IsParameter: typing.Optional[bool] = ..., DuringRead: typing.Optional[bool] = ..., DataSize: typing.Optional[int] = ..., TransferSize: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            SQLState (str, optional): SQLState value.
            ErrorCode (int, optional): ErrorCode value.
            NextException (object, optional): NextException value.
            Index (int, optional): Index value.
            IsParameter (bool, optional): IsParameter value.
            DuringRead (bool, optional): DuringRead value.
            DataSize (int, optional): DataSize value.
            TransferSize (int, optional): TransferSize value.
        """
    @property
    def Index(self) -> int:
        """
        is the index of the parameter or column value.
        """

    @property
    def IsParameter(self) -> bool:
        """
        is TRUE if a parameter value is truncated.
        """

    @property
    def DuringRead(self) -> bool:
        """
        is TRUE if a read was truncated.
        """

    @property
    def DataSize(self) -> int:
        """
        contains the number of bytes of data that should have been transferred.
        
        This number may be approximate if data conversions were being performed. The value may be -1 if the size is unknown.
        """

    @property
    def TransferSize(self) -> int:
        """
        contains the number of bytes of data actually transferred.
        
        The value may be -1 if the size is unknown.
        """


__all__ = ['DataTruncation']

