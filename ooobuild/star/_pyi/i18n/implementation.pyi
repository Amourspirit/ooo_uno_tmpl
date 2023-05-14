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
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class Implementation(object):
    """
    Struct Class

    Implementation name details returned in a sequence by XLocaleData.getCollatorImplementations().

    See Also:
        `API Implementation <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1Implementation.html>`_
    """
    typeName: Literal['com.sun.star.i18n.Implementation']

    def __init__(self, unoID: typing.Optional[str] = ..., isDefault: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            unoID (str, optional): unoID value.
            isDefault (bool, optional): isDefault value.
        """
        ...


    @property
    def unoID(self) -> str:
        """
        The implementation name.
        """
        ...

    @unoID.setter
    def unoID(self, value: str) -> None:
        ...

    @property
    def isDefault(self) -> bool:
        """
        If this is the default implementation.
        """
        ...

    @isDefault.setter
    def isDefault(self, value: bool) -> None:
        ...

