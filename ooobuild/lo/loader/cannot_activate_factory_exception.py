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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.loader
# Libre Office Version: 2024.2
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class CannotActivateFactoryException(Exception_85530a09):
    """
    Exception Class

    indicates an error during component activation
    
    This exception is thrown when an application tries to activate a component factory using the XImplementationLoader.activate() method, but the component factory can not be activated.
    
    Possible reasons for this error is a missing shared library or .jar file, a badly linked library, a wrong LD_LIBRARY_PATH or PATH, an incomplete classpath, or a missing java installation. The Message should contain some more detailed explanations.

    See Also:
        `API CannotActivateFactoryException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1loader_1_1CannotActivateFactoryException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.loader'
    __ooo_full_ns__: str = 'com.sun.star.loader.CannotActivateFactoryException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.loader.CannotActivateFactoryException'
    __pyunostruct__: str = 'com.sun.star.loader.CannotActivateFactoryException'

    typeName: str = 'com.sun.star.loader.CannotActivateFactoryException'
    """Literal Constant ``com.sun.star.loader.CannotActivateFactoryException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        super()._init(**kwargs)


__all__ = ['CannotActivateFactoryException']

