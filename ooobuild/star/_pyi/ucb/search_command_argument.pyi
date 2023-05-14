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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing
from ..beans.property import Property as Property_8f4e0a76
from .search_info import SearchInfo as SearchInfo_8daf0a24


class SearchCommandArgument(object):
    """
    Struct Class

    The argument for the command \"search\".

    See Also:
        `API SearchCommandArgument <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1SearchCommandArgument.html>`_
    """
    typeName: Literal['com.sun.star.ucb.SearchCommandArgument']

    def __init__(self, Properties: typing.Optional[typing.Tuple[Property_8f4e0a76, ...]] = ..., Info: typing.Optional[SearchInfo_8daf0a24] = ...) -> None:
        """
        Constructor

        Arguments:
            Properties (typing.Tuple[Property, ...], optional): Properties value.
            Info (SearchInfo, optional): Info value.
        """
        ...


    @property
    def Properties(self) -> typing.Tuple[Property_8f4e0a76, ...]:
        """
        the properties for which values shall be provided through the ContentResultSet returned by the search command.
        """
        ...


    @property
    def Info(self) -> SearchInfo_8daf0a24:
        """
        the search criteria.
        """
        ...


