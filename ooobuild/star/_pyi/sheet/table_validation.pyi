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
# Namespace: com.sun.star.sheet
import typing
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_sheet_condition import XSheetCondition as XSheetCondition_e1940d19
if typing.TYPE_CHECKING:
    from .validation_alert_style import ValidationAlertStyle as ValidationAlertStyle_2a930f35
    from .validation_type import ValidationType as ValidationType_d6110cce

class TableValidation(XPropertySet_bc180bfa, XSheetCondition_e1940d19):
    """
    Service Class

    represents the data validation settings for a cell or cell range.

    See Also:
        `API TableValidation <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1TableValidation.html>`_
    """
    @property
    def ErrorAlertStyle(self) -> 'ValidationAlertStyle_2a930f35':
        """
        specifies the style of the error message.
        
        This is used only if TableValidation.ShowErrorMessage is set to TRUE.
        """
        ...
    @property
    def ErrorMessage(self) -> str:
        """
        specifies the text of the error message.
        
        This is only used if TableValidation.ShowErrorMessage is set to TRUE.
        """
        ...
    @property
    def ErrorTitle(self) -> str:
        """
        specifies the title of the window showing the error message.
        
        This is only used if TableValidation.ShowErrorMessage is set to TRUE.
        """
        ...
    @property
    def IgnoreBlankCells(self) -> bool:
        """
        specifies if blank cells should be allowed.
        """
        ...
    @property
    def InputMessage(self) -> str:
        """
        specifies the text of the input message.
        
        This is only used if TableValidation.ShowInputMessage is set to TRUE.
        """
        ...
    @property
    def InputTitle(self) -> str:
        """
        specifies the title of the window showing the input message.
        
        This is only used if TableValidation.ShowInputMessage is set to TRUE.
        """
        ...
    @property
    def ShowErrorMessage(self) -> bool:
        """
        specifies if an error message is displayed when invalid data is entered.
        """
        ...
    @property
    def ShowInputMessage(self) -> bool:
        """
        specifies if an input message is shown when the cursor is in a cell with these validation settings.
        """
        ...
    @property
    def ShowList(self) -> int:
        """
        specifies if the list of possible values should be shown on the cell and how.
        
        See also TableValidationVisibility
        """
        ...
    @property
    def Type(self) -> 'ValidationType_d6110cce':
        """
        specifies the type of validation.
        """
        ...


