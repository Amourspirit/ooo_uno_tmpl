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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.awt
# Libre Office Version: 7.2
from enum import Enum


class FontSlant(Enum):
    """
    Enum Class

    

    See Also:
        `API FontSlant <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html#a362a86d3ebca4a201d13bc3e7b94340e>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.FontSlant'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.awt.FontSlant'

    DONTKNOW = 'DONTKNOW'
    """
    specifies a font with an unknown slant.
    
    specifies that the menu item type is unknown.
    """
    ITALIC = 'ITALIC'
    """
    specifies an italic font (slant designed into the font).
    """
    NONE = 'NONE'
    """
    specifies a font without slant.
    """
    OBLIQUE = 'OBLIQUE'
    """
    specifies an oblique font (slant not designed into the font).
    """
    REVERSE_ITALIC = 'REVERSE_ITALIC'
    """
    specifies a reverse italic font (slant designed into the font).
    """
    REVERSE_OBLIQUE = 'REVERSE_OBLIQUE'
    """
    specifies a reverse oblique font (slant not designed into the font).
    """

__all__ = ['FontSlant']

