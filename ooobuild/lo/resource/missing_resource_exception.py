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
# Namespace: com.sun.star.resource
# Libre Office Version: 2024.2
import typing
from ..uno.runtime_exception import RuntimeException as RuntimeException_d7390ced
from ..uno.x_interface import XInterface as XInterface_8f010a43

class MissingResourceException(RuntimeException_d7390ced):
    """
    Exception Class

    is used to signal that a resource is missing.

    See Also:
        `API MissingResourceException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1resource_1_1MissingResourceException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.resource'
    __ooo_full_ns__: str = 'com.sun.star.resource.MissingResourceException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.resource.MissingResourceException'
    __pyunostruct__: str = 'com.sun.star.resource.MissingResourceException'

    typeName: str = 'com.sun.star.resource.MissingResourceException'
    """Literal Constant ``com.sun.star.resource.MissingResourceException``"""

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


__all__ = ['MissingResourceException']

