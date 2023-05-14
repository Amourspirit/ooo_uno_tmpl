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
# Namespace: com.sun.star.sdb
# Libre Office Version: 7.3
from typing_extensions import Literal
from .row_change_event import RowChangeEvent as RowChangeEvent_ba0c0bc1
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class RowsChangeEvent(RowChangeEvent_ba0c0bc1):
    """
    Struct Class

    indicates which rows have changed and the type of change action on the row set.

    See Also:
        `API RowsChangeEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sdb_1_1RowsChangeEvent.html>`_
    """
    typeName: Literal['com.sun.star.sdb.RowsChangeEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., Action: typing.Optional[int] = ..., Rows: typing.Optional[int] = ..., Bookmarks: typing.Optional[typing.Tuple[object, ...]] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Action (int, optional): Action value.
            Rows (int, optional): Rows value.
            Bookmarks (typing.Tuple[object, ...], optional): Bookmarks value.
        """
        ...


    @property
    def Bookmarks(self) -> typing.Tuple[object, ...]:
        ...

    @Bookmarks.setter
    def Bookmarks(self, value: typing.Tuple[object, ...]) -> None:
        ...

