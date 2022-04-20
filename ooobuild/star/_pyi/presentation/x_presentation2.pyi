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
# Namespace: com.sun.star.presentation
from typing_extensions import Literal
import typing
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_presentation import XPresentation as XPresentation_30890f78
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_slide_show_controller import XSlideShowController as XSlideShowController_a55c1232

class XPresentation2(XPropertySet_bc180bfa, XPresentation_30890f78):
    """
    enhances the XPresentation interface to give access to a XSlideShowController and to start a presentation with arguments.
    
    **since**
    
        OOo 3.0

    See Also:
        `API XPresentation2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1presentation_1_1XPresentation2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.presentation.XPresentation2']

    def getController(self) -> 'XSlideShowController_a55c1232':
        """
        if the slide show is running, this returns a controller object to control the running slide show.
        """
    def isRunning(self) -> bool:
        """
        returns true if the slide show is currently running
        """
    def startWithArguments(self, Arguments: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        start the slide show with the given arguments.
        
        All arguments override the values from Presentation.
        """

