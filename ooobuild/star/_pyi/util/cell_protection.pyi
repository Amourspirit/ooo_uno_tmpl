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
# Namespace: com.sun.star.util
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class CellProtection(object):
    """
    Struct Class

    describes the kind of protection for a protectable cell.

    See Also:
        `API CellProtection <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1CellProtection.html>`_
    """
    typeName: Literal['com.sun.star.util.CellProtection']

    def __init__(self, IsLocked: typing.Optional[bool] = ..., IsFormulaHidden: typing.Optional[bool] = ..., IsHidden: typing.Optional[bool] = ..., IsPrintHidden: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            IsLocked (bool, optional): IsLocked value.
            IsFormulaHidden (bool, optional): IsFormulaHidden value.
            IsHidden (bool, optional): IsHidden value.
            IsPrintHidden (bool, optional): IsPrintHidden value.
        """
        ...


    @property
    def IsLocked(self) -> bool:
        """
        specifies if the cell is locked from modifications by the user.
        """
        ...


    @property
    def IsFormulaHidden(self) -> bool:
        """
        specifies if the formula is hidden from the user.
        """
        ...


    @property
    def IsHidden(self) -> bool:
        """
        specifies if the cell is hidden from the user.
        """
        ...


    @property
    def IsPrintHidden(self) -> bool:
        """
        specifies if the cell is hidden on printouts.
        """
        ...


