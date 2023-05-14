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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sdb
# Libre Office Version: 7.4
from typing_extensions import Literal
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
    typeName: Literal['com.sun.star.sdb.DatabaseRegistrationEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., Name: typing.Optional[str] = ..., OldLocation: typing.Optional[str] = ..., NewLocation: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Name (str, optional): Name value.
            OldLocation (str, optional): OldLocation value.
            NewLocation (str, optional): NewLocation value.
        """
        ...


    @property
    def Name(self) -> str:
        """
        is the name of the database registration affected by the event
        """
        ...


    @property
    def OldLocation(self) -> str:
        """
        is the old location of the database which is affected by the event
        """
        ...


    @property
    def NewLocation(self) -> str:
        """
        is the new location of the database which is affected by the event
        """
        ...


