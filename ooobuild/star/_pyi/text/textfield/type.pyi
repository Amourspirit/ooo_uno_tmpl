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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.text.textfield
from typing_extensions import Literal


class Type:
    """
    Const Class

    Text field types.
    
    Right now this only contains the types that are supported by the edit engine, but it should eventually contain all field types that are used across all engines.
    
    **since**
    
        LibreOffice 3.6

    See Also:
        `API Type <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1textfield_1_1Type.html>`_
    """
    UNSPECIFIED: Literal[-1]
    DATE: Literal[0]
    URL: Literal[1]
    PAGE: Literal[2]
    PAGES: Literal[3]
    TIME: Literal[4]
    TABLE: Literal[5]
    EXTENDED_TIME: Literal[6]
    EXTENDED_FILE: Literal[7]
    AUTHOR: Literal[8]
    MEASURE: Literal[9]
    DOCINFO_TITLE: Literal[10]
    PRESENTATION_HEADER: Literal[11]
    PRESENTATION_FOOTER: Literal[12]
    PRESENTATION_DATE_TIME: Literal[13]
    PAGE_NAME: Literal[14]
    DOCINFO_CUSTOM: Literal[15]

