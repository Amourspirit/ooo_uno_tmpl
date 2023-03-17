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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.drawing
import typing
from .shape import Shape as Shape_85cc09e5
if typing.TYPE_CHECKING:
    from ..frame.x_model import XModel as XModel_7a6e095c

class OLE2Shape(Shape_85cc09e5):
    """
    Service Class

    This service is for an OLE shape.

    See Also:
        `API OLE2Shape <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1OLE2Shape.html>`_
    """
    @property
    def CLSID(self) -> str:
        """
        If you get this property you get the CLSID of the OLE2 document stream contained in this OLE2 shape.
        
        If you set it, an empty OLE2 document stream with this CLSID is created within this OLE2 shape.
        """
        ...
    @property
    def IsInternal(self) -> bool:
        """
        This property returns TRUE for all OLE2 that are internal Office components.
        """
        ...
    @property
    def Model(self) -> 'XModel_7a6e095c':
        """
        This is the model for the OLE2 inside this shape.
        
        This property returns an empty reference if the OLE2 is not an Office component.
        """
        ...
    @property
    def PersistName(self) -> str:
        """
        this is the internal storage name that keeps this OLE2 persist.
        """
        ...

