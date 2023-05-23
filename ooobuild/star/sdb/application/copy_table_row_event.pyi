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
# Namespace: com.sun.star.sdb.application
# Libre Office Version: 7.4
from ...lang.event_object import EventObject as EventObject_a3d70b03
from ...uno.x_interface import XInterface as XInterface_8f010a43
import typing
from ...sdbc.x_result_set import XResultSet as XResultSet_98e30aa7


class CopyTableRowEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies an event happening while copying table data between databases.
    
    Whenever this event is fired to an XCopyTableListener, com.sun.star.lang.EventObject.Source contains the wizard instance which actually does the copying.

    See Also:
        `API CopyTableRowEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sdb_1_1application_1_1CopyTableRowEvent.html>`_
    """
    typeName: str = 'com.sun.star.sdb.application.CopyTableRowEvent'

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., SourceData: typing.Optional[XResultSet_98e30aa7] = ..., Error: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            SourceData (XResultSet, optional): SourceData value.
            Error (object, optional): Error value.
        """
        ...

    @property
    def SourceData(self) -> XResultSet_98e30aa7:
        """
        contains the result set which is being copied by the wizard currently.
        """
        ...
    @SourceData.setter
    def SourceData(self, value: XResultSet_98e30aa7) -> None:
        ...
    @property
    def Error(self) -> object:
        """
        denotes the error which happened while copying the data.
        
        Usually, this contains an instance of com.sun.star.sdbc.SQLException.
        """
        ...
    @Error.setter
    def Error(self, value: object) -> None:
        ...
