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
# Namespace: com.sun.star.awt
from __future__ import annotations
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_adjustment_listener import XAdjustmentListener as XAdjustmentListener_fdfc0e11

class XSpinValue(XInterface_8f010a43):
    """
    gives access to the value and settings of a control which is associated with a spinnable value.

    See Also:
        `API XSpinValue <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XSpinValue.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt'
    __ooo_full_ns__: str = 'com.sun.star.awt.XSpinValue'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.XSpinValue'

    @abstractmethod
    def addAdjustmentListener(self, listener: XAdjustmentListener_fdfc0e11) -> None:
        """
        registers an adjustment event listener.
        """
        ...
    @abstractmethod
    def getMaximum(self) -> int:
        """
        returns the currently set maximum value of the control
        """
        ...
    @abstractmethod
    def getMinimum(self) -> int:
        """
        returns the currently set minimum value of the control
        """
        ...
    @abstractmethod
    def getOrientation(self) -> int:
        """
        returns the current orientation of the control
        """
        ...
    @abstractmethod
    def getSpinIncrement(self) -> int:
        """
        returns the value by which the current value of the control should be incremented or decremented upon spinning.
        """
        ...
    @abstractmethod
    def getValue(self) -> int:
        """
        returns the current value of the control.
        """
        ...
    @abstractmethod
    def removeAdjustmentListener(self, listener: XAdjustmentListener_fdfc0e11) -> None:
        """
        unregisters an adjustment event listener.
        """
        ...
    @abstractmethod
    def setMaximum(self, maxValue: int) -> None:
        """
        sets the maximum value which can be set on the control
        """
        ...
    @abstractmethod
    def setMinimum(self, minValue: int) -> None:
        """
        sets the minimum value which can be set on the control
        """
        ...
    @abstractmethod
    def setOrientation(self, orientation: int) -> None:
        """
        controls the orientation of the control

        Raises:
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
        ...
    @abstractmethod
    def setSpinIncrement(self, spinIncrement: int) -> None:
        """
        sets the value by which the current value of the control should be incremented or decremented upon spinning.
        """
        ...
    @abstractmethod
    def setValue(self, value: int) -> None:
        """
        sets the current value of the control
        """
        ...
    @abstractmethod
    def setValues(self, minValue: int, maxValue: int, currentValue: int) -> None:
        """
        sets the value and value range of the control
        """
        ...

__all__ = ['XSpinValue']

