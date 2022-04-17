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
# Namespace: com.sun.star.sdb
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class ColumnSettings(XPropertySet_bc180bfa):
    """
    Service Class

    describes the common properties of a database column.

    See Also:
        `API ColumnSettings <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1ColumnSettings.html>`_
    """
    @property
    def Align(self) -> int:
        """
        specifies the alignment of columns text.
        
        <p<blockquote>
        
        If the value is VOID , a default alignment should be used according to the datatype of the column.
        """
    @property
    def ControlDefault(self) -> str:
        """
        describes the default value which should be displayed by a control when moving to a new row.
        
        The default is NULL.
        """
    @property
    def ControlModel(self) -> 'XPropertySet_bc180bfa':
        """
        indicates a control model which defines the settings for layouting.
        
        The default is NULL.
        """
    @property
    def FormatKey(self) -> int:
        """
        contains the index of the number format that is used for the column.
        
        The proper value can be determined by using the com.sun.star.util.XNumberFormatter interface.
        
        If the value is VOID , a default number format should be used according to the datatype of the column.
        """
    @property
    def HelpText(self) -> str:
        """
        describes an optional help text which can be used by UI components when representing this column.
        
        The default is NULL.
        """
    @property
    def Hidden(self) -> bool:
        """
        determines whether the column should be displayed or not.
        """
    @property
    def Position(self) -> int:
        """
        Position of the column within a grid.
        
        If the value is VOID , the default position should be taken according.
        """
    @property
    def Width(self) -> int:
        """
        specifies the width of the column displayed in a grid, the unit is 10THMM.
        
        If the value is VOID , a default width should be used according to the label of the column.
        """


