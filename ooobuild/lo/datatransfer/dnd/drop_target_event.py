# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.datatransfer.dnd
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
from ...lang.event_object import EventObject as EventObject_a3d70b03
from ...uno.x_interface import XInterface as XInterface_8f010a43
import typing


class DropTargetEvent(EventObject_a3d70b03):
    """
    Struct Class

    This class is the base class for DropTargetDragEvent and DropTargetDropEvent.
    
    To access the XDropTarget that originated this event, use the com.sun.star.lang.EventObject.Source member of this object.

    See Also:
        `API DropTargetEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1DropTargetEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.datatransfer.dnd'
    __ooo_full_ns__: str = 'com.sun.star.datatransfer.dnd.DropTargetEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.datatransfer.dnd.DropTargetEvent'
    """Literal Constant ``com.sun.star.datatransfer.dnd.DropTargetEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Dummy: typing.Optional[int] = 0) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Dummy (int, optional): Dummy value.
        """

        if isinstance(Source, DropTargetEvent):
            oth: DropTargetEvent = Source
            self.Source = oth.Source
            self.Dummy = oth.Dummy
            return

        kargs = {
            "Source": Source,
            "Dummy": Dummy,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._dummy = kwargs["Dummy"]
        inst_keys = ('Dummy',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Dummy(self) -> int:
        """
        UNO specification does not allow empty struct definitions.
        """
        return self._dummy

    @Dummy.setter
    def Dummy(self, value: int) -> None:
        self._dummy = value


__all__ = ['DropTargetEvent']
