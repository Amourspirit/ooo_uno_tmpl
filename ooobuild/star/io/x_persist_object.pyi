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
# Namespace: com.sun.star.io
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_object_input_stream import XObjectInputStream as XObjectInputStream_dfb60d0b
    from .x_object_output_stream import XObjectOutputStream as XObjectOutputStream_ee190d8c


class XPersistObject(XInterface_8f010a43):
    """
    allows to make UNO objects persistent
    
    Every UNO object, that wants to be serializable, should implement this interface. The object stores stores itself, when the write method is called.
    
    The object needs to be created before it deserializes itself again (by using the read method). Therefore it must be creatable by name via a factory, which is in general the global service manager. The create and read mechanism is implemented by the com.sun.star.io.ObjectInputStream.
    
    The serialization format (the series of strings, integers, objects) must be specified at the specification of the concrete service.
    
    The interface does not support any special versioning mechanism.

    See Also:
        `API XPersistObject <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XPersistObject.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.io.XPersistObject'

    def getServiceName(self) -> str:
        """
        gives the service name of the object
        
        This name is used to create such an object by a factory during deserialization.
        """
        ...
    def read(self, InStream: XObjectInputStream_dfb60d0b) -> None:
        """
        reads all the persistent data of the object from the stream.
        
        In case other XPersistObjects are read from the stream, the implementation uses a factory to create these objects (in general the global service manager).
        
        The implementation must read the data in the order documented at the service specification.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def write(self, OutStream: XObjectOutputStream_ee190d8c) -> None:
        """
        writes all the persistent data of the object to the stream.
        
        The implementation must write the data in the order documented in the service specification.

        Raises:
            com.sun.star.io.IOException: ``IOException``
        """
        ...



