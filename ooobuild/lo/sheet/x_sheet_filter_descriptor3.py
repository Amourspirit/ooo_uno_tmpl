# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .table_filter_field3 import TableFilterField3 as TableFilterField3_fbfc0d86

class XSheetFilterDescriptor3(XInterface_8f010a43):
    """
    provides access to a collection of filter conditions (filter fields).
    
    This interface uses the TableFilterField3 struct. whereas the XSheetFilterDescriptor2 interface uses the TableFilterField2 struct.
    
    **since**
    
        LibreOffice 3.5

    See Also:
        `API XSheetFilterDescriptor3 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSheetFilterDescriptor3.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.XSheetFilterDescriptor3'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sheet.XSheetFilterDescriptor3'

    @abstractmethod
    def getFilterFields3(self) -> 'typing.Tuple[TableFilterField3_fbfc0d86, ...]':
        """
        returns the collection of filter fields.
        """
        ...
    @abstractmethod
    def setFilterFields3(self, aFilterFields: 'typing.Tuple[TableFilterField3_fbfc0d86, ...]') -> None:
        """
        sets a new collection of filter fields.
        """
        ...

__all__ = ['XSheetFilterDescriptor3']

