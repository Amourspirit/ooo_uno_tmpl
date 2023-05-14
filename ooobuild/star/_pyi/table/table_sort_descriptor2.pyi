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
from ..util.sort_descriptor2 import SortDescriptor2 as SortDescriptor2_d7270cbf
if typing.TYPE_CHECKING:
    from .table_sort_field import TableSortField as TableSortField_d3860c84

class TableSortDescriptor2(SortDescriptor2_d7270cbf):
    """
    Service Class

    specifies properties which describe sorting of fields (rows or columns) in a table.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API TableSortDescriptor2 <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1table_1_1TableSortDescriptor2.html>`_
    """
    @property
    def SortFields(self) -> 'typing.Tuple[TableSortField_d3860c84, ...]':
        """
        specifies a list of individual sort fields.
        
        Each entry specifies properties that state the row/column to be sorted and how that should be done.
        """
        ...

    @SortFields.setter
    def SortFields(self, value: 'typing.Tuple[TableSortField_d3860c84, ...]') -> None:
        ...

    @property
    def IsSortColumns(self) -> bool:
        """
        specifies if the columns or rows are to be sorted.
        """
        ...

    @IsSortColumns.setter
    def IsSortColumns(self, value: bool) -> None:
        ...
    @property
    def MaxSortFieldsCount(self) -> int:
        """
        contains the maximum number of sort fields the descriptor can hold.
        """
        ...

    @MaxSortFieldsCount.setter
    def MaxSortFieldsCount(self, value: int) -> None:
        ...

