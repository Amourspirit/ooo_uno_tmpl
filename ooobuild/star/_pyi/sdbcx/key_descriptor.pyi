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

class KeyDescriptor(Descriptor_a5200b3b, XColumnsSupplier_f0600da9):
    """
    Service Class

    is used to define a new key for a table.

    See Also:
        `API KeyDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbcx_1_1KeyDescriptor.html>`_
    """
    @property
    def DeleteRule(self) -> int:
        """
        is the rule which is applied for deletions; only used for foreign keys.
        """
    @property
    def ReferencedTable(self) -> str:
        """
        is the name of the referenced table, only used for foreign keys.
        """
    @property
    def Type(self) -> int:
        """
        indicates the type of the key.
        """
    @property
    def UpdateRule(self) -> int:
        """
        is the rule which is applied for updates; only used for foreign keys.
        """


