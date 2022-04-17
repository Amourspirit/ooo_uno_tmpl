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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.3
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class NoConvergenceException(Exception_85530a09):
    """
    Exception Class

    Thrown by a Calc Add-In function this exception indicates the function's algorithm did not converge to a meaningful result.
    
    **since**
    
        OOo 3.3

    See Also:
        `API NoConvergenceException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1sheet_1_1NoConvergenceException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.sheet'
    __ooo_full_ns__: str = 'com.sun.star.sheet.NoConvergenceException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.sheet.NoConvergenceException'
    __pyunostruct__: str = 'com.sun.star.sheet.NoConvergenceException'

    typeName: str = 'com.sun.star.sheet.NoConvergenceException'
    """Literal Constant ``com.sun.star.sheet.NoConvergenceException``"""

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


__all__ = ['NoConvergenceException']

