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
# Namespace: com.sun.star.graphic
from __future__ import annotations
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from .x_graphic import XGraphic as XGraphic_a4da0afc

class XGraphicMapper(ABC):
    """
    This interface allows mapping of XGraphics for a certain string key.
    
    **since**
    
        LibreOffice 7.1

    See Also:
        `API XGraphicMapper <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1graphic_1_1XGraphicMapper.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.graphic'
    __ooo_full_ns__: str = 'com.sun.star.graphic.XGraphicMapper'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.graphic.XGraphicMapper'

    @abstractmethod
    def findGraphic(self, Id: str) -> XGraphic_a4da0afc:
        """
        Find if we have the XGraphic for the certain key.
        """
        ...
    @abstractmethod
    def putGraphic(self, Id: str, Graphic: XGraphic_a4da0afc) -> None:
        """
        Insert a new entry to map an id/key to the XGraphic.
        """
        ...

__all__ = ['XGraphicMapper']


