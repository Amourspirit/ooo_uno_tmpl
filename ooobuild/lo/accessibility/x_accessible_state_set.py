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
# Namespace: com.sun.star.accessibility
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XAccessibleStateSet(XInterface_8f010a43):
    """
    Implement this interface to represent a set of states.
    
    The interface XAccessibleStateSet represents a set of states of an accessible object. It can hold any combination of states defined by the constants collection AccessibleStateType.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XAccessibleStateSet <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleStateSet.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.accessibility'
    __ooo_full_ns__: str = 'com.sun.star.accessibility.XAccessibleStateSet'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.accessibility.XAccessibleStateSet'

    @abstractmethod
    def contains(self, aState: int) -> bool:
        """
        Checks if the given state is a member of the state set of the called object.
        """
    @abstractmethod
    def containsAll(self, aStateSet: 'typing.Tuple[int, ...]') -> bool:
        """
        Checks if all of the given states are in the state set of the called object.
        """
    @abstractmethod
    def getStates(self) -> 'typing.Tuple[int, ...]':
        """
        Get all currently set states as a sequence of state ids.
        
        The purpose of this function is to reduce the communication between accessibility objects and AT. Without this function an AT-Tool had to call contains() for every state type. Now a single call is sufficient.
        """
    @abstractmethod
    def isEmpty(self) -> bool:
        """
        Checks whether the current state set is empty.
        """

__all__ = ['XAccessibleStateSet']
