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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.configuration
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from ..uno.runtime_exception import RuntimeException as RuntimeException_d7390ced
from ..uno.x_interface import XInterface as XInterface_8f010a43

class CorruptedConfigurationException(RuntimeException_d7390ced):
    """
    Exception Class

    This exception is thrown in case a configuration does not exists or contains corrupt data.
    
    This exception must be used as base exception to derive specialized exceptions from it which identify a concrete error case.
    
    **since**
    
        OOo 2.3

    See Also:
        `API CorruptedConfigurationException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1configuration_1_1CorruptedConfigurationException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.configuration'
    __ooo_full_ns__: str = 'com.sun.star.configuration.CorruptedConfigurationException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.configuration.CorruptedConfigurationException'
    __pyunostruct__: str = 'com.sun.star.configuration.CorruptedConfigurationException'

    typeName: str = 'com.sun.star.configuration.CorruptedConfigurationException'
    """Literal Constant ``com.sun.star.configuration.CorruptedConfigurationException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, Details: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Details (str, optional): Details value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "Details": Details,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._details = kwargs["Details"]
        inst_keys = ('Details',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def Details(self) -> str:
        """
        Instead of the message part of an exception, this value describe the type of corruption more in detail.
        """
        return self._details
    
    @Details.setter
    def Details(self, value: str) -> None:
        self._details = value


__all__ = ['CorruptedConfigurationException']

