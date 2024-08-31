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
# Namespace: com.sun.star.awt
from __future__ import annotations
import typing

import uno
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_image_producer import XImageProducer as XImageProducer_ba930bd3


class XImageConsumer(XInterface_8f010a43):
    """
    specifies a data sink for an image.
    
    An image consumer is a component which wants to display or just receive an image from an image producer.

    See Also:
        `API XImageConsumer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XImageConsumer.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.awt.XImageConsumer'

    def complete(self, Status: int, xProducer: XImageProducer_ba930bd3) -> None:
        """
        is called for the notification of the degree to which the image is delivered.
        
        The complete method is called when the image producer has finished delivering all of the pixels that the source image contains, or when a single frame of a multi-frame animation has been completed, or when an error in loading or producing the image has occurred. The image consumer should remove itself from the list of consumers registered with the image producer at this time, unless it is interested in successive frames.
        """
        ...
    def init(self, Width: int, Height: int) -> None:
        """
        initializes the consumer with image dimensions.
        """
        ...
    def setColorModel(self, BitCount: int, RGBAPal: uno.ByteSequence, RedMask: int, GreenMask: int, BlueMask: int, AlphaMask: int) -> None:
        """
        changes color model for next pixels typically called once after initialization.
        """
        ...
    def setPixelsByBytes(self, nX: int, nY: int, nWidth: int, nHeight: int, aProducerData: uno.ByteSequence, nOffset: int, nScanSize: int) -> None:
        """
        delivers a chunk of pixels as long values.
        
        The pixels of the image are delivered using one or more calls to this method. Each call specifies the location and size of the rectangle of source pixels that are contained in the array of pixels. The specified color model object should be used to convert the pixels into their corresponding color and alpha components. Pixel (m,n) is stored in the pixels array at index (n * nScanSize
        """
        ...
    def setPixelsByLongs(self, nX: int, nY: int, nWidth: int, nHeight: int, aProducerData: uno.ByteSequence, nOffset: int, nScanSize: int) -> None:
        """
        delivers a chunk of pixels as byte values.
        
        The pixels of the image are delivered using one or more calls to this method. Each call specifies the location and size of the rectangle of source pixels that are contained in the array of pixels. The specified color model object should be used to convert the pixels into their corresponding color and alpha components. Pixel (m,n) is stored in the pixels array at index (n * nScanSize
        """
        ...


