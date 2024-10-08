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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.drawing
from __future__ import annotations
import typing

from abc import ABC
if typing.TYPE_CHECKING:
    from ..awt.rectangle import Rectangle as Rectangle_84b109e9
    from ..awt.x_window import XWindow as XWindow_713b0924
    from ..rendering.x_bitmap import XBitmap as XBitmap_b1b70b7b
    from ..rendering.x_canvas import XCanvas as XCanvas_b19b0b7a
    from ..rendering.x_sprite_canvas import XSpriteCanvas as XSpriteCanvas_ff8b0df1


class XPresenterHelper(ABC):
    """
    This interface is a collection of functions that were necessary to implement larger parts of the presenter screen as extension.
    
    The methods of this interface give access to services that could only be implemented in the Office core, not in an extension.
    
    As the presenter screen is no extension any more, this hack can go again; it just needs clean-up.

    See Also:
        `API XPresenterHelper <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XPresenterHelper.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.drawing.XPresenterHelper'

    def captureMouse(self, xWindow: XWindow_713b0924) -> None:
        """
        Capture the mouse so that no other window will receive mouse events.
        
        Note that this is a potentially dangerous method. Not calling releaseMouse eventually can lead to an unresponsive application.
        """
        ...
    def createCanvas(self, xWindow: XWindow_713b0924, nRequestedCanvasFeatureList: int, sOptionalCanvasServiceName: str) -> XCanvas_b19b0b7a:
        """
        Create a new canvas for the given window.
        """
        ...
    def createSharedCanvas(self, xUpdateCanvas: XSpriteCanvas_ff8b0df1, xUpdateWindow: XWindow_713b0924, xSharedCanvas: XCanvas_b19b0b7a, xSharedWindow: XWindow_713b0924, xWindow: XWindow_713b0924) -> XCanvas_b19b0b7a:
        """
        Create a new canvas for the given window.
        
        The new canvas is a wrapper around the given shared canvas. The wrapper only modifies the origin in all output and clipping methods.
        """
        ...
    def createWindow(self, xParentWindow: XWindow_713b0924, bCreateSystemChildWindow: bool, bInitiallyVisible: bool, bEnableChildTransparentMode: bool, bEnableParentClip: bool) -> XWindow_713b0924:
        """
        Create a new window as child window of the given parent window.
        """
        ...
    def getWindowExtentsRelative(self, xChildWindow: XWindow_713b0924, xParentWindow: XWindow_713b0924) -> Rectangle_84b109e9:
        """
        Return the bounding box of the given child window relative to the direct or indirect parent window.
        """
        ...
    def loadBitmap(self, id: str, xCanvas: XCanvas_b19b0b7a) -> XBitmap_b1b70b7b:
        """
        Load a bitmap with a given ID.
        """
        ...
    def releaseMouse(self, xWindow: XWindow_713b0924) -> None:
        """
        Release a previously captured mouse.
        """
        ...
    def toTop(self, xWindow: XWindow_713b0924) -> None:
        """
        Move the specified window to the top of its stacking order.
        
        As a result the window will be painted over all its overlapping siblings.
        """
        ...


