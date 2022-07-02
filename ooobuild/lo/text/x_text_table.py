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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.text
import typing
from abc import abstractmethod
from .x_text_content import XTextContent as XTextContent_b16e0ba5
if typing.TYPE_CHECKING:
    from ..table.x_cell import XCell as XCell_70d408e8
    from ..table.x_table_columns import XTableColumns as XTableColumns_c66d0c31
    from ..table.x_table_rows import XTableRows as XTableRows_a37e0afb
    from .x_text_table_cursor import XTextTableCursor as XTextTableCursor_e2f90d30

class XTextTable(XTextContent_b16e0ba5):
    """
    manages a text table.

    See Also:
        `API XTextTable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XTextTable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.XTextTable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.text.XTextTable'

    @abstractmethod
    def createCursorByCellName(self, aCellName: str) -> 'XTextTableCursor_e2f90d30':
        """
        creates a text table cursor and returns the XTextTableCursor interface.
        
        Initially the cursor is positioned in the cell with the specified name.
        """
        ...
    @abstractmethod
    def getCellByName(self, aCellName: str) -> 'XCell_70d408e8':
        """
        Example: The cell in the 4th column and third row has the name \"D3\".
        
        In cells that are split, the naming convention is more complex. In this case the name is a concatenation of the former cell name (i.e. \"D3\") and the number of the new column and row index inside of the original table cell separated by dots. This is done recursively.
        
        Example: If the cell \"D3\" is horizontally split, it now contains the cells \"D3.1.1\" and \"D3.1.2\"
        """
        ...
    @abstractmethod
    def getCellNames(self) -> 'typing.Tuple[str, ...]':
        """
        """
        ...
    @abstractmethod
    def getColumns(self) -> 'XTableColumns_c66d0c31':
        """
        """
        ...
    @abstractmethod
    def getRows(self) -> 'XTableRows_a37e0afb':
        """
        """
        ...
    @abstractmethod
    def initialize(self, nRows: int, nColumns: int) -> None:
        """
        determines the numbers of rows and columns of the text table.
        
        This method must be called after the object is created and before the object is insert or attached elsewhere.
        """
        ...

__all__ = ['XTextTable']

