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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.util
from typing_extensions import Literal
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XProtectable(XInterface_8f010a43):
    """
    makes it possible to protect objects from modifications.

    See Also:
        `API XProtectable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XProtectable.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.util.XProtectable']

    def isProtected(self) -> bool:
        """
        """
        ...
    def protect(self, aPassword: str) -> None:
        """
        activates the protection.
        """
        ...
    def unprotect(self, aPassword: str) -> None:
        """
        removes the protection.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...


