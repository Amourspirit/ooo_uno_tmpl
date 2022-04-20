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
from .lock_scope import LockScope as LockScope_839109c5
from .lock_type import LockType as LockType_7a09096d


class LockEntry(object):
    """
    Struct Class

    defines the types of locks that can be used with a resource.

    See Also:
        `API LockEntry <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1LockEntry.html>`_
    """
    typeName: Literal['com.sun.star.ucb.LockEntry']

    def __init__(self, Scope: typing.Optional[LockScope_839109c5] = ..., Type: typing.Optional[LockType_7a09096d] = ...) -> None:
        """
        Constructor

        Arguments:
            Scope (LockScope, optional): Scope value.
            Type (LockType, optional): Type value.
        """


    @property
    def Scope(self) -> LockScope_839109c5:
        """
        defines the lock's scope.
        """


    @property
    def Type(self) -> LockType_7a09096d:
        """
        defines the type of the lock.
        """


