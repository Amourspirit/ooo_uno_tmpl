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
# Namespace: com.sun.star.document
import typing
from .xxml_basic_exporter import XXMLBasicExporter as XXMLBasicExporter_26ee0eeb
if typing.TYPE_CHECKING:
    from ..xml.sax.x_document_handler import XDocumentHandler as XDocumentHandler_9b90e28

class XMLOasisBasicExporter(XXMLBasicExporter_26ee0eeb):
    """
    Service Class

    Filter for exporting Basic macros to the OASIS Open Office file format.
    
    First the XExporter.setSourceDocument() method must be called in order to provide the export component with the source document from which the data should be exported. After that, the export is started by calling the XFilter.filter() method.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XMLOasisBasicExporter <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1document_1_1XMLOasisBasicExporter.html>`_
    """
    def createWithHandler(self, DocumentHandler: 'XDocumentHandler_9b90e28') -> None:
        """
        """


