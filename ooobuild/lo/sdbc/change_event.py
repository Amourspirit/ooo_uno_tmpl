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
# Namespace: com.sun.star.sdbc
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class ChangeEvent(EventObject_a3d70b03):
    """
    Struct Class

    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API ChangeEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sdbc_1_1ChangeEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sdbc'
    __ooo_full_ns__: str = 'com.sun.star.sdbc.ChangeEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sdbc.ChangeEvent'
    """Literal Constant ``com.sun.star.sdbc.ChangeEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Action: typing.Optional[int] = 0, Rows: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Action (int, optional): Action value.
            Rows (int, optional): Rows value.
        """

        if isinstance(Source, ChangeEvent):
            oth: ChangeEvent = Source
            self.Source = oth.Source
            self.Action = oth.Action
            self.Rows = oth.Rows
            return

        kargs = {
            "Source": Source,
            "Action": Action,
            "Rows": Rows,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._action = kwargs["Action"]
        self._rows = kwargs["Rows"]
        inst_keys = ('Action', 'Rows')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Action(self) -> int:
        """
        indicates the type of change.
        """
        return self._action
    
    @Action.setter
    def Action(self, value: int) -> None:
        self._action = value

    @property
    def Rows(self) -> int:
        """
        indicates the number of rows affected by the change.
        """
        return self._rows
    
    @Rows.setter
    def Rows(self, value: int) -> None:
        self._rows = value


__all__ = ['ChangeEvent']
