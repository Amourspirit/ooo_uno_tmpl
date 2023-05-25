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
# Namespace: com.sun.star.mozilla
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from com.sun.star.mozilla.MozillaProductType import MozillaProductTypeProto  # type: ignore


class XProfileDiscover(XInterface_8f010a43):
    """
    is the interface used to list and get information for Mozilla/Thunderbird profiles

    See Also:
        `API XProfileDiscover <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1mozilla_1_1XProfileDiscover.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.mozilla.XProfileDiscover'

    def getDefaultProfile(self, product: MozillaProductTypeProto) -> str:
        """
        attempts to get the default profile name for the given product.
        """
        ...
    def getProfileCount(self, product: MozillaProductTypeProto) -> int:
        """
        attempts to get the profiles count.
        """
        ...
    def getProfileExists(self, product: MozillaProductTypeProto, profileName: str) -> bool:
        """
        return true if the given profile exists
        """
        ...
    def getProfileList(self, product: MozillaProductTypeProto, list: typing.Tuple[str, ...]) -> int:
        """
        attempts to get the profile list for the given product.

        * ``list`` is an out direction argument.
        """
        ...
    def getProfilePath(self, product: MozillaProductTypeProto, profileName: str) -> str:
        """
        attempts to get the full path for the given profile.
        """
        ...
    def isProfileLocked(self, product: MozillaProductTypeProto, profileName: str) -> bool:
        """
        attempts to get whether profile is locked by other applications.
        """
        ...

