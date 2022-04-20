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
# Libre Office Version: 7.2
# Namespace: com.sun.star.drawing
from .generic_draw_page import GenericDrawPage as GenericDrawPage_fd960dbc
from .x_master_page_target import XMasterPageTarget as XMasterPageTarget_1a670e9c
from ..form.x_forms_supplier import XFormsSupplier as XFormsSupplier_c8f90c6f

class DrawPage(GenericDrawPage_fd960dbc, XMasterPageTarget_1a670e9c, XFormsSupplier_c8f90c6f):
    """
    Service Class

    This service specifies a page for the actual draw pages to contain the drawings.

    See Also:
        `API DrawPage <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1DrawPage.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.drawing'
    __ooo_full_ns__: str = 'com.sun.star.drawing.DrawPage'
    __ooo_type_name__: str = 'service'



__all__ = ['DrawPage']

