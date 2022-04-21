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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.io
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class DataTransferEvent(EventObject_a3d70b03):
    """
    Struct Class

    is broadcast by a filter.

    See Also:
        `API DataTransferEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1io_1_1DataTransferEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.io'
    __ooo_full_ns__: str = 'com.sun.star.io.DataTransferEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.io.DataTransferEvent'
    """Literal Constant ``com.sun.star.io.DataTransferEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, aException: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            aException (object, optional): aException value.
        """

        if isinstance(Source, DataTransferEvent):
            oth: DataTransferEvent = Source
            self.Source = oth.Source
            self.aException = oth.aException
            return

        kargs = {
            "Source": Source,
            "aException": aException,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._a_exception = kwargs["aException"]
        inst_keys = ('aException',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def aException(self) -> object:
        """
        specifies an occurred exception.
        """
        return self._a_exception
    
    @aException.setter
    def aException(self, value: object) -> None:
        self._a_exception = value


__all__ = ['DataTransferEvent']
