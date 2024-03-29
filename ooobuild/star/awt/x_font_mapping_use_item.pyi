# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.4
import typing


class XFontMappingUseItem(object):
    """
    Struct Class

    Information about a font mapping that took place.
    
    **since**
    
        LibreOffice 7.3

    See Also:
        `API XFontMappingUseItem <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1XFontMappingUseItem.html>`_
    """
    typeName: str = 'com.sun.star.awt.XFontMappingUseItem'

    def __init__(self, usedFonts: typing.Optional[typing.Tuple[str, ...]] = ..., originalFont: typing.Optional[str] = ..., count: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            usedFonts (typing.Tuple[str, ...], optional): usedFonts value.
            originalFont (str, optional): originalFont value.
            count (int, optional): count value.
        """
        ...

    @property
    def usedFonts(self) -> typing.Tuple[str, ...]:
        """
        A list of fonts that were actually used, in their order.
        
        Each font is identified as family name or 'familyName/styleName' (if style name is not empty).
        """
        ...
    @usedFonts.setter
    def usedFonts(self, value: typing.Tuple[str, ...]) -> None:
        ...
    @property
    def originalFont(self) -> str:
        """
        The family name or 'familyName/styleName' (if style name is not empty) of the requested font.
        """
        ...
    @originalFont.setter
    def originalFont(self, value: str) -> None:
        ...
    @property
    def count(self) -> int:
        """
        The number of times this mapping took place.
        """
        ...
    @count.setter
    def count(self, value: int) -> None:
        ...

