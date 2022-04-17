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
from ..container.x_named import XNamed as XNamed_a6520b08
from .x_exporter import XExporter as XExporter_be500c18
from .x_filter import XFilter as XFilter_a6300b25
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca

class ExportFilter(XNamed_a6520b08, XExporter_be500c18, XFilter_a6300b25, XInitialization_d46c0cca):
    """
    Service Class

    filter for exports
    
    Such filters can be used for exporting a content. Of course it's possible to combine it with the service ImportFilter if import functionality should be available at same implementation too.

    See Also:
        `API ExportFilter <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1document_1_1ExportFilter.html>`_
    """


