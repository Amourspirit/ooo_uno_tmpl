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
# Namespace: com.sun.star.form
import typing
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_load_listener import XLoadListener as XLoadListener_bb200bda

class XLoadable(XInterface_8f010a43):
    """
    provides functionality to implement objects which may be loaded.
    
    The object is typically implemented by high-level objects which can connect to a data source.

    See Also:
        `API XLoadable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XLoadable.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.form'
    __ooo_full_ns__: str = 'com.sun.star.form.XLoadable'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.form.XLoadable'

    @abstractmethod
    def addLoadListener(self, aListener: 'XLoadListener_bb200bda') -> None:
        """
        adds the specified listener to receive load-related events
        """
        ...
    @abstractmethod
    def isLoaded(self) -> bool:
        """
        returns if the object is in loaded state.
        """
        ...
    @abstractmethod
    def load(self) -> None:
        """
        loads the data.
        
        If the data is already loaded (->isLoaded), then the method returns silently. In this case, you should use ->reload.
        """
        ...
    @abstractmethod
    def reload(self) -> None:
        """
        does a smart refresh of the object.
        
        The final state will be the same as if unload and load were called, but reload is the more efficient way to do the same. If the object isn't loaded, nothing happens.
        """
        ...
    @abstractmethod
    def removeLoadListener(self, aListener: 'XLoadListener_bb200bda') -> None:
        """
        removes the specified listener.
        """
        ...
    @abstractmethod
    def unload(self) -> None:
        """
        unloads the data.
        """
        ...

__all__ = ['XLoadable']

