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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class ListAction(object):
    """
    Struct Class

    This struct contains information needed in the notifications of a XDynamicResultSet.

    See Also:
        `API ListAction <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1ListAction.html>`_
    """
    typeName: Literal['com.sun.star.ucb.ListAction']

    def __init__(self, Position: typing.Optional[int] = ..., Count: typing.Optional[int] = ..., ListActionType: typing.Optional[int] = ..., ActionInfo: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Position (int, optional): Position value.
            Count (int, optional): Count value.
            ListActionType (int, optional): ListActionType value.
            ActionInfo (object, optional): ActionInfo value.
        """


    @property
    def Position(self) -> int:
        """
        The position where something has happened (index begins with 1 as usual with JDBC ).
        
        Its value does not necessary indicate the new position in the new com.sun.star.sdbc.XResultSet, but a position while doing the changes step by step beginning with the old com.sun.star.sdbc.XResultSet.
        """


    @property
    def Count(self) -> int:
        """
        The count of involved rows.
        """


    @property
    def ListActionType(self) -> int:
        """
        specifies the kind of modification happened to all assigned rows.
        
        The value of the other members of this struct depend on the value of this member:
        """


    @property
    def ActionInfo(self) -> object:
        """
        depending on the content of ListAction.ListActionType the ListAction.ActionInfo could contain additional information about the changes happened (see table above).
        """


