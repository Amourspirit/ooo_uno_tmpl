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
# Namespace: com.sun.star.embed
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73


class XCommonEmbedPersist(XInterface_8f010a43):
    """
    specifies common implementation for embedded objects and links persistence.

    See Also:
        `API XCommonEmbedPersist <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XCommonEmbedPersist.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.embed.XCommonEmbedPersist'

    def isReadonly(self) -> bool:
        """
        allows to detect if the data store is read-only.

        Raises:
            com.sun.star.embed.WrongStateException: ``WrongStateException``
        """
        ...
    def reload(self, aMediaArgs: typing.Tuple[PropertyValue_c9610c73, ...], aObjectArgs: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        """
        lets the object or the link reload itself.
        
        If the object has persistence it will be reloaded from its persistent entry.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.embed.WrongStateException: ``WrongStateException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    def storeOwn(self) -> None:
        """
        lets the object or the link store itself.

        Raises:
            com.sun.star.embed.WrongStateException: ``WrongStateException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...


