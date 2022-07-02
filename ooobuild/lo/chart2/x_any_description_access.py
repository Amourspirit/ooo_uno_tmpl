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
# Libre Office Version: 7.2
# Namespace: com.sun.star.chart2
import typing
from abc import abstractmethod
from ..chart.x_complex_description_access import XComplexDescriptionAccess as XComplexDescriptionAccess_7a521120

class XAnyDescriptionAccess(XComplexDescriptionAccess_7a521120):
    """
    Offers any access to column and row descriptions.
    
    This allows to set date values as categories.
    
    Can be obtained from interface XChartDocument via method getData().
    
    **since**
    
        OOo 3.4

    See Also:
        `API XAnyDescriptionAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1XAnyDescriptionAccess.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.chart2'
    __ooo_full_ns__: str = 'com.sun.star.chart2.XAnyDescriptionAccess'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.chart2.XAnyDescriptionAccess'

    @abstractmethod
    def getAnyColumnDescriptions(self) -> 'typing.Tuple[typing.Tuple[object, ...], ...]':
        """
        retrieves the descriptions for all columns.
        """
        ...
    @abstractmethod
    def getAnyRowDescriptions(self) -> 'typing.Tuple[typing.Tuple[object, ...], ...]':
        """
        retrieves the descriptions for all rows.
        """
        ...
    @abstractmethod
    def setAnyColumnDescriptions(self, rColumnDescriptions: 'typing.Tuple[typing.Tuple[object, ...], ...]') -> None:
        """
        sets the descriptions for all columns.
        """
        ...
    @abstractmethod
    def setAnyRowDescriptions(self, rRowDescriptions: 'typing.Tuple[typing.Tuple[object, ...], ...]') -> None:
        """
        sets the descriptions for all rows.
        """
        ...

__all__ = ['XAnyDescriptionAccess']

