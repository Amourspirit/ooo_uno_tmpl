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
# Namespace: com.sun.star.graphic
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..geometry.real_rectangle3_d import RealRectangle3D as RealRectangle3D_d9d0e04

class XPrimitive3D(XInterface_8f010a43):
    """
    XPrimitive3D interface.
    
    This is the basic interface for graphic 3D primitives. They need to be able

    See Also:
        `API XPrimitive3D <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1graphic_1_1XPrimitive3D.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.graphic.XPrimitive3D']

    def getDecomposition(self, aViewParameters: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> 'typing.Tuple[XPrimitive3D, ...]':
        """
        Retrieve decomposed list of simpler primitives.
        
        double Time
        
        Defines the point in time for which the geometry is defined. This may lead to varied results for animated objects. This value is defined in the range [0.0 .. n[, negative values are not allowed. If not given, a value of 0.0 is implied.
        """
    def getRange(self, aViewParameters: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> 'RealRectangle3D_d9d0e04':
        """
        Retrieve bound rect of primitive.
        
        This method calculates the actual bound rect of the area in world coordinates. Note that for view-dependent primitives, the necessary pixel adjustments are taken into account. For that reason the ViewParameters need to be given.
        """

