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
from __future__ import annotations
import typing
from abc import abstractmethod
from .x_shape import XShape as XShape_8fd00a3d
if typing.TYPE_CHECKING:
    from ..awt.x_control_model import XControlModel as XControlModel_affc0b7e

class XControlShape(XShape_8fd00a3d):
    """
    is implemented by a ControlShape to access the controls model.

    See Also:
        `API XControlShape <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XControlShape.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.XControlShape'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.drawing.XControlShape'

    @abstractmethod
    def getControl(self) -> XControlModel_affc0b7e:
        """
        returns the control model of this Shape.
        """
        ...
    @abstractmethod
    def setControl(self, xControl: XControlModel_affc0b7e) -> None:
        """
        sets the control model for this Shape.
        """
        ...

__all__ = ['XControlShape']

