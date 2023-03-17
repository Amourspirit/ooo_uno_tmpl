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
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt
import typing
from abc import abstractproperty
from .uno_control_model import UnoControlModel as UnoControlModel_c8ce0c58
from ..container.x_container import XContainer as XContainer_d6fb0cc6
from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47
from ..lang.x_multi_service_factory import XMultiServiceFactory as XMultiServiceFactory_191e0eb6
if typing.TYPE_CHECKING:
    from .font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from ..util.color import Color as Color_68e908c5

class UnoControlDialogModel(UnoControlModel_c8ce0c58, XContainer_d6fb0cc6, XNameContainer_cb90e47, XMultiServiceFactory_191e0eb6):
    """
    Service Class

    specifies the standard model of a UnoControlDialog.
    
    **since**
    
        OOo 2.3

    See Also:
        `API UnoControlDialogModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlDialogModel.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.UnoControlDialogModel'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def BackgroundColor(self) -> 'Color_68e908c5':
        """
        specifies the background color (RGB) of the dialog.
        """
        ...

    @abstractproperty
    def Closeable(self) -> bool:
        """
        specifies if the dialog is closeable.
        """
        ...

    @abstractproperty
    def DesktopAsParent(self) -> bool:
        """
        If set to true the dialog will have the desktop as parent.
        
        **since**
        
            OOo 2.3
        """
        ...

    @abstractproperty
    def Enabled(self) -> bool:
        """
        determines whether a dialog is enabled or disabled.
        """
        ...

    @abstractproperty
    def FontDescriptor(self) -> 'FontDescriptor_bc110c0a':
        """
        specifies the font attributes of the text in the caption bar of the dialog.
        """
        ...

    @abstractproperty
    def FontEmphasisMark(self) -> int:
        """
        specifies the com.sun.star.text.FontEmphasis value of the text in the caption bar of the dialog.
        """
        ...

    @abstractproperty
    def FontRelief(self) -> int:
        """
        specifies the com.sun.star.text.FontRelief value of the text in the caption bar of the dialog.
        """
        ...

    @abstractproperty
    def Graphic(self) -> 'XGraphic_a4da0afc':
        """
        specifies a graphic to be displayed as a background image
        
        If this property is present, it interacts with the ImageURL in the following way:
        
        **since**
        
            OOo 2.4
        """
        ...

    @abstractproperty
    def HScroll(self) -> bool:
        """
        specifies that a horizontal scrollbar should be added to the dialog
        
        **since**
        
            LibreOffice 4.0
        """
        ...

    @abstractproperty
    def HelpText(self) -> str:
        """
        specifies the help text of the dialog.
        """
        ...

    @abstractproperty
    def HelpURL(self) -> str:
        """
        specifies the help URL of the dialog.
        """
        ...

    @abstractproperty
    def ImageURL(self) -> str:
        """
        specifies a URL that references a graphic that should be used as a background image.
        
        **since**
        
            OOo 2.4
        """
        ...

    @abstractproperty
    def Moveable(self) -> bool:
        """
        specifies if the dialog is moveable.
        """
        ...

    @abstractproperty
    def ScrollHeight(self) -> int:
        """
        specifies the total height of the scrollable dialog content
        
        **since**
        
            LibreOffice 4.0
        """
        ...

    @abstractproperty
    def ScrollLeft(self) -> int:
        """
        specifies the horizontal position of the scrolled dialog content
        
        **since**
        
            LibreOffice 4.0
        """
        ...

    @abstractproperty
    def ScrollTop(self) -> int:
        """
        specifies the vertical position of the scrolled dialog content
        
        **since**
        
            LibreOffice 4.0
        """
        ...

    @abstractproperty
    def ScrollWidth(self) -> int:
        """
        specifies the total width of the scrollable dialog content
        
        **since**
        
            LibreOffice 4.0
        """
        ...

    @abstractproperty
    def Sizeable(self) -> bool:
        """
        specifies if the dialog is sizeable.
        """
        ...

    @abstractproperty
    def TextColor(self) -> 'Color_68e908c5':
        """
        specifies the text color (RGB) of the dialog.
        """
        ...

    @abstractproperty
    def TextLineColor(self) -> 'Color_68e908c5':
        """
        specifies the text line color (RGB) of the dialog.
        """
        ...

    @abstractproperty
    def Title(self) -> str:
        """
        specifies the text that is displayed in the caption bar of the dialog.
        """
        ...

    @abstractproperty
    def VScroll(self) -> bool:
        """
        specifies that a vertical scrollbar should be added to the dialog
        
        **since**
        
            LibreOffice 4.0
        """
        ...



__all__ = ['UnoControlDialogModel']

