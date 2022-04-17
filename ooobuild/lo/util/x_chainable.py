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
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XChainable(XInterface_8f010a43):
    """
    enables the object to be a member of a chain.

    See Also:
        `API XChainable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XChainable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.XChainable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.util.XChainable'

    @abstractmethod
    def getPredecessor(self) -> 'XChainable':
        """
        """
    @abstractmethod
    def getSuccessor(self) -> 'XChainable':
        """
        """
    @abstractmethod
    def isChainable(self, xChainable: 'XChainable') -> bool:
        """
        checks if the specified object can be linked to this.
        """
    @abstractmethod
    def setSuccessor(self, xChainable: 'XChainable') -> None:
        """
        connects the specified object to this object as the successor in a chain.
        
        This implies that this object will become the predecessor of xChainable.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """

__all__ = ['XChainable']

