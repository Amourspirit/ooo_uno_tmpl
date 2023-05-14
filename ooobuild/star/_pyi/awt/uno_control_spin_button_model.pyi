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
    from ..util.color import Color as Color_68e908c5

class UnoControlSpinButtonModel(UnoControlModel_c8ce0c58):
    """
    Service Class

    specifies the standard model of a UnoControlSpinButton.
    
    A spin button is a control which has a numeric value associated with it, and allows to change this value using two spin buttons.
    
    A spin button is similar to a scroll bar, but it usually has no (own) visual representation of the associated value, but is used to propagate its value to other controls.
    
    **since**
    
        OOo 2.0

    See Also:
        `API UnoControlSpinButtonModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlSpinButtonModel.html>`_
    """
    @property
    def BackgroundColor(self) -> 'Color_68e908c5':
        """
        specifies the RGB color to be used for the control
        """
        ...

    @BackgroundColor.setter
    def BackgroundColor(self, value: 'Color_68e908c5') -> None:
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
    def Enabled(self) -> bool:
        """
        determines whether the control is enabled or disabled.
        """
        ...

    @Enabled.setter
    def Enabled(self, value: bool) -> None:
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
    def Orientation(self) -> int:
        """
        specifies the ScrollBarOrientation of the control.
        """
        ...

    @Orientation.setter
    def Orientation(self, value: int) -> None:
        ...
    @property
    def Printable(self) -> bool:
        """
        specifies whether the control will be printed with the document.
        """
        ...

    @Printable.setter
    def Printable(self, value: bool) -> None:
        ...
    @property
    def Repeat(self) -> bool:
        """
        specifies whether the mouse should show repeating behavior, i.e.
        
        repeatedly trigger an action when keeping pressed.
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
        """
        ...

    @RepeatDelay.setter
    def RepeatDelay(self, value: int) -> None:
        ...
    @property
    def SpinIncrement(self) -> int:
        """
        specifies the increment by which the value is changed when using operating the spin button.
        """
        ...

    @SpinIncrement.setter
    def SpinIncrement(self, value: int) -> None:
        ...
    @property
    def SpinValue(self) -> int:
        """
        specifies the current value of the control.
        """
        ...

    @SpinValue.setter
    def SpinValue(self, value: int) -> None:
        ...
    @property
    def SpinValueMax(self) -> int:
        """
        specifies the maximum value of the control.
        """
        ...

    @SpinValueMax.setter
    def SpinValueMax(self, value: int) -> None:
        ...
    @property
    def SpinValueMin(self) -> int:
        """
        specifies the minimum value of the control.
        """
        ...

    @SpinValueMin.setter
    def SpinValueMin(self, value: int) -> None:
        ...
    @property
    def SymbolColor(self) -> 'Color_68e908c5':
        """
        specifies the RGB color to be used when painting symbols which are part of the control's appearance, such as the arrow buttons.
        """
        ...

    @SymbolColor.setter
    def SymbolColor(self, value: 'Color_68e908c5') -> None:
        ...

