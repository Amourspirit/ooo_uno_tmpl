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
from .font_slant import FontSlant as FontSlant_849509ed


class FontDescriptor(object):
    """
    Struct Class

    describes the characteristics of a font.
    
    For example, this can be used to select a font.

    See Also:
        `API FontDescriptor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1FontDescriptor.html>`_
    """
    typeName: Literal['com.sun.star.awt.FontDescriptor']

    def __init__(self, Name: typing.Optional[str] = ..., Height: typing.Optional[int] = ..., Width: typing.Optional[int] = ..., StyleName: typing.Optional[str] = ..., Family: typing.Optional[int] = ..., CharSet: typing.Optional[int] = ..., Pitch: typing.Optional[int] = ..., CharacterWidth: typing.Optional[float] = ..., Weight: typing.Optional[float] = ..., Slant: typing.Optional[FontSlant_849509ed] = ..., Underline: typing.Optional[int] = ..., Strikeout: typing.Optional[int] = ..., Orientation: typing.Optional[float] = ..., Kerning: typing.Optional[bool] = ..., WordLineMode: typing.Optional[bool] = ..., Type: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            Height (int, optional): Height value.
            Width (int, optional): Width value.
            StyleName (str, optional): StyleName value.
            Family (int, optional): Family value.
            CharSet (int, optional): CharSet value.
            Pitch (int, optional): Pitch value.
            CharacterWidth (float, optional): CharacterWidth value.
            Weight (float, optional): Weight value.
            Slant (FontSlant, optional): Slant value.
            Underline (int, optional): Underline value.
            Strikeout (int, optional): Strikeout value.
            Orientation (float, optional): Orientation value.
            Kerning (bool, optional): Kerning value.
            WordLineMode (bool, optional): WordLineMode value.
            Type (int, optional): Type value.
        """


    @property
    def Name(self) -> str:
        """
        specifies the exact name of the font.
        """


    @property
    def Height(self) -> int:
        """
        specifies the height of the font in the measure of the destination.
        """


    @property
    def Width(self) -> int:
        """
        specifies the width of the font in the measure of the destination.
        """


    @property
    def StyleName(self) -> str:
        """
        specifies the style name of the font.
        """


    @property
    def Family(self) -> int:
        """
        specifies the general style of the font.
        
        Use one value out of the constant group com.sun.star.awt.FontFamily.
        """


    @property
    def CharSet(self) -> int:
        """
        specifies the character set which is supported by the font.
        
        Use one value out of the constant group com.sun.star.awt.CharSet.
        """


    @property
    def Pitch(self) -> int:
        """
        specifies the pitch of the font.
        
        Use one value out of the constant group com.sun.star.awt.FontPitch.
        """


    @property
    def CharacterWidth(self) -> float:
        """
        specifies the character width.
        
        Depending on the specified width, a font that supports this width may be selected.
        
        The value is expressed as a percentage.
        """


    @property
    def Weight(self) -> float:
        """
        specifies the thickness of the line.
        
        Depending on the specified weight, a font that supports this thickness may be selected.
        
        The value is expressed as a percentage.
        """


    @property
    def Slant(self) -> FontSlant_849509ed:
        """
        specifies the slant of the font.
        """


    @property
    def Underline(self) -> int:
        """
        specifies the kind of underlining.
        
        Use one value out of the constant group com.sun.star.awt.FontUnderline.
        """


    @property
    def Strikeout(self) -> int:
        """
        specifies the kind of strikeout.
        
        Use one value out of the constant group com.sun.star.awt.FontStrikeout.
        """


    @property
    def Orientation(self) -> float:
        """
        specifies the rotation of the font.
        
        The unit of measure is degrees; 0 is the baseline.
        """


    @property
    def Kerning(self) -> bool:
        """
        For requesting, it specifies if there is a kerning table available.
        
        For selecting, it specifies if the kerning table is to be used.
        """


    @property
    def WordLineMode(self) -> bool:
        """
        specifies if only words get underlined.
        
        TRUE means that only non-space characters get underlined, FALSE means that the spacing also gets underlined.
        
        This property is only valid if the property com.sun.star.awt.FontDescriptor.Underline is not FontUnderline.NONE.
        """


    @property
    def Type(self) -> int:
        """
        specifies the technology of the font representation.
        
        One or more values out of the constant group com.sun.star.awt.FontType can be combined by an arithmetical or-operation.
        """


