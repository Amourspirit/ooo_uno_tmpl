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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.awt
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing
from .rectangle import Rectangle as Rectangle_84b109e9
from .window_class import WindowClass as WindowClass_99f60ac2
from .x_window_peer import XWindowPeer as XWindowPeer_99760ab0


class WindowDescriptor(object):
    """
    Struct Class

    describes a window.

    See Also:
        `API WindowDescriptor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1WindowDescriptor.html>`_
    """
    typeName: Literal['com.sun.star.awt.WindowDescriptor']

    def __init__(self, Type: typing.Optional[WindowClass_99f60ac2] = ..., WindowServiceName: typing.Optional[str] = ..., Parent: typing.Optional[XWindowPeer_99760ab0] = ..., ParentIndex: typing.Optional[int] = ..., Bounds: typing.Optional[Rectangle_84b109e9] = ..., WindowAttributes: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Type (WindowClass, optional): Type value.
            WindowServiceName (str, optional): WindowServiceName value.
            Parent (XWindowPeer, optional): Parent value.
            ParentIndex (int, optional): ParentIndex value.
            Bounds (Rectangle, optional): Bounds value.
            WindowAttributes (int, optional): WindowAttributes value.
        """


    @property
    def Type(self) -> WindowClass_99f60ac2:
        """
        specifies the type of window.
        """


    @property
    def WindowServiceName(self) -> str:
        """
        specifies the name of the component service.
        
        A zero length name means that the VCL creates a blank top, a container, or a simple window. The following service names are defined:
        """


    @property
    def Parent(self) -> XWindowPeer_99760ab0:
        """
        specifies the parent of the component.
        
        If Parent == 0 && ParentIndex == -1, then the window is on the desktop.
        """


    @property
    def ParentIndex(self) -> int:
        """
        specifies the index of the parent window, if available.
        
        If Parent == 0 and this struct is a member of an array, then this is the offset from the beginning of the array to the parent. A value of -1 means desktop.
        """


    @property
    def Bounds(self) -> Rectangle_84b109e9:
        """
        specifies the position and size of the window.
        
        This member is ignored if the window attribute is com.sun.star.awt.WindowAttribute.FULLSIZE.
        """


    @property
    def WindowAttributes(self) -> int:
        """
        specifies the window attributes.
        
        Use one value out of the constant group com.sun.star.awt.WindowAttribute.
        """


