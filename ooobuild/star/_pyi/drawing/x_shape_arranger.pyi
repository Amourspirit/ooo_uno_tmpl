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
# Namespace: com.sun.star.drawing
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .arrangement import Arrangement as Arrangement_c9be0c68
    from .x_shape import XShape as XShape_8fd00a3d
    from .x_shapes import XShapes as XShapes_9a800ab0


class XShapeArranger(XInterface_8f010a43):
    """
    Objects implementing this interface can be used to arrange Shapes.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XShapeArranger <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XShapeArranger.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.drawing.XShapeArranger']

    def arrange(self, xShapes: 'XShapes_9a800ab0', eType: 'Arrangement_c9be0c68') -> None:
        """
        applies the specified Arrangement to the specified collection of Shapes.
        """
        ...
    def bringToFront(self, xShapes: 'XShapes_9a800ab0', nSteps: int) -> None:
        """
        moves the specified Shapes by a specified number of objects more to the front.
        """
        ...
    def reverseOrder(self, xShapes: 'XShapes_9a800ab0') -> None:
        """
        reverses the order of the specified collection of Shapes.
        """
        ...
    def sendToBack(self, xShapes: 'XShapes_9a800ab0', nSteps: int) -> None:
        """
        moves the specified Shapes nSteps objects more to the back.
        """
        ...
    def setBehindShape(self, xShapes: 'XShapes_9a800ab0', xShape: 'XShape_8fd00a3d') -> None:
        """
        moves the specified collection of Shapes behind the specified single Shape.
        """
        ...
    def setInFrontOf(self, xShapes: 'XShapes_9a800ab0', xShape: 'XShape_8fd00a3d') -> None:
        """
        moves the specified collection of Shapes in front of the specified single Shape.
        """
        ...


