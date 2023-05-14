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
# Namespace: com.sun.star.xml
from ..document.export_filter import ExportFilter as ExportFilter_e5320d4f

class XMLExportFilter(ExportFilter_e5320d4f):
    """
    Service Class

    describes an export filter for XML-based file formats.
    
    It is an extension of com.sun.star.document.ExportFilter and differs from it only in that an com.sun.star.xml.sax.XDocumentHandler needs to be passed through the XInitialization interface. This XDocumentHandler will then be used to export the XML data stream.

    See Also:
        `API XMLExportFilter <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1xml_1_1XMLExportFilter.html>`_
    """
    ...

