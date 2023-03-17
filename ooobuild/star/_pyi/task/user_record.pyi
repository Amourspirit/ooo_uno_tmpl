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
# Namespace: com.sun.star.task
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class UserRecord(object):
    """
    Struct Class


    See Also:
        `API UserRecord <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1task_1_1UserRecord.html>`_
    """
    typeName: Literal['com.sun.star.task.UserRecord']

    def __init__(self, Passwords: typing.Optional[typing.Tuple[str, ...]] = ..., UserName: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Passwords (typing.Tuple[str, ...], optional): Passwords value.
            UserName (str, optional): UserName value.
        """
        ...


    @property
    def Passwords(self) -> typing.Tuple[str, ...]:
        """
        specifies the passwords for the given user.
        """
        ...


    @property
    def UserName(self) -> str:
        """
        specifies the user name.
        """
        ...


