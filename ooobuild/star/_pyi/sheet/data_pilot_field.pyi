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
from .x_data_pilot_field import XDataPilotField as XDataPilotField_e0350cdf
from .x_data_pilot_field_grouping import XDataPilotFieldGrouping as XDataPilotFieldGrouping_55b3102a
if typing.TYPE_CHECKING:
    from .data_pilot_field_auto_show_info import DataPilotFieldAutoShowInfo as DataPilotFieldAutoShowInfo_88d7114d
    from .data_pilot_field_group_info import DataPilotFieldGroupInfo as DataPilotFieldGroupInfo_56691020
    from .data_pilot_field_layout_info import DataPilotFieldLayoutInfo as DataPilotFieldLayoutInfo_671e1091
    from .data_pilot_field_orientation import DataPilotFieldOrientation as DataPilotFieldOrientation_78701113
    from .data_pilot_field_reference import DataPilotFieldReference as DataPilotFieldReference_562f1016
    from .data_pilot_field_sort_info import DataPilotFieldSortInfo as DataPilotFieldSortInfo_466d0fbb
    from .general_function import GeneralFunction as GeneralFunction_e2280d25

class DataPilotField(XPropertySet_bc180bfa, XNamed_a6520b08, XDataPilotField_e0350cdf, XDataPilotFieldGrouping_55b3102a):
    """
    Service Class

    represents a single field in a data pilot table.
    
    If the data pilot table is based on a spreadsheet cell range, a field is represented by a column of the range and is named using the topmost cell of the column.
    
    **since**
    
        LibreOffice 5.3

    See Also:
        `API DataPilotField <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1DataPilotField.html>`_
    """
    @property
    def Subtotals(self) -> 'typing.Tuple[GeneralFunction_e2280d25, ...]':
        """
        specifies the functions used to calculate subtotals for this field.
        
        This property is supported by column and row fields only.
        
        An empty sequence means no subtotals. The same effect can be achieved by setting the property Function to the value GeneralFunction.NONE. If the length of the sequence is greater than 1, then the sequence MUST NOT contain one of the values GeneralFunction.NONE or GeneralFunction.AUTO.
        
        The order of the functions in this sequence is reflected in the DataPilot table. Multiple entries of the same function are ignored when setting the property.
        """
    @property
    def Subtotals2(self) -> 'typing.Tuple[int, ...]':
        """
        specifies the functions used to calculate subtotals for this field.
        
        This property is supported by column and row fields only.
        
        An empty sequence means no subtotals. The same effect can be achieved by setting the property Function2 to the value GeneralFunction.NONE. If the length of the sequence is greater than 1, then the sequence MUST NOT contain one of the values GeneralFunction2.NONE or GeneralFunction2.AUTO.
        
        The order of the functions in this sequence is reflected in the DataPilot table. Multiple entries of the same function are ignored when setting the property.
        
        **since**
        
            LibreOffice 5.3
        """
    @property
    def AutoShowInfo(self) -> 'DataPilotFieldAutoShowInfo_88d7114d':
        """
        enables the automatic inclusion of only a number of items with the highest or lowest result values.
        """
    @property
    def Function(self) -> 'GeneralFunction_e2280d25':
        """
        specifies the function used to calculate results for this field.
        
        For column and row fields, this is the function for subtotals (GeneralFunction.NONE means no subtotals). For data fields, this is the function shown in the data pilot table.
        """
    @property
    def Function2(self) -> int:
        """
        specifies the function used to calculate results for this field.
        
        For column and row fields, this is the function for subtotals (GeneralFunction2.NONE means no subtotals). For data fields, this is the function shown in the data pilot table.
        
        **since**
        
            LibreOffice 5.3
        """
    @property
    def GroupInfo(self) -> 'DataPilotFieldGroupInfo_56691020':
        """
        contains the grouping information of the DataPilot field.
        
        By changing the value of this property it is possible to modify the grouping settings of this field.
        """
    @property
    def HasAutoShowInfo(self) -> bool:
        """
        specifies whether this field has auto show information.
        """
    @property
    def HasLayoutInfo(self) -> bool:
        """
        specifies whether this field has layout information.
        """
    @property
    def HasReference(self) -> bool:
        """
        specifies whether this field has a reference.
        """
    @property
    def HasSortInfo(self) -> bool:
        """
        specifies whether this field has sorting information.
        """
    @property
    def IsGroupField(self) -> bool:
        """
        specifies whether this field is a group field.
        """
    @property
    def LayoutInfo(self) -> 'DataPilotFieldLayoutInfo_671e1091':
        """
        controls how the field's items are laid out in the result table.
        """
    @property
    def Orientation(self) -> 'DataPilotFieldOrientation_78701113':
        """
        specifies the orientation of the field.
        
        If the orientation of a field has been changed using this property, the field will be moved to the last position in the collection of all fields with the specified orientation.
        """
    @property
    def Reference(self) -> 'DataPilotFieldReference_562f1016':
        """
        controls how the results are shown in relation to a selected reference result.
        """
    @property
    def SelectedPage(self) -> str:
        """
        specifies the selected page which is used to filter the data pilot.
        """
    @property
    def ShowEmpty(self) -> bool:
        """
        specifies whether to show this field also if it is empty or not.
        """
    @property
    def SortInfo(self) -> 'DataPilotFieldSortInfo_466d0fbb':
        """
        controls how the field's items are sorted.
        """
    @property
    def UseSelectedPage(self) -> bool:
        """
        specifies whether to use the selected page to filter the data pilot or show all.
        """
    @property
    def UsedHierarchy(self) -> str:
        """
        specifies which hierarchy of the dimension is used.
        """


