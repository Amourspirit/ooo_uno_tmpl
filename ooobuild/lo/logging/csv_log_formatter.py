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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.logging
from __future__ import annotations
from abc import abstractmethod
from .x_csv_log_formatter import XCsvLogFormatter as XCsvLogFormatter_b560e49

class CsvLogFormatter(XCsvLogFormatter_b560e49):
    """
    Service Class

    specifies a service which formats log records for RFC4180-style CSV-Files
    
    Every log record, as passed to XCsvLogFormatter.format(), will be formatted into a single row for a CSV file. The sequence number, the thread ID, the time of the logged event, the source class/method name will get logged alongside the message, if this is not disabled. The Formatter also supports logging an arbitrary number of user-defined columns. If the Formatter is configured to have more than one (user-defined) column the data to log has to be preformatted with the formatMultiColumn method.
    
    **since**
    
        OOo 3.0

    See Also:
        `API CsvLogFormatter <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1logging_1_1CsvLogFormatter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.logging'
    __ooo_full_ns__: str = 'com.sun.star.logging.CsvLogFormatter'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def create(self) -> None:
        """
        creates a CsvLogFormatter instance
        """
        ...

__all__ = ['CsvLogFormatter']

