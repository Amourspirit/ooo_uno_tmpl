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
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from ..sdbc.x_result_set import XResultSet as XResultSet_98e30aa7


class WelcomeDynamicResultSetStruct(object):
    """
    Struct Class

    This struct is to be contained in the first notification of an XDynamicResultSet.

    See Also:
        `API WelcomeDynamicResultSetStruct <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1WelcomeDynamicResultSetStruct.html>`_
    """
    typeName: Literal['com.sun.star.ucb.WelcomeDynamicResultSetStruct']

    def __init__(self, Old: typing.Optional[XResultSet_98e30aa7] = ..., New: typing.Optional[XResultSet_98e30aa7] = ...) -> None:
        """
        Constructor

        Arguments:
            Old (XResultSet, optional): Old value.
            New (XResultSet, optional): New value.
        """


    @property
    def Old(self) -> XResultSet_98e30aa7:
        """
        The static result set containing the previous version of result set data.
        """


    @property
    def New(self) -> XResultSet_98e30aa7:
        """
        The static result set containing the new version of result set data.
        """


