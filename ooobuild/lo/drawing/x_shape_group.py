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
# Namespace: com.sun.star.drawing
from abc import abstractmethod
from .x_shape import XShape as XShape_8fd00a3d

class XShapeGroup(XShape_8fd00a3d):
    """
    is implemented by Shapes that contain other Shapes.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XShapeGroup <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XShapeGroup.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.XShapeGroup'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.drawing.XShapeGroup'

    @abstractmethod
    def enterGroup(self) -> None:
        """
        enters the group which enables the editing function for the parts of a grouped Shape.
        
        Then the parts can be edited instead of the group as a whole.
        
        This affects only the user interface. The behavior is not specified if this instance is not visible on any view. In this case it may or may not work.
        """
    @abstractmethod
    def leaveGroup(self) -> None:
        """
        leaves the group, which disables the editing function for the parts of a grouped Shape.
        
        Then only the group as a whole can be edited.
        
        This affects only the user interface. The behavior is not specified if this instance is not visible on any view. In this case it may or may not work.
        """

__all__ = ['XShapeGroup']

