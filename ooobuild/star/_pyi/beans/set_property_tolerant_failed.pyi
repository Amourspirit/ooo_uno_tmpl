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
# Namespace: com.sun.star.beans
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class SetPropertyTolerantFailed(object):
    """
    Struct Class

    specifies information about a single property failed to be set.

    See Also:
        `API SetPropertyTolerantFailed <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1SetPropertyTolerantFailed.html>`_
    """
    typeName: Literal['com.sun.star.beans.SetPropertyTolerantFailed']

    def __init__(self, Name: typing.Optional[str] = ..., Result: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            Result (int, optional): Result value.
        """


    @property
    def Name(self) -> str:
        """
        specifies the name of the property.
        """


    @property
    def Result(self) -> int:
        """
        specifies the success or error code for setting the properties value.
        
        Since the property was not successful set the result will never be com.sun.star.beans.TolerantPropertySetResultType.SUCCESS.
        """


