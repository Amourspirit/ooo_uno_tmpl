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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class DocumentHeaderField(object):
    """
    Struct Class

    This struct contains a name-value pair of a document header (i.e.
    
    the \"subject\" field and the appropriate value of a MIME message).

    See Also:
        `API DocumentHeaderField <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ucb_1_1DocumentHeaderField.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.ucb'
    __ooo_full_ns__: str = 'com.sun.star.ucb.DocumentHeaderField'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.ucb.DocumentHeaderField'
    """Literal Constant ``com.sun.star.ucb.DocumentHeaderField``"""

    def __init__(self, Name: typing.Optional[str] = '', Value: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
            Value (str, optional): Value value.
        """
        super().__init__()

        if isinstance(Name, DocumentHeaderField):
            oth: DocumentHeaderField = Name
            self.Name = oth.Name
            self.Value = oth.Value
            return

        kargs = {
            "Name": Name,
            "Value": Value,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._name = kwargs["Name"]
        self._value = kwargs["Value"]


    @property
    def Name(self) -> str:
        """
        The name of the header field.
        """
        return self._name

    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value

    @property
    def Value(self) -> str:
        """
        The value of the header field.
        """
        return self._value

    @Value.setter
    def Value(self, value: str) -> None:
        self._value = value


__all__ = ['DocumentHeaderField']
