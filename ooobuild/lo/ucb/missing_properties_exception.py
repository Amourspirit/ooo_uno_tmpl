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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class MissingPropertiesException(Exception_85530a09):
    """
    Exception Class

    This exception is used to indicate that there are properties missing.
    
    For example, to create a new resource, usually one ore more property values must be set prior to executing the command \"insert\", which makes the new resource persistent.

    See Also:
        `API MissingPropertiesException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1MissingPropertiesException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.MissingPropertiesException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.ucb.MissingPropertiesException'
    __pyunostruct__: str = 'com.sun.star.ucb.MissingPropertiesException'

    typeName: str = 'com.sun.star.ucb.MissingPropertiesException'
    """Literal Constant ``com.sun.star.ucb.MissingPropertiesException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, Properties: typing.Optional[typing.Tuple[str, ...]] = UNO_NONE) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Properties (typing.Tuple[str, ...], optional): Properties value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "Properties": Properties,
        }
        if kargs["Properties"] is UNO_NONE:
            kargs["Properties"] = None
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._properties = kwargs["Properties"]
        inst_keys = ('Properties',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def Properties(self) -> typing.Tuple[str, ...]:
        """
        contains the names of the missing properties.
        """
        return self._properties
    
    @Properties.setter
    def Properties(self, value: typing.Tuple[str, ...]) -> None:
        self._properties = value


__all__ = ['MissingPropertiesException']
