# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .table_page_break_data import TablePageBreakData as TablePageBreakData_8ac0de5


class XSheetPageBreak(XInterface_8f010a43):
    """
    provides access to page breaks in a sheet.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XSheetPageBreak <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSheetPageBreak.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.XSheetPageBreak']

    def getColumnPageBreaks(self) -> 'typing.Tuple[TablePageBreakData_8ac0de5, ...]':
        """
        returns a sequence of descriptions of all horizontal page breaks on the sheet.
        
        This includes manual and automatic page breaks. To add or remove manual breaks, use the com.sun.star.table.TableColumn.IsStartOfNewPage property of the column.
        """
        ...
    def getRowPageBreaks(self) -> 'typing.Tuple[TablePageBreakData_8ac0de5, ...]':
        """
        returns a sequence of descriptions of all vertical page breaks on the sheet.
        
        This includes manual and automatic page breaks. To add or remove manual breaks, use the com.sun.star.table.TableRow.IsStartOfNewPage property of the row.
        """
        ...
    def removeAllManualPageBreaks(self) -> None:
        """
        removes all manual page breaks on the sheet.
        """
        ...


