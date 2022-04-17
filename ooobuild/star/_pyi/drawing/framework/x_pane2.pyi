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
# Namespace: com.sun.star.drawing.framework
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ...accessibility.x_accessible import XAccessible as XAccessible_1cbc0eb6

class XPane2(ABC):
    """
    An extension of the XPane interface that adds support for a) showing and hiding the windows that internally belong to the pane and b) setting the accessibility object.
    
    This is typically an optional interface.

    See Also:
        `API XPane2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1framework_1_1XPane2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.drawing.framework.XPane2']

    def getAccessible(self) -> 'XAccessible_1cbc0eb6':
        """
        Return the accessibility object that is currently associated with the windows that implement the pane.
        """
    def isVisible(self) -> bool:
        """
        Return whether all windows that are used to implement the pane are visible.
        """
    def setAccessible(self, xAccessible: 'XAccessible_1cbc0eb6') -> None:
        """
        Set the accessibility object for the pane.
        
        When there is more than one window used to implement the pane then the given accessibility object is usually set at the topmost window. However, the details are implementation dependent.
        """
    def setVisible(self, bIsVisible: bool) -> None:
        """
        Hide or show the pane.
        
        If there is more than one window used to implement the pane then it is left to the implementation if one, some, or all windows are hidden or shown as long as the pane becomes hidden or visible.
        """

