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
# Namespace: com.sun.star.frame.status
# Libre Office Version: 7.3
from typing_extensions import Literal
import uno
import typing


class ClipboardFormats(object):
    """
    Struct Class

    contains a list of format IDs and names which are part of the system clipboard.
    
    **since**
    
        OOo 2.0

    See Also:
        `API ClipboardFormats <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1frame_1_1status_1_1ClipboardFormats.html>`_
    """
    typeName: Literal['com.sun.star.frame.status.ClipboardFormats']

    def __init__(self, Identifiers: typing.Optional[uno.ByteSequence] = ..., Names: typing.Optional[typing.Tuple[str, ...]] = ...) -> None:
        """
        Constructor

        Arguments:
            Identifiers (uno.ByteSequence, optional): Identifiers value.
            Names (typing.Tuple[str, ...], optional): Names value.
        """
        ...


    @property
    def Identifiers(self) -> uno.ByteSequence:
        """
        specifies a sequence of format IDs which are contained in the system clipboard.
        """
        ...

    @Identifiers.setter
    def Identifiers(self, value: uno.ByteSequence) -> None:
        ...

    @property
    def Names(self) -> typing.Tuple[str, ...]:
        """
        specifies a sequence of format names which are contained in the system clipboard.
        """
        ...

    @Names.setter
    def Names(self, value: typing.Tuple[str, ...]) -> None:
        ...

