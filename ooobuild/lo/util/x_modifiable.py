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
from .x_modify_broadcaster import XModifyBroadcaster as XModifyBroadcaster_fd990df0

class XModifiable(XModifyBroadcaster_fd990df0):
    """
    makes the modify state of the object accessible.
    
    Additionally, it makes it possible to register listener objects, which get notification whenever the status or content of the object changes.

    See Also:
        `API XModifiable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XModifiable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.util'
    __ooo_full_ns__: str = 'com.sun.star.util.XModifiable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.util.XModifiable'

    @abstractmethod
    def isModified(self) -> bool:
        """
        The modification is always in relation to a certain state (i.e., the initial, loaded, or last stored version).
        """
    @abstractmethod
    def setModified(self, bModified: bool) -> None:
        """
        sets the status of the modified-flag from outside of the object.

        Raises:
            com.sun.star.beans.PropertyVetoException: ``PropertyVetoException``
        """

__all__ = ['XModifiable']

