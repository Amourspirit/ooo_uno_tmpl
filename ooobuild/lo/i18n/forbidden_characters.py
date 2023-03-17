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
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.4
from ooo.oenv.env_const import UNO_NONE
import typing


class ForbiddenCharacters(object):
    """
    Struct Class

    Locale (mostly CJK) dependent characters that are forbidden at the start or end of a line.
    
    Returned by XLocaleData.getForbiddenCharacters() and used with XForbiddenCharacters methods.

    See Also:
        `API ForbiddenCharacters <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1ForbiddenCharacters.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.i18n'
    __ooo_full_ns__: str = 'com.sun.star.i18n.ForbiddenCharacters'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.i18n.ForbiddenCharacters'
    """Literal Constant ``com.sun.star.i18n.ForbiddenCharacters``"""

    def __init__(self, beginLine: typing.Optional[str] = '', endLine: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            beginLine (str, optional): beginLine value.
            endLine (str, optional): endLine value.
        """
        super().__init__()

        if isinstance(beginLine, ForbiddenCharacters):
            oth: ForbiddenCharacters = beginLine
            self.beginLine = oth.beginLine
            self.endLine = oth.endLine
            return

        kargs = {
            "beginLine": beginLine,
            "endLine": endLine,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._begin_line = kwargs["beginLine"]
        self._end_line = kwargs["endLine"]


    @property
    def beginLine(self) -> str:
        """
        Characters forbidden at the start of a line.
        """
        return self._begin_line
    
    @beginLine.setter
    def beginLine(self, value: str) -> None:
        self._begin_line = value

    @property
    def endLine(self) -> str:
        """
        Characters forbidden at the end of a line.
        """
        return self._end_line
    
    @endLine.setter
    def endLine(self, value: str) -> None:
        self._end_line = value


__all__ = ['ForbiddenCharacters']
