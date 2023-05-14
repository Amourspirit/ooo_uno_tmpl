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

class UnoControlProgressBarModel(UnoControlModel_c8ce0c58):
    """
    Service Class

    specifies the standard model of a UnoControlProgressBar.
    
    **since**
    
        OOo 2.0

    See Also:
        `API UnoControlProgressBarModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlProgressBarModel.html>`_
    """
    @property
    def BackgroundColor(self) -> 'Color_68e908c5':
        """
        specifies the background color (RGB) of the control.
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
    def FillColor(self) -> 'Color_68e908c5':
        """
        specifies the fill color (RGB) of the control.
        """
        ...

    @FillColor.setter
    def FillColor(self, value: 'Color_68e908c5') -> None:
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
    def Printable(self) -> bool:
        """
        specifies that the control will be printed with the document.
        """
        ...

    @Printable.setter
    def Printable(self, value: bool) -> None:
        ...
    @property
    def ProgressValue(self) -> int:
        """
        specifies the progress value of the control.
        """
        ...

    @ProgressValue.setter
    def ProgressValue(self, value: int) -> None:
        ...
    @property
    def ProgressValueMax(self) -> int:
        """
        specifies the maximum progress value of the control.
        """
        ...

    @ProgressValueMax.setter
    def ProgressValueMax(self, value: int) -> None:
        ...
    @property
    def ProgressValueMin(self) -> int:
        """
        specifies the minimum progress value of the control.
        """
        ...

    @ProgressValueMin.setter
    def ProgressValueMin(self, value: int) -> None:
        ...

