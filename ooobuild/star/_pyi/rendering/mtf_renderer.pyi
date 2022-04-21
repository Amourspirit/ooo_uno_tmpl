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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.rendering
import typing
from .x_mtf_renderer import XMtfRenderer as XMtfRenderer_f0d90d7c
if typing.TYPE_CHECKING:
    from .x_bitmap_canvas import XBitmapCanvas as XBitmapCanvas_fe5f0dd7

class MtfRenderer(XMtfRenderer_f0d90d7c):
    """
    Service Class


    See Also:
        `API MtfRenderer <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1rendering_1_1MtfRenderer.html>`_
    """
    def createWithBitmapCanvas(self, Canvas: 'XBitmapCanvas_fe5f0dd7') -> None:
        """
        """


