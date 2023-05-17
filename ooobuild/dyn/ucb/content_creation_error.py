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
from __future__ import annotations
import uno
from typing import Any, cast, TYPE_CHECKING


if TYPE_CHECKING:

    from com.sun.star.ucb.ContentCreationError import CONTENT_CREATION_FAILED as CONTENT_CREATION_ERROR_CONTENT_CREATION_FAILED
    from com.sun.star.ucb.ContentCreationError import IDENTIFIER_CREATION_FAILED as CONTENT_CREATION_ERROR_IDENTIFIER_CREATION_FAILED
    from com.sun.star.ucb.ContentCreationError import NO_CONTENT_BROKER as CONTENT_CREATION_ERROR_NO_CONTENT_BROKER
    from com.sun.star.ucb.ContentCreationError import NO_CONTENT_PROVIDER as CONTENT_CREATION_ERROR_NO_CONTENT_PROVIDER
    from com.sun.star.ucb.ContentCreationError import NO_IDENTIFIER_FACTORY as CONTENT_CREATION_ERROR_NO_IDENTIFIER_FACTORY
    from com.sun.star.ucb.ContentCreationError import UNKNOWN as CONTENT_CREATION_ERROR_UNKNOWN

    class ContentCreationError(uno.Enum):
        """
        Enum Class


        See Also:
            `API ContentCreationError <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1ucb.html#aa2e437022c4d519cf5488a06e5e81ef4>`_
        """

        def __init__(self, value: Any) -> None:
            super().__init__('com.sun.star.ucb.ContentCreationError', value)

        __ooo_ns__: str = 'com.sun.star.ucb'
        __ooo_full_ns__: str = 'com.sun.star.ucb.ContentCreationError'
        __ooo_type_name__: str = 'enum'

        CONTENT_CREATION_FAILED = cast("ContentCreationError", CONTENT_CREATION_ERROR_CONTENT_CREATION_FAILED)
        """
        Provider was unable to create the content instance.
        """
        IDENTIFIER_CREATION_FAILED = cast("ContentCreationError", CONTENT_CREATION_ERROR_IDENTIFIER_CREATION_FAILED)
        """
        Creation of content identifier failed.
        """
        NO_CONTENT_BROKER = cast("ContentCreationError", CONTENT_CREATION_ERROR_NO_CONTENT_BROKER)
        """
        """
        NO_CONTENT_PROVIDER = cast("ContentCreationError", CONTENT_CREATION_ERROR_NO_CONTENT_PROVIDER)
        """
        No Content Provider for given content identifier available.
        """
        NO_IDENTIFIER_FACTORY = cast("ContentCreationError", CONTENT_CREATION_ERROR_NO_IDENTIFIER_FACTORY)
        """
        """
        UNKNOWN = cast("ContentCreationError", CONTENT_CREATION_ERROR_UNKNOWN)
        """
        Unknown.
        
        An unknown I/O error has occurred.
        """

else:

    from ooo.helper.enum_helper import UnoEnumMeta
    class ContentCreationError(metaclass=UnoEnumMeta, type_name="com.sun.star.ucb.ContentCreationError", name_space="com.sun.star.ucb"):
        """Dynamically created class that represents ``com.sun.star.ucb.ContentCreationError`` Enum. Class loosely mimics Enum"""
        pass

__all__ = ['ContentCreationError']
