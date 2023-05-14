# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
# Namespace: com.sun.star.chart2.data
import typing
from abc import abstractmethod
from .x_database_data_provider import XDatabaseDataProvider as XDatabaseDataProvider_8fe51146
if typing.TYPE_CHECKING:
    from ...sdbc.x_connection import XConnection as XConnection_a36a0b0c

class DatabaseDataProvider(XDatabaseDataProvider_8fe51146):
    """
    Service Class


    See Also:
        `API DatabaseDataProvider <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1data_1_1DatabaseDataProvider.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2.data'
    __ooo_full_ns__: str = 'com.sun.star.chart2.data.DatabaseDataProvider'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def createWithConnection(self, connection: 'XConnection_a36a0b0c') -> None:
        """
        """
        ...

__all__ = ['DatabaseDataProvider']

