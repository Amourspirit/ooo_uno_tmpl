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
# Namespace: com.sun.star.auth
# Libre Office Version: 7.2
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class InvalidPrincipalException(Exception_85530a09):
    """
    Exception Class

    indicates an invalid principal was specified.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API InvalidPrincipalException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1auth_1_1InvalidPrincipalException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.auth'
    __ooo_full_ns__: str = 'com.sun.star.auth.InvalidPrincipalException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.auth.InvalidPrincipalException'
    __pyunostruct__: str = 'com.sun.star.auth.InvalidPrincipalException'

    typeName: str = 'com.sun.star.auth.InvalidPrincipalException'
    """Literal Constant ``com.sun.star.auth.InvalidPrincipalException``"""

    def __init__(self, Message: typing.Optional[str] = '', Context: typing.Optional[XInterface_8f010a43] = None) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
        """
        kargs = {
            "Message": Message,
            "Context": Context,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        super()._init(**kwargs)


__all__ = ['InvalidPrincipalException']

