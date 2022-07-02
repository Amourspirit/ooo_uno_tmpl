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
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XEnhancedCustomShapeDefaulter(XInterface_8f010a43):
    """

    See Also:
        `API XEnhancedCustomShapeDefaulter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XEnhancedCustomShapeDefaulter.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.drawing.XEnhancedCustomShapeDefaulter']

    def createCustomShapeDefaults(self, aShapeType: str) -> None:
        """
        This interface allows to create shape properties for the given \"ShapeType\".
        
        The \"ShapeType\" string can be empty then the current \"ShapeType\" of the shape is used.
        
        SJ: following shape types can't be created with this method, they are part of the gallery (soon they also will be added) gallery: quadrat gallery: round-quadrat gallery: circle gallery: circle-pie gallery: frame gallery: flower gallery: cloud gallery: puzzle gallery: octagon-bevel gallery: diamond-bevel gallery: up-right-arrow gallery: up-right-down-arrow gallery: corner-right-arrow gallery: split-arrow gallery: up-right-arrow-callout gallery: split-round-arrow gallery: s-sharped-arrow Gallery: star6 Gallery: star12 Gallery: concave-star6 Gallery: signet Gallery: doorplate gallery: fontwork-arch-left-curve gallery: fontwork-arch-right-curve gallery: fontwork-arch-left-pour gallery: fontwork-arch-right-pour
        """
        ...


