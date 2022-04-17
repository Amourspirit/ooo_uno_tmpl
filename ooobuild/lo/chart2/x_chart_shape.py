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
# Namespace: com.sun.star.chart2
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.point import Point as Point_5fb2085e
    from ..awt.size import Size as Size_576707ef

class XChartShape(XInterface_8f010a43):
    """
    this interface is used for a wrapper of objects implementing the service com.sun.star.drawing.Shape

    See Also:
        `API XChartShape <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1XChartShape.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.XChartShape'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart2.XChartShape'

    @abstractmethod
    def getPosition(self) -> 'Point_5fb2085e':
        """
        the method corresponds to the identical methods of the interface com.sun.star.drawing.XShape
        """
    @abstractmethod
    def getPropertyValue(self, PropertyName: str) -> object:
        """
        the method corresponds to the identical methods of the interface com.sun.star.beans.XPropertySet

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
    @abstractmethod
    def getShapeType(self) -> str:
        """
        the method corresponds to the identical methods of the interface com.sun.star.drawing.XShape ??????????? deprecated
        """
    @abstractmethod
    def getSize(self) -> 'Size_576707ef':
        """
        the method corresponds to the identical methods of the interface com.sun.star.drawing.XShape
        """
    @abstractmethod
    def setPosition(self, aPosition: 'Point_5fb2085e') -> None:
        """
        the method corresponds to the identical methods of the interface com.sun.star.drawing.XShape
        """
    @abstractmethod
    def setPropertyValue(self, aPropertyName: str, aValue: object) -> None:
        """
        the method corresponds to the identical methods of the interface com.sun.star.beans.XPropertySet

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.beans.PropertyVetoException: ``PropertyVetoException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
    @abstractmethod
    def setSize(self, aSize: 'Size_576707ef') -> None:
        """
        the method corresponds to the identical methods of the interface com.sun.star.drawing.XShape

        Raises:
            com.sun.star.beans.PropertyVetoException: ``PropertyVetoException``
        """

__all__ = ['XChartShape']
