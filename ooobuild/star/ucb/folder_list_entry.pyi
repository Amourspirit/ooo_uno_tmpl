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
import typing


class FolderListEntry(object):
    """
    Struct Class

    Information about a single folder in a FolderList.

    See Also:
        `API FolderListEntry <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1FolderListEntry.html>`_
    """
    typeName: str = 'com.sun.star.ucb.FolderListEntry'

    def __init__(self, Title: typing.Optional[str] = ..., ID: typing.Optional[str] = ..., Subscribed: typing.Optional[bool] = ..., New: typing.Optional[bool] = ..., Removed: typing.Optional[bool] = ..., Purge: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            Title (str, optional): Title value.
            ID (str, optional): ID value.
            Subscribed (bool, optional): Subscribed value.
            New (bool, optional): New value.
            Removed (bool, optional): Removed value.
            Purge (bool, optional): Purge value.
        """
        ...

    @property
    def Title(self) -> str:
        """
        The title of the folder.
        """
        ...
    @Title.setter
    def Title(self, value: str) -> None:
        ...
    @property
    def ID(self) -> str:
        """
        A (unique) identifier for the folder (used by IMAP, where different folders with equal human-readable titles may exist; otherwise, it may be left empty).
        """
        ...
    @ID.setter
    def ID(self, value: str) -> None:
        ...
    @property
    def Subscribed(self) -> bool:
        """
        The folder is subscribed.
        """
        ...
    @Subscribed.setter
    def Subscribed(self, value: bool) -> None:
        ...
    @property
    def New(self) -> bool:
        """
        The folder is new.
        """
        ...
    @New.setter
    def New(self, value: bool) -> None:
        ...
    @property
    def Removed(self) -> bool:
        """
        The folder has been removed.
        """
        ...
    @Removed.setter
    def Removed(self, value: bool) -> None:
        ...
    @property
    def Purge(self) -> bool:
        """
        The folder shall be purged (only used in conjunction with the FolderListCommand.SET).
        """
        ...
    @Purge.setter
    def Purge(self, value: bool) -> None:
        ...
