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
from .uno_control_model import UnoControlModel as UnoControlModel_c8ce0c58
if typing.TYPE_CHECKING:
    from .font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ..util.color import Color as Color_68e908c5

class UnoControlFixedLineModel(UnoControlModel_c8ce0c58):
    """
    Service Class

    specifies the standard model of a UnoControlFixedLine.

    See Also:
        `API UnoControlFixedLineModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlFixedLineModel.html>`_
    """
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
    def Label(self) -> str:
        """
        specifies the label of the control.
        """
        ...
    @Label.setter
    def Label(self, value: str) -> None:
        ...
    @property
    def Orientation(self) -> int:
        """
        specifies the orientation of the control.
        """
        ...
    @Orientation.setter
    def Orientation(self, value: int) -> None:
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

