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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.awt.grid
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
from ...lang.event_object import EventObject as EventObject_a3d70b03
from ...uno.x_interface import XInterface as XInterface_8f010a43
import typing


class GridSelectionEvent(EventObject_a3d70b03):
    """
    Struct Class

    An event used by a XGridControl to notify changes in its row selection.

    See Also:
        `API GridSelectionEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1grid_1_1GridSelectionEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.grid'
    __ooo_full_ns__: str = 'com.sun.star.awt.grid.GridSelectionEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.awt.grid.GridSelectionEvent'
    """Literal Constant ``com.sun.star.awt.grid.GridSelectionEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, SelectedRowIndexes: typing.Optional[typing.Tuple[int, ...]] = (), SelectedColumnIndexes: typing.Optional[typing.Tuple[int, ...]] = ()) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            SelectedRowIndexes (typing.Tuple[int, ...], optional): SelectedRowIndexes value.
            SelectedColumnIndexes (typing.Tuple[int, ...], optional): SelectedColumnIndexes value.
        """

        if isinstance(Source, GridSelectionEvent):
            oth: GridSelectionEvent = Source
            self.Source = oth.Source
            self.SelectedRowIndexes = oth.SelectedRowIndexes
            self.SelectedColumnIndexes = oth.SelectedColumnIndexes
            return

        kargs = {
            "Source": Source,
            "SelectedRowIndexes": SelectedRowIndexes,
            "SelectedColumnIndexes": SelectedColumnIndexes,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._selected_row_indexes = kwargs["SelectedRowIndexes"]
        self._selected_column_indexes = kwargs["SelectedColumnIndexes"]
        inst_keys = ('SelectedRowIndexes', 'SelectedColumnIndexes')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def SelectedRowIndexes(self) -> typing.Tuple[int, ...]:
        """
        denotes the indexes of the rows being selected at the time the event was fired.
        """
        return self._selected_row_indexes
    
    @SelectedRowIndexes.setter
    def SelectedRowIndexes(self, value: typing.Tuple[int, ...]) -> None:
        self._selected_row_indexes = value

    @property
    def SelectedColumnIndexes(self) -> typing.Tuple[int, ...]:
        """
        denotes the indexes of the columns being selected at the time the event was fired.
        """
        return self._selected_column_indexes
    
    @SelectedColumnIndexes.setter
    def SelectedColumnIndexes(self, value: typing.Tuple[int, ...]) -> None:
        self._selected_column_indexes = value


__all__ = ['GridSelectionEvent']
