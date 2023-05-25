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
# Namespace: com.sun.star.sdbc
from __future__ import annotations
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XWarningsSupplier(XInterface_8f010a43):
    """
    should be implemented of objects which may report warnings or non critical errors.

    See Also:
        `API XWarningsSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XWarningsSupplier.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.XWarningsSupplier'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbc.XWarningsSupplier'

    @abstractmethod
    def clearWarnings(self) -> None:
        """
        clears all warnings reported for the object implementing the interface.
        
        After a call to this method, the method com.sun.star.sdbc.XWarningsSupplier.getWarnings() returns VOID until a new warning is reported for the object.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    @abstractmethod
    def getWarnings(self) -> object:
        """
        returns the first warning reported by calls on an object that supports the usage of warnings.
        
        Note: Subsequent warnings will be chained to this com.sun.star.sdbc.SQLWarning.

        Raises:
            SQLException: ``SQLException``
        """
        ...

__all__ = ['XWarningsSupplier']


