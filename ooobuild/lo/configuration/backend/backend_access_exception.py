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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.configuration.backend
# Libre Office Version: 7.2
import typing
from ...lang.wrapped_target_exception import WrappedTargetException as WrappedTargetException_38ae0f93
from ...uno.x_interface import XInterface as XInterface_8f010a43

class BackendAccessException(WrappedTargetException_38ae0f93):
    """
    Exception Class

    Generic exception thrown when physical access to an underlying backend fails.
    
    Wraps an exception that originates in the underlying access layer.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API BackendAccessException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1configuration_1_1backend_1_1BackendAccessException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.configuration.backend'
    __ooo_full_ns__: str = 'com.sun.star.configuration.backend.BackendAccessException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.configuration.backend.BackendAccessException'
    __pyunostruct__: str = 'com.sun.star.configuration.backend.BackendAccessException'

    typeName: str = 'com.sun.star.configuration.backend.BackendAccessException'
    """Literal Constant ``com.sun.star.configuration.backend.BackendAccessException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, TargetException: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            TargetException (object, optional): TargetException value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "TargetException": TargetException,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        super()._init(**kwargs)


__all__ = ['BackendAccessException']

