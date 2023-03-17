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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.ui.dialogs
from typing_extensions import Literal
"""
Const

denotes ways to leave a Wizard's page

**since**

    OOo 3.3

See Also:
    `API WizardTravelType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ui_1_1dialogs_1_1WizardTravelType.html>`_
"""
FORWARD: Literal[1]
"""
indicates the wizard page is left due to forward traveling through the wizard
"""
BACKWARD: Literal[2]
"""
indicates the wizard page is left due to backward traveling through the wizard
"""
FINISH: Literal[3]
"""
indicates the wizard page is left since the wizard is about to be finished
"""

