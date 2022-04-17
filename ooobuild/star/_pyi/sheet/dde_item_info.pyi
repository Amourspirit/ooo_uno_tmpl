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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class DDEItemInfo(object):
    """
    Struct Class

    describes an item of a DDE connection.
    
    A DDE connection consists of the DDE service name, the DDE topic and a list of DDE items which may contain cached result sets.
    
    **since**
    
        OOo 3.1

    See Also:
        `API DDEItemInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DDEItemInfo.html>`_
    """
    typeName: Literal['com.sun.star.sheet.DDEItemInfo']

    def __init__(self, Results: typing.Optional[typing.Tuple[typing.Tuple[object, ...], ...]] = ..., Item: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Results (typing.Tuple[typing.Tuple[object, ...], ...], optional): Results value.
            Item (str, optional): Item value.
        """


    @property
    def Results(self) -> typing.Tuple[typing.Tuple[object, ...], ...]:
        """
        The results of the item cached from the last update of the DDE link if available.
        
        This sequence may be empty.
        """


    @property
    def Item(self) -> str:
        """
        The name of the DDE item.
        """


