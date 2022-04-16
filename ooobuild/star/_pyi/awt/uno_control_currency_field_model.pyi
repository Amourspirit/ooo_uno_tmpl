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
# Namespace: com.sun.star.awt
import typing
from .uno_control_model import UnoControlModel as UnoControlModel_c8ce0c58
if typing.TYPE_CHECKING:
    from .font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ..style.vertical_alignment import VerticalAlignment as VerticalAlignment_8d0e12
    from ..util.color import Color as Color_68e908c5

class UnoControlCurrencyFieldModel(UnoControlModel_c8ce0c58):
    """
    Service Class

    specifies the standard model of a UnoControlCurrencyField.
    
    **since**
    
        OOo 2.0

    See Also:
        `API UnoControlCurrencyFieldModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlCurrencyFieldModel.html>`_
    """
    @property
    def BackgroundColor(self) -> 'Color_68e908c5':
        """
        specifies the background color (RGB) of the control.
        """
    @property
    def Border(self) -> int:
        """
        specifies the border style of the control.
        """
    @property
    def BorderColor(self) -> int:
        """
        specifies the color of the border, if present
        
        Not every border style (see Border) may support coloring. For instance, usually a border with 3D effect will ignore the BorderColor setting.
        
        **since**
        
            OOo 2.0
        """
    @property
    def CurrencySymbol(self) -> str:
        """
        specifies the currency symbol.
        """
    @property
    def DecimalAccuracy(self) -> int:
        """
        specifies the decimal accuracy.
        """
    @property
    def Enabled(self) -> bool:
        """
        determines whether the control is enabled or disabled.
        """
    @property
    def FontDescriptor(self) -> 'FontDescriptor_bc110c0a':
        """
        specifies the font attributes of the text in the control.
        """
    @property
    def FontEmphasisMark(self) -> int:
        """
        specifies the com.sun.star.text.FontEmphasis value of the text in the control.
        """
    @property
    def FontRelief(self) -> int:
        """
        specifies the com.sun.star.text.FontRelief value of the text in the control.
        """
    @property
    def HelpText(self) -> str:
        """
        specifies the help text of the control.
        """
    @property
    def HelpURL(self) -> str:
        """
        specifies the help URL of the control.
        """
    @property
    def HideInactiveSelection(self) -> bool:
        """
        specifies whether the selection in the control should be hidden when the control is not active (focused).
        
        **since**
        
            OOo 2.0
        """
    @property
    def MouseWheelBehavior(self) -> int:
        """
        defines how the mouse wheel can be used to scroll through the control's content.
        
        Usually, the mouse wheel spins the numeric value displayed in the control. Using this property, and one of the MouseWheelBehavior constants, you can control under which circumstances this is possible.
        """
    @property
    def PrependCurrencySymbol(self) -> bool:
        """
        specifies whether the currency symbol is to be prepended.
        """
    @property
    def Printable(self) -> bool:
        """
        specifies that the control will be printed with the document.
        """
    @property
    def ReadOnly(self) -> bool:
        """
        specifies that the content of the control cannot be modified by the user.
        """
    @property
    def Repeat(self) -> bool:
        """
        specifies whether the mouse should show repeating behavior, i.e.
        
        repeatedly trigger an action when keeping pressed.
        
        **since**
        
            OOo 2.0
        """
    @property
    def RepeatDelay(self) -> int:
        """
        specifies the mouse repeat delay, in milliseconds.
        
        When the user presses a mouse in a control area where this triggers an action (such as spinning the value), then usual control implementations allow to repeatedly trigger this action, without the need to release the mouse button and to press it again. The delay between two such triggers is specified with this property.
        
        **since**
        
            OOo 2.0
        """
    @property
    def ShowThousandsSeparator(self) -> bool:
        """
        specifies whether the thousands separator is to be displayed.
        """
    @property
    def Spin(self) -> bool:
        """
        specifies that the control has a spin button.
        """
    @property
    def StrictFormat(self) -> bool:
        """
        specifies that the value is checked during the user input.
        """
    @property
    def Tabstop(self) -> bool:
        """
        specifies that the control can be reached with the TAB key.
        """
    @property
    def TextColor(self) -> 'Color_68e908c5':
        """
        specifies the text color (RGB) of the control.
        """
    @property
    def TextLineColor(self) -> 'Color_68e908c5':
        """
        specifies the text line color (RGB) of the control.
        """
    @property
    def Value(self) -> float:
        """
        specifies the value displayed in the control.
        """
    @property
    def ValueMax(self) -> float:
        """
        specifies the maximum value that can be entered.
        """
    @property
    def ValueMin(self) -> float:
        """
        specifies the minimum value that can be entered.
        """
    @property
    def ValueStep(self) -> float:
        """
        specifies the value step when using the spin button.
        """
    @property
    def VerticalAlign(self) -> 'VerticalAlignment_8d0e12':
        """
        specifies the vertical alignment of the text in the control.
        
        **since**
        
            OOo 3.3
        """
    @property
    def WritingMode(self) -> int:
        """
        denotes the writing mode used in the control, as specified in the com.sun.star.text.WritingMode2 constants group.
        
        Only com.sun.star.text.WritingMode2.LR_TB and com.sun.star.text.WritingMode2.RL_TB are supported at the moment.
        
        **since**
        
            OOo 3.1
        """


