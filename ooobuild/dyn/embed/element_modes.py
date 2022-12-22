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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.embed
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class ElementModes(metaclass=UnoConstMeta, type_name="com.sun.star.embed.ElementModes", name_space="com.sun.star.embed"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.embed.ElementModes``"""
        pass

    class ElementModesEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.embed.ElementModes", name_space="com.sun.star.embed"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.embed.ElementModes`` as Enum values"""
        pass

else:
    from ...lo.embed.element_modes import ElementModes as ElementModes

    class ElementModesEnum(IntEnum):
        """
        Enum of Const Class ElementModes

        The constant set contains possible modes to open an element.
        
        The modes can be combined by \"or\" operation. ElementModes.READ and ElementModes.WRITE are base modes. A result mode must include one of base modes.
        """
        READ = ElementModes.READ
        """
        specifies opening of an element for reading.
        """
        SEEKABLE = ElementModes.SEEKABLE
        """
        specifies opening of a seekable element.
        
        This mode is ignored for Storage elements. This flag makes sense only in combination with ElementModes.READ and/or ElementModes.WRITE.
        """
        SEEKABLEREAD = ElementModes.SEEKABLEREAD
        """
        specifies opening of a seekable element for reading.
        
        This is just a combination of the previous two values. For storages it is the same as ElementModes.READ.
        """
        WRITE = ElementModes.WRITE
        """
        specifies opening of an element for writing.
        """
        READWRITE = ElementModes.READWRITE
        """
        specifies opening of an element for reading and writing.
        
        For a stream element is also specifies that it must be seekable.
        """
        TRUNCATE = ElementModes.TRUNCATE
        """
        lets the document be truncated immediately after opening.
        
        This flag makes sense only in combination with ElementModes.WRITE.
        """
        NOCREATE = ElementModes.NOCREATE
        """
        restricts creation of a new element on opening in case a requested one does not exist.
        
        This flag makes sense only in combination with ElementModes.WRITE.
        """

__all__ = ['ElementModes', 'ElementModesEnum']
