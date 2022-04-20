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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .x_spreadsheet import XSpreadsheet as XSpreadsheet_bc910bf1


class ActivationEvent(EventObject_a3d70b03):
    """
    Struct Class

    describes a change of the active sheet.
    
    The new active sheet is given with this event.
    
    **since**
    
        OOo 2.0

    See Also:
        `API ActivationEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1ActivationEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.ActivationEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.sheet.ActivationEvent'
    """Literal Constant ``com.sun.star.sheet.ActivationEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, ActiveSheet: typing.Optional[XSpreadsheet_bc910bf1] = None) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            ActiveSheet (XSpreadsheet, optional): ActiveSheet value.
        """

        if isinstance(Source, ActivationEvent):
            oth: ActivationEvent = Source
            self.Source = oth.Source
            self.ActiveSheet = oth.ActiveSheet
            return

        kargs = {
            "Source": Source,
            "ActiveSheet": ActiveSheet,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._active_sheet = kwargs["ActiveSheet"]
        inst_keys = ('ActiveSheet',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def ActiveSheet(self) -> XSpreadsheet_bc910bf1:
        """
        specifies the new active Spreadsheet.
        """
        return self._active_sheet
    
    @ActiveSheet.setter
    def ActiveSheet(self, value: XSpreadsheet_bc910bf1) -> None:
        self._active_sheet = value


__all__ = ['ActivationEvent']
