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
# Namespace: com.sun.star.accessibility
import typing

import uno
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
    __pyunointerface__: str = 'com.sun.star.accessibility.XAccessibleStateSet'

    def contains(self, aState: int) -> bool:
        """
        Checks if the given state is a member of the state set of the called object.
        """
        ...
    def containsAll(self, aStateSet: uno.ByteSequence) -> bool:
        """
        Checks if all of the given states are in the state set of the called object.
        """
        ...
    def getStates(self) -> uno.ByteSequence:
        """
        Get all currently set states as a sequence of state ids.
        
        The purpose of this function is to reduce the communication between accessibility objects and AT. Without this function an AT-Tool had to call contains() for every state type. Now a single call is sufficient.
        """
        ...
    def isEmpty(self) -> bool:
        """
        Checks whether the current state set is empty.
        """
        ...

