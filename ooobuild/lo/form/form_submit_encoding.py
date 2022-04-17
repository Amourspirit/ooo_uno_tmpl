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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.form
# Libre Office Version: 7.3
from enum import Enum


class FormSubmitEncoding(Enum):
    """
    Enum Class

    

    See Also:
        `API FormSubmitEncoding <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1form.html#a4a4c5c07c0618f59711919741a523ab8>`_
    """
    __ooo_ns__: str = 'com.sun.star.form'
    __ooo_full_ns__: str = 'com.sun.star.form.FormSubmitEncoding'
    __ooo_type_name__: str = 'enum'

    MULTIPART = 'MULTIPART'
    """
    Specifies to use \"multipart/form-data\" as submit encoding.
    
    Usually used when the form contains a file upload element.
    """
    TEXT = 'TEXT'
    """
    specifies to use \"text/plain\"
    
    Usually used if the FormSubmitMethod attribute has the value POST and the content should be reviewed as full text.
    """
    URL = 'URL'
    """
    When the button is clicked, a URL set for the button is opened.
    
    Specifies to use \"application/x-www-form-urlencoded\" as submit encoding.
    
    Usually used if the FormSubmitMethod attribute has the value POST.
    """

__all__ = ['FormSubmitEncoding']
