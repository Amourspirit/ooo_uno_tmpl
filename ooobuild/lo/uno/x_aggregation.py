# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.uno
from __future__ import annotations
from abc import abstractmethod
from .x_interface import XInterface as XInterface_8f010a43

class XAggregation(XInterface_8f010a43):
    """
    Objects which implement this interface can become aggregates of a delegator.
    
    That means if an object \"A\" aggregates \"B\", \"A\" can provide all or some of the interfaces of \"B\". Whenever the method XInterface.queryInterface() is called on either of the objects, the call will be forwarded to object \"A\". Object \"A\" now can determine whether to use the interfaces of \"A\" or \"B\" or neither. Actually, any number of aggregates can be used, even nested ones (aggregated objects which are delegators by themselves).
    
    The following rules are to be observed:
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XAggregation <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1uno_1_1XAggregation.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.uno'
    __ooo_full_ns__: str = 'com.sun.star.uno.XAggregation'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.uno.XAggregation'

    @abstractmethod
    def queryAggregation(self, aType: object) -> object:
        """
        is similar to XInterface.queryInterface(), but it is to be processed directly without being forwarded to the delegator.
        
        This method is only called from within an implementation of XInterface.queryInterface() or XAggregation.queryAggregation(). This method is to be called by the delegator if it does not implement the interface itself. An object which got aggregated cannot depend on getting its own interface when it calls the method XInterface.queryInterface().
        """
        ...
    @abstractmethod
    def setDelegator(self, pDelegator: XInterface_8f010a43) -> None:
        """
        sets the object to which all calls to the method XInterface.queryInterface() have to be forwarded.
        """
        ...

__all__ = ['XAggregation']

