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
# Namespace: com.sun.star.table
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from ..lang.locale import Locale as Locale_70d308fa
from .table_sort_field_type import TableSortFieldType as TableSortFieldType_9a50e26


class TableSortField(object):
    """
    Struct Class

    describes how to sort a single field (row/column) in a tables sort descriptor.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API TableSortField <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1table_1_1TableSortField.html>`_
    """
    typeName: Literal['com.sun.star.table.TableSortField']

    def __init__(self, Field: typing.Optional[int] = ..., IsAscending: typing.Optional[bool] = ..., IsCaseSensitive: typing.Optional[bool] = ..., FieldType: typing.Optional[TableSortFieldType_9a50e26] = ..., CollatorLocale: typing.Optional[Locale_70d308fa] = ..., CollatorAlgorithm: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Field (int, optional): Field value.
            IsAscending (bool, optional): IsAscending value.
            IsCaseSensitive (bool, optional): IsCaseSensitive value.
            FieldType (TableSortFieldType, optional): FieldType value.
            CollatorLocale (Locale, optional): CollatorLocale value.
            CollatorAlgorithm (str, optional): CollatorAlgorithm value.
        """
        ...


    @property
    def Field(self) -> int:
        """
        index of the row or column in the table to be sorted; 0-based.
        """
        ...

    @Field.setter
    def Field(self, value: int) -> None:
        ...

    @property
    def IsAscending(self) -> bool:
        """
        TRUE if data are sorted in ascending order, FALSE if in descending order.
        """
        ...

    @IsAscending.setter
    def IsAscending(self, value: bool) -> None:
        ...

    @property
    def IsCaseSensitive(self) -> bool:
        """
        specifies if the case of letters is important when comparing entries.
        """
        ...

    @IsCaseSensitive.setter
    def IsCaseSensitive(self, value: bool) -> None:
        ...

    @property
    def FieldType(self) -> TableSortFieldType_9a50e26:
        """
        type of contents in the field.
        
        If the value is com.sun.star.table.TableSortFieldType.AUTOMATIC the algorithm used for sorting is application specific. Especially it may or may not use the values given by \"CollatorLocale\" and \"CollatorAlgorithm\".
        """
        ...

    @FieldType.setter
    def FieldType(self, value: TableSortFieldType_9a50e26) -> None:
        ...

    @property
    def CollatorLocale(self) -> Locale_70d308fa:
        """
        the locale used by the collator when comparing/sorting text.
        
        This property will not be used when the \"FieldType\" is com.sun.star.table.TableSortFieldType.NUMERIC
        """
        ...

    @CollatorLocale.setter
    def CollatorLocale(self, value: Locale_70d308fa) -> None:
        ...

    @property
    def CollatorAlgorithm(self) -> str:
        """
        the algorithm used by the collator when comparing/sorting text.
        
        This property will not be used when the \"FieldType\" is com.sun.star.table.TableSortFieldType.NUMERIC
        """
        ...

    @CollatorAlgorithm.setter
    def CollatorAlgorithm(self, value: str) -> None:
        ...

