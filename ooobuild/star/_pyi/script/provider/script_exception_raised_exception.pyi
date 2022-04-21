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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.script.provider
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing
from .script_error_raised_exception import ScriptErrorRaisedException as ScriptErrorRaisedException_585f15bc
from ...uno.x_interface import XInterface as XInterface_8f010a43

class ScriptExceptionRaisedException(ScriptErrorRaisedException_585f15bc):
    """
    Exception Class

    is a checked exception that represents the detail of an exception thrown by a LanguageScriptProvider whilst executing a script

    See Also:
        `API ScriptExceptionRaisedException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1script_1_1provider_1_1ScriptExceptionRaisedException.html>`_
    """

    typeName: Literal['com.sun.star.script.provider.ScriptExceptionRaisedException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., scriptName: typing.Optional[str] = ..., language: typing.Optional[str] = ..., lineNum: typing.Optional[int] = ..., exceptionType: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            scriptName (str, optional): scriptName value.
            language (str, optional): language value.
            lineNum (int, optional): lineNum value.
            exceptionType (str, optional): exceptionType value.
        """
    @property
    def exceptionType(self) -> str:
        """
        Name of script where error occurred.
        """


__all__ = ['ScriptExceptionRaisedException']

