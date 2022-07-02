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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.sdbc
from abc import abstractproperty
from .connection_properties import ConnectionProperties as ConnectionProperties_1a9f0ee1

class FILEConnectionProperties(ConnectionProperties_1a9f0ee1):
    """
    Service Class

    represents the properties for a FILE connection (session) with a specific database.
    
    These properties can be used when calling the method com.sun.star.sdbc.XDriver.connect() or com.sun.star.sdbc.XDriverManager.getConnectionWithInfo().
    
    The properties for a connection contain additional information about how to connect to a database and how to control the behavior of the resulting connection should be.

    See Also:
        `API FILEConnectionProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbc_1_1FILEConnectionProperties.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.FILEConnectionProperties'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def CharSet(self) -> str:
        """
        specifies the encoding to use to translate the backend data
        
        See the IANA character set list for a list of valid values.
        
        For internal purposes (e.g., when using an encoding for which no IANA character set name exists), this may also be an UNSIGNED SHORT value representing one of the rtl_TextEncoding values in rtl/textenc.h.
        """
        ...



__all__ = ['FILEConnectionProperties']

