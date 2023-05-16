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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.datatransfer.clipboard
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class RenderingCapabilities(metaclass=UnoConstMeta, type_name="com.sun.star.datatransfer.clipboard.RenderingCapabilities", name_space="com.sun.star.datatransfer.clipboard"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.datatransfer.clipboard.RenderingCapabilities``"""
        pass

    class RenderingCapabilitiesEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.datatransfer.clipboard.RenderingCapabilities", name_space="com.sun.star.datatransfer.clipboard"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.datatransfer.clipboard.RenderingCapabilities`` as Enum values"""
        pass

else:
    from com.sun.star.datatransfer.clipboard import RenderingCapabilities as RenderingCapabilities

    class RenderingCapabilitiesEnum(IntEnum):
        """
        Enum of Const Class RenderingCapabilities

        These flags describe the capabilities a system clipboard has to transfer data to other applications via the OS.
        """
        Delayed = RenderingCapabilities.Delayed
        """
        The implementation supports delayed rendering.
        """
        Persistant = RenderingCapabilities.Persistant
        """
        The implementation is able to store the data persistent in the system so that it does not get lost when the source application no longer exist.
        """
        Persistent = RenderingCapabilities.Persistent
        """
        The implementation is able to store the data persistent in the system so that it does not get lost when the source application no longer exist.
        """

__all__ = ['RenderingCapabilities', 'RenderingCapabilitiesEnum']
