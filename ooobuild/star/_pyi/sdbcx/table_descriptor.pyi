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
# Namespace: com.sun.star.sdbcx
from .descriptor import Descriptor as Descriptor_a5200b3b
from .x_columns_supplier import XColumnsSupplier as XColumnsSupplier_f0600da9
from .x_keys_supplier import XKeysSupplier as XKeysSupplier_c8a70c64

class TableDescriptor(Descriptor_a5200b3b, XColumnsSupplier_f0600da9, XKeysSupplier_c8a70c64):
    """
    Service Class

    is used to define a table of a database.
    
    A table is described by its name and one or more columns and the keys for semantic rules.
    
    In addition, it may contain keys, and to define semantic rules for the table.  Note:  Indexes can only be appended when the table is already appended at the database.

    See Also:
        `API TableDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbcx_1_1TableDescriptor.html>`_
    """
    @property
    def CatalogName(self) -> str:
        """
        is the name of the table catalog.
        """
        ...

    @CatalogName.setter
    def CatalogName(self, value: str) -> None:
        ...
    @property
    def Description(self) -> str:
        """
        supplies a comment on the table, Could be empty if not supported by the driver.
        """
        ...

    @Description.setter
    def Description(self, value: str) -> None:
        ...
    @property
    def SchemaName(self) -> str:
        """
        is the name of the table schema.
        """
        ...

    @SchemaName.setter
    def SchemaName(self, value: str) -> None:
        ...

