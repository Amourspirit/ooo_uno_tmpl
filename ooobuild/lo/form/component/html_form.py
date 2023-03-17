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
# Namespace: com.sun.star.form.component
import typing
from abc import abstractproperty
from ..x_reset import XReset as XReset_71670917
from ..x_submit import XSubmit as XSubmit_7b060988
from .form import Form as Form_ca1d0c51
if typing.TYPE_CHECKING:
    from ..form_submit_encoding import FormSubmitEncoding as FormSubmitEncoding_fdd50deb
    from ..form_submit_method import FormSubmitMethod as FormSubmitMethod_e2a90d25

class HTMLForm(Form_ca1d0c51, XReset_71670917, XSubmit_7b060988):
    """
    Service Class

    This service specifies the special kind of Forms for HTML documents.
    
    An HTMLForm fulfills the specification of forms in HTML. It supplies the possibility of submitting or resetting the contents of a form. For more information on HTML forms, please see the documentation of HTML.

    See Also:
        `API HTMLForm <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1form_1_1component_1_1HTMLForm.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form.component'
    __ooo_full_ns__: str = 'com.sun.star.form.component.HTMLForm'
    __ooo_type_name__: str = 'service'

    @abstractproperty
    def SubmitEncoding(self) -> 'FormSubmitEncoding_fdd50deb':
        """
        specifies the kind of encoding for submission.
        """
        ...

    @abstractproperty
    def SubmitMethod(self) -> 'FormSubmitMethod_e2a90d25':
        """
        specifies the kind of submission.
        """
        ...

    @abstractproperty
    def TargetFrame(self) -> str:
        """
        describes the frame, where to open the document specified by the TargetURL.
        """
        ...

    @abstractproperty
    def TargetURL(self) -> str:
        """
        specifies the URL, which should be used for submission.
        """
        ...



__all__ = ['HTMLForm']

