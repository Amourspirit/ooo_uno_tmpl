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
# Namespace: com.sun.star.sdb
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class DatabaseRegistrationEvent(EventObject_a3d70b03):
    """
    Struct Class

    describes a change in a database registration
    
    **since**
    
        LibreOffice 3.3

    See Also:
        `API DatabaseRegistrationEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sdb_1_1DatabaseRegistrationEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdb'
    __ooo_full_ns__: str = 'com.sun.star.sdb.DatabaseRegistrationEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sdb.DatabaseRegistrationEvent'
    """Literal Constant ``com.sun.star.sdb.DatabaseRegistrationEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Name: typing.Optional[str] = '', OldLocation: typing.Optional[str] = '', NewLocation: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Name (str, optional): Name value.
            OldLocation (str, optional): OldLocation value.
            NewLocation (str, optional): NewLocation value.
        """

        if isinstance(Source, DatabaseRegistrationEvent):
            oth: DatabaseRegistrationEvent = Source
            self.Source = oth.Source
            self.Name = oth.Name
            self.OldLocation = oth.OldLocation
            self.NewLocation = oth.NewLocation
            return

        kargs = {
            "Source": Source,
            "Name": Name,
            "OldLocation": OldLocation,
            "NewLocation": NewLocation,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._name = kwargs["Name"]
        self._old_location = kwargs["OldLocation"]
        self._new_location = kwargs["NewLocation"]
        inst_keys = ('Name', 'OldLocation', 'NewLocation')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Name(self) -> str:
        """
        is the name of the database registration affected by the event
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def OldLocation(self) -> str:
        """
        is the old location of the database which is affected by the event
        """
        return self._old_location
    
    @OldLocation.setter
    def OldLocation(self, value: str) -> None:
        self._old_location = value

    @property
    def NewLocation(self) -> str:
        """
        is the new location of the database which is affected by the event
        """
        return self._new_location
    
    @NewLocation.setter
    def NewLocation(self, value: str) -> None:
        self._new_location = value


__all__ = ['DatabaseRegistrationEvent']