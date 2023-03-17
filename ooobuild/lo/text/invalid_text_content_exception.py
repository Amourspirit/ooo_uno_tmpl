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
# Namespace: com.sun.star.text
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43
from .x_text_content import XTextContent as XTextContent_b16e0ba5

class InvalidTextContentException(Exception_85530a09):
    """
    Exception Class

    is thrown whenever a method gets a TextContent as an actual argument when the text content cannot be used for that operation.

    See Also:
        `API InvalidTextContentException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1text_1_1InvalidTextContentException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.text'
    __ooo_full_ns__: str = 'com.sun.star.text.InvalidTextContentException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.text.InvalidTextContentException'
    __pyunostruct__: str = 'com.sun.star.text.InvalidTextContentException'

    typeName: str = 'com.sun.star.text.InvalidTextContentException'
    """Literal Constant ``com.sun.star.text.InvalidTextContentException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None, TextContent: typing.Optional[XTextContent_b16e0ba5] = None) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            TextContent (XTextContent, optional): TextContent value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
            "TextContent": TextContent,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._text_content = kwargs["TextContent"]
        inst_keys = ('TextContent',)
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)

    @property
    def TextContent(self) -> XTextContent_b16e0ba5:
        """
        contains the interface of the text content that caused the exception.
        """
        return self._text_content
    
    @TextContent.setter
    def TextContent(self, value: XTextContent_b16e0ba5) -> None:
        self._text_content = value


__all__ = ['InvalidTextContentException']

