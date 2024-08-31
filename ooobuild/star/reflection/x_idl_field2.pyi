# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.reflection
from __future__ import annotations
import typing

from .x_idl_member import XIdlMember as XIdlMember_e3400cfc
if typing.TYPE_CHECKING:
    from .x_idl_class import XIdlClass as XIdlClass_d63a0c9a
    from com.sun.star.reflection.FieldAccessMode import FieldAccessModeProto  # type: ignore


class XIdlField2(XIdlMember_e3400cfc):
    """
    Reflects an IDL interface attribute, enum or compound type (i.e.
    
    struct/exception) member.

    See Also:
        `API XIdlField2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XIdlField2.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.reflection.XIdlField2'

    def get(self, obj: typing.Any) -> typing.Any:
        """
        Gets the value of the reflected field from the given object, i.e.
        
        an interface, enum or compound type (struct/exception). For enums, the given object is ignored; the returned value reflects the constant enum 32-bit value.
        
        When setting an interface attribute raises a non com.sun.star.uno.RuntimeException, it is wrapped in a com.sun.star.lang.WrappedTargetRuntimeException.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getAccessMode(self) -> FieldAccessModeProto:
        """
        Returns the access mode of the field, i.e.
        
        read-write, read-only or write-only (access mode \"const\" is deprecated).
        """
        ...
    def getType(self) -> XIdlClass_d63a0c9a:
        """
        Returns the type of the field.
        """
        ...
    def set(self, obj: typing.Any, value: typing.Any) -> None:
        """
        Sets the value of the reflected field of the given object, i.e.
        
        an interface or compound type (struct/exception).
        
        When setting an interface attribute raises a non com.sun.star.uno.RuntimeException, it is wrapped in a com.sun.star.lang.WrappedTargetRuntimeException.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.IllegalAccessException: ``IllegalAccessException``
        """
        ...
