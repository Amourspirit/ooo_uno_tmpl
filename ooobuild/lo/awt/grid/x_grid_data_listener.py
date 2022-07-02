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
# Libre Office Version: 7.2
# Namespace: com.sun.star.awt.grid
import typing
from abc import abstractmethod
from ...lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .grid_data_event import GridDataEvent as GridDataEvent_ebcb0d2a

class XGridDataListener(XEventListener_c7230c4a):
    """
    An instance of this interface is used by the XGridDataModel to get notifications about data model changes.
    
    Usually you must not implement this interface yourself, but you must notify it correctly if you implement the XGridDataModel yourself
    
    .
    
    **since**
    
        OOo 3.3

    See Also:
        `API XGridDataListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1grid_1_1XGridDataListener.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.awt.grid'
    __ooo_full_ns__: str = 'com.sun.star.awt.grid.XGridDataListener'
    __ooo_type_name__: str = 'interface'
    __pyunointerface__: str = 'com.sun.star.awt.grid.XGridDataListener'

    @abstractmethod
    def dataChanged(self, Event: 'GridDataEvent_ebcb0d2a') -> None:
        """
        is called when existing data in a grid control's data model has been modified.
        """
        ...
    @abstractmethod
    def rowHeadingChanged(self, Event: 'GridDataEvent_ebcb0d2a') -> None:
        """
        is called when the title of one or more rows changed.
        """
        ...
    @abstractmethod
    def rowsInserted(self, Event: 'GridDataEvent_ebcb0d2a') -> None:
        """
        is called when one or more rows of data have been inserted into a grid control's data model.
        """
        ...
    @abstractmethod
    def rowsRemoved(self, Event: 'GridDataEvent_ebcb0d2a') -> None:
        """
        is called when one or more rows of data have been removed from a grid control's data model.
        """
        ...

__all__ = ['XGridDataListener']

