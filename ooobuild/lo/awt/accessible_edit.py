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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt
from __future__ import annotations
from ..accessibility.x_accessible_context import XAccessibleContext as XAccessibleContext_8eae119b
from ..accessibility.x_accessible_editable_text import XAccessibleEditableText as XAccessibleEditableText_eb141375
from ..accessibility.x_accessible_event_broadcaster import XAccessibleEventBroadcaster as XAccessibleEventBroadcaster_3d811522
from ..accessibility.x_accessible_extended_component import XAccessibleExtendedComponent as XAccessibleExtendedComponent_539d159a

class AccessibleEdit(XAccessibleContext_8eae119b, XAccessibleEditableText_eb141375, XAccessibleEventBroadcaster_3d811522, XAccessibleExtendedComponent_539d159a):
    """
    Service Class

    specifies accessibility support for an edit.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API AccessibleEdit <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1AccessibleEdit.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.AccessibleEdit'
    __ooo_type_name__: str = 'service'


__all__ = ['AccessibleEdit']

