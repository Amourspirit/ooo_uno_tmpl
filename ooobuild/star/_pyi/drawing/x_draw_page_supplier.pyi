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
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_draw_page import XDrawPage as XDrawPage_b07a0b57

class XDrawPageSupplier(XInterface_8f010a43):
    """
    represents something that provides a DrawPage.
    
    This interface is provided if the container only supports exactly one DrawPage. For containers which support multiple DrawPages interface XDrawPagesSupplier is supported.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XDrawPageSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XDrawPageSupplier.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.drawing.XDrawPageSupplier']

    def getDrawPage(self) -> 'XDrawPage_b07a0b57':
        """
        returns the DrawPage.
        """

