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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.3
from ooo.oenv.env_const import UNO_NONE
from .insert_command_argument import InsertCommandArgument as InsertCommandArgument_19550eb9
from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
import typing


class InsertCommandArgument2(InsertCommandArgument_19550eb9):
    """
    Struct Class

    The argument for the command \"insert\" augmented with some properties.

    See Also:
        `API InsertCommandArgument2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1InsertCommandArgument2.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.InsertCommandArgument2'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.InsertCommandArgument2'
    """Literal Constant ``com.sun.star.ucb.InsertCommandArgument2``"""

    def __init__(self, Data: typing.Optional[XInputStream_98d40ab4] = None, ReplaceExisting: typing.Optional[bool] = False, MimeType: typing.Optional[str] = '', DocumentId: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Data (XInputStream, optional): Data value.
            ReplaceExisting (bool, optional): ReplaceExisting value.
            MimeType (str, optional): MimeType value.
            DocumentId (str, optional): DocumentId value.
        """

        if isinstance(Data, InsertCommandArgument2):
            oth: InsertCommandArgument2 = Data
            self.Data = oth.Data
            self.ReplaceExisting = oth.ReplaceExisting
            self.MimeType = oth.MimeType
            self.DocumentId = oth.DocumentId
            return

        kargs = {
            "Data": Data,
            "ReplaceExisting": ReplaceExisting,
            "MimeType": MimeType,
            "DocumentId": DocumentId,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._mime_type = kwargs["MimeType"]
        self._document_id = kwargs["DocumentId"]
        inst_keys = ('MimeType', 'DocumentId')
        kargs = kwargs.copy()
        for key in inst_keys:
            del kargs[key]
        super()._init(**kargs)


    @property
    def MimeType(self) -> str:
        """
        contains the MIME type of the document to insert
        """
        return self._mime_type
    
    @MimeType.setter
    def MimeType(self, value: str) -> None:
        self._mime_type = value

    @property
    def DocumentId(self) -> str:
        """
        contains the Document Id of the document to insert
        """
        return self._document_id
    
    @DocumentId.setter
    def DocumentId(self, value: str) -> None:
        self._document_id = value


__all__ = ['InsertCommandArgument2']