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
# Namespace: com.sun.star.security
# Libre Office Version: 7.2
from ooo.oenv.env_const import UNO_NONE
import typing


class RuntimePermission(object):
    """
    Struct Class

    This permission grants runtime access to some named functionality.
    
    A RuntimePermission contains a name (also referred to as a \"target name\") but no actions list; you either have the named permission or you don't.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API RuntimePermission <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1security_1_1RuntimePermission.html>`_
    """
    __ooo_ns__: str = 'com.sun.star.security'
    __ooo_full_ns__: str = 'com.sun.star.security.RuntimePermission'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.security.RuntimePermission'
    """Literal Constant ``com.sun.star.security.RuntimePermission``"""

    def __init__(self, Name: typing.Optional[str] = '') -> None:
        """
        Constructor

        Arguments:
            Name (str, optional): Name value.
        """
        super().__init__()

        if isinstance(Name, RuntimePermission):
            oth: RuntimePermission = Name
            self.Name = oth.Name
            return

        kargs = {
            "Name": Name,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._name = kwargs["Name"]


    @property
    def Name(self) -> str:
        """
        name of permission
        """
        return self._name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._name = value


__all__ = ['RuntimePermission']
