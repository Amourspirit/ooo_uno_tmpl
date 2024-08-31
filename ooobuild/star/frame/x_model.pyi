# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing

from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_controller import XController as XController_b00e0b8f
    from ..uno.x_interface import XInterface as XInterface_8f010a43


class XModel(XComponent_98dc0ab5):
    """
    represents a component which is created from a URL and arguments.
    
    It is a representation of a resource in the sense that it was created/loaded from the resource. The arguments are passed to the loader to modify its behavior. An example for such an argument is \"AsTemplate\", which loads the resource as a template for a new document. (see com.sun.star.document.MediaDescriptor for further details)
    
    Models can be controlled by controller components, which are usually views of the model. (see Controller for further details)
    
    If there is at least one controller, there is by definition a current controller. And if that controller supports the interface com.sun.star.view.XSelectionSupplier, it has a current selection too.

    See Also:
        `API XModel <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XModel.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.frame.XModel'

    def attachResource(self, URL: str, Arguments: typing.Tuple[PropertyValue_c9610c73, ...]) -> bool:
        """
        informs a model about its resource description.
        """
        ...
    def connectController(self, Controller: XController_b00e0b8f) -> None:
        """
        is called whenever a new controller is created for this model.
        
        The com.sun.star.lang.XComponent interface of the controller must be used to recognize when it is deleted.
        """
        ...
    def disconnectController(self, Controller: XController_b00e0b8f) -> None:
        """
        is called whenever an existing controller should be deregistered at this model.
        
        The com.sun.star.lang.XComponent interface of the controller must be used to recognize when it is deleted.
        """
        ...
    def getArgs(self) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        """
        provides read access on currently representation of the com.sun.star.document.MediaDescriptor of this model which describes the model and its state
        """
        ...
    def getCurrentController(self) -> XController_b00e0b8f:
        """
        provides access to the controller which currently controls this model
        """
        ...
    def getCurrentSelection(self) -> XInterface_8f010a43:
        """
        provides read access on current selection on controller
        """
        ...
    def getURL(self) -> str:
        """
        provides information about the location of this model
        """
        ...
    def hasControllersLocked(self) -> bool:
        """
        determines if there is at least one lock remaining.
        
        While there is at least one lock remaining, some notifications for display updates are not broadcasted to the controllers.
        """
        ...
    def lockControllers(self) -> None:
        """
        suspends some notifications to the controllers which are used for display updates.
        
        The calls to XModel.lockControllers() and XModel.unlockControllers() may be nested and even overlapping, but they must be in pairs. While there is at least one lock remaining, some notifications for display updates are not broadcasted.
        """
        ...
    def setCurrentController(self, Controller: XController_b00e0b8f) -> None:
        """
        sets a registered controller as the current controller.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    def unlockControllers(self) -> None:
        """
        resumes the notifications which were suspended by XModel.lockControllers().
        
        The calls to XModel.lockControllers() and XModel.unlockControllers() may be nested and even overlapping, but they must be in pairs. While there is at least one lock remaining, some notifications for display updates are not broadcasted.
        """
        ...


