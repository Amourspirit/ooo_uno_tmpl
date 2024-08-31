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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.rendering
# Libre Office Version: 2024.2
import typing
from .color_component import ColorComponent as ColorComponent_e4c0e78


class ARGBColor(object):
    """
    Struct Class

    ARGB color quad.

    See Also:
        `API ARGBColor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1ARGBColor.html>`_
    """
    typeName: str = 'com.sun.star.rendering.ARGBColor'

    def __init__(self, Alpha: typing.Optional[ColorComponent_e4c0e78] = ..., Red: typing.Optional[ColorComponent_e4c0e78] = ..., Green: typing.Optional[ColorComponent_e4c0e78] = ..., Blue: typing.Optional[ColorComponent_e4c0e78] = ...) -> None:
        """
        Constructor

        Arguments:
            Alpha (ColorComponent, optional): Alpha value.
            Red (ColorComponent, optional): Red value.
            Green (ColorComponent, optional): Green value.
            Blue (ColorComponent, optional): Blue value.
        """
        ...

    @property
    def Alpha(self) -> ColorComponent_e4c0e78:
        """
        Alpha component.
        
        Valid range is [0,1.0], with 0.0 denoting fully transparent, and 1.0 fully opaque.
        """
        ...
    @Alpha.setter
    def Alpha(self, value: ColorComponent_e4c0e78) -> None:
        ...
    @property
    def Red(self) -> ColorComponent_e4c0e78:
        """
        Red component. Valid range is [0,1.0].
        """
        ...
    @Red.setter
    def Red(self, value: ColorComponent_e4c0e78) -> None:
        ...
    @property
    def Green(self) -> ColorComponent_e4c0e78:
        """
        Green component. Valid range is [0,1.0].
        """
        ...
    @Green.setter
    def Green(self, value: ColorComponent_e4c0e78) -> None:
        ...
    @property
    def Blue(self) -> ColorComponent_e4c0e78:
        """
        Blue component. Valid range is [0,1.0].
        """
        ...
    @Blue.setter
    def Blue(self, value: ColorComponent_e4c0e78) -> None:
        ...

