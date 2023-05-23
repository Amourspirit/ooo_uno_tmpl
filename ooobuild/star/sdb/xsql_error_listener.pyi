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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdb
import typing

from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .sql_error_event import SQLErrorEvent as SQLErrorEvent_ac5f0b3d


class XSQLErrorListener(XEventListener_c7230c4a):
    """
    the listener interface for receiving \"errorOccured\" events posted by any database object.

    See Also:
        `API XSQLErrorListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1XSQLErrorListener.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sdb.XSQLErrorListener'

    def errorOccured(self, aEvent: 'SQLErrorEvent_ac5f0b3d') -> None:
        """
        invoked when a database error occurs, just before a com.sun.star.sdbc.SQLException is thrown to the application.
        """
        ...

