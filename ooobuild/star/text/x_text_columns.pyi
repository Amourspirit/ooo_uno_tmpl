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
# Namespace: com.sun.star.text
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .text_column import TextColumn as TextColumn_9b3f0ae0


class XTextColumns(XInterface_8f010a43):
    """
    manages columns within the object.
    
    The values used are relative. So it is not necessary to know the width of the object. The sum of the relative width values depends on the object and is defined in \"ReferenceValue.\"

    See Also:
        `API XTextColumns <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XTextColumns.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.text.XTextColumns'

    def getColumnCount(self) -> int:
        """
        """
        ...
    def getColumns(self) -> typing.Tuple[TextColumn_9b3f0ae0, ...]:
        """
        returns the column description of the object.
        """
        ...
    def getReferenceValue(self) -> int:
        """
        As described above, the width values are relative.
        """
        ...
    def setColumnCount(self, nColumns: int) -> None:
        """
        sets the number of columns.
        
        The minimum is 1 column.
        """
        ...
    def setColumns(self, Columns: typing.Tuple[TextColumn_9b3f0ae0, ...]) -> None:
        """
        sets the descriptors of all columns.
        
        The number of members in the sequence must be the same as the number of columns of the object.
        """
        ...


