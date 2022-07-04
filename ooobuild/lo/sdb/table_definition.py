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
# Namespace: com.sun.star.sdb
from abc import abstractmethod
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class TableDefinition(XPropertySet_bc180bfa):
    """
    Service Class

    This IDL was created from the service's places of use, so it is probably incomplete.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API TableDefinition <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1TableDefinition.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.TableDefinition'
    __ooo_type_name__: str = 'service'

    @abstractmethod
    def createDefault(self) -> None:
        """
        """
        ...
    @abstractmethod
    def createWithName(self, Name: str) -> None:
        """
        """
        ...


__all__ = ['TableDefinition']

