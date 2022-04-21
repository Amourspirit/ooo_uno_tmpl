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
from .lock_entry import LockEntry as LockEntry_839e09dd
from .lock_scope import LockScope as LockScope_839109c5
from .lock_type import LockType as LockType_7a09096d
import typing
from .lock_depth import LockDepth as LockDepth_835c09c0


class Lock(LockEntry_839e09dd):
    """
    Struct Class

    defines a lock.

    See Also:
        `API Lock <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1Lock.html>`_
    """
    typeName: Literal['com.sun.star.ucb.Lock']

    def __init__(self, Scope: typing.Optional[LockScope_839109c5] = ..., Type: typing.Optional[LockType_7a09096d] = ..., LockTokens: typing.Optional[typing.Tuple[str, ...]] = ..., Depth: typing.Optional[LockDepth_835c09c0] = ..., Owner: typing.Optional[object] = ..., Timeout: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Scope (LockScope, optional): Scope value.
            Type (LockType, optional): Type value.
            LockTokens (typing.Tuple[str, ...], optional): LockTokens value.
            Depth (LockDepth, optional): Depth value.
            Owner (object, optional): Owner value.
            Timeout (int, optional): Timeout value.
        """


    @property
    def LockTokens(self) -> typing.Tuple[str, ...]:
        """
        the lock tokens.
        
        Each lock token is a URI.
        """


    @property
    def Depth(self) -> LockDepth_835c09c0:
        """
        defines the lock's depth.
        """


    @property
    def Owner(self) -> object:
        """
        the owner of the lock.
        
        This element provides information sufficient for either directly contacting a principal (such as a telephone number or email URI), or for discovering the principal (such as the URL of a homepage) who owns the lock.
        """


    @property
    def Timeout(self) -> int:
        """
        a timeout value for the lock.
        
        This element specifies the number of seconds between granting of the lock and the automatic removal of that lock. The value must not be greater than 2^32-1. A value of -1 stands for an infinite lock, that will never be removed automatically.
        """


