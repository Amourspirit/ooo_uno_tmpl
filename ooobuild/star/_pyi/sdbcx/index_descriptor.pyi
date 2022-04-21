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
# Libre Office Version: 7.2
# Namespace: com.sun.star.sdbcx
from .descriptor import Descriptor as Descriptor_a5200b3b
from .x_columns_supplier import XColumnsSupplier as XColumnsSupplier_f0600da9

class IndexDescriptor(Descriptor_a5200b3b, XColumnsSupplier_f0600da9):
    """
    Service Class

    is used to define a new index for a database table.

    See Also:
        `API IndexDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbcx_1_1IndexDescriptor.html>`_
    """
    @property
    def Catalog(self) -> str:
        """
        is the name of the index catalog, may be empty.
        """
    @property
    def IsClustered(self) -> bool:
        """
        indicates that the index is clustered.
        """
    @property
    def IsUnique(self) -> bool:
        """
        indicates that the index allow only unique values.
        """


