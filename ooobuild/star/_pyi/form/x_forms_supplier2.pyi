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
# Namespace: com.sun.star.form
from typing_extensions import Literal
from .x_forms_supplier import XFormsSupplier as XFormsSupplier_c8f90c6f

class XFormsSupplier2(XFormsSupplier_c8f90c6f):
    """
    extends the XFormsSupplier with convenience methods

    See Also:
        `API XFormsSupplier2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XFormsSupplier2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.form.XFormsSupplier2']

    def hasForms(self) -> bool:
        """
        determines whether there are currently forms available at all
        
        If you need read access to the forms collection, then you might check the existence of forms using hasForms(), and if it returns FALSE, you can do as if XFormsSupplier.getForms() would have returned an empty container.
        
        Semantically, hasForms() is equivalent to calling XElementAccess.hasElements() on the container returned by XFormsSupplier.getForms(). But when using the latter, the implementation is forced to create an empty container, which might be potentially expensive.
        """

