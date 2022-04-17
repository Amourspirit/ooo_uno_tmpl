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
# Namespace: com.sun.star.text
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..container.x_index_replace import XIndexReplace as XIndexReplace_feed0dd7

class NumberingRules(XPropertySet_bc180bfa, XIndexReplace_feed0dd7):
    """
    Service Class

    provides access to the numbering rules.
    
    Numbering rules may be set at a Paragraph object. The numbering rules are levels of property values. Each level contains equal properties.

    See Also:
        `API NumberingRules <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1NumberingRules.html>`_
    """
    @property
    def DefaultListId(self) -> str:
        """
        id of default list for the numbering rules instance
        """
    @property
    def IsAbsoluteMargins(self) -> bool:
        """
        determines if the margins are absolute or relative to the preceding numbering level.
        """
    @property
    def IsAutomatic(self) -> bool:
        """
        determines if the numbering rules are automatically created as opposed to numbering rules that are part of a numbering style.
        """
    @property
    def IsContinuousNumbering(self) -> bool:
        """
        determines if the numbering levels are counted continuously or if each numbering level is counted separately.
        """
    @property
    def Name(self) -> str:
        """
        contains the name of the numbering rules.
        
        It is used to identify a certain numbering rules property
        """
    @property
    def NumberingIsOutline(self) -> bool:
        """
        This numbering is used in the outline of the document (e.g.
        
        headings).
        """
    @property
    def NumberingType(self) -> int:
        """
        the type of numbering (Arabic, characters, roman numbers, etc.).
        """


