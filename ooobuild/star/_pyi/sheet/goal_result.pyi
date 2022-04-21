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
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class GoalResult(object):
    """
    Struct Class

    is the result of a goal seek operation.

    See Also:
        `API GoalResult <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1GoalResult.html>`_
    """
    typeName: Literal['com.sun.star.sheet.GoalResult']

    def __init__(self, Divergence: typing.Optional[float] = ..., Result: typing.Optional[float] = ...) -> None:
        """
        Constructor

        Arguments:
            Divergence (float, optional): Divergence value.
            Result (float, optional): Result value.
        """


    @property
    def Divergence(self) -> float:
        """
        the amount by which the result changed in the last iteration.
        """


    @property
    def Result(self) -> float:
        """
        the resulting value.
        """


