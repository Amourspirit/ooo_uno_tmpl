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
# Namespace: com.sun.star.table
import typing
from abc import abstractproperty
from ..util.sort_descriptor import SortDescriptor as SortDescriptor_ca680c8d
if typing.TYPE_CHECKING:
    from .table_orientation import TableOrientation as TableOrientation_ee780d84
    from ..util.sort_field import SortField as SortField_90080a52

class TableSortDescriptor(SortDescriptor_ca680c8d):
    """
    Service Class

    contains properties which describe sorting of rows or columns in a table.
    
    It extends the general com.sun.star.util.SortDescriptor with table-specific properties.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API TableSortDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1table_1_1TableSortDescriptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.table'
    __ooo_full_ns__: str = 'com.sun.star.table.TableSortDescriptor'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def SortFields(self) -> 'typing.Tuple[SortField_90080a52, ...]':
        """
        specifies the descriptions of the individual sort fields.
        """

    @abstractproperty
    def ContainsHeader(self) -> bool:
        """
        specifies whether the first row or column (depending on com.sun.star.util.SortDescriptor.SortColumns) is a header which should not be sorted.
        """

    @abstractproperty
    def MaxFieldCount(self) -> int:
        """
        contains the maximum number of sort fields the descriptor can hold.
        """

    @abstractproperty
    def Orientation(self) -> 'TableOrientation_ee780d84':
        """
        specifies the sorting orientation (sort rows or columns).
        
        Some implementations may not support sorting columns.
        """



__all__ = ['TableSortDescriptor']

