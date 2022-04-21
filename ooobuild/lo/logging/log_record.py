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
# Namespace: com.sun.star.logging
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
import typing
from ..util.date_time import DateTime as DateTime_84de09d3


class LogRecord(object):
    """
    Struct Class

    assembles the complete information about a to-be-logged event
    
    **since**
    
        OOo 2.3

    See Also:
        `API LogRecord <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1logging_1_1LogRecord.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.logging'
    __ooo_full_ns__: str = 'com.sun.star.logging.LogRecord'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.logging.LogRecord'
    """Literal Constant ``com.sun.star.logging.LogRecord``"""

    def __init__(self, LoggerName: typing.Optional[str] = '', SourceClassName: typing.Optional[str] = '', SourceMethodName: typing.Optional[str] = '', Message: typing.Optional[str] = '', LogTime: typing.Optional[DateTime_84de09d3] = UNO_NONE, SequenceNumber: typing.Optional[int] = 0, ThreadID: typing.Optional[str] = '', Level: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            LoggerName (str, optional): LoggerName value.
            SourceClassName (str, optional): SourceClassName value.
            SourceMethodName (str, optional): SourceMethodName value.
            Message (str, optional): Message value.
            LogTime (DateTime, optional): LogTime value.
            SequenceNumber (int, optional): SequenceNumber value.
            ThreadID (str, optional): ThreadID value.
            Level (int, optional): Level value.
        """
        super().__init__()

        if isinstance(LoggerName, LogRecord):
            oth: LogRecord = LoggerName
            self.LoggerName = oth.LoggerName
            self.SourceClassName = oth.SourceClassName
            self.SourceMethodName = oth.SourceMethodName
            self.Message = oth.Message
            self.LogTime = oth.LogTime
            self.SequenceNumber = oth.SequenceNumber
            self.ThreadID = oth.ThreadID
            self.Level = oth.Level
            return

        kargs = {
            "LoggerName": LoggerName,
            "SourceClassName": SourceClassName,
            "SourceMethodName": SourceMethodName,
            "Message": Message,
            "LogTime": LogTime,
            "SequenceNumber": SequenceNumber,
            "ThreadID": ThreadID,
            "Level": Level,
        }
        if kargs["LogTime"] is UNO_NONE:
            kargs["LogTime"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._logger_name = kwargs["LoggerName"]
        self._source_class_name = kwargs["SourceClassName"]
        self._source_method_name = kwargs["SourceMethodName"]
        self._message = kwargs["Message"]
        self._log_time = kwargs["LogTime"]
        self._sequence_number = kwargs["SequenceNumber"]
        self._thread_id = kwargs["ThreadID"]
        self._level = kwargs["Level"]


    @property
    def LoggerName(self) -> str:
        """
        specifies the name of the logger at which the record is logged
        """
        return self._logger_name
    
    @LoggerName.setter
    def LoggerName(self, value: str) -> None:
        self._logger_name = value

    @property
    def SourceClassName(self) -> str:
        """
        specifies the name of the class, in which the record was logged.
        
        This name might be empty, in case the caller to one of the various log methods of XLogger did not specify it.
        """
        return self._source_class_name
    
    @SourceClassName.setter
    def SourceClassName(self, value: str) -> None:
        self._source_class_name = value

    @property
    def SourceMethodName(self) -> str:
        """
        specifies the name of the method, in which the record was logged.
        
        This name might be empty, in case the caller to one of the various log methods of XLogger did not specify it.
        """
        return self._source_method_name
    
    @SourceMethodName.setter
    def SourceMethodName(self, value: str) -> None:
        self._source_method_name = value

    @property
    def Message(self) -> str:
        """
        specifies the to-be-logged message
        """
        return self._message
    
    @Message.setter
    def Message(self, value: str) -> None:
        self._message = value

    @property
    def LogTime(self) -> DateTime_84de09d3:
        """
        specifies the time at which the event was logged
        """
        return self._log_time
    
    @LogTime.setter
    def LogTime(self, value: DateTime_84de09d3) -> None:
        self._log_time = value

    @property
    def SequenceNumber(self) -> int:
        """
        specifies the number of the log event.
        
        Subsequent events get assigned increasing sequence numbers by the XLogger at which they're logged.
        """
        return self._sequence_number
    
    @SequenceNumber.setter
    def SequenceNumber(self, value: int) -> None:
        self._sequence_number = value

    @property
    def ThreadID(self) -> str:
        """
        specifies the ID of the thread in which the event was logged
        """
        return self._thread_id
    
    @ThreadID.setter
    def ThreadID(self, value: str) -> None:
        self._thread_id = value

    @property
    def Level(self) -> int:
        """
        specifies the level of the log event
        """
        return self._level
    
    @Level.setter
    def Level(self, value: int) -> None:
        self._level = value


__all__ = ['LogRecord']
