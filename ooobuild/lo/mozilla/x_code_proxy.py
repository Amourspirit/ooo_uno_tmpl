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
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from com.sun.star.mozilla.MozillaProductType import MozillaProductTypeProto

class XCodeProxy(XInterface_8f010a43):
    """
    is the interface to run Mozilla XPCOM code to run Mozilla XPCOM code in OOo,you should first implement this interface, then pass this object to xProxyRunner->Run

    See Also:
        `API XCodeProxy <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1mozilla_1_1XCodeProxy.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.mozilla'
    __ooo_full_ns__: str = 'com.sun.star.mozilla.XCodeProxy'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.mozilla.XCodeProxy'

    @abstractmethod
    def getProductType(self) -> MozillaProductTypeProto:
        """
        which Mozilla product this code is write for
        """
        ...
    @abstractmethod
    def getProfileName(self) -> str:
        """
        which Mozilla profile this code will use
        """
        ...
    @abstractmethod
    def run(self) -> int:
        """
        all Mozilla XPCOM code must be called in run() or functions called by run()
        """
        ...

__all__ = ['XCodeProxy']

