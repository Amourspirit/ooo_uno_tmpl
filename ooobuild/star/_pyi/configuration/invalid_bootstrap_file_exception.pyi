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
# Namespace: com.sun.star.configuration
# Libre Office Version: 7.3
from typing_extensions import Literal
from ooo.oenv.env_const import UNO_NONE
import typing
from .cannot_load_configuration_exception import CannotLoadConfigurationException as CannotLoadConfigurationException_b325176a
from ..uno.x_interface import XInterface as XInterface_8f010a43

class InvalidBootstrapFileException(CannotLoadConfigurationException_b325176a):
    """
    Exception Class

    is thrown when creating a configuration provider fails because a bootstrap file needed to locate the configuration contains invalid data

    See Also:
        `API InvalidBootstrapFileException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1configuration_1_1InvalidBootstrapFileException.html>`_
    """

    typeName: Literal['com.sun.star.configuration.InvalidBootstrapFileException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., BootstrapFileURL: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            BootstrapFileURL (str, optional): BootstrapFileURL value.
        """
    @property
    def BootstrapFileURL(self) -> str:
        """
        the URL of the bootstrap file that is invalid
        """


__all__ = ['InvalidBootstrapFileException']

