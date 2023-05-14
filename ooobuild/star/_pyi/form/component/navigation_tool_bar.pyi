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
# Namespace: com.sun.star.form.component
import typing
from ..form_control_model import FormControlModel as FormControlModel_e2990d22
if typing.TYPE_CHECKING:
    from ...awt.font_descriptor import FontDescriptor as FontDescriptor_bc110c0a

class NavigationToolBar(FormControlModel_e2990d22):
    """
    Service Class

    This service specifies the model for control which provides controller functionality for a DataForm, such as navigating or filtering the form.

    See Also:
        `API NavigationToolBar <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1NavigationToolBar.html>`_
    """
    @property
    def Border(self) -> int:
        """
        denotes the border style of the control.
        
        Allowed values are
        """
        ...

    @Border.setter
    def Border(self, value: int) -> None:
        ...
    @property
    def Enabled(self) -> bool:
        """
        determines whether the control is enabled or disabled.
        """
        ...

    @Enabled.setter
    def Enabled(self, value: bool) -> None:
        ...
    @property
    def FontDescriptor(self) -> 'FontDescriptor_bc110c0a':
        """
        contains the font attributes for the text in the control
        """
        ...

    @FontDescriptor.setter
    def FontDescriptor(self, value: 'FontDescriptor_bc110c0a') -> None:
        ...
    @property
    def FontEmphasisMark(self) -> int:
        """
        specifies the emphasis mark for the font described in FontDescriptor
        
        The value must be one of the com.sun.star.text.FontEmphasis constants.
        """
        ...

    @FontEmphasisMark.setter
    def FontEmphasisMark(self, value: int) -> None:
        ...
    @property
    def FontRelief(self) -> int:
        """
        specifies the relief for the font described in FontDescriptor
        
        The value must be one of the com.sun.star.text.FontRelief constants.
        """
        ...

    @FontRelief.setter
    def FontRelief(self, value: int) -> None:
        ...
    @property
    def IconSize(self) -> int:
        """
        specifies the size of the icons in the control
        
        At least the following values are to be supported:
        """
        ...

    @IconSize.setter
    def IconSize(self, value: int) -> None:
        ...
    @property
    def RepeatDelay(self) -> int:
        """
        specifies a repeat delay for the control
        
        Some buttons of a NavigationToolBar may show repeating behavior, e.g. may be repeatedly triggered when the user keeps the mouse pressed over such a button.The delay between two such triggers (in milliseconds) is specified with this property.
        """
        ...

    @RepeatDelay.setter
    def RepeatDelay(self, value: int) -> None:
        ...
    @property
    def ShowFilterSort(self) -> bool:
        """
        determines whether the control should provide functionality for filtering and sorting the parent form
        """
        ...

    @ShowFilterSort.setter
    def ShowFilterSort(self, value: bool) -> None:
        ...
    @property
    def ShowNavigation(self) -> bool:
        """
        determines whether the control should provide functionality for navigating the parent form
        """
        ...

    @ShowNavigation.setter
    def ShowNavigation(self, value: bool) -> None:
        ...
    @property
    def ShowPosition(self) -> bool:
        """
        determines whether the control should provide functionality for positioning the parent form
        """
        ...

    @ShowPosition.setter
    def ShowPosition(self, value: bool) -> None:
        ...
    @property
    def ShowRecordActions(self) -> bool:
        """
        determines whether the control should provide functionality for acting on the current record of the parent form
        """
        ...

    @ShowRecordActions.setter
    def ShowRecordActions(self, value: bool) -> None:
        ...
    @property
    def TextColor(self) -> int:
        """
        specifies the text color (as RGB value) of the control.
        """
        ...

    @TextColor.setter
    def TextColor(self, value: int) -> None:
        ...
    @property
    def TextLineColor(self) -> int:
        """
        specifies the text line color (as RGB value) of the control.
        
        This color is used if the FontDescriptor defines that the text in the control should be underlined or stroke out.
        """
        ...

    @TextLineColor.setter
    def TextLineColor(self, value: int) -> None:
        ...

