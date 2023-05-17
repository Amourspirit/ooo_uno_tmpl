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
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .x_model import XModel as XModel_7a6e095c
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..container.x_enumeration import XEnumeration as XEnumeration_f2180daa
    from .x_controller2 import XController2 as XController2_bbcf0bc1
    from .x_frame import XFrame as XFrame_7a570956


class XModel2(XModel_7a6e095c):
    """
    extends interface XModel.
    
    The following functions are added:
    
    **since**
    
        LibreOffice 6.3

    See Also:
        `API XModel2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XModel2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.frame.XModel2']

    def createDefaultViewController(self, Frame: 'XFrame_7a570956') -> 'XController2_bbcf0bc1':
        """
        creates the default view instance for this model.
        
        Effectively, this method is equivalent to calling createView() with the ViewName being \"Default\".

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    def createViewController(self, ViewName: str, Arguments: 'typing.Tuple[PropertyValue_c9610c73, ...]', Frame: 'XFrame_7a570956') -> 'XController2_bbcf0bc1':
        """
        creates a new view instance classified by the specified name and arguments.
        
        The newly created controller must not be connected with the document and the frame. That is, you should neither call XFrame.setComponent(), nor XController.attachFrame(), nor XController.attachModel(), nor XModel.connectController(), not XModel.setCurrentController(). All of this is the responsibility of the caller, which will do it in the proper order.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    def getAvailableViewControllerNames(self) -> 'typing.Tuple[str, ...]':
        """
        provides the available names of the factory to be used to create views.
        
        The names are usually logical view names. The following names have a defined meaning, i.e. every concrete implementation which returns such a name must ensure it has the same meaning, and if a concrete implementation has a view with the given meaning, it must give it the name as defined here:
        
        Implementations of this interface might decide to support additional view names, which then are documented in the respective service descriptions.
        """
        ...
    def getControllers(self) -> 'XEnumeration_f2180daa':
        """
        provides list of all currently connected controller objects.
        
        Please note: Because this interface will might be used inside multi threaded environments those list can contain still disposed items or it new added controller will be missing (if they were added after this enumeration was created).
        """
        ...
    def setArgs(self, Arguments: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        Sets com.sun.star.document.MediaDescriptor properties of the current model during runtime.
        
        **since**
        
            LibreOffice 6.3

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.util.InvalidStateException: ``InvalidStateException``
        """
        ...


