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
# Namespace: com.sun.star.form
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..container.x_index_container import XIndexContainer as XIndexContainer_1c040ebe

class XGridPeer(XInterface_8f010a43):
    """
    represents the window peer of a GridControl and allows you to set and retrieve the model data.
    
    Usually, the columns used are the columns as supplied by the grid control model.
    
    You should use this interface only if you know exactly what you are doing. Tampering with the columns of a grid control which is part of a complex form can really hurt...
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XGridPeer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XGridPeer.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.form.XGridPeer']

    def getColumns(self) -> 'XIndexContainer_1c040ebe':
        """
        retrieves the currently used column definitions of the peer.
        """
        ...
    def setColumns(self, aColumns: 'XIndexContainer_1c040ebe') -> None:
        """
        sets the column definition for the peer.
        """
        ...


