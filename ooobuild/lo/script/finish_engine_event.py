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
# Namespace: com.sun.star.script
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .finish_reason import FinishReason as FinishReason_ca230c66


class FinishEngineEvent(EventObject_a3d70b03):
    """
    Struct Class

    event contains the reasons and the data for the XEngineListener.finished() method.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API FinishEngineEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1script_1_1FinishEngineEvent.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.script'
    __ooo_full_ns__: str = 'com.sun.star.script.FinishEngineEvent'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.script.FinishEngineEvent'
    """Literal Constant ``com.sun.star.script.FinishEngineEvent``"""

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = None, Finish: typing.Optional[FinishReason_ca230c66] = FinishReason_ca230c66.OK, ErrorMessage: typing.Optional[str] = '', Return: typing.Optional[object] = None) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Finish (FinishReason, optional): Finish value.
            ErrorMessage (str, optional): ErrorMessage value.
            Return (object, optional): Return value.
        """

        if isinstance(Source, FinishEngineEvent):
            oth: FinishEngineEvent = Source
            self.Source = oth.Source
            self.Finish = oth.Finish
            self.ErrorMessage = oth.ErrorMessage
            self.Return = oth.Return
            return

        kargs = {
            "Source": Source,
            "Finish": Finish,
            "ErrorMessage": ErrorMessage,
            "Return": Return,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._finish = kwargs["Finish"]
        self._error_message = kwargs["ErrorMessage"]
        self._return = kwargs["Return"]
        inst_keys = ('Finish', 'ErrorMessage', 'Return')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def Finish(self) -> FinishReason_ca230c66:
        """
        specifies why the script terminates.
        """
        return self._finish

    @Finish.setter
    def Finish(self, value: FinishReason_ca230c66) -> None:
        self._finish = value

    @property
    def ErrorMessage(self) -> str:
        """
        error message.
        
        Only valid if Reason is RuntimeError or CompileError.
        """
        return self._error_message

    @ErrorMessage.setter
    def ErrorMessage(self, value: str) -> None:
        self._error_message = value

    @property
    def Return(self) -> object:
        """
        contains the return value.
        
        This field is only valid if FinishEngineEvent.Finish is FinishReason.OK.
        """
        return self._return

    @Return.setter
    def Return(self, value: object) -> None:
        self._return = value


__all__ = ['FinishEngineEvent']
