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
# Namespace: com.sun.star.sheet
from __future__ import annotations
from abc import abstractproperty
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_data_pilot_results import XDataPilotResults as XDataPilotResults_fc0c0ded
from .x_dimensions_supplier import XDimensionsSupplier as XDimensionsSupplier_1baa0ee6
from ..util.x_refreshable import XRefreshable as XRefreshable_b0d60b81

class DataPilotSource(XPropertySet_bc180bfa, XDataPilotResults_fc0c0ded, XDimensionsSupplier_1baa0ee6, XRefreshable_b0d60b81):
    """
    Service Class

    represents a data pilot source.
    
    A component that implements this service can be used as data source for a data pilot table in a spreadsheet document.
    
    **since**
    
        OOo 3.0

    See Also:
        `API DataPilotSource <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1DataPilotSource.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.DataPilotSource'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def ColumnFieldCount(self) -> int:
        """
        specifies the number of column fields.
        
        **since**
        
            OOo 3.0
        """
        ...

    @abstractproperty
    def ColumnGrand(self) -> bool:
        """
        specifies if grand totals for the columns are inserted.
        """
        ...

    @abstractproperty
    def DataFieldCount(self) -> int:
        """
        specifies the number of data fields.
        
        **since**
        
            OOo 3.0
        """
        ...

    @abstractproperty
    def RowFieldCount(self) -> int:
        """
        specifies the number of row fields.
        
        **since**
        
            OOo 3.0
        """
        ...

    @abstractproperty
    def RowGrand(self) -> bool:
        """
        specifies if grand totals for the rows are inserted.
        """
        ...


__all__ = ['DataPilotSource']

