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
# Namespace: com.sun.star.text.textfield
from ...container.x_child import XChild as XChild_a6390b07
from ...container.x_enumeration_access import XEnumerationAccess as XEnumerationAccess_4bac0ffc
from ...rdf.x_metadatable import XMetadatable as XMetadatable_a3000af0
from ..text_field import TextField as TextField_90260a56
from ..x_text import XText as XText_690408ca

class MetadataField(TextField_90260a56, XChild_a6390b07, XEnumerationAccess_4bac0ffc, XMetadatable_a3000af0, XText_690408ca):
    """
    Service Class

    is a com.sun.star.text.TextField whose content is specified by RDF metadata.
    
    **since**
    
        OOo 3.2

    See Also:
        `API MetadataField <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1MetadataField.html>`_
    """
    @property
    def IsFixedLanguage(self) -> bool:
        """
        determines whether changes in language attributes at the position of the text field also change the number format as appropriate for this language.
        """
    @property
    def NumberFormat(self) -> int:
        """
        this is the number format for this field.
        """

