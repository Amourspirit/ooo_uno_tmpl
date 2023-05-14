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
from ..text_field import TextField as TextField_90260a56

class PageCount(TextField_90260a56):
    """
    Service Class

    specifies service of a text field that displays the number of pages contained in the document.

    See Also:
        `API PageCount <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1PageCount.html>`_
    """
    @property
    def NumberingType(self) -> int:
        """
        specifies the type of the numbering as com.sun.star.style.NumberingType
        """
        ...

    @NumberingType.setter
    def NumberingType(self, value: int) -> None:
        ...

