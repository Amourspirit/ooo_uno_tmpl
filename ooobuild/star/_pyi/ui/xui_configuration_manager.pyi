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
# Namespace: com.sun.star.ui
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
    from ..container.x_index_container import XIndexContainer as XIndexContainer_1c040ebe
    from .x_accelerator_configuration import XAcceleratorConfiguration as XAcceleratorConfiguration_46580ffb

class XUIConfigurationManager(XInterface_8f010a43):
    """
    specifies a user interface configuration manager interface which controls the structure of all customizable user interface elements.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XUIConfigurationManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XUIConfigurationManager.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ui.XUIConfigurationManager']

    def createSettings(self) -> 'XIndexContainer_1c040ebe':
        """
        creates an empty settings data container.
        """
    def getEventsManager(self) -> 'XInterface_8f010a43':
        """
        retrieves the events manager from the user interface configuration manager.
        
        Every user interface configuration manager has one events manager instance which controls the mapping of events to script URLs of a module or document.
        """
    def getImageManager(self) -> 'XInterface_8f010a43':
        """
        retrieves the image manager from the user interface configuration manager.
        
        Every user interface configuration manager has one image manager instance which controls all images of a module or document.
        """
    def getSettings(self, ResourceURL: str, bWriteable: bool) -> 'XIndexAccess_f0910d6d':
        """
        retrieves the settings of a user interface element.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def getShortCutManager(self) -> 'XAcceleratorConfiguration_46580ffb':
        """
        retrieves the keyboard short cut manager from the user interface configuration manager.
        
        Every user interface configuration manager has one keyboard short cut manager instance which controls all short cuts of a module or document.
        """
    def getUIElementsInfo(self, ElementType: int) -> 'typing.Tuple[typing.Tuple[PropertyValue_c9610c73, ...], ...]':
        """
        retrieves information about all user interface elements within the user interface configuration manager.
        
        The following com.sun.star.beans.PropertyValue entries are defined inside the sequence for every user interface element.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def hasSettings(self, ResourceURL: str) -> bool:
        """
        determines if the settings of a user interface element is part the user interface configuration manager.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def insertSettings(self, NewResourceURL: str, aNewData: 'XIndexAccess_f0910d6d') -> None:
        """
        inserts the settings of a new user interface element.
        
        If the settings data is already present a com.sun.star.container.ElementExistException is thrown. If the NewResourceURL is not valid or describes an unknown type a com.sun.star.lang.IllegalArgumentException is thrown. If the configuration manager is read-only a com.sun.star.lang.IllegalAccessException is thrown.

        Raises:
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.IllegalAccessException: ``IllegalAccessException``
        """
    def removeSettings(self, ResourceURL: str) -> None:
        """
        removes the settings of an existing user interface element.
        
        If the settings data cannot be found a com.sun.star.container.NoSuchElementException is thrown. If the ResourceURL is not valid or describes an unknown type a com.sun.star.lang.IllegalArgumentException is thrown. If the configuration manager is read-only a com.sun.star.lang.IllegalAccessException is thrown.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.IllegalAccessException: ``IllegalAccessException``
        """
    def replaceSettings(self, ResourceURL: str, aNewData: 'XIndexAccess_f0910d6d') -> None:
        """
        replaces the settings of a user interface element with new settings.
        
        If the settings data cannot be found a com.sun.star.container.NoSuchElementException is thrown. If the ResourceURL is not valid or describes an unknown type a com.sun.star.lang.IllegalArgumentException is thrown. If the configuration manager is read-only a com.sun.star.lang.IllegalAccessException is thrown.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.IllegalAccessException: ``IllegalAccessException``
        """
    def reset(self) -> None:
        """
        resets the configuration manager to the default user interface configuration data.
        
        This means that all user interface configuration data of the instance will be removed. A module based user interface configuration manager removes user defined elements, but set all other elements back to default. It is not possible to remove default elements from a module user interface configuration manager.
        """

