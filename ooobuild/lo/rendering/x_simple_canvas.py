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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.rendering
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..geometry.affine_matrix2_d import AffineMatrix2D as AffineMatrix2D_ff040da8
    from ..geometry.real_point2_d import RealPoint2D as RealPoint2D_d6e70c78
    from ..geometry.real_rectangle2_d import RealRectangle2D as RealRectangle2D_d9b0e03
    from .font_metrics import FontMetrics as FontMetrics_e4540d34
    from .render_state import RenderState as RenderState_e4490d27
    from .string_context import StringContext as StringContext_d50e22
    from .view_state import ViewState as ViewState_cab30c62
    from .x_bitmap import XBitmap as XBitmap_b1b70b7b
    from .x_canvas import XCanvas as XCanvas_b19b0b7a
    from .x_canvas_font import XCanvasFont as XCanvasFont_e3380d11
    from .x_graphic_device import XGraphicDevice as XGraphicDevice_ca80e2c
    from .x_poly_polygon2_d import XPolyPolygon2D as XPolyPolygon2D_e1b0e20
    from ..util.color import Color as Color_68e908c5

class XSimpleCanvas(XInterface_8f010a43):
    """
    Provides the basic graphical output operations for a canvas.
    
    This interface is a simplified version of the XCanvas interface. It holds explicit state, i.e. the pen and fill color, the current transformation, clip and font are persistently remembered.
    
    In contrast to the XCanvas interface, XSimpleCanvas does not distinguish between stroke and fill operations; instead, switching between stroke and fill (or taking both) works by setting appropriate pen and fill colors.

    See Also:
        `API XSimpleCanvas <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XSimpleCanvas.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.XSimpleCanvas'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.rendering.XSimpleCanvas'

    @abstractmethod
    def drawBitmap(self, xBitmap: 'XBitmap_b1b70b7b', aLeftTop: 'RealPoint2D_d6e70c78') -> None:
        """
        Draws the bitmap on the canvas.
        """
        ...
    @abstractmethod
    def drawLine(self, aStartPoint: 'RealPoint2D_d6e70c78', aEndPoint: 'RealPoint2D_d6e70c78') -> None:
        """
        Draws a line on the canvas.
        """
        ...
    @abstractmethod
    def drawPixel(self, aPoint: 'RealPoint2D_d6e70c78') -> None:
        """
        Sets a single pixel on the canvas.
        """
        ...
    @abstractmethod
    def drawPolyPolygon(self, xPolyPolygon: 'XPolyPolygon2D_e1b0e20') -> None:
        """
        Draws a poly-polygon on the canvas.
        """
        ...
    @abstractmethod
    def drawRect(self, aRect: 'RealRectangle2D_d9b0e03') -> None:
        """
        Draws a rectangle on the canvas.
        """
        ...
    @abstractmethod
    def drawText(self, aText: 'StringContext_d50e22', aOutPos: 'RealPoint2D_d6e70c78', nTextDirection: int) -> None:
        """
        Draws text on the canvas.
        """
        ...
    @abstractmethod
    def getCanvas(self) -> 'XCanvas_b19b0b7a':
        """
        Query the underlying XCanvas.
        """
        ...
    @abstractmethod
    def getCurrentClipRect(self) -> 'RealRectangle2D_d9b0e03':
        """
        Retrieve current clip rect.
        """
        ...
    @abstractmethod
    def getCurrentFillColor(self) -> 'Color_68e908c5':
        """
        Retrieve color currently used for fills.
        """
        ...
    @abstractmethod
    def getCurrentFont(self) -> 'XCanvasFont_e3380d11':
        """
        Retrieve currently selected font.
        """
        ...
    @abstractmethod
    def getCurrentPenColor(self) -> 'Color_68e908c5':
        """
        Retrieve color currently used for lines.
        """
        ...
    @abstractmethod
    def getCurrentRenderState(self, bUseFillColor: bool) -> 'RenderState_e4490d27':
        """
        Retrieve render state.
        """
        ...
    @abstractmethod
    def getCurrentTransformation(self) -> 'AffineMatrix2D_ff040da8':
        """
        Retrieve current transformation matrix.
        """
        ...
    @abstractmethod
    def getCurrentViewState(self) -> 'ViewState_cab30c62':
        """
        Retrieve view state.
        """
        ...
    @abstractmethod
    def getDevice(self) -> 'XGraphicDevice_ca80e2c':
        """
        Request the associated graphic device for this canvas.
        
        A graphic device provides methods specific to the underlying output device capabilities, which are common for all canvases rendering to such a device. This includes device resolution, color space, or bitmap formats.
        """
        ...
    @abstractmethod
    def getFontMetrics(self) -> 'FontMetrics_e4540d34':
        """
        Request the font metrics of the current font.
        """
        ...
    @abstractmethod
    def selectFont(self, sFontName: str, size: float, bold: bool, italic: bool) -> None:
        """
        Select a font.
        
        This method selects the specified font (or a close substitute) as the current font for text output.
        """
        ...
    @abstractmethod
    def setFillColor(self, nsRgbaColor: 'Color_68e908c5') -> None:
        """
        Sets the fill color.
        
        To disable filling, simply set this color to something with zero alpha (i.e. fully transparent).
        """
        ...
    @abstractmethod
    def setPenColor(self, nsRgbaColor: 'Color_68e908c5') -> None:
        """
        Sets the color used by line and text operations.
        
        To disable stroking, simply set this color to something with zero alpha (i.e. fully transparent).
        """
        ...
    @abstractmethod
    def setRectClip(self, aRect: 'RealRectangle2D_d9b0e03') -> None:
        """
        Sets the clip to the specified rectangle.
        """
        ...
    @abstractmethod
    def setTransformation(self, aTransform: 'AffineMatrix2D_ff040da8') -> None:
        """
        Set the current transform matrix.
        """
        ...

__all__ = ['XSimpleCanvas']

