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
# Namespace: com.sun.star.rendering
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_canvas import XCanvas as XCanvas_b19b0b7a
if typing.TYPE_CHECKING:
    from ..geometry.real_rectangle2_d import RealRectangle2D as RealRectangle2D_d9b0e03
    from .render_state import RenderState as RenderState_e4490d27
    from .view_state import ViewState as ViewState_cab30c62

class XBitmapCanvas(XCanvas_b19b0b7a):
    """
    This is a specialization of the canvas interface for bitmapped canvases.
    
    This interface is a specialization of the canvas interface for bitmapped canvases, where additional methods for accessing and moving of bitmap content are provided.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XBitmapCanvas <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XBitmapCanvas.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.rendering'
    __ooo_full_ns__: str = 'com.sun.star.rendering.XBitmapCanvas'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.rendering.XBitmapCanvas'

    @abstractmethod
    def copyRect(self, sourceCanvas: XBitmapCanvas, sourceRect: RealRectangle2D_d9b0e03, sourceViewState: ViewState_cab30c62, sourceRenderState: RenderState_e4490d27, destRect: RealRectangle2D_d9b0e03, destViewState: ViewState_cab30c62, destRenderState: RenderState_e4490d27) -> None:
        """
        This method copies a rectangular area from a place of one canvas to a place on another.
        
        This method copies a rectangular area from a place of one canvas to a place on another. Source and destination areas are permitted to overlap. If the source view or render state has a clipping set, the regions clipped away from the source rectangle are regarded fully transparent for the copy operation. The device color for both source and destination render state is ignored, the compositing mode only for the source render state.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            VolatileContentDestroyedException: ``VolatileContentDestroyedException``
        """
        ...

__all__ = ['XBitmapCanvas']

