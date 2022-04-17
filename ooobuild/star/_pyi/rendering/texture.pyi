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
# Namespace: com.sun.star.rendering
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from ..geometry.affine_matrix2_d import AffineMatrix2D as AffineMatrix2D_ff040da8
from .stroke_attributes import StrokeAttributes as StrokeAttributes_2dd10f65
from .x_bitmap import XBitmap as XBitmap_b1b70b7b
from .x_parametric_poly_polygon2_d import XParametricPolyPolygon2D as XParametricPolyPolygon2D_b3511228


class Texture(object):
    """
    Struct Class

    Contains all information needed to define a texture.
    
    This structure contains all information necessary to define a texture. A texture describes the filled area of polygonal shapes, providing its own transformation matrix, repeat mode, and transparency.
    
    To achieve uniformity, if this texture has a bitmap set, it is scaled in such a way that it will cover the same [0,1]x[0,1] box as the hatch and the gradient. The transformation member can then be used to scale the complete texture as it fits suit.
    
    **since**
    
        OOo 2.0

    See Also:
        `API Texture <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1Texture.html>`_
    """
    typeName: Literal['com.sun.star.rendering.Texture']

    def __init__(self, AffineTransform: typing.Optional[AffineMatrix2D_ff040da8] = ..., Alpha: typing.Optional[float] = ..., NumberOfHatchPolygons: typing.Optional[int] = ..., Bitmap: typing.Optional[XBitmap_b1b70b7b] = ..., Gradient: typing.Optional[XParametricPolyPolygon2D_b3511228] = ..., Hatching: typing.Optional[XParametricPolyPolygon2D_b3511228] = ..., HatchAttributes: typing.Optional[StrokeAttributes_2dd10f65] = ..., RepeatModeX: typing.Optional[int] = ..., RepeatModeY: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            AffineTransform (AffineMatrix2D, optional): AffineTransform value.
            Alpha (float, optional): Alpha value.
            NumberOfHatchPolygons (int, optional): NumberOfHatchPolygons value.
            Bitmap (XBitmap, optional): Bitmap value.
            Gradient (XParametricPolyPolygon2D, optional): Gradient value.
            Hatching (XParametricPolyPolygon2D, optional): Hatching value.
            HatchAttributes (StrokeAttributes, optional): HatchAttributes value.
            RepeatModeX (int, optional): RepeatModeX value.
            RepeatModeY (int, optional): RepeatModeY value.
        """


    @property
    def AffineTransform(self) -> AffineMatrix2D_ff040da8:
        """
        Texture transformation from texture to primitive space.
        
        This member allows arbitrary transformations of the texture, relative to the textured primitive. Thus, the total transformation from the [0,1]x[0,1] texture space to the device coordinate space is the concatenation of texture, render state, and view state transformation (with only render state and view state transformation being applied to the textured primitive).
        """


    @property
    def Alpha(self) -> float:
        """
        Overall transparency of the texturing.
        
        The valid range for this value is [0,1], where 0 denotes complete transparency, and 1 denotes fully opaque.
        """


    @property
    def NumberOfHatchPolygons(self) -> int:
        """
        Specifies the number of parameterized polygons used for the texture.
        
        This member specifies the number of polygons the parametric polygon interface is queried. The continuous range [0,1] of the XParametricPolyPolygon.getOutline() method is divided up into numberOfHatchPolygons equal parts, and for everyone of these parts, the start of the interval is plugged into the getOutline method. For example, if numberOfHatchPolygons is 2, then getOutline is called twice, once with 0.0 and once with 0.5. Use this parameter to control the density of the hatching.
        """


    @property
    def Bitmap(self) -> XBitmap_b1b70b7b:
        """
        Texture bitmap.
        
        This member can be used together with gradient and hatching.
        
        The bitmap is scaled to a one-by-one rectangle, to cover the same area as both the gradient and the hatching.
        """


    @property
    def Gradient(self) -> XParametricPolyPolygon2D_b3511228:
        """
        Texture gradient.
        
        This member can be used together with bitmap and hatching. The parametric polygons color value is used to fill the returned polygonal outlines.
        """


    @property
    def Hatching(self) -> XParametricPolyPolygon2D_b3511228:
        """
        Texture hatching.
        
        This member can be used together with bitmap and gradient. The parametric polygons color value is used to stroke the returned polygonal outlines.
        """


    @property
    def HatchAttributes(self) -> StrokeAttributes_2dd10f65:
        """
        Specifies the stroke attributes used for hatching.
        
        Use 0.0 as the strokeWidth here to indicate hair lines.
        """


    @property
    def RepeatModeX(self) -> int:
        """
        Repeat mode of the texture, x direction.
        
        The repeat mode is separated into x and y direction, this is the x direction part. Permissible values are from the TexturingMode constants.
        """


    @property
    def RepeatModeY(self) -> int:
        """
        Repeat mode of the texture, y direction.
        
        The repeat mode is separated into x and y direction, this is the y direction part. Permissible values are from the TexturingMode constants.
        """


