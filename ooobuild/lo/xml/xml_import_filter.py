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
# Namespace: com.sun.star.xml
from ..document.import_filter import ImportFilter as ImportFilter_e4e90d48
from .sax.x_document_handler import XDocumentHandler as XDocumentHandler_9b90e28

class XMLImportFilter(ImportFilter_e4e90d48, XDocumentHandler_9b90e28):
    """
    Service Class

    describes an import filter for XML-based file formats.
    
    It is an extension of com.sun.star.document.ImportFilter and differs from it in that this filter additionally supports the com.sun.star.xml.sax.XDocumentHandler interface.

    See Also:
        `API XMLImportFilter <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1xml_1_1XMLImportFilter.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.xml'
    __ooo_full_ns__: str = 'com.sun.star.xml.XMLImportFilter'
    __ooo_type_name__: str = 'service'



__all__ = ['XMLImportFilter']

