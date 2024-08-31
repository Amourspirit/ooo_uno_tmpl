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
# Namespace: com.sun.star.sdbcx
from __future__ import annotations
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_columns_supplier import XColumnsSupplier as XColumnsSupplier_f0600da9
from .x_data_descriptor_factory import XDataDescriptorFactory as XDataDescriptorFactory_46170fe5

class Index(XPropertySet_bc180bfa, XColumnsSupplier_f0600da9, XDataDescriptorFactory_46170fe5):
    """
    Service Class

    is used to specify the index for a database table.
    
    It refers to one or more columns of a table.
    
    Note:  All properties and columns of an index could by modified before they are appended to a table. In that case the service is a data descriptor.

    See Also:
        `API Index <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbcx_1_1Index.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbcx'
    __ooo_full_ns__: str = 'com.sun.star.sdbcx.Index'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Catalog(self) -> str:
        """
        is the name of the index catalog, may be empty.
        """
        ...

    @abstractproperty
    def IsClustered(self) -> bool:
        """
        indicates that the index is clustered.
        """
        ...

    @abstractproperty
    def IsPrimaryKeyIndex(self) -> bool:
        """
        indicates that the index is used for the primary key.
        """
        ...

    @abstractproperty
    def IsUnique(self) -> bool:
        """
        indicates that the index allow only unique values.
        """
        ...

    @abstractproperty
    def Name(self) -> str:
        """
        is the name of the index.
        """
        ...


__all__ = ['Index']

