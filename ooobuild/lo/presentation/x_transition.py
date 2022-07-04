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
# Namespace: com.sun.star.presentation
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_slide_show_view import XSlideShowView as XSlideShowView_3eb40fa9
    from ..rendering.x_bitmap import XBitmap as XBitmap_b1b70b7b

class XTransition(XInterface_8f010a43):
    """
    Transition interface to render custom transitions over time.
    
    **since**
    
        OOo 2.4

    See Also:
        `API XTransition <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1presentation_1_1XTransition.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.presentation'
    __ooo_full_ns__: str = 'com.sun.star.presentation.XTransition'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.presentation.XTransition'

    @abstractmethod
    def update(self, t: float) -> None:
        """
        Update transition on screen to given time state.
        """
        ...
    @abstractmethod
    def viewChanged(self, view: 'XSlideShowView_3eb40fa9', leavingBitmap: 'XBitmap_b1b70b7b', enteringBitmap: 'XBitmap_b1b70b7b') -> None:
        """
        """
        ...

__all__ = ['XTransition']

