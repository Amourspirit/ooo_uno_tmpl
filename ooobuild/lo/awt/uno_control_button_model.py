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
# Namespace: com.sun.star.awt
import typing
from abc import abstractproperty
from .uno_control_model import UnoControlModel as UnoControlModel_c8ce0c58
if typing.TYPE_CHECKING:
    from .font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from ..style.vertical_alignment import VerticalAlignment as VerticalAlignment_8d0e12
    from ..util.color import Color as Color_68e908c5

class UnoControlButtonModel(UnoControlModel_c8ce0c58):
    """
    Service Class

    specifies the standard model of a UnoControlButton.
    
    **since**
    
        OOo 2.0

    See Also:
        `API UnoControlButtonModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlButtonModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.UnoControlButtonModel'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Align(self) -> int:
        """
        specifies the horizontal alignment of the text in the control.
        """

    @abstractproperty
    def BackgroundColor(self) -> 'Color_68e908c5':
        """
        specifies the background color (RGB) of the control.
        """

    @abstractproperty
    def DefaultButton(self) -> bool:
        """
        specifies that the button is the default button on the document.
        """

    @abstractproperty
    def Enabled(self) -> bool:
        """
        determines whether the control is enabled or disabled.
        """

    @abstractproperty
    def FocusOnClick(self) -> bool:
        """
        specifies whether the button control should grab the focus when clicked.
        
        If set to TRUE (which is the default), the button control automatically grabs the focus when the user clicks onto it with the mouse.
        If set to FALSE, the focus is preserved when the user operates the button control with the mouse.
        
        **since**
        
            OOo 2.0
        """

    @abstractproperty
    def FontDescriptor(self) -> 'FontDescriptor_bc110c0a':
        """
        specifies the font attributes of the text in the control.
        """

    @abstractproperty
    def FontEmphasisMark(self) -> int:
        """
        specifies the com.sun.star.text.FontEmphasis value of the text in the control.
        """

    @abstractproperty
    def FontRelief(self) -> int:
        """
        specifies the com.sun.star.text.FontRelief value of the text in the control.
        """

    @abstractproperty
    def Graphic(self) -> 'XGraphic_a4da0afc':
        """
        specifies a graphic to be displayed at the button
        
        If this property is present, it interacts with the ImageURL in the following way:
        
        **since**
        
            OOo 2.1
        """

    @abstractproperty
    def HelpText(self) -> str:
        """
        specifies the help text of the control.
        """

    @abstractproperty
    def HelpURL(self) -> str:
        """
        specifies the help URL of the control.
        """

    @abstractproperty
    def ImageAlign(self) -> int:
        """
        specifies the alignment of the image inside the button as ImageAlign value.
        """

    @abstractproperty
    def ImagePosition(self) -> int:
        """
        specifies the position of the image, if any, relative to the text, if any
        
        Valid values of this property are specified with ImagePosition.
        
        If this property is present, it supersedes the ImageAlign property - setting one of both properties sets the other one to the best possible match.
        """

    @abstractproperty
    def ImageURL(self) -> str:
        """
        specifies a URL to an image to use for the button.
        """

    @abstractproperty
    def Label(self) -> str:
        """
        specifies the label of the control.
        """

    @abstractproperty
    def MultiLine(self) -> bool:
        """
        specifies that the text may be displayed on more than one line.
        
        **since**
        
            OOo 2.0
        """

    @abstractproperty
    def Printable(self) -> bool:
        """
        specifies that the control will be printed with the document.
        """

    @abstractproperty
    def PushButtonType(self) -> int:
        """
        specifies the default action of the button as PushButtonType value.
        """

    @abstractproperty
    def Repeat(self) -> bool:
        """
        specifies whether the control should show repeating behavior.
        
        Normally, when you click a button with the mouse, you need to release the mouse button, and press it again. With this property set to TRUE, the button is repeatedly pressed while you hold down the mouse button.
        
        **since**
        
            OOo 2.0
        """

    @abstractproperty
    def RepeatDelay(self) -> int:
        """
        specifies the mouse repeat delay, in milliseconds.
        
        When the user presses a mouse in a control area where this triggers an action (such as pressing the button), then usual control implementations allow to repeatedly trigger this action, without the need to release the mouse button and to press it again. The delay between two such triggers is specified with this property.
        
        **since**
        
            OOo 2.0
        """

    @abstractproperty
    def State(self) -> int:
        """
        specifies the state of the control.
        
        If Toggle property is set to TRUE, the pressed state is enabled and its pressed state can be obtained with this property.
        """

    @abstractproperty
    def Tabstop(self) -> bool:
        """
        specifies that the control can be reached with the TAB key.
        """

    @abstractproperty
    def TextColor(self) -> 'Color_68e908c5':
        """
        specifies the text color (RGB) of the control.
        """

    @abstractproperty
    def TextLineColor(self) -> 'Color_68e908c5':
        """
        specifies the text line color (RGB) of the control.
        """

    @abstractproperty
    def Toggle(self) -> bool:
        """
        specifies whether the button should toggle on a single operation.
        
        If this property is set to TRUE, a single operation of the button control (pressing space while it is focused, or clicking onto it) toggles it between a pressed and a not pressed state.
        
        The default for this property is FALSE, which means the button behaves like a usual push button.
        
        **since**
        
            OOo 2.0
        """

    @abstractproperty
    def VerticalAlign(self) -> 'VerticalAlignment_8d0e12':
        """
        specifies the vertical alignment of the text in the control.
        
        **since**
        
            OOo 2.0
        """



__all__ = ['UnoControlButtonModel']

