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
# Libre Office Version: 7.4
# Namespace: com.sun.star.form.inspection
from ...inspection.x_property_handler import XPropertyHandler as XPropertyHandler_3e950fbf

class CellBindingPropertyHandler(XPropertyHandler_3e950fbf):
    """
    Service Class

    implements a property handler for use with a com.sun.star.inspection.ObjectInspector which is able to provide properties to bind a form component to a spreadsheet cell.
    
    The handler expects a value named \"ContextDocument\" in the context in which it is created. That is, the com.sun.star.uno.XComponentContext used for creating the CellBindingPropertyHandler is examined for a value with this name. If the object in this value denotes a spreadsheet document (indicated by supporting the com.sun.star.sheet.XSpreadsheetDocument interface), this document is used to create the com.sun.star.form.binding.ValueBindings to bind the inspected object to cells in this document.

    See Also:
        `API CellBindingPropertyHandler <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1inspection_1_1CellBindingPropertyHandler.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.inspection'
    __ooo_full_ns__: str = 'com.sun.star.form.inspection.CellBindingPropertyHandler'
    __ooo_type_name__: str = 'service'



__all__ = ['CellBindingPropertyHandler']

