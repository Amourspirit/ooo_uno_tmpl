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
# Libre Office Version: 7.2
# Namespace: com.sun.star.awt
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .point import Point as Point_5fb2085e
    from .size import Size as Size_576707ef

class XUnitConversion(XInterface_8f010a43):
    """
    allows converting between different measurement units
    
    **since**
    
        OOo 3.0

    See Also:
        `API XUnitConversion <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XUnitConversion.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XUnitConversion'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XUnitConversion'

    @abstractmethod
    def convertPointToLogic(self, Point: 'Point_5fb2085e', TargetUnit: int) -> 'Point_5fb2085e':
        """
        converts the given Point, which is specified in pixels, into the given logical unit

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def convertPointToPixel(self, Point: 'Point_5fb2085e', SourceUnit: int) -> 'Point_5fb2085e':
        """
        converts the given Point, which is specified in the given logical unit, into pixels

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def convertSizeToLogic(self, Size: 'Size_576707ef', TargetUnit: int) -> 'Size_576707ef':
        """
        converts the given Size, which is specified in pixels, into the given logical unit

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    @abstractmethod
    def convertSizeToPixel(self, Size: 'Size_576707ef', SourceUnit: int) -> 'Size_576707ef':
        """
        converts the given Size, which is specified in the given logical unit, into pixels

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

__all__ = ['XUnitConversion']

