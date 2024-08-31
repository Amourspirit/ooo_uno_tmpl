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
# Namespace: com.sun.star.embed
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.size import Size as Size_576707ef
    from .visual_representation import VisualRepresentation as VisualRepresentation_2a2b0f4c

class XVisualObject(XInterface_8f010a43):
    """
    represents common visualization functionality for embedded objects.

    See Also:
        `API XVisualObject <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XVisualObject.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.embed'
    __ooo_full_ns__: str = 'com.sun.star.embed.XVisualObject'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.embed.XVisualObject'

    @abstractmethod
    def getMapUnit(self, nAspect: int) -> int:
        """
        retrieves map mode the object communicates in.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def getPreferredVisualRepresentation(self, nAspect: int) -> VisualRepresentation_2a2b0f4c:
        """
        retrieves visual representation of the object in preferable format.
        
        If the object persistence entry contains cached visual representation then it can be retrieved by using this method even in loaded state.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.embed.WrongStateException: ``WrongStateException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def getVisualAreaSize(self, nAspect: int) -> Size_576707ef:
        """
        gets the size of object's visual area.
        
        The size must be provided in logical units according to map mode the object communicates in.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.embed.WrongStateException: ``WrongStateException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    @abstractmethod
    def setVisualAreaSize(self, nAspect: int, aSize: Size_576707ef) -> None:
        """
        sets the size of object's visual area.
        
        The size must be provided in logical units according to map mode the object communicates in.
        
        If an object is inplace- or ui-active the method must not initiate repainting itself.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.embed.WrongStateException: ``WrongStateException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...

__all__ = ['XVisualObject']

