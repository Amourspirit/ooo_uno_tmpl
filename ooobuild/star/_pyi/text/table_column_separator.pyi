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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.text
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class TableColumnSeparator(object):
    """
    Struct Class

    The width of the cells of a text table is defined by the position of the separator between neighboring cells.
    
    If cells of the table are merged, this separator is not removed, but it is hidden.
    
    A text table or a text table row provides the separators in a sequence of TableColumnSeparators. If the table only consists of one column, then this sequence is empty.
    
    The real width of a table depends on the environment (page style and number of text columns at the table's position, alignment, and left and right margins). For that reason, the table column separator does not contain metric values for the column widths. The values are relative to the value of the property TextTable.TableColumnRelativeSum.
    
    A table provides this property only if all rows have the same structure. If the table does not provide the property, then it cannot be set using.
    
    The state of TableColumnSeparator.IsVisible and the count of the sequence must be the same in as it was in. Hidden separators cannot be moved and they cannot be overtaken by visible separators.

    See Also:
        `API TableColumnSeparator <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1text_1_1TableColumnSeparator.html>`_
    """
    typeName: Literal['com.sun.star.text.TableColumnSeparator']

    def __init__(self, Position: typing.Optional[int] = ..., IsVisible: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            Position (int, optional): Position value.
            IsVisible (bool, optional): IsVisible value.
        """
        ...


    @property
    def Position(self) -> int:
        """
        contains the position of the separator.
        """
        ...


    @property
    def IsVisible(self) -> bool:
        """
        determines if the separator is visible.
        """
        ...


