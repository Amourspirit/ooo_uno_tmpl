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
# Namespace: com.sun.star.table
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..container.x_named import XNamed as XNamed_a6520b08
from .x_cell_range import XCellRange as XCellRange_a2f70ad5

class TableColumn(XPropertySet_bc180bfa, XNamed_a6520b08, XCellRange_a2f70ad5):
    """
    Service Class

    represents a special cell range containing all cells of a single specific column in a table or spreadsheet.

    See Also:
        `API TableColumn <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1table_1_1TableColumn.html>`_
    """
    @property
    def IsStartOfNewPage(self) -> bool:
        """
        is TRUE, if there is a manual horizontal page break attached to the column.
        """
    @property
    def IsVisible(self) -> bool:
        """
        is TRUE, if the column is visible.
        """
    @property
    def OptimalWidth(self) -> bool:
        """
        is TRUE, if the column always keeps its optimal width.
        """
    @property
    def Width(self) -> int:
        """
        contains the width of the column (in 1/100th mm).
        
        When hidden, it returns the width which the column would have, if it were visible.
        """


