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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.form.component
from __future__ import annotations
from abc import abstractproperty
from ..x_reset import XReset as XReset_71670917
from .rich_text_control import RichTextControl as RichTextControl_6b7310c9

class TextField(RichTextControl_6b7310c9, XReset_71670917):
    """
    Service Class

    specifies a component which allows the input of text, either single- or multi-line.

    See Also:
        `API TextField <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1TextField.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.component'
    __ooo_full_ns__: str = 'com.sun.star.form.component.TextField'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def DefaultText(self) -> str:
        """
        contains a default value for the control.
        
        This value is used when the control is initially displayed, and for resetting it.
        """
        ...


__all__ = ['TextField']

