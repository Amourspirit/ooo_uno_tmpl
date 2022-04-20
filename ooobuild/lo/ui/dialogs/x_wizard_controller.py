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
# Namespace: com.sun.star.ui.dialogs
import typing
from abc import abstractmethod, ABC
if typing.TYPE_CHECKING:
    from ...awt.x_window import XWindow as XWindow_713b0924
    from .x_wizard_page import XWizardPage as XWizardPage_ed7c0d3d

class XWizardController(ABC):
    """
    is the interface of a client-provided controller of a custom Wizard.
    
    **since**
    
        OOo 3.3

    See Also:
        `API XWizardController <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1XWizardController.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ui.dialogs'
    __ooo_full_ns__: str = 'com.sun.star.ui.dialogs.XWizardController'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.ui.dialogs.XWizardController'

    @abstractmethod
    def canAdvance(self) -> bool:
        """
        """
    @abstractmethod
    def confirmFinish(self) -> bool:
        """
        called when the wizard is about to be finished.
        
        This method allows the controller to do any final checks, and ultimately veto finishing the wizard.
        """
    @abstractmethod
    def createPage(self, ParentWindow: 'XWindow_713b0924', PageId: int) -> 'XWizardPage_ed7c0d3d':
        """
        creates a page
        
        Wizard pages are created on demand, when the respective page is reached during traveling through the wizard. Effectively, this means the method is called at most once for each possible page ID.
        """
    @abstractmethod
    def getPageTitle(self, PageId: int) -> str:
        """
        provides the title of a page given by ID
        
        The page titles are displayed in the wizard's roadmap.
        """
    @abstractmethod
    def onActivatePage(self, PageId: int) -> None:
        """
        called when a new page in the wizard is being activated
        """
    @abstractmethod
    def onDeactivatePage(self, PageId: int) -> None:
        """
        called when a page in the wizard is being deactivated
        """

__all__ = ['XWizardController']

