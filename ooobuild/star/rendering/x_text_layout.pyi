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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.rendering
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..geometry.real_point2_d import RealPoint2D as RealPoint2D_d6e70c78
    from ..geometry.real_rectangle2_d import RealRectangle2D as RealRectangle2D_d9b0e03
    from .caret import Caret as Caret_9b480ab5
    from .string_context import StringContext as StringContext_d50e22
    from .text_hit import TextHit as TextHit_b25d0b90
    from .x_canvas_font import XCanvasFont as XCanvasFont_e3380d11
    from .x_poly_polygon2_d import XPolyPolygon2D as XPolyPolygon2D_e1b0e20


class XTextLayout(XInterface_8f010a43):
    """
    This is the central interface for text layouting.
    
    This is the central interface for text-related tasks more complicated than simple string rendering. Note that all query methods are subject to the current layout state of this object. That is, calls to XTextLayout.justify() or XTextLayout.applyLogicalAdvancements() are likely to change subsequent output of those query methods.
    
    Similar to XCanvasFont, all measurements and coordinates accepted and returned by this interface are relative to the font's local coordinate system (which only equals device coordinate space, if the combined render transformation used during text output is the identity transformation). Conversely, if the combined transformation used during text output is not the identity transformation, all measurements returned by this interface should be subjected to that transformation, to yield values in device coordinate space. Depending on the underlying font technology, actual device output might be off by up to one device pixel from the transformed metrics.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XTextLayout <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XTextLayout.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.rendering.XTextLayout'

    def applyLogicalAdvancements(self, aAdvancements: typing.Tuple[float, ...]) -> None:
        """
        Apply explicit advancements for every character in the layout string.
        
        This method applies the specified advancements to every logical character in the input string (not for every glyph. There might be multiple glyphs per input character, or multiple input characters per glyph). This is useful to explicitly manipulate the exact output positions of characters, e.g. relative to a reference output device.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def combinedJustify(self, aNextLayouts: typing.Tuple[XTextLayout, ...], nSize: float) -> float:
        """
        Justify a number of text layouts to the given size.
        
        This method can be used to combine the layout of a text line into a single justification run. This is e.g. useful if the line consists of several text portions (e.g. because of different fonts or colors), but it is desirable to spread the available space more globally across the different layout objects. If, for example, one layout object contains significantly more whitespace or Kashidas than the rest, this method can assign proportionally more space to this layout object.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getBaselineOffset(self) -> float:
        """
        This method yields the baseline offset.
        
        This method returns the baseline offset for this layout object, either measured from the top or the left edge, depending on the writing direction (horizontally or vertically). Since rendering this layout via XCanvas.drawTextLayout() outputs relative to the layout object's baseline, this method can be used to e.g. output relative to the left, top edge.
        """
        ...
    def getCaret(self, nInsertionIndex: int, bExcludeLigatures: bool) -> Caret_9b480ab5:
        """
        This method converts an insertion index to a caret.
        
        This method generates caret information for a given insertion point in the layout text.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def getFont(self) -> XCanvasFont_e3380d11:
        """
        Request the associated font for this layout.
        """
        ...
    def getMainTextDirection(self) -> int:
        """
        This method returns the main writing direction.
        
        This method returns the main writing direction of this layout, i.e. either LEFT_TO_RIGHT or RIGHT_TO_LEFT.
        """
        ...
    def getNextInsertionIndex(self, nStartIndex: int, nCaretAdvancement: int, bExcludeLigatures: bool) -> int:
        """
        This method calculates a new insertion index.
        
        This method calculates a new insertion index, given a start index and the number of characters to skip. This is most useful for caret traveling.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def getText(self) -> StringContext_d50e22:
        """
        Request the text this layout contains.
        """
        ...
    def getTextHit(self, aHitPoint: RealPoint2D_d6e70c78) -> TextHit_b25d0b90:
        """
        This method determines the hit position in the text.
        
        This method determines the index of the character hit at the specified position (in font coordinate space).
        """
        ...
    def justify(self, nSize: float) -> float:
        """
        Justify the text to the given size.
        
        This method is the core of the XTextLayout interface, because it layouts the text in a typographically correct way into the available space.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def queryInkMeasures(self) -> typing.Tuple[RealRectangle2D_d9b0e03, ...]:
        """
        Query the ink bounding boxes for every glyph in the layouted text.
        
        Ink, or tight bounding boxes in this case means that for e.g. an \"a\", the bounding box for the XPolyPolygon2D describing the glyph \"a\" is returned, not the logical dimensions of the character in the font.
        """
        ...
    def queryLogicalAdvancements(self) -> typing.Tuple[float, ...]:
        """
        Query the advancements for every character in the input string.
        
        This method returns a sequence of advancements, one for each character in the input string (not for every glyph. There might be multiple glyphs per input character, or multiple input characters per glyph).
        
        An advancement value is the distance of the glyph to the beginning edge, which is left for LTR text and is right for RTL text. The maximum of the advancements can be deemed as the width of the whole text layout.
        
        This method can be used to query for the layout's default advancements, which can subsequently be changed and applied to the layout via XTextLayout.applyLogicalAdvancements().
        """
        ...
    def queryLogicalHighlighting(self, nStartIndex: int, nEndIndex: int) -> XPolyPolygon2D_e1b0e20:
        """
        This method generates a highlight polygon.
        
        This method generates a highlighting polygon from two insertion indices. This polygon will not always be visually continuous, if e.g. the text direction changes in the middle of the selection, the might be parts visually between start and end position that are not selected.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def queryMeasures(self) -> typing.Tuple[RealRectangle2D_d9b0e03, ...]:
        """
        Query the logical bounding boxes of every character in the given text string.
        
        Logical bounding boxes means the space that the font allocates for the given character, which, e.g. for a \".\", might be significantly broader than the bounds returned via XTextLayout.queryInkMeasures().
        """
        ...
    def queryTextBounds(self) -> RealRectangle2D_d9b0e03:
        """
        Query the overall bounding box of the text.
        
        This method is similar to XTextLayout.queryTextMeasures(), only that the overall bounds are returned by this method.
        """
        ...
    def queryTextShapes(self) -> typing.Tuple[XPolyPolygon2D_e1b0e20, ...]:
        """
        Extract the polygonal shapes of the layouted text.
        
        Each glyph is represented by a separate XPolyPolygon2D in the returned sequence.
        """
        ...
    def queryVisualHighlighting(self, nStartIndex: int, nEndIndex: int) -> XPolyPolygon2D_e1b0e20:
        """
        This method generates a highlight polygon.
        
        This method generates a highlighting polygon from two insertion indices. This polygon will be visually continuous, i.e. will not have non-highlighted text in between.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...



