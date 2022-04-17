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
from abc import abstractmethod, ABC

class XSlidePreviewCacheListener(ABC):
    """
    Listener for asynchronous preview creations.
    
    Called when a slide preview has been created that was previously requested via a call to XSlidePreviewCache.getSlidePreview(). The implementor may then call getSlidePreview() a second time to get the up-to-date version of the preview.

    See Also:
        `API XSlidePreviewCacheListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XSlidePreviewCacheListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.XSlidePreviewCacheListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.drawing.XSlidePreviewCacheListener'

    @abstractmethod
    def notifyPreviewCreation(self, nSlideIndex: int) -> None:
        """
        Called by a XSlidePreviewCache object when a preview has been created for the slide with the given index.
        """

__all__ = ['XSlidePreviewCacheListener']
