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
# Namespace: com.sun.star.awt
from __future__ import annotations
import typing
from .uno_control_model import UnoControlModel as UnoControlModel_c8ce0c58
if typing.TYPE_CHECKING:
    from .font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ..util.color import Color as Color_68e908c5
    from ..util.date import Date as Date_60040844
    from com.sun.star.style.VerticalAlignment import VerticalAlignmentProto  # type: ignore

class UnoControlDateFieldModel(UnoControlModel_c8ce0c58):
    """
    Service Class

    specifies the standard model of a UnoControlDateField.
    
    **since**
    
        OOo 2.0

    See Also:
        `API UnoControlDateFieldModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlDateFieldModel.html>`_
    """
    @property
    def BackgroundColor(self) -> Color_68e908c5:
        """
        specifies the background color(RGB) of the control.
        """
        ...
    @BackgroundColor.setter
    def BackgroundColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def Border(self) -> int:
        """
        specifies the border style of the control.
        """
        ...
    @Border.setter
    def Border(self, value: int) -> None:
        ...
    @property
    def BorderColor(self) -> int:
        """
        specifies the color of the border, if present
        
        Not every border style (see Border) may support coloring. For instance, usually a border with 3D effect will ignore the BorderColor setting.
        
        **since**
        
            OOo 2.0
        """
        ...
    @BorderColor.setter
    def BorderColor(self, value: int) -> None:
        ...
    @property
    def Date(self) -> Date_60040844:
        """
        specifies the date displayed in the control.
        """
        ...
    @Date.setter
    def Date(self, value: Date_60040844) -> None:
        ...
    @property
    def DateFormat(self) -> int:
        """
        specifies the format of the displayed date.
        """
        ...
    @DateFormat.setter
    def DateFormat(self, value: int) -> None:
        ...
    @property
    def DateMax(self) -> Date_60040844:
        """
        specifies the maximum date that can be entered.
        """
        ...
    @DateMax.setter
    def DateMax(self, value: Date_60040844) -> None:
        ...
    @property
    def DateMin(self) -> Date_60040844:
        """
        specifies the minimum date that can be entered.
        """
        ...
    @DateMin.setter
    def DateMin(self, value: Date_60040844) -> None:
        ...
    @property
    def DateShowCentury(self) -> bool:
        """
        specifies, if the date century is displayed.
        """
        ...
    @DateShowCentury.setter
    def DateShowCentury(self, value: bool) -> None:
        ...
    @property
    def Dropdown(self) -> bool:
        """
        specifies, if the control has a dropdown button.
        """
        ...
    @Dropdown.setter
    def Dropdown(self, value: bool) -> None:
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
    def FontDescriptor(self) -> FontDescriptor_bc110c0a:
        """
        specifies the font attributes of the text in the control.
        """
        ...
    @FontDescriptor.setter
    def FontDescriptor(self, value: FontDescriptor_bc110c0a) -> None:
        ...
    @property
    def FontEmphasisMark(self) -> int:
        """
        specifies the com.sun.star.text.FontEmphasis value of the text in the control.
        """
        ...
    @FontEmphasisMark.setter
    def FontEmphasisMark(self, value: int) -> None:
        ...
    @property
    def FontRelief(self) -> int:
        """
        specifies the com.sun.star.text.FontRelief value of the text in the control.
        """
        ...
    @FontRelief.setter
    def FontRelief(self, value: int) -> None:
        ...
    @property
    def HelpText(self) -> str:
        """
        specifies the help text of the control.
        """
        ...
    @HelpText.setter
    def HelpText(self, value: str) -> None:
        ...
    @property
    def HelpURL(self) -> str:
        """
        specifies the help URL of the control.
        """
        ...
    @HelpURL.setter
    def HelpURL(self, value: str) -> None:
        ...
    @property
    def HideInactiveSelection(self) -> bool:
        """
        specifies whether the selection in the control should be hidden when the control is not active (focused).
        
        **since**
        
            OOo 2.0
        """
        ...
    @HideInactiveSelection.setter
    def HideInactiveSelection(self, value: bool) -> None:
        ...
    @property
    def MouseWheelBehavior(self) -> int:
        """
        defines how the mouse wheel can be used to scroll through the control's content.
        
        Usually, the mouse wheel spins the numeric value displayed in the control. Using this property, and one of the MouseWheelBehavior constants, you can control under which circumstances this is possible.
        """
        ...
    @MouseWheelBehavior.setter
    def MouseWheelBehavior(self, value: int) -> None:
        ...
    @property
    def Printable(self) -> bool:
        """
        specifies that the control will be printed with the document.
        """
        ...
    @Printable.setter
    def Printable(self, value: bool) -> None:
        ...
    @property
    def ReadOnly(self) -> bool:
        """
        specifies that the content of the control cannot be modified by the user.
        """
        ...
    @ReadOnly.setter
    def ReadOnly(self, value: bool) -> None:
        ...
    @property
    def Repeat(self) -> bool:
        """
        specifies whether the mouse should show repeating behavior, i.e.
        
        repeatedly trigger an action when keeping pressed.
        
        **since**
        
            OOo 2.0
        """
        ...
    @Repeat.setter
    def Repeat(self, value: bool) -> None:
        ...
    @property
    def RepeatDelay(self) -> int:
        """
        specifies the mouse repeat delay, in milliseconds.
        
        When the user presses a mouse in a control area where this triggers an action (such as spinning the value), then usual control implementations allow to repeatedly trigger this action, without the need to release the mouse button and to press it again. The delay between two such triggers is specified with this property.
        
        **since**
        
            OOo 2.0
        """
        ...
    @RepeatDelay.setter
    def RepeatDelay(self, value: int) -> None:
        ...
    @property
    def Spin(self) -> bool:
        """
        specifies that the control has a spin button.
        """
        ...
    @Spin.setter
    def Spin(self, value: bool) -> None:
        ...
    @property
    def StrictFormat(self) -> bool:
        """
        specifies that the date is checked during the user input.
        """
        ...
    @StrictFormat.setter
    def StrictFormat(self, value: bool) -> None:
        ...
    @property
    def Tabstop(self) -> bool:
        """
        specifies that the control can be reached with the TAB key.
        """
        ...
    @Tabstop.setter
    def Tabstop(self, value: bool) -> None:
        ...
    @property
    def Text(self) -> str:
        """
        specifies the text displayed in the control.
        
        **since**
        
            OOo 2.0
        """
        ...
    @Text.setter
    def Text(self, value: str) -> None:
        ...
    @property
    def TextColor(self) -> Color_68e908c5:
        """
        specifies the text color (RGB) of the control.
        """
        ...
    @TextColor.setter
    def TextColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def TextLineColor(self) -> Color_68e908c5:
        """
        specifies the text line color (RGB) of the control.
        """
        ...
    @TextLineColor.setter
    def TextLineColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def VerticalAlign(self) -> VerticalAlignmentProto:
        """
        specifies the vertical alignment of the text in the control.
        
        **since**
        
            OOo 3.3
        """
        ...
    @VerticalAlign.setter
    def VerticalAlign(self, value: VerticalAlignmentProto) -> None:
        ...
    @property
    def WritingMode(self) -> int:
        """
        denotes the writing mode used in the control, as specified in the com.sun.star.text.WritingMode2 constants group.
        
        Only com.sun.star.text.WritingMode2.LR_TB and com.sun.star.text.WritingMode2.RL_TB are supported at the moment.
        
        **since**
        
            OOo 3.1
        """
        ...
    @WritingMode.setter
    def WritingMode(self, value: int) -> None:
        ...