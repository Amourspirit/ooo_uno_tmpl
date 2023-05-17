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

from .x_shape_descriptor import XShapeDescriptor as XShapeDescriptor_be80e5c
if typing.TYPE_CHECKING:
    from ..awt.point import Point as Point_5fb2085e
    from ..awt.size import Size as Size_576707ef


class XShape(XShapeDescriptor_be80e5c):
    """
    lets you do a basic transformation on a Shape and get its type.

    See Also:
        `API XShape <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XShape.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.drawing.XShape']

    def getPosition(self) -> 'Point_5fb2085e':
        """
        gets the current position of this object.
        """
        ...
    def getSize(self) -> 'Size_576707ef':
        """
        gets the size of this object.
        """
        ...
    def setPosition(self, aPosition: 'Point_5fb2085e') -> None:
        """
        sets the current position of this object
        """
        ...
    def setSize(self, aSize: 'Size_576707ef') -> None:
        """
        sets the size of this object.

        Raises:
            com.sun.star.beans.PropertyVetoException: ``PropertyVetoException``
        """
        ...


