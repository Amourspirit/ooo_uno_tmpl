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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.style
from __future__ import annotations
import typing

from ..container.x_named import XNamed as XNamed_a6520b08


class XStyle(XNamed_a6520b08):
    """
    specifies a template for a style (aka style sheet).

    See Also:
        `API XStyle <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1style_1_1XStyle.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.style.XStyle'

    def getParentStyle(self) -> str:
        """
        """
        ...
    def isInUse(self) -> bool:
        """
        """
        ...
    def isUserDefined(self) -> bool:
        """
        identifies a style as defined by the user.
        """
        ...
    def setParentStyle(self, aParentStyle: str) -> None:
        """
        sets the name of the parent style.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...


