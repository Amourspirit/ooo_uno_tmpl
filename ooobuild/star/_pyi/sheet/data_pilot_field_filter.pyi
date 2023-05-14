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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class DataPilotFieldFilter(object):
    """
    Struct Class


    See Also:
        `API DataPilotFieldFilter <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DataPilotFieldFilter.html>`_
    """
    typeName: Literal['com.sun.star.sheet.DataPilotFieldFilter']

    def __init__(self, FieldName: typing.Optional[str] = ..., MatchValueName: typing.Optional[str] = ..., MatchValue: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            FieldName (str, optional): FieldName value.
            MatchValueName (str, optional): MatchValueName value.
            MatchValue (str, optional): MatchValue value.
        """
        ...


    @property
    def FieldName(self) -> str:
        """
        Field name.
        """
        ...

    @FieldName.setter
    def FieldName(self, value: str) -> None:
        ...

    @property
    def MatchValueName(self) -> str:
        """
        String value that needs to match against, locale dependent.
        
        This is the value as name/label as also displayed in the filter popup dialog, maybe formatted by user applied number formats.
        """
        ...

    @MatchValueName.setter
    def MatchValueName(self, value: str) -> None:
        ...

    @property
    def MatchValue(self) -> str:
        """
        String value that needs to match against, locale independent.
        
        This is the underlying value formatted in a standardized way, for example ISO 8601 YYYY-MM-DD for dates.
        """
        ...

    @MatchValue.setter
    def MatchValue(self, value: str) -> None:
        ...

