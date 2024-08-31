# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.awt
from __future__ import annotations
import typing
from abc import abstractmethod
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
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.UnoControlSpinButtonModel'
    __ooo_type_name__: str = 'service'

    @property
    @abstractmethod
    def BackgroundColor(self) -> Color_68e908c5:
        """
        specifies the RGB color to be used for the control
        """
        ...

    @property
    @abstractmethod
    def Border(self) -> int:
        """
        specifies the border style of the control.
        """
        ...

    @property
    @abstractmethod
    def BorderColor(self) -> int:
        """
        specifies the color of the border, if present
        
        Not every border style (see Border) may support coloring. For instance, usually a border with 3D effect will ignore the BorderColor setting.
        
        **since**
        
            OOo 2.0
        """
        ...

    @property
    @abstractmethod
    def Enabled(self) -> bool:
        """
        determines whether the control is enabled or disabled.
        """
        ...

    @property
    @abstractmethod
    def HelpText(self) -> str:
        """
        specifies the help text of the control.
        """
        ...

    @property
    @abstractmethod
    def HelpURL(self) -> str:
        """
        specifies the help URL of the control.
        """
        ...

    @property
    @abstractmethod
    def MouseWheelBehavior(self) -> int:
        """
        defines how the mouse wheel can be used to scroll through the control's content.
        
        Usually, the mouse wheel spins the numeric value displayed in the control. Using this property, and one of the MouseWheelBehavior constants, you can control under which circumstances this is possible.
        """
        ...

    @property
    @abstractmethod
    def Orientation(self) -> int:
        """
        specifies the ScrollBarOrientation of the control.
        """
        ...

    @property
    @abstractmethod
    def Printable(self) -> bool:
        """
        specifies whether the control will be printed with the document.
        """
        ...

    @property
    @abstractmethod
    def Repeat(self) -> bool:
        """
        specifies whether the mouse should show repeating behavior, i.e.
        
        repeatedly trigger an action when keeping pressed.
        """
        ...

    @property
    @abstractmethod
    def RepeatDelay(self) -> int:
        """
        specifies the mouse repeat delay, in milliseconds.
        
        When the user presses a mouse in a control area where this triggers an action (such as spinning the value), then usual control implementations allow to repeatedly trigger this action, without the need to release the mouse button and to press it again. The delay between two such triggers is specified with this property.
        """
        ...

    @property
    @abstractmethod
    def SpinIncrement(self) -> int:
        """
        specifies the increment by which the value is changed when using operating the spin button.
        """
        ...

    @property
    @abstractmethod
    def SpinValue(self) -> int:
        """
        specifies the current value of the control.
        """
        ...

    @property
    @abstractmethod
    def SpinValueMax(self) -> int:
        """
        specifies the maximum value of the control.
        """
        ...

    @property
    @abstractmethod
    def SpinValueMin(self) -> int:
        """
        specifies the minimum value of the control.
        """
        ...

    @property
    @abstractmethod
    def SymbolColor(self) -> Color_68e908c5:
        """
        specifies the RGB color to be used when painting symbols which are part of the control's appearance, such as the arrow buttons.
        """
        ...


__all__ = ['UnoControlSpinButtonModel']

