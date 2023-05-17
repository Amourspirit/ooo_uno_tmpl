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
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..sdbc.x_prepared_statement import XPreparedStatement as XPreparedStatement_fbc80de4


class XCommandPreparation(XInterface_8f010a43):
    """
    is used for preparation of commands.
    
    A command could be a table, query, or any kind of SQL statement prepared by the user.

    See Also:
        `API XCommandPreparation <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1XCommandPreparation.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sdb.XCommandPreparation']

    def prepareCommand(self, command: str, commandType: int) -> 'XPreparedStatement_fbc80de4':
        """
        creates a com.sun.star.sdbc.PreparedStatement object for sending parameterized SQL statements to the database.
        
        A SQL statement with or without IN parameters can be pre-compiled and stored in a PreparedStatement object. This object can then be used to efficiently execute this statement multiple times.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...


