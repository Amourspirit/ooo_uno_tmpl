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
# Libre Office Version: 7.2
# Namespace: com.sun.star.text.fieldmaster
from ..text_field_master import TextFieldMaster as TextFieldMaster_d6410cc2

class DDE(TextFieldMaster_d6410cc2):
    """
    Service Class

    specifies service of a DDE field master.

    See Also:
        `API DDE <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1fieldmaster_1_1DDE.html>`_
    """
    @property
    def Content(self) -> str:
        """
        contains the content.
        """
        ...
    @property
    def DDECommandElement(self) -> str:
        """
        contains the element string of the DDE command.
        """
        ...
    @property
    def DDECommandFile(self) -> str:
        """
        contains the file string of the DDE command.
        """
        ...
    @property
    def DDECommandType(self) -> str:
        """
        contains the type string of the DDE command.
        """
        ...
    @property
    def IsAutomaticUpdate(self) -> bool:
        """
        determines whether DDE link is updated automatically.
        """
        ...


