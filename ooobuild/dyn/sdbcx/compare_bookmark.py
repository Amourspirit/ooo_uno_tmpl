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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sdbcx
import uno
from enum import IntEnum
from typing import TYPE_CHECKING
from ooo.oenv.env_const import UNO_ENVIRONMENT, UNO_RUNTIME

_DYNAMIC = False
if (not TYPE_CHECKING) and UNO_RUNTIME and UNO_ENVIRONMENT:
    _DYNAMIC = True

if not TYPE_CHECKING and _DYNAMIC:
    # document generators will most likely not see this.
    from ooo.helper.enum_helper import UnoConstMeta, ConstEnumMeta

    class CompareBookmark(metaclass=UnoConstMeta, type_name="com.sun.star.sdbcx.CompareBookmark", name_space="com.sun.star.sdbcx"):
        """Dynamic Class. Contains all the constant values of ``com.sun.star.sdbcx.CompareBookmark``"""
        pass

    class CompareBookmarkEnum(IntEnum, metaclass=ConstEnumMeta, type_name="com.sun.star.sdbcx.CompareBookmark", name_space="com.sun.star.sdbcx"):
        """Dynamic Enum. Contains all the constant values of ``com.sun.star.sdbcx.CompareBookmark`` as Enum values"""
        pass

else:
    if TYPE_CHECKING:
        from com.sun.star.sdbcx import CompareBookmark as CompareBookmark
    else:
        # keep document generators happy
        from ...lo.sdbcx.compare_bookmark import CompareBookmark as CompareBookmark

    class CompareBookmarkEnum(IntEnum):
        """
        Enum of Const Class CompareBookmark

        describes the result of a comparison of two bookmarks.
        """
        LESS = CompareBookmark.LESS
        """
        the first bookmark is before the second.
        """
        EQUAL = CompareBookmark.EQUAL
        """
        the first bookmark is equal to the second.
        """
        GREATER = CompareBookmark.GREATER
        """
        the first bookmark is after the second one.
        """
        NOT_EQUAL = CompareBookmark.NOT_EQUAL
        """
        the first bookmark is not the same as the second one.
        """
        NOT_COMPARABLE = CompareBookmark.NOT_COMPARABLE
        """
        the two bookmarks are not comparable.
        """

__all__ = ['CompareBookmark', 'CompareBookmarkEnum']
