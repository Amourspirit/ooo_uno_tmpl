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
# Namespace: com.sun.star.packages.zip
# Libre Office Version: 7.3
import typing
from ...io.io_exception import IOException as IOException_8c450a27
from ...uno.x_interface import XInterface as XInterface_8f010a43

class ZipIOException(IOException_8c450a27):
    """
    Exception Class

    used to indicate that a ZIP exception has occurred.
    
    Usually can be thrown from XInputStream interface implementations.
    
    This interface is an IDL version of the Java interface java.util.zip.ZipException with some minor adaptations.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API ZipIOException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1packages_1_1zip_1_1ZipIOException.html>`_
    """

    __ooo_ns__: str = 'com.sun.star.packages.zip'
    __ooo_full_ns__: str = 'com.sun.star.packages.zip.ZipIOException'
    __ooo_type_name__: str = 'exception'
    __pyunointerface__: str = 'com.sun.star.packages.zip.ZipIOException'
    __pyunostruct__: str = 'com.sun.star.packages.zip.ZipIOException'

    typeName: str = 'com.sun.star.packages.zip.ZipIOException'
    """Literal Constant ``com.sun.star.packages.zip.ZipIOException``"""

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


__all__ = ['ZipIOException']
