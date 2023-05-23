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
# Namespace: com.sun.star.awt.grid
from __future__ import annotations
import typing
from abc import abstractmethod, abstractproperty
from ...lang.x_component import XComponent as XComponent_98dc0ab5
from ...util.x_cloneable import XCloneable as XCloneable_99d00aa3
if typing.TYPE_CHECKING:
    from .x_grid_column_listener import XGridColumnListener as XGridColumnListener_44350fba
    from ...style.horizontal_alignment import HorizontalAlignment as HorizontalAlignment_1f800f02
    from com.sun.star.style.HorizontalAlignment import HorizontalAlignmentProto

class XGridColumn(XComponent_98dc0ab5, XCloneable_99d00aa3):
    """
    The XGridColumn defines the properties and behavior of a column in a grid control.
    
    **since**
    
        OOo 3.3

    See Also:
        `API XGridColumn <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1grid_1_1XGridColumn.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.grid'
    __ooo_full_ns__: str = 'com.sun.star.awt.grid.XGridColumn'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.grid.XGridColumn'

    @abstractmethod
    def addGridColumnListener(self, Listener: XGridColumnListener_44350fba) -> None:
        """
        Adds a listener for the GridColumnEvent posted after the grid changes.
        """
        ...
    @abstractmethod
    def removeGridColumnListener(self, Listener: XGridColumnListener_44350fba) -> None:
        """
        Removes a listener previously added with addColumnListener().
        """
        ...
    @abstractproperty
    def ColumnWidth(self) -> int:
        """
        specifies the current width of the column.
        """
        ...

    @abstractproperty
    def DataColumnIndex(self) -> int:
        """
        denotes the index of the data column which should be used to fetch this grid column's data
        
        A grid control has a column model and a data model, both containing a possibly different number of columns. The DataColumnIndex attribute defines the index of the column within the data model, which should be used to retrieve actual data.
        
        Using this, you can do runtime changes to the column model, i.e. insertion and removal of columns, without necessarily needing to adjust the data model, too.
        
        If DataColumnIndex is negative, the it will be ignored, then the column's index within its column model, as determined by the Index attribute, will be used.
        """
        ...

    @abstractproperty
    def Flexibility(self) -> int:
        """
        specifies the flexibility of the column when it is automatically resized due to the grid control as a whole being resized.
        
        Specify 0 here if you do not want the column to be resized automatically.
        
        If a column has a flexibility greater than 0, it is set in relationship to the flexibility of all other such columns, and the respective widths of the columns are changed in the same relationship.
        
        Note that a column's flexibility is ignored if its Resizeable attribute is FALSE.
        
        A column's flexibility cannot be negative, attempts to set a negative value will raise an exception.
        """
        ...

    @abstractproperty
    def HelpText(self) -> str:
        """
        is the help text associated with the column.
        
        A grid control will usually display a column's help text as tooltip.
        """
        ...

    @abstractproperty
    def HorizontalAlign(self) -> HorizontalAlignmentProto:
        """
        Specifies the horizontal alignment of the content in the control.
        """
        ...

    @abstractproperty
    def Identifier(self) -> object:
        """
        specifies an identifier of the column
        
        This identifier will not be evaluated by the grid control, or its model. It is merely for clients to identify particular columns.
        """
        ...

    @abstractproperty
    def Index(self) -> int:
        """
        denotes the index of the column within the grid column model it belongs to
        
        If the column is not yet part of a column model, Index is -1.
        """
        ...

    @abstractproperty
    def MaxWidth(self) -> int:
        """
        specifies the maximal width the column can have.
        """
        ...

    @abstractproperty
    def MinWidth(self) -> int:
        """
        specifies the minimal width the column can have.
        """
        ...

    @abstractproperty
    def Resizeable(self) -> bool:
        """
        controls whether or not the column's width is fixed or not.
        
        If this is TRUE, the user can interactively change the column's width. Also, the column is subject to auto-resizing, if its Flexibility attribute is greater 0.
        """
        ...

    @abstractproperty
    def Title(self) -> str:
        """
        A title is displayed in the column header row if UnoControlGridModel.ShowColumnHeader() is set to TRUE
        """
        ...


__all__ = ['XGridColumn']

