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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.sdbc
from abc import abstractmethod
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XRef(XInterface_8f010a43):
    """
    is the reference to a SQL structured type value in the database.
    
    A Ref can be saved to persistent storage. A Ref is dereferenced by passing it as a parameter to a SQL statement and executing the statement.

    See Also:
        `API XRef <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XRef.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.XRef'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.sdbc.XRef'

    @abstractmethod
    def getBaseTypeName(self) -> str:
        """
        gets the fully-qualified SQL structured type name of the referenced item.

        Raises:
            SQLException: ``SQLException``
        """

__all__ = ['XRef']
