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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.packages.zip
from typing_extensions import Literal
import typing
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ...io.x_input_stream import XInputStream as XInputStream_98d40ab4

class XZipFileAccess(XInterface_8f010a43):
    """
    allows to get reading access to non-encrypted entries inside zip file.

    See Also:
        `API XZipFileAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1packages_1_1zip_1_1XZipFileAccess.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.packages.zip.XZipFileAccess']

    def getStreamByPattern(self, aPattern: str) -> 'XInputStream_98d40ab4':
        """
        allows to get stream by specifying a pattern.
        
        The first stream with a name that fits to the pattern will be returned. The pattern allows to use \"*\" wildcard symbol. If the name contains \"*\" or \"\\\" symbols itself they must guarded with backslash \"\\\". The slashes have no special meaning here so they can be replaced by wildcards also.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.packages.WrongPasswordException: ``WrongPasswordException``
            com.sun.star.packages.zip.ZipException: ``ZipException``
        """
        ...


