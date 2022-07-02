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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.awt
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class SimpleFontMetric(object):
    """
    Struct Class

    describes the general metrics of a certain font.

    See Also:
        `API SimpleFontMetric <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1SimpleFontMetric.html>`_
    """
    typeName: Literal['com.sun.star.awt.SimpleFontMetric']

    def __init__(self, Ascent: typing.Optional[int] = ..., Descent: typing.Optional[int] = ..., Leading: typing.Optional[int] = ..., Slant: typing.Optional[int] = ..., FirstChar: typing.Optional[str] = ..., LastChar: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Ascent (int, optional): Ascent value.
            Descent (int, optional): Descent value.
            Leading (int, optional): Leading value.
            Slant (int, optional): Slant value.
            FirstChar (str, optional): FirstChar value.
            LastChar (str, optional): LastChar value.
        """
        ...


    @property
    def Ascent(self) -> int:
        """
        specifies the portion of a lower case character that rises above the height of the character \"x\" of the font.
        
        For example, the letters \"b\", \"d\", \"h\", \"k\" and \"l\" have an ascent unequal to 0.
        
        The ascent is measured in pixels, thus the font metric is device dependent.
        """
        ...


    @property
    def Descent(self) -> int:
        """
        specifies the portion of a letter falling below the baseline.
        
        For example, the letters \"g\", \"p\", and \"y\" have a descent unequal to 0.
        
        The descent is measured in pixels, thus the font metric is device dependent.
        """
        ...


    @property
    def Leading(self) -> int:
        """
        specifies the vertical space between lines of this font; it is also called internal line spacing.
        
        The leading is measured in pixels, thus the font metric is device dependent.
        """
        ...


    @property
    def Slant(self) -> int:
        """
        specifies the slant of the characters (italic).
        
        The slant is measured in degrees from 0 to 359.
        """
        ...


    @property
    def FirstChar(self) -> str:
        """
        specifies the code of the first printable character in the font.
        """
        ...


    @property
    def LastChar(self) -> str:
        """
        specifies the code of the last printable character in the font.
        """
        ...


