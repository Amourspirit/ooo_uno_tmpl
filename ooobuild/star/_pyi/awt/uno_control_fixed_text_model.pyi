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

class UnoControlFixedTextModel(UnoControlModel_c8ce0c58):
    """
    Service Class

    specifies the standard model of a UnoControlFixedText.
    
    **since**
    
        OOo 2.0

    See Also:
        `API UnoControlFixedTextModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlFixedTextModel.html>`_
    """
    @property
    def Align(self) -> int:
        """
        specifies the horizontal alignment of the text in the control.
        """
        ...

    @Align.setter
    def Align(self, value: int) -> None:
        ...
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
    def FontDescriptor(self) -> 'FontDescriptor_bc110c0a':
        """
        specifies the font attributes of the text in the control.
        """
        ...

    @FontDescriptor.setter
    def FontDescriptor(self, value: 'FontDescriptor_bc110c0a') -> None:
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
    def Label(self) -> str:
        """
        specifies the label of the control.
        """
        ...

    @Label.setter
    def Label(self, value: str) -> None:
        ...
    @property
    def MultiLine(self) -> bool:
        """
        specifies that the text may be displayed on more than one line.
        """
        ...

    @MultiLine.setter
    def MultiLine(self, value: bool) -> None:
        ...
    @property
    def NoLabel(self) -> bool:
        """
        suppresses automatic accelerator assignment on this control.
        
        **since**
        
            OOo 2.4
        """
        ...

    @NoLabel.setter
    def NoLabel(self, value: bool) -> None:
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
    def TextColor(self) -> 'Color_68e908c5':
        """
        specifies the text color (RGB) of the control.
        """
        ...

    @TextColor.setter
    def TextColor(self, value: 'Color_68e908c5') -> None:
        ...
    @property
    def TextLineColor(self) -> 'Color_68e908c5':
        """
        specifies the text line color (RGB) of the control.
        """
        ...

    @TextLineColor.setter
    def TextLineColor(self, value: 'Color_68e908c5') -> None:
        ...
    @property
    def VerticalAlign(self) -> 'VerticalAlignment_8d0e12':
        """
        specifies the vertical alignment of the text in the control.
        
        **since**
        
            OOo 2.0
        """
        ...

    @VerticalAlign.setter
    def VerticalAlign(self, value: 'VerticalAlignment_8d0e12') -> None:
        ...

