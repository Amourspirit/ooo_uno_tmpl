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
import typing
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_database_environment import XDatabaseEnvironment as XDatabaseEnvironment_8280e43
if typing.TYPE_CHECKING:
    from ..util.x_number_formats_supplier import XNumberFormatsSupplier as XNumberFormatsSupplier_3afb0fb7

class DatabaseEnvironment(XPropertySet_bc180bfa, XDatabaseEnvironment_8280e43):
    """
    Service Class

    It enables the service user to establish connections to databases or to use database access beans to gain access to database components. This service takes control over all other database services.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API DatabaseEnvironment <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1DatabaseEnvironment.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.DatabaseEnvironment'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def NumberFormatsSupplier(self) -> 'XNumberFormatsSupplier_3afb0fb7':
        """
        provides an object for formatting numbers.
        """
        ...



__all__ = ['DatabaseEnvironment']

