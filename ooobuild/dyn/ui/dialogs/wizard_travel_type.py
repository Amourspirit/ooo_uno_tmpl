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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.ui.dialogs
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class WizardTravelType(metaclass=UnoConstMeta, type_name="com.sun.star.ui.dialogs.WizardTravelType", name_space="com.sun.star.ui.dialogs"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.ui.dialogs.WizardTravelType``"""
        pass

    class WizardTravelTypeEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.ui.dialogs.WizardTravelType", name_space="com.sun.star.ui.dialogs"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.ui.dialogs.WizardTravelType`` as Enum values"""
        pass

else:
    from ....lo.ui.dialogs.wizard_travel_type import WizardTravelType as WizardTravelType

    class WizardTravelTypeEnum(IntEnum):
        """
        Enum of Const Class WizardTravelType

        denotes ways to leave a Wizard's page
        
        **since**
        
            OOo 3.3
        """
        FORWARD = WizardTravelType.FORWARD
        """
        indicates the wizard page is left due to forward traveling through the wizard
        """
        BACKWARD = WizardTravelType.BACKWARD
        """
        indicates the wizard page is left due to backward traveling through the wizard
        """
        FINISH = WizardTravelType.FINISH
        """
        indicates the wizard page is left since the wizard is about to be finished
        """

__all__ = ['WizardTravelType', 'WizardTravelTypeEnum']
