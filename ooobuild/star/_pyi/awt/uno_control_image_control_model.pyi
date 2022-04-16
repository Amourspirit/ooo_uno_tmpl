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
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc
    from ..util.color import Color as Color_68e908c5

class UnoControlImageControlModel(UnoControlModel_c8ce0c58):
    """
    Service Class

    specifies the standard model of a UnoControlImageControl.
    
    **since**
    
        OOo 2.0

    See Also:
        `API UnoControlImageControlModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlImageControlModel.html>`_
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
    def Enabled(self) -> bool:
        """
        determines whether the control is enabled or disabled.
        """
    @property
    def Graphic(self) -> 'XGraphic_a4da0afc':
        """
        specifies a graphic to be displayed on the control
        
        If this property is present, it interacts with the ImageURL in the following way:
        
        **since**
        
            OOo 2.1
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
    def ImageURL(self) -> str:
        """
        specifies a URL to an image to use for the control.
        """
    @property
    def Printable(self) -> bool:
        """
        specifies that the control will be printed with the document.
        """
    @property
    def ScaleImage(self) -> bool:
        """
        specifies if the image is automatically scaled to the size of the control.
        """
    @property
    def ScaleMode(self) -> int:
        """
        defines how to scale the image
        
        If this property is present, it supersedes the ScaleImage property.
        
        The value of this property is one of the ImageScaleMode constants.
        
        **since**
        
            OOo 3.1
        """
    @property
    def Tabstop(self) -> bool:
        """
        specifies that the control can be reached with the TAB key.
        
        **since**
        
            OOo 1.1.2
        """


