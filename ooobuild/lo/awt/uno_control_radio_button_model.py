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

class UnoControlRadioButtonModel(UnoControlModel_c8ce0c58):
    """
    Service Class

    specifies the standard model of a UnoControlRadioButton.
    
    **since**
    
        OOo 2.0

    See Also:
        `API UnoControlRadioButtonModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlRadioButtonModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.UnoControlRadioButtonModel'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def Align(self) -> int:
        """
        specifies the horizontal alignment of the text in the control.
        
        **since**
        
            OOo 2.0
        """

    @abstractproperty
    def BackgroundColor(self) -> int:
        """
        specifies the background color (RGB) of the control.
        """

    @abstractproperty
    def Enabled(self) -> bool:
        """
        determines whether the control is enabled or disabled.
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
        specifies a graphic to be displayed besides the label of the control
        
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
    def ImagePosition(self) -> int:
        """
        specifies the position of the image, if any, relative to the text, if any
        
        Valid values of this property are specified with ImagePosition.
        """

    @abstractproperty
    def ImageURL(self) -> str:
        """
        specifies a URL to an image to display besides the label of the control
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
    def State(self) -> int:
        """
        specifies the state of the control.
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
    def VerticalAlign(self) -> 'VerticalAlignment_8d0e12':
        """
        specifies the vertical alignment of the text in the control.
        
        **since**
        
            OOo 2.0
        """

    @abstractproperty
    def VisualEffect(self) -> int:
        """
        specifies a visual effect to apply to the radio button control.
        
        Possible values for this property are VisualEffect.FLAT and VisualEffect.LOOK3D.
        
        **since**
        
            OOo 2.0
        """

    @abstractproperty
    def WritingMode(self) -> int:
        """
        denotes the writing mode used in the control, as specified in the com.sun.star.text.WritingMode2 constants group.
        
        Only com.sun.star.text.WritingMode2.LR_TB and com.sun.star.text.WritingMode2.RL_TB are supported at the moment.
        
        **since**
        
            OOo 3.1
        """



__all__ = ['UnoControlRadioButtonModel']

