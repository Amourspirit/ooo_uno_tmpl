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
# Namespace: com.sun.star.form.control
from ...awt.uno_control_image_control import UnoControlImageControl as UnoControlImageControl_29c00f2b
from ..x_approve_action_broadcaster import XApproveActionBroadcaster as XApproveActionBroadcaster_693d10b9

class ImageButton(UnoControlImageControl_29c00f2b, XApproveActionBroadcaster_693d10b9):
    """
    Service Class

    describes a control which can be used for displaying images on a control acting like a button.
    
    The model of the control has to support the com.sun.star.form.component.ImageButton service.
    
    The control is clickable, the action taken upon clicking depends on the settings of the model the control belongs to.

    See Also:
        `API ImageButton <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1control_1_1ImageButton.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.control'
    __ooo_full_ns__: str = 'com.sun.star.form.control.ImageButton'
    __ooo_type_name__: str = 'service'



__all__ = ['ImageButton']

