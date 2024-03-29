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
# Namespace: com.sun.star.task
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from .user_record import UserRecord as UserRecord_9a2e0ab9


class UrlRecord(object):
    """
    Struct Class


    See Also:
        `API UrlRecord <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1task_1_1UrlRecord.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.task'
    __ooo_full_ns__: str = 'com.sun.star.task.UrlRecord'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.task.UrlRecord'
    """Literal Constant ``com.sun.star.task.UrlRecord``"""

    def __init__(self, UserList: typing.Optional[typing.Tuple[UserRecord_9a2e0ab9, ...]] = (), Url: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            UserList (typing.Tuple[UserRecord, ...], optional): UserList value.
            Url (str, optional): Url value.
        """
        super().__init__()

        if isinstance(UserList, UrlRecord):
            oth: UrlRecord = UserList
            self.UserList = oth.UserList
            self.Url = oth.Url
            return

        kargs = {
            "UserList": UserList,
            "Url": Url,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._user_list = kwargs["UserList"]
        self._url = kwargs["Url"]


    @property
    def UserList(self) -> typing.Tuple[UserRecord_9a2e0ab9, ...]:
        return self._user_list

    @UserList.setter
    def UserList(self, value: typing.Tuple[UserRecord_9a2e0ab9, ...]) -> None:
        self._user_list = value

    @property
    def Url(self) -> str:
        """
        The URL for which these passwords where given.
        """
        return self._url

    @Url.setter
    def Url(self, value: str) -> None:
        self._url = value


__all__ = ['UrlRecord']
