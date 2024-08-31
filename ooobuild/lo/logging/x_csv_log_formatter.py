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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.logging
from __future__ import annotations
import typing
from abc import abstractmethod, abstractproperty
from .x_log_formatter import XLogFormatter as XLogFormatter_e23d0d1d

class XCsvLogFormatter(XLogFormatter_e23d0d1d):
    """
    specifies the interface used for formatting log records for RFC4180 CSV output
    
    **since**
    
        OOo 3.0

    See Also:
        `API XCsvLogFormatter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1logging_1_1XCsvLogFormatter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.logging'
    __ooo_full_ns__: str = 'com.sun.star.logging.XCsvLogFormatter'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.logging.XCsvLogFormatter'

    @abstractmethod
    def formatMultiColumn(self, columnData: typing.Tuple[str, ...]) -> str:
        """
        if the CsvLogFormatter is set to have more than one column, any logged information has to be send through this method before calling log().
        
        E.g.:
        
        XLoggerInstance.log(1000, XCsvLogFormatterInstance.formatMultiColumn(columnData))
        """
        ...
    @abstractproperty
    def Columnnames(self) -> typing.Tuple[str, ...]:
        """
        Defines the names of the additional columns this defaults to only one row titled \"message\".
        
        if this is set to more than one column, the messages need to be preformatted using formatMultiColumn
        """
        ...

    @abstractproperty
    def LogEventNo(self) -> bool:
        """
        Defines if the EventNo should be logged.
        """
        ...

    @abstractproperty
    def LogSource(self) -> bool:
        """
        Defines if the Source should be logged.
        """
        ...

    @abstractproperty
    def LogThread(self) -> bool:
        """
        Defines if the ThreadId should be logged.
        """
        ...

    @abstractproperty
    def LogTimestamp(self) -> bool:
        """
        Defines if the Timestamp should be logged.
        """
        ...


__all__ = ['XCsvLogFormatter']

