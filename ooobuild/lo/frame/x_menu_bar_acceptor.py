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
# Namespace: com.sun.star.frame
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XMenuBarAcceptor(XInterface_8f010a43):
    """
    provides function to update a menu bar for inplace editing.
    
    **since**
    
        OOo 2.0
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XMenuBarAcceptor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XMenuBarAcceptor.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.frame'
    __ooo_full_ns__: str = 'com.sun.star.frame.XMenuBarAcceptor'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.frame.XMenuBarAcceptor'

    @abstractmethod
    def updateMenuBar(self, xMenuBar: object) -> None:
        """
        update menu bar according to the current frame mode.
        
        This is used in inplace editing mode where we have to merge our own menu into the container applications menu.
        """
        ...

__all__ = ['XMenuBarAcceptor']

