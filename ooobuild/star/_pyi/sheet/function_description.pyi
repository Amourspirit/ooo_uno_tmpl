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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sheet
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from .function_argument import FunctionArgument as FunctionArgument_f1080daa

class FunctionDescription(ABC):
    """
    Service Class

    collects all properties used to describe a function.

    See Also:
        `API FunctionDescription <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1FunctionDescription.html>`_
    """
    @property
    def Arguments(self) -> 'typing.Tuple[FunctionArgument_f1080daa, ...]':
        """
        returns a sequence of localized descriptions of the function's arguments (in the order specified by the function).
        """
    @property
    def Category(self) -> int:
        """
        returns the function's category.
        """
    @property
    def Description(self) -> str:
        """
        returns a localized description of the function.
        """
    @property
    def Id(self) -> int:
        """
        returns the function's unique identifier.
        """
    @property
    def Name(self) -> str:
        """
        returns the localized function's name.
        """


