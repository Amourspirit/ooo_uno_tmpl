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
# Namespace: com.sun.star.xsd
from .x_data_type import XDataType as XDataType_83f209cb

class String(XDataType_83f209cb):
    """
    Service Class

    specifies an XSD compliant string type

    See Also:
        `API String <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1xsd_1_1String.html>`_
    """
    @property
    def Length(self) -> int:
        """
        specifies the length of the string
        
        Note that you cannot specify Length together with MinLength or MaxLength.
        """
    @property
    def MaxLength(self) -> int:
        """
        specifies the maximum length of the string
        
        Note that you cannot specify MaxLength together with Length.
        """
    @property
    def MinLength(self) -> int:
        """
        specifies the minimum length of the string
        
        Note that you cannot specify MinLength together with Length.
        """


