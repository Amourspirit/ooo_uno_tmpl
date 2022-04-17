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
# Libre Office Version: 7.3
# Namespace: com.sun.star.drawing
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
    from .x_slide_preview_cache_listener import XSlidePreviewCacheListener as XSlidePreviewCacheListener_af761239
    from ..geometry.integer_size2_d import IntegerSize2D as IntegerSize2D_f2690d53
    from ..rendering.x_bitmap import XBitmap as XBitmap_b1b70b7b
    from ..rendering.x_canvas import XCanvas as XCanvas_b19b0b7a
    from ..uno.x_interface import XInterface as XInterface_8f010a43

class XSlidePreviewCache(ABC):
    """
    A cache of preview bitmaps for the slides of one Impress or Draw document in one size.
    
    There may be more than one cache for one document. These are internally connected and for missing previews one cache may take it from another cache and scale it to the desired size. When a preview is not present then it is created asynchronously. On creation all registered listeners are notified.
    
    Slides are referenced via their index in an XIndexAccess container in order to allow multiple references to a single slide (custom presentations).

    See Also:
        `API XSlidePreviewCache <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XSlidePreviewCache.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.XSlidePreviewCache'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.drawing.XSlidePreviewCache'

    @abstractmethod
    def addPreviewCreationNotifyListener(self, xListener: 'XSlidePreviewCacheListener_af761239') -> None:
        """
        Register a listener that is called when a preview has been created asynchronously.
        """
    @abstractmethod
    def getSlidePreview(self, nSlideIndex: int, xCanvas: 'XCanvas_b19b0b7a') -> 'XBitmap_b1b70b7b':
        """
        Return a preview for the given slide index.
        
        The returned bitmap may be the requested preview, a preview of the preview, i.e. a scaled up or down version, or an empty reference when the preview is not yet present.
        
        This call may lead to the asynchronous creation of the requested preview. In that case all registered listeners are notified when the preview has been created.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    @abstractmethod
    def pause(self) -> None:
        """
        Stop the asynchronous creation of previews temporarily.
        
        Call resume() to restart it.
        """
    @abstractmethod
    def removePreviewCreationNotifyListener(self, xListener: 'XSlidePreviewCacheListener_af761239') -> None:
        """
        Remove a previously registered listener for preview creations.
        """
    @abstractmethod
    def resume(self) -> None:
        """
        Resume the asynchronous creation of slide previews.
        """
    @abstractmethod
    def setDocumentSlides(self, xSlides: 'XIndexAccess_f0910d6d', xDocument: 'XInterface_8f010a43') -> None:
        """
        Set the set of slides for which the cache will provide the previews.
        
        All slides in the given XIndexAccess are required to come from the given model.
        """
    @abstractmethod
    def setPreviewSize(self, aSize: 'IntegerSize2D_f2690d53') -> None:
        """
        Define the size of the previews that are managed by the called cache.
        """
    @abstractmethod
    def setVisibleRange(self, nFirstVisibleSlideIndex: int, nLastVisibleSlideIndex: int) -> None:
        """
        Define which slides are currently visible on the screen and which are not.
        
        This information is used for give preview creation for visible slides a higher priority than for those slides that are not visible.
        """

__all__ = ['XSlidePreviewCache']

