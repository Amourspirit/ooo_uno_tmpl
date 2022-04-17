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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.ui.dialogs
import typing
from .x_wizard import XWizard as XWizard_bae60bc0
if typing.TYPE_CHECKING:
    from .x_wizard_controller import XWizardController as XWizardController_469d0fe4

class Wizard(XWizard_bae60bc0):
    """
    Service Class

    provides a framework for implementing a wizard dialog.
    
    **since**
    
        OOo 3.3

    See Also:
        `API Wizard <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1Wizard.html>`_
    """
    def createMultiplePathsWizard(self, PageIds: 'typing.Tuple[typing.Tuple[int, ...], ...]', Controller: 'XWizardController_469d0fe4') -> None:
        """
        creates a wizard with a multiple possible execution paths

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def createSinglePathWizard(self, PageIds: 'typing.Tuple[int, ...]', Controller: 'XWizardController_469d0fe4') -> None:
        """
        creates a wizard with a single execution path

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """


