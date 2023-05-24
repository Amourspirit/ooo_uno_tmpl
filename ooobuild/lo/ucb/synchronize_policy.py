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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from typing import cast
from enum import Enum
from com.sun.star.ucb.SynchronizePolicy import SynchronizePolicyProto

class SynchronizePolicy(Enum):
    """
    Enum Class


    See Also:
        `API SynchronizePolicy <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#aaa633f0c45560a4367cb74d393c0c619>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.SynchronizePolicy'
    __ooo_type_name__: str = 'enum'

    @property
    def typeName(self) -> str:
        return 'com.sun.star.ucb.SynchronizePolicy'

    CLIENT_IS_MASTER = cast(SynchronizePolicyProto, 'CLIENT_IS_MASTER')
    """
    Client is master.
    """
    NONE_IS_MASTER = cast(SynchronizePolicyProto, 'NONE_IS_MASTER')
    """
    None is master.
    """
    SERVER_IS_MASTER = cast(SynchronizePolicyProto, 'SERVER_IS_MASTER')
    """
    Server is master.
    """

__all__ = ['SynchronizePolicy']

