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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.form.component
from __future__ import annotations
import typing
from abc import abstractproperty
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
    __ooo_ns__: str = 'com.sun.star.form.component'
    __ooo_full_ns__: str = 'com.sun.star.form.component.NavigationToolBar'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Border(self) -> int:
        """
        denotes the border style of the control.
        
        Allowed values are
        """
        ...

    @abstractproperty
    def Enabled(self) -> bool:
        """
        determines whether the control is enabled or disabled.
        """
        ...

    @abstractproperty
    def FontDescriptor(self) -> FontDescriptor_bc110c0a:
        """
        contains the font attributes for the text in the control
        """
        ...

    @abstractproperty
    def FontEmphasisMark(self) -> int:
        """
        specifies the emphasis mark for the font described in FontDescriptor
        
        The value must be one of the com.sun.star.text.FontEmphasis constants.
        """
        ...

    @abstractproperty
    def FontRelief(self) -> int:
        """
        specifies the relief for the font described in FontDescriptor
        
        The value must be one of the com.sun.star.text.FontRelief constants.
        """
        ...

    @abstractproperty
    def IconSize(self) -> int:
        """
        specifies the size of the icons in the control
        
        At least the following values are to be supported:
        """
        ...

    @abstractproperty
    def RepeatDelay(self) -> int:
        """
        specifies a repeat delay for the control
        
        Some buttons of a NavigationToolBar may show repeating behavior, e.g. may be repeatedly triggered when the user keeps the mouse pressed over such a button.The delay between two such triggers (in milliseconds) is specified with this property.
        """
        ...

    @abstractproperty
    def ShowFilterSort(self) -> bool:
        """
        determines whether the control should provide functionality for filtering and sorting the parent form
        """
        ...

    @abstractproperty
    def ShowNavigation(self) -> bool:
        """
        determines whether the control should provide functionality for navigating the parent form
        """
        ...

    @abstractproperty
    def ShowPosition(self) -> bool:
        """
        determines whether the control should provide functionality for positioning the parent form
        """
        ...

    @abstractproperty
    def ShowRecordActions(self) -> bool:
        """
        determines whether the control should provide functionality for acting on the current record of the parent form
        """
        ...

    @abstractproperty
    def TextColor(self) -> int:
        """
        specifies the text color (as RGB value) of the control.
        """
        ...

    @abstractproperty
    def TextLineColor(self) -> int:
        """
        specifies the text line color (as RGB value) of the control.
        
        This color is used if the FontDescriptor defines that the text in the control should be underlined or stroke out.
        """
        ...


__all__ = ['NavigationToolBar']

