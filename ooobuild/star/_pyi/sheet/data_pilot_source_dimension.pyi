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
# Namespace: com.sun.star.sheet
import typing
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..container.x_named import XNamed as XNamed_a6520b08
from .x_hierarchies_supplier import XHierarchiesSupplier as XHierarchiesSupplier_29a50f34
from ..util.x_cloneable import XCloneable as XCloneable_99d00aa3
if typing.TYPE_CHECKING:
    from .data_pilot_field_orientation import DataPilotFieldOrientation as DataPilotFieldOrientation_78701113
    from .general_function import GeneralFunction as GeneralFunction_e2280d25
    from .table_filter_field import TableFilterField as TableFilterField_ee760d53

class DataPilotSourceDimension(XPropertySet_bc180bfa, XNamed_a6520b08, XHierarchiesSupplier_29a50f34, XCloneable_99d00aa3):
    """
    Service Class

    represents a dimension in a data pilot source.
    
    A dimension is equivalent to a column of a cell range in a spreadsheet used for a data pilot field.
    
    In more complex data sources, a dimension may contain several hierarchies, which consolidate items of a complex data type, called levels.
    
    Example: In a database, a column contains date values. This column will be a dimension of the data pilot source. One hierarchy may contain the 3 levels year, month, day. Another hierarchy may contain the 2 levels year and week number.
    
    **since**
    
        LibreOffice 5.3

    See Also:
        `API DataPilotSourceDimension <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1DataPilotSourceDimension.html>`_
    """
    @property
    def Filter(self) -> 'typing.Tuple[TableFilterField_ee760d53, ...]':
        """
        specifies which values are used.
        """
        ...

    @Filter.setter
    def Filter(self, value: 'typing.Tuple[TableFilterField_ee760d53, ...]') -> None:
        ...

    @property
    def Flags(self) -> int:
        """
        contains flags that control the usage of the dimension.
        """
        ...

    @Flags.setter
    def Flags(self, value: int) -> None:
        ...
    @property
    def Function(self) -> 'GeneralFunction_e2280d25':
        """
        specifies how data are aggregated.
        """
        ...

    @Function.setter
    def Function(self, value: 'GeneralFunction_e2280d25') -> None:
        ...
    @property
    def Function2(self) -> int:
        """
        specifies how data are aggregated.
        
        **since**
        
            LibreOffice 5.3
        """
        ...

    @Function2.setter
    def Function2(self, value: int) -> None:
        ...
    @property
    def IsDataLayoutDimension(self) -> bool:
        """
        contains TRUE if this is the dimension used to layout the different data dimensions.
        """
        ...

    @IsDataLayoutDimension.setter
    def IsDataLayoutDimension(self, value: bool) -> None:
        ...
    @property
    def Orientation(self) -> 'DataPilotFieldOrientation_78701113':
        """
        specifies where the dimension is used.
        """
        ...

    @Orientation.setter
    def Orientation(self, value: 'DataPilotFieldOrientation_78701113') -> None:
        ...
    @property
    def Original(self) -> 'XNamed_a6520b08':
        """
        returns the name of the dimension from which this dimension was cloned, or NULL if it was not cloned.
        """
        ...

    @Original.setter
    def Original(self, value: 'XNamed_a6520b08') -> None:
        ...
    @property
    def Position(self) -> int:
        """
        specifies the position of the dimension within its orientation.
        """
        ...

    @Position.setter
    def Position(self, value: int) -> None:
        ...
    @property
    def UsedHierarchy(self) -> int:
        """
        specifies which hierarchy of the dimension is used.
        """
        ...

    @UsedHierarchy.setter
    def UsedHierarchy(self, value: int) -> None:
        ...

