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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.script
from __future__ import annotations
import typing

import uno
from .x_invocation import XInvocation as XInvocation_be070c0f


class XAutomationInvocation(XInvocation_be070c0f):
    """

    See Also:
        `API XAutomationInvocation <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XAutomationInvocation.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.script.XAutomationInvocation'

    def invokeGetProperty(self, aFunctionName: str, aParams: typing.Tuple[object, ...], aOutParamIndex: uno.ByteSequence, aOutParam: typing.Tuple[object, ...]) -> typing.Any:
        """

        * ``aOutParamIndex`` is an out direction argument.
        * ``aOutParam`` is an out direction argument.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.script.CannotConvertException: ``CannotConvertException``
            com.sun.star.reflection.InvocationTargetException: ``InvocationTargetException``
        """
        ...
    def invokePutProperty(self, aFunctionName: str, aParams: typing.Tuple[object, ...], aOutParamIndex: uno.ByteSequence, aOutParam: typing.Tuple[object, ...]) -> typing.Any:
        """

        * ``aOutParamIndex`` is an out direction argument.
        * ``aOutParam`` is an out direction argument.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.script.CannotConvertException: ``CannotConvertException``
            com.sun.star.reflection.InvocationTargetException: ``InvocationTargetException``
        """
        ...


