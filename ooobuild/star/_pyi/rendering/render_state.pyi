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
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing
from ..geometry.affine_matrix2_d import AffineMatrix2D as AffineMatrix2D_ff040da8
from .color_component import ColorComponent as ColorComponent_e4c0e78
from .x_poly_polygon2_d import XPolyPolygon2D as XPolyPolygon2D_e1b0e20


class RenderState(object):
    """
    Struct Class

    This structure contains information passed to each XCanvas render operation.
    
    This structure contains information considered as the render state, i.e. the common setup required to render each individual XCanvas primitive.
    
    **since**
    
        OOo 2.0

    See Also:
        `API RenderState <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1RenderState.html>`_
    """
    typeName: Literal['com.sun.star.rendering.RenderState']

    def __init__(self, DeviceColor: typing.Optional[typing.Tuple[ColorComponent_e4c0e78, ...]] = ..., AffineTransform: typing.Optional[AffineMatrix2D_ff040da8] = ..., Clip: typing.Optional[XPolyPolygon2D_e1b0e20] = ..., CompositeOperation: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            DeviceColor (typing.Tuple[ColorComponent, ...], optional): DeviceColor value.
            AffineTransform (AffineMatrix2D, optional): AffineTransform value.
            Clip (XPolyPolygon2D, optional): Clip value.
            CompositeOperation (int, optional): CompositeOperation value.
        """
        ...


    @property
    def DeviceColor(self) -> typing.Tuple[ColorComponent_e4c0e78, ...]:
        """
        The device color associated with this render operation.
        
        Note that this need not be RGB here, but depends on the active device color space.
        """
        ...


    @property
    def AffineTransform(self) -> AffineMatrix2D_ff040da8:
        """
        The affine transform associated with this render operation.
        
        This is used to transform coordinates of canvas primitives from user space to view space (from which they are subsequently transformed to device space by the view transform).
        """
        ...


    @property
    def Clip(self) -> XPolyPolygon2D_e1b0e20:
        """
        The clipping area associated with this render operation.
        
        This clipping is interpreted in the user coordinate system, i.e. subject to the render state transform followed by the view transform before mapped to device coordinate space.
        
        Specifying an empty interface denotes no clipping, i.e. everything rendered to the canvas will be visible (subject to device-dependent constraints, of course). Specifying an empty XPolyPolygon2D, i.e. a poly-polygon containing zero polygons, or an XPolyPolygon2D with any number of empty sub-polygons, denotes the NULL clip. That means, nothing rendered to the canvas will be visible.
        """
        ...


    @property
    def CompositeOperation(self) -> int:
        """
        The composition mode associated with this render operation.
        
        The composite mode determines in which way the primitive and possibly existing background is combined. The permissible values must be one out of the CompositeOperation constants.
        """
        ...


