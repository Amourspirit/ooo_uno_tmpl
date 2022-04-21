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
# Namespace: com.sun.star.sdb
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
import typing
from ..sdbc.sql_warning import SQLWarning as SQLWarning_96f10a6a
from ..uno.x_interface import XInterface as XInterface_8f010a43

class SQLContext(SQLWarning_96f10a6a):
    """
    Exception Class

    provides special information about the context where a com.sun.star.sdbc.SQLException occurred.
    
    As usual for SQLExceptions, several SQLContext-objects may be chained, then the most recent context is appended to the list's tail.

    See Also:
        `API SQLContext <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1sdb_1_1SQLContext.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.SQLContext'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.sdb.SQLContext'
    __pyunostruct__: str = 'com.sun.star.sdb.SQLContext'

    typeName: str = 'com.sun.star.sdb.SQLContext'
    """Literal Constant ``com.sun.star.sdb.SQLContext``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, SQLState: typing.Optional[str] = '', ErrorCode: typing.Optional[int] = 0, NextException: typing.Optional[object] = None, Details: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            SQLState (str, optional): SQLState value.
            ErrorCode (int, optional): ErrorCode value.
            NextException (object, optional): NextException value.
            Details (str, optional): Details value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "SQLState": SQLState,
            "ErrorCode": ErrorCode,
            "NextException": NextException,
            "Details": Details,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._details = kwargs["Details"]
        inst_keys = ('Details',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def Details(self) -> str:
        """
        provides special info about the details where a com.sun.star.sdbc.SQLException occurred.
        
        As usual for SQLExceptions, several SQLContext-objects may be chained, then the most recent context is appended to the list's tail
        """
        return self._details
    
    @Details.setter
    def Details(self, value: str) -> None:
        self._details = value


__all__ = ['SQLContext']

